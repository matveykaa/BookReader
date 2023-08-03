from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from reader.models import Book


class BookForm(FlaskForm):
    title = StringField('Name', validators=[DataRequired(), Length(min=5, max=100)])
    author = StringField('Author', validators=[DataRequired(), Length(min=5, max=100)])
    ganre = StringField('Genre',validators=[DataRequired(), Length(min=5, max=25)])
    cover = FileField('Cover', validators=[FileAllowed(['png', 'jpg'])])
    ratting =IntegerField('My rating', validators=[DataRequired(), NumberRange(min=1, max=5)])
    description = TextAreaField('Sense', validators=[DataRequired(), Length(max=500)])
    notes = TextAreaField('Notes', validators=[DataRequired(), Length(max=500)])

    submit = SubmitField('Add')

    def validate_title(self, title):
        title = Book.query.filter_by(title=title.data).first()
        if title:
            raise ValidationError('The book already exists')

class UpdateBook(FlaskForm):
    title = StringField('Name', validators=[DataRequired(), Length(min=5, max=100)])
    author = StringField('Author', validators=[DataRequired(), Length(min=5, max=100)])
    ganre = StringField('Genre', validators=[DataRequired(), Length(min=5, max=25)])
    cover = FileField('Cover', validators=[FileAllowed(['png', 'jpg'])])
    ratting = IntegerField('My rating', validators=[DataRequired(), NumberRange(min=1, max=5)])
    description = TextAreaField('Sense', validators=[DataRequired(), Length(max=500)])
    notes = TextAreaField('Notes', validators=[DataRequired(), Length(max=500)])

    submit = SubmitField('Add')