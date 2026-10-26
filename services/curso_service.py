
from extensions import db
from models import Curso


def obtener_todos():
    """
    Obtiene todos los cursos registrados.
    """
    return Curso.query.order_by(Curso.id_curso.asc()).all()


def agregar_curso(nombre, instructor, duracion):
    """
    Registra un nuevo curso en la base de datos.
    """
    nuevo_curso = Curso(
        nombre=nombre,
        instructor=instructor,
        duracion=duracion
    )

    try:
        db.session.add(nuevo_curso)
        db.session.commit()
        return nuevo_curso
    except Exception:
        db.session.rollback()
        raise


def obtener_por_id(id_curso):
    """
    Busca un curso por su identificador.
    Devuelve el curso si existe o None si no existe.
    """
    return db.session.get(Curso, id_curso)


def editar_curso(curso, nombre, instructor, duracion):
    """
    Actualiza los datos de un curso existente.
    """
    curso.nombre = nombre
    curso.instructor = instructor
    curso.duracion = duracion

    try:
        db.session.commit()
        return curso
    except Exception:
        db.session.rollback()
        raise


def eliminar_curso(curso):
    """
    Elimina un curso existente de la base de datos.
    """
    try:
        db.session.delete(curso)
        db.session.commit()
    except Exception:
        db.session.rollback()
        raise


def buscar_cursos(termino):
    """
    Busca cursos por nombre o instructor.
    Si el término está vacío, devuelve todos los cursos.
    """
    consulta = Curso.query

    if termino and termino.strip():
        patron = f"%{termino.strip()}%"

        consulta = consulta.filter(
            db.or_(
                Curso.nombre.ilike(patron),
                Curso.instructor.ilike(patron)
            )
        )

    return consulta.order_by(Curso.id_curso.asc()).all()
