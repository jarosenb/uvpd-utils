from flask_wtf import Form
from wtforms import FloatField, FileField, BooleanField, HiddenField, StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired


class DeepSearchForm(Form):
    sequence = StringField()

    InitMass = FloatField()
    FinalMass = FloatField()

    Increment = FloatField()

    a = BooleanField('a')
    ap1 = BooleanField('a+')
    x = BooleanField('x')
    xp1 = BooleanField('x+')
    b = BooleanField('b')
    y = BooleanField('y')
    ym1 = BooleanField('y-')
    ym2 = BooleanField('y--')
    c = BooleanField('c')
    z = BooleanField('z')

    ppm = IntegerField(default=10)

    raw = TextAreaField()

class ChargeForm(Form):

    sequence = StringField()
    charge = IntegerField()

    a = BooleanField('a')
    ap1 = BooleanField('a+')
    x = BooleanField('x')
    xp1 = BooleanField('x+')
    b = BooleanField('b')
    y = BooleanField('y')
    ym1 = BooleanField('y-')
    ym2 = BooleanField('y--')
    c = BooleanField('c')
    z = BooleanField('z')

    ppm=IntegerField(default=10)

    raw = TextAreaField()

class IntensityForm(Form):

    sequence = StringField()
    tic = StringField()

    mods = StringField()

    a = BooleanField('a')
    ap1 = BooleanField('a+')
    x = BooleanField('x')
    xp1 = BooleanField('x+')
    b = BooleanField('b')
    y = BooleanField('y')
    ym1 = BooleanField('y-')
    ym2 = BooleanField('y--')
    c = BooleanField('c')
    z = BooleanField('z')

    ppm = IntegerField(default=10)

    raw = TextAreaField()


