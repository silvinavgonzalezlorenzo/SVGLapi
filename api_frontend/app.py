from flask import Flask, render_template, request, url_for, jsonify, redirect

from flask_cors import CORS

import mysql.connector

#import random

from datetime import date 

app = Flask(__name__)
CORS(app) #ESTO HABILITA CORS PARA TODAS LAS RUTAS

# CLASE CATALOGO
class Catalogo:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host = host, # "localhost",
            user = user, # "root",
            password = password, # "        ",
            database= database, # "sistemaclub"
        )
        self.cursor = self.conn.cursor()
        
        self.cursor.execute(f"USE `{database}`")
        
            
    def agregar_socio(self, nombre, apellido, tel, ciudad, pais):
        sql = "INSERT INTO `sistemaclub`.`sisclub` (`nombre`, `apellido`, `tel`, `ciudad`, `pais` ) VALUES ('" + \
        nombre + "', '" + apellido + "', '" + tel + "', '" + ciudad + "', '" + pais + "');"
    
        self.cursor.execute(sql) 
        self.conn.commit()
        return True
            
    def eliminar_socio(self, id):
        sql = "DELETE FROM `sistemaclub`.`sisclub` WHERE (`idsisclub` = '" + str(id) + "');"
        self.cursor.execute(sql)
        self.conn.commit()
        return True
        
    def traer_socio_por_id(self, id):
        sql = "SELECT * FROM `sistemaclub`.`sisclub` WHERE (`idsisclub` = '" + str(id) + "');"
        print(sql) #PARA MOSTRAR CÓMO SE EJECUTÓ ESA PARTE DEL SCRIPT (Y PODER CHEQUEAR QUE ESTÁ OK)
        self.cursor.execute(sql)
        socio = self.cursor.fetchone()
        return socio
        
    def modificar_socio(self, id, nombre, apellido, tel, ciudad, pais):
        sql = "UPDATE `sistemaclub`.`sisclub` SET `nombre` = '" + nombre + "', `apellido` = '" + apellido + "', `tel` = '" + tel + "', `ciudad` = '" + ciudad + "', `pais` = '" + pais + "' WHERE (`idsisclub` = '" + str(id) + "');"
        print(sql) #PARA MOSTRAR CÓMO SE EJECUTÓ ESA PARTE DEL SCRIPT (Y PODER CHEQUEAR QUE ESTÁ OK)
        self.cursor.execute(sql)
        self.conn.commit()
        return True
        
    def traer_socios(self): # ESTO ES UN METODO TIPO GET
        sql = "SELECT * FROM `sistemaclub`.`sisclub`;"
        self.cursor.execute(sql) # ESTO EJECUTA LA CONSULTA
        socios = self.cursor.fetchall() # ESTO DEVUELVE UNA LISTA DE TUPLAS
        return socios 
  
# FIN CLASE CATALOGO

####################################################
# PROGRAMA PRINCIPAL

catalogo = Catalogo(host='localhost', user='root', password='          ', database='sistemaclub')

@app.route("/socios", methods=["POST"]) #ESTO ES UN DECORADOR
def agregar_socio():
    
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    tel = request.form['tel']
    ciudad = request.form['ciudad']
    pais = request.form['pais']
    
    si_se_agrego = catalogo.agregar_socio(nombre, apellido, tel, ciudad, pais)
    if si_se_agrego:
        return jsonify({"mensaje": "socio agregado"}), 200 # ESTO ES UNA RESPUESTA HTTP OK
    else:
       return jsonify({"mensaje": "Error"}), 400 # ESTO ES UNA RESPUESTA HTTP ERROR

@app.route("/socios", methods=["GET"])
def traer_socios():
    socios = catalogo.traer_socios()
    return jsonify(socios), 200 # ESTO ES UNA RESPUESTA HTTP OK

@app.route("/socios/<int:idsisclub>", methods=["DELETE"])
def eliminar_socio(idsisclub):
    socio_eliminado = catalogo.eliminar_socio(idsisclub)
    if socio_eliminado:
        return jsonify({"mensaje": "socio eliminado"}), 200
    else:
        return jsonify({"mensaje": "Error"}), 400

@app.route("/socios/<int:idsisclub>", methods=["GET"])
def traer_socio_por_id(idsisclub):
    socio = catalogo.traer_socio_por_id(idsisclub)
    return jsonify(socio), 200

@app.route("/socios/<int:idsisclub>", methods=["POST"])
def modificar_socio(idsisclub):    
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    tel = request.form['tel']
    ciudad = request.form['ciudad']
    pais = request.form['pais']
    
    si_se_modifico = catalogo.modificar_socio(idsisclub, nombre, apellido, tel, ciudad, pais)
    if si_se_modifico:
        return jsonify({"mensaje": "socio modificado"}), 200
    else:
        return jsonify({"mensaje": "Error"}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
    
