import json
import sqlite3

from config import FICHERO
from requests import Session
import requests
import json


class ConsultaDBException(Exception):
    pass
class LocalDBException(Exception):
    pass


class Dbmanager():
    def __init__(self):
        self.FICHERO=FICHERO
        self.registros="""
        SELECT *
            FROM registro
            ORDER BY momento;
        """
        self.cantidad_monedero_1="""
        SELECT cantidad
            FROM monedero
            WHERE cryptomoneda is "{}"
        """
        self.inserta="""
                        INSERT INTO registro (momento,moneda_inicial,moneda_inicial_Q,moneda_final,moneda_final_Q,precio_unitario)
                        VALUES(:momento,:moneda_inicial,:moneda_inicial_Q,:moneda_final, :moneda_final_Q, :precio_unitario)
                    """
        self.graba__monedero="""
        UPDATE monedero
            SET "cantidad" = cantidad + {}
            WHERE "cryptomoneda" is "{}";
        """
    def registro(self):
        try: 
            sqlite3.connect(self.FICHERO)
        except sqlite3.Error as e:
            raise  ConsultaDBException(str(e))
        conn=sqlite3.connect(self.FICHERO)
        cur=conn.cursor()
        cur.execute(self.registros)
        keys= []
        for item in cur.description:
            keys.append(item[0])
        movimientos=[]
        for registro in cur.fetchall():
            ix_clave=0
            d= {}
            for columna in keys:
                d[columna] = registro[ix_clave]
                ix_clave += 1
            movimientos.append(d)
        conn.close()
        return movimientos
    def p_registro(self):
        try: 
            sqlite3.connect(self.FICHERO)
            return True
        except sqlite3.Error as e:
            raise  ConsultaDBException(str(e))
    def crypto_monedero(self,cryptomoneda):
        conn=sqlite3.connect(self.FICHERO)
        cur=conn.cursor()
        cur.execute(self.cantidad_monedero_1.format(cryptomoneda))
        cantidad=cur.fetchall()
        cantidad=cantidad[0]
        cantidad=cantidad[0]
        conn.close()
        return cantidad
    def escribebase(self, params):
        conn = sqlite3.connect(self.FICHERO)
        cur = conn.cursor()
        cur.execute(self.inserta,params)
        conn.commit()
        conn.close()
    def escribe_monedero(self,moneda2Q,moneda2):
        conn = sqlite3.connect(self.FICHERO)
        cur = conn.cursor()
        cur.execute(self.graba__monedero.format(moneda2Q,moneda2))
        conn.commit()
        conn.close()
class Apimanager():
    def __init__(self):
        self.urlc="https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount={}&symbol={}&convert={}&CMC_PRO_API_KEY=f892e6e1-beb2-4c50-8a44-1dfae22119b4"
        self.urlp="https://pro-api.coinmarketcap.com/v1/tools/price-conversion?amount={}&symbol={}&convert=EUR&CMC_PRO_API_KEY=f892e6e1-beb2-4c50-8a44-1dfae22119b4"
        self.headers={
            'accepts' : 'application/json'
        }
    def compara(self,cantidad,moneda1,moneda2):
        moneda1=str(moneda1)
        moneda2=str(moneda2)
        url=self.urlc.format(cantidad,moneda1,moneda2)
        session=Session()
        session.headers.update(self.headers)
        respuesta=requests.get(url)
        data_dict=json.loads(respuesta.text)
        valor=data_dict["data"]["quote"][moneda2]["price"]
        return valor
    def p_api(self):
        try:
            cantidad=1
            moneda1="EUR"
            moneda2="BTC"
            self.compara(cantidad,moneda1,moneda2)
            return True
        except:
            return False