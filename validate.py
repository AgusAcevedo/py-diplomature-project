import re

# -------------------------------------------------------------------
#               MODULO VALIDACIONES(REGEX)
#
# Entrega Final Python Avanzado 25/04/2022    Curso: 999186445
#
# Integrantes: Agustin Acevedo
# -------------------------------------------------------------------


class Validation:
    def __init__(self):
        self.email_pattern = "[^[a-z 0-9]+[\.-_]?[a-z 0-9]\w+[.]\w"
        self.name_pattern = "^[A-Z]{1}[A-Za-záéíóú]"

    def valite_name(self, entry):
        return re.search(self.name_pattern, entry)

    def valite_email(self, entry):
        return re.search(self.email_pattern, entry)
