from os.path import dirname
from os.path import join
from os.path import abspath
from datetime import datetime

# -------------------------------------------------------------------
#               MODULO DECORADOR
#
# Entrega Final Python Avanzado 25/04/2022    Curso: 999186445
#
# Integrantes: Agustin Acevedo
# -------------------------------------------------------------------


def update_log(funcion):
    def envoltura(*args, **kwargs):
        ruta = dirname(abspath(__file__))
        log = join(ruta, "log_file.txt")

        archivo = open(log, "a")

        fecha = datetime.now()
        funcion.__name__.upper()
        if funcion.__name__ == "insertRegister":
            operacion = "ALTA"
            valores = 'Nombre: "{0}" - Apellido: "{1}" - DNI: "{2}" - Temperatura: "{3}" - Telefono: "{4}" - Email: "{5}"'.format(
                args[1],
                args[2],
                args[3],
                args[4],
                args[5],
                args[6],
            )
        elif funcion.__name__ == "deleteRegister":
            operacion = "BAJA"
            valores = 'Id: "{0}"'.format(args[1])
        elif funcion.__name__ == "updateRegister":
            operacion = "MODIFICACION"
            valores = 'Id: "{0}" - Valor modificado: "{1}" - Nuevo valor: "{2}"'.format(
                args[1], args[2], args[3]
            )
        else:
            valores = args[1]

        msg = "[{0}-{1}-{2} {3}] {4} | {5}".format(
            fecha.strftime("%Y"),
            fecha.strftime("%m"),
            fecha.strftime("%d"),
            fecha.strftime("%X"),
            operacion,
            valores,
        )
        print("-" * 85 + "\n" + msg, file=archivo)

        return funcion(*args, **kwargs)

    return envoltura
