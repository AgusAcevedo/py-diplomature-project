from tkinter import Tk
from view import Ventana
from observer import Alta_observer,Borrar_observer,Modificar_observer

# -------------------------------------------------------------------
#               MODULO CONTROLADOR
#
# Entrega Final Python Avanzado 25/04/2022    Curso: 999186445
#
# Integrantes: Agustin Acevedo
# -------------------------------------------------------------------


class Controller:
    def __init__(self, vista):
        self.obj_vista = Ventana(vista)

        self.obs_a = Alta_observer(self.obj_vista.obj_modelo)
        self.obs_b = Borrar_observer(self.obj_vista.obj_modelo)
        self.obs_c = Modificar_observer(self.obj_vista.obj_modelo)


if __name__ == "__main__":
    root = Tk()
    app = Controller(root)
    root.mainloop()
