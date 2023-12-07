from flask import Flask, request, jsonify

from flask_cors import CORS

import mysql.connector

app = Flask(__name__)
CORS(app) #ESTO HABILITA CORS PARA TODAS LAS RUTAS

# CLASE CATALOGO
class Catalogo:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "Pepino+Milucito@2011-2023@",
            database="sistemaclub"
        )
        self.cursor = self.conn.cursor()
        
        self.cursor.execute(f"USE `{database}`")
        
            
    def agregar_socio(self, nombre, apellido, tel, ciudad, pais):
        sql = "INSERT INTO `sistemaclub`.`socios` (`nombre`, `apellido`, `tel`, `ciudad`, `pais` ) VALUES (" + nombre + ", " + apellido + ", " + tel + ", " + ciudad + ", " + pais + ");"
    
        self.cursor.execute(sql)
        self.conn.commit()
        return True
            
    def eliminar_socio(self, codigo):
        sql = "DELETE FROM `sistemaclub`.`socios` WHERE (`id` = " + str(codigo) + ");"
        self.cursor.execute(sql)
        self.conn.commit()
        return True
        
    def traer_socio_por_id(self, codigo):
        sql = "SELECT * FROM `sistemaclub`.`socios` WHERE (`id` = " + str(codigo) + ");"
        self.cursor.execute(sql)
        socio = self.cursor.fetchone()
        return socio
        
    def modificar_socio(self, codigo, nombre, apellido, tel):
        sql = "UPDATE `sistemaclub`.`socio` SET `nombre` = '" + nombre + "', `apellido` = " + apellido + ", `tel` = " + tel + " WHERE (`id` = " + str(codigo) + ");"
        self.cursor.execute(sql)
        self.conn.commit()
        return True
        
    def traer_socios(self): # ESTO ES UN METODO TIPO GET
        sql = "SELECT * FROM `sistemaclub`.`socios`;"
        self.cursor.execute(sql) # ESTO EJECUTA LA CONSULTA
        socios = self.cursor.fetchall() # ESTO DEVUELVE UNA LISTA DE TUPLAS
        return socios 
  
# FIN CLASE CATALOGO

####################################################
# PROGRAMA PRINCIPAL

catalogo = Catalogo(host='localhost', user='root', password='', database='sistemaclub')

@app.route("/socios", methods=["POST"]) #ESTO ES UN DECORADOR
def agregar_socio():
    
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    tel = request.form['tel']
    
    si_se_agrego = catalogo.agregar_socio(nombre, apellido, tel)
    if si_se_agrego:
        return jsonify({"mensaje": "socio agregado"}), 200 # ESTO ES UNA RESPUESTA HTTP OK
    else:
       return jsonify({"mensaje": "Error"}), 400 # ESTO ES UNA RESPUESTA HTTP ERROR

@app.route("/socios", methods=["GET"])
def traer_socios():
    socios = catalogo.traer_socios()
    return jsonify(socios), 200 # ESTO ES UNA RESPUESTA HTTP OK

@app.route("/socios/<int:codigo>", methods=["DELETE"])
def eliminar_socio(codigo):
    socio_eliminado = catalogo.eliminar_socio(codigo)
    if socio_eliminado:
        return jsonify({"mensaje": "socio eliminado"}), 200
    else:
        return jsonify({"mensaje": "Error"}), 400

@app.route("/socios/<int:codigo>", methods=["GET"])
def traer_socio_por_id(codigo):
    socio = catalogo.traer_socio_por_id(codigo)
    return jsonify(socio), 200

@app.route("/socios/<int:codigo>", methods=["PUT"])
def modificar_socio(codigo):    
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    tel = request.form['tel']
    
    si_se_modifico = catalogo.modificar_socio(codigo, nombre, apellido, tel)
    if si_se_modifico:
        return jsonify({"mensaje": "socio modificado"}), 200
    else:
        return jsonify({"mensaje": "Error"}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)
    
    