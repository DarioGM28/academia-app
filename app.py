
import os
from flask_wtf.csrf import CSRFProtect

from dotenv import load_dotenv
from flask import Flask, render_template, redirect, url_for, flash, request
from sqlalchemy import URL, text
from sqlalchemy.exc import SQLAlchemyError

from extensions import db, migrate
from models import Curso
from forms import CursoForm


from services.curso_service import (
    obtener_todos,
    buscar_cursos,
    agregar_curso as agregar_curso_servicio,
    obtener_por_id,
    editar_curso as editar_curso_servicio,
    eliminar_curso as eliminar_curso_servicio
)



load_dotenv()

app = Flask(__name__)
csrf = CSRFProtect(app)

# Configuración de MySQL
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")


if not all([DB_USER, DB_PASSWORD, DB_NAME, SECRET_KEY]):
    raise RuntimeError(
        "Faltan variables de configuración en el archivo .env"
    )


app.config["SECRET_KEY"] = SECRET_KEY

database_url = URL.create(
    drivername="mysql+pymysql",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    query={"charset": "utf8mb4"},
)

app.config["SQLALCHEMY_DATABASE_URI"] = database_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


db.init_app(app)
migrate.init_app(app, db)


# Mantener registrado el modelo para Flask-Migrate
_ = Curso



@app.route("/")
def inicio():
    termino = request.args.get("buscar", "").strip()
    cursos = buscar_cursos(termino)

    return render_template(
        "index.html",
        cursos=cursos,
        termino=termino
    )



@app.route("/cursos/agregar", methods=["GET", "POST"])
def agregar_curso():
    form = CursoForm()

    if form.validate_on_submit():
        try:
            agregar_curso_servicio(
                nombre=form.nombre.data.strip(),
                instructor=form.instructor.data.strip(),
                duracion=form.duracion.data
            )

            flash("El curso se agregó correctamente.", "success")
            return redirect(url_for("inicio"))

        except SQLAlchemyError:
            app.logger.exception("Error al guardar el curso")
            flash(
                "No se pudo guardar el curso. "
                "Verifica la conexión y vuelve a intentarlo.",
                "danger"
            )

    return render_template("agregar_curso.html", form=form)


@app.route("/cursos/editar/<int:id_curso>", methods=["GET", "POST"])
def editar_curso(id_curso):
    curso = obtener_por_id(id_curso)

    if curso is None:
        flash("El curso solicitado no existe.", "warning")
        return redirect(url_for("inicio"))

    form = CursoForm(obj=curso)

    if form.validate_on_submit():
        try:
            editar_curso_servicio(
                curso=curso,
                nombre=form.nombre.data.strip(),
                instructor=form.instructor.data.strip(),
                duracion=form.duracion.data
            )

            flash("El curso se actualizó correctamente.", "success")
            return redirect(url_for("inicio"))

        except SQLAlchemyError:
            app.logger.exception("Error al actualizar el curso")
            db.session.rollback()

            flash(
                "No se pudo actualizar el curso. "
                "Verifica la conexión e inténtalo nuevamente.",
                "danger"
            )

    return render_template(
        "editar_curso.html",
        form=form,
        curso=curso
    )


@app.route("/cursos/eliminar/<int:id_curso>", methods=["POST"])
def eliminar_curso(id_curso):
    curso = obtener_por_id(id_curso)

    if curso is None:
        flash("El curso que intentas eliminar no existe.", "warning")
        return redirect(url_for("inicio"))

    try:
        eliminar_curso_servicio(curso)
        flash("El curso se eliminó correctamente.", "success")

    except SQLAlchemyError:
        app.logger.exception("Error al eliminar el curso")
        db.session.rollback()

        flash(
            "No se pudo eliminar el curso. "
            "Verifica la conexión e inténtalo nuevamente.",
            "danger"
        )

    return redirect(url_for("inicio"))


@app.route("/verificar-db")
def verificar_db():
    db.session.execute(text("SELECT 1"))
    return "Conexión con MySQL exitosa."


if __name__ == "__main__":
    app.run(debug=True)
