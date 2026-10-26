
from extensions import db


class Curso(db.Model):
    __tablename__ = "cursos"

    id_curso = db.Column(
        "idCurso",
        db.Integer,
        primary_key=True,
        autoincrement=True
    )

    nombre = db.Column(
        db.String(150),
        nullable=False
    )

    instructor = db.Column(
        db.String(100),
        nullable=False
    )

    duracion = db.Column(
        db.Numeric(8, 2),
        nullable=False
    )

    def __repr__(self):
        return f"<Curso {self.nombre}>"
