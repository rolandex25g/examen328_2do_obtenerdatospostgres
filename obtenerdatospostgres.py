# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 10:46:33 2020

@author: ASUS
"""

import psycopg2 as pc
conexion=pc.connect(user="postgres",
                    password="root",
                    host="127.0.0.1",
                    port="5432",
                    database="academico")

print(conexion.get_dsn_parameters())

#puntero a base de datos
cursor=conexion.cursor()
sql = "select * from materia"
cursor.execute(sql)
#print(cursor)
registros=cursor.fetchall()
print(registros)

for registro in registros:
    print("idMateria:", registro[0])
    print("sigla:", registro[1])
    print("nombre_materia:", registro[2])
cursor.close()
conexion.close()


