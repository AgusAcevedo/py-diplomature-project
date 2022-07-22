# -------------------------------------------------------------------
#               MODULO OBSERVADOR
#
# Entrega Final Python Avanzado 25/04/2022    Curso: 999186445
#
# Integrantes: Agustin Acevedo
# -------------------------------------------------------------------

class Tema():
    
    observadores = []

    def add(self, observador):
        self.observadores.append(observador)

    def notify_alta(self, *args):
        self.observadores[0].update(*args)
    
    def notify_borrar(self, *args):
        self.observadores[1].update(*args)
    
    def notify_modificar(self, *args):
        self.observadores[2].update(*args)


class Observer():
    def update(self,):
        raise NotImplementedError("Delegación de actualización")


class Alta_observer(Observer):
    def __init__(self, observador):
        self.obs_a = observador
        self.obs_a.add(self)
        
    def update(self, *args):
        print(f"Se realizo un alta, ver log para mas info - ref: dni = {args[0]}")
     
class Borrar_observer(Observer):
    def __init__(self, observador):
        self.obs_b = observador
        self.obs_b.add(self)
    
    def update(self, *args):
        print(f"Se realizo una baja, ver log para mas info - ref: id = {args[0]}")

class Modificar_observer(Observer):
    def __init__(self, observador):
        self.obs_c = observador
        self.obs_c.add(self)
    
    def update(self, *args):
        print(f"Se realizo una modificación, ver log para mas info - ref: id = {args[0]}")
