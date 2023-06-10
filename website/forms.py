from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import HiddenField
from wtforms import BooleanField

class SearchForm(FlaskForm):
    search_term = StringField('Search')
    compare_term = StringField('Compare (Optional)')
    submit = SubmitField('Submit')