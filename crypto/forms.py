from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import (DateTimeField, IntegerField, SelectField, SubmitField,
                    validators)
from wtforms.validators import DataRequired, NumberRange


class Formulario(FlaskForm):
    momento=DateTimeField(label="fecha",validators=[DataRequired(message="debe especificarse fecha")],format='%Y-%m-%d %H:%M:%S', default=datetime.today())
    moneda_inicial=SelectField(label="moneda_inicial",validators=[DataRequired(message="debe especificarse")],choices=[('EUR'),('BTC'),('ETH'),('XRP'),('LTC'),('BCH'),('BNB'),('USDT'),('EOS'),('BSV'),('XLM'),('ADA'),('TRX')])
    moneda_inicial_Q=IntegerField(label="moneda_inicial_Q",validators=[DataRequired(message="debe especificar cantidad"), NumberRange(message="debe ser mayor que 0", min=0)])
    moneda_final=SelectField(label="moneda_final",choices=[('EUR'),('BTC'),('ETH'),('XRP'),('LTC'),('BCH'),('BNB'),('USDT'),('EOS'),('BSV'),('XLM'),('ADA'),('TRX')])
    moneda_final_Q=IntegerField(label="moneda_final_Q",default=0,validators=[NumberRange(min=0, message="debe ser mayor que 0")])
    precio_unitario=IntegerField(label="precio_unitario",default=0,validators=[NumberRange(min=0, message="debe ser mayor que 0")])
    calcular=SubmitField('Calcular')
    comprar=SubmitField('Comprar')
