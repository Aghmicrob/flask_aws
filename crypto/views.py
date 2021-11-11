from flask import Flask, render_template, request
from flask.helpers import url_for
from flask_wtf import *
from werkzeug.utils import redirect
from wtforms import *

from crypto import app
from crypto.forms import Formulario
from crypto.models import ConsultaDBException, Dbmanager
from crypto.models import Apimanager


class ConsultaDBException(Exception):
    pass

dbmanager=Dbmanager()
api=Apimanager()
@app.route("/")
def inicio():
    try: 
        movimientos=dbmanager.registro()
        return render_template("index.html", items=movimientos)
    except:
        movimientos=()
        e="error accseo a base de datos"
        return render_template("index.html", items=movimientos,error=e)


@app.route('/compra', methods=["GET", "POST"])
def nueva_transaccion():
    formulario=Formulario()
    if request.method== "GET":
        return render_template("compra.html",el_formulario=formulario)
    elif formulario.calcular.data:
        if formulario.validate_on_submit():
            if api.p_api() ==False:
                return "error de la api"
            else:
                formulario_datos=request.form
                cantidad_2=api.compara(formulario_datos["moneda_inicial_Q"],formulario_datos["moneda_inicial"],formulario_datos["moneda_final"])
                cantidad_1 = float(formulario_datos["moneda_inicial_Q"])
                precio_unidad= cantidad_1 / cantidad_2
                formulario.moneda_final_Q.raw_data=[cantidad_2]
                formulario.precio_unitario.raw_data=[precio_unidad]
                return render_template("compra.html",el_formulario=formulario)
            


@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('inicio')), 404


@app.errorhandler(500)
def server_error(e):
    return redirect(url_for('inicio')), 500

