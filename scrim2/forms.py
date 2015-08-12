from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, SelectField, TextAreaField
from wtforms.validators import Required, Length
from consts import *

class EditUserForm(Form):
    skill_level = SelectField('skill_level', choices=CHOICES_SKILLS)
    main_class  = SelectField('main_class', choices=CHOICES_CLASSES)

