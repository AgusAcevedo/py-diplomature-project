from peewee import *
from decorator import update_log
from observer import Tema

from validate import Validation

# -------------------------------------------------------------------
#               MODULO MODELO 
#
# Entrega Final Python Avanzado 25/04/2022    Curso: 999186445
#
# Integrantes: Agustin Acevedo
# -------------------------------------------------------------------


""" DB Table columns:    
| id   |  name  |  surname  |  dni  |  temp  |  phone  |  email |
| int  |  text  |  text     |  int  |  real  |  text   |  text  |
"""

obj_validation = Validation

try:
    db = SqliteDatabase("base_entrega_final.db")

    class BaseModel(Model):
        class Meta:
            database = db

    class Member(BaseModel):
        name = CharField()
        surname = CharField()
        dni = CharField()
        temp = CharField()
        phone = CharField()
        email = CharField()

    db.connect()
    db.create_tables([Member])
except:
    print("Error")

class BaseDeDatos(Tema):
    def __init__(self,):
        pass

    def actualizar_treeview(self, mitreeview):
        # limpieza de tabla
        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)

        resultado = Member.select()

        for fila in resultado:
            mitreeview.insert(
                "",
                0,
                #text=fila.id,
                values=(fila.id, fila.name, fila.surname, fila.dni, fila.temp, fila.phone, fila.email),
            )
    
    @update_log
    def insertRegister(self, value1, value2, value3, value4, value5, value6):
        member = Member()
        member.name = value1
        member.surname = value2
        member.dni = value3
        member.temp = value4
        member.phone = value5
        member.email = value6
        member.save()
        self.notify_alta(value3)

    @update_log
    def deleteRegister(self, delete_id):
        borrar = Member.get(Member.id == delete_id)
        borrar.delete_instance()
        self.notify_borrar(delete_id)

    @update_log
    def updateRegister(self, update_id, update_colum, update_data_value):
        if update_colum == "Nombre":
            actualizar = Member.update(
                name= update_data_value
            ).where(Member.id == update_id)
            actualizar.execute()
            self.notify_modificar(update_id)

        if update_colum == "Apellido":
            actualizar = Member.update(
                surname= update_data_value
            ).where(Member.id == update_id)
            actualizar.execute()
            self.notify_modificar(update_id)

        if update_colum == "DNI":
            actualizar = Member.update(
                dni= update_data_value
            ).where(Member.id == update_id)
            actualizar.execute()
            self.notify_modificar(update_id)

        if update_colum == "Temperatura":
            actualizar = Member.update(
                temp= update_data_value
            ).where(Member.id == update_id)
            actualizar.execute()
            self.notify_modificar(update_id)

        if update_colum == "Télefono":
            actualizar = Member.update(
                phone= update_data_value
            ).where(Member.id == update_id)
            actualizar.execute()
            self.notify_modificar(update_id)

        if update_colum == "email":
            actualizar = Member.update(
                email= update_data_value
            ).where(Member.id == update_id)
            actualizar.execute()
            self.notify_modificar(update_id)