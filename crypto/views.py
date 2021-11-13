from flask import Flask, render_template, request
from flask.helpers import url_for
from flask_wtf import *
from werkzeug.utils import bind_arguments, redirect
from wtforms import *
from wtforms.widgets.core import SubmitInput

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
    if dbmanager.p_registro() == False:
        movimientos=()
        e="error acceso a base de datos"
        return render_template("index.html", items=movimientos,error=e)
    else: 
        movimientos=dbmanager.registro()
        return render_template("index.html", items=movimientos)

@app.route('/compra', methods=["GET", "POST"])
def nueva_transaccion():
    formulario=Formulario()
    if request.method== "GET":
        return render_template("compra.html",el_formulario=formulario)
    elif formulario.calcular.data:
        if formulario.validate_on_submit():
            if api.p_api() ==False:
                mensaje="error acceso a la api"
                return render_template("compra.html",el_formulario=formulario,mensajes=mensaje)
            elif request.form["moneda_inicial"] == request.form["moneda_final"]:
                mensaje="Por favor elige una moneda de destino distinta a la de origen"
                return render_template("compra.html",el_formulario=formulario,mensajes=mensaje)
            else:
                formulario_datos=request.form
                cantidad_inicio=request.form["moneda_inicial_Q"]
                cantidad_inicio=float(cantidad_inicio)
                cantidad_disponible=dbmanager.crypto_monedero(formulario_datos["moneda_inicial"])
                cantidad_disponible=float(cantidad_disponible)
                if cantidad_disponible < cantidad_inicio and formulario_datos["moneda_inicial"] !="EUR":
                    mensaje="no tienes cryptomonedas suficientes"
                    return render_template("compra.html",el_formulario=formulario,mensajes=mensaje)
                else: 
                    cantidad_2=api.compara(formulario_datos["moneda_inicial_Q"],formulario_datos["moneda_inicial"],formulario_datos["moneda_final"])
                    cantidad_1 = float(formulario_datos["moneda_inicial_Q"])
                    precio_unidad= cantidad_1 / cantidad_2
                    formulario.moneda_final_Q.raw_data=[cantidad_2]
                    formulario.precio_unitario.raw_data=[precio_unidad]
                    return render_template("compra.html",el_formulario=formulario)
        else: 
            mensaje="error al rellenar formulario, vuelva al inicio y rellenelo otra vez"
            return render_template("compra.html",el_formulario=formulario,mensajes=mensaje)
    elif formulario.comprar.data:
        if formulario.validate_on_submit():
            formulario_datos=request.form
            if formulario_datos["moneda_final_Q"] == "0":
                mensaje="no se olvide de pulsar calcular antes de pulsar comprar"
                return render_template("compra.html",el_formulario=formulario,mensajes=mensaje)
            else:
                dbmanager.escribebase(formulario_datos)
                dbmanager.suma_monedero(formulario_datos["moneda_final_Q"],formulario_datos["moneda_final"])
                if formulario_datos["moneda_inicial"] != "EUR":
                    dbmanager.sustrae_monedero(formulario_datos["moneda_inicial_Q"],formulario_datos["moneda_inicial"])
                return redirect(url_for("inicio"))
        else: 
            mensaje="error al rellenar formulario, vuelva al inicio y rellenelo otra vez"
            return render_template("compra.html",el_formulario=formulario,mensajes=mensaje)
@app.route('/status')
def status(): 
    if dbmanager.p_monedero()==False or dbmanager.p_invertido()==False or dbmanager.p_saldo_cartera()==False or dbmanager.p_recuperado()==False or api.p_valor()==False:
        total=0
        valor_inversion=0
        monedero=()
        mensaje="error comunicacion con base de datos"
        return render_template("status.html",total=total,valor_actual=valor_inversion,monedero=monedero,mensajes=mensaje)
    else:
        total_0=dbmanager.invertido()
        total=total_0[0]
        valor_actual_cryptos=dbmanager.saldo_cartera()
        saldo_0=dbmanager.recuperado()
        saldo_euros_invertidos=saldo_0[0]
        miramonedero=dbmanager.monedero()
        if total== None or saldo_euros_invertidos==None or valor_actual_cryptos ==0:
            total=0
            valor_inversion=0
            mensaje="aun no has comprado nada, o has vendido todad las cryptos que tenias, vuelve a comprar"
            return render_template("status.html",total=total,valor_actual=valor_inversion,mensajes=mensaje)
        else: 
            valor_inversion = total + valor_actual_cryptos +  saldo_euros_invertidos
            return render_template("status.html",total=total,valor_actual=valor_inversion,cryptos=miramonedero)


@app.errorhandler(404)
def page_not_found():
    return render_template("error.html")
    

@app.errorhandler(500)
def server_error():
    return render_template("error.html")

