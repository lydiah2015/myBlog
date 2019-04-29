from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,TextAreaField
from wtforms.validators import Required,Length

class BlogForm(FlaskForm):
    title=StringField('Title', validators=[Required(), Length(1, 255)])
    blog=TextAreaField("Blog",validators=[Required()])
    submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    comment=TextAreaField("",validators=[Required()])
    submit = SubmitField('Submit')