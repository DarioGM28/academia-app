
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SubmitField
from wtforms.validators import (
    DataRequired,
    Length,
    NumberRange,
    InputRequired,
)


class CursoForm(FlaskForm):
    nombre = StringField(
        "Nombre del curso",
        validators=[
            DataRequired(message="El nombre es obligatorio."),
            Length(
                max=150,
                message="El nombre no puede superar 150 caracteres."
            )
        ]
    )

    instructor = StringField(
        "Nombre del instructor",
        validators=[
            DataRequired(message="El instructor es obligatorio."),
            Length(
                max=100,
                message="El instructor no puede superar 100 caracteres."
            )
        ]
    )

    duracion = DecimalField(
        "Duración en horas",
        places=2,
        validators=[
            InputRequired(message="La duración es obligatoria."),
            NumberRange(
                min=0.01,
                message="La duración debe ser mayor que cero."
            )
        ]
    )

    submit = SubmitField("Guardar curso")
