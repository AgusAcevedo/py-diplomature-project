from tkinter import ttk
from tkinter import *
from tkinter.messagebox import *
from modelo import BaseDeDatos, Validation
import os

# -------------------------------------------------------------------
#               MODULO VISTA
#
# Entrega Final Python Avanzado 25/04/2022    Curso: 999186445
#
# Integrantes: Agustin Acevedo
# -------------------------------------------------------------------


class Ventana:
    def __init__(self, ventana):

        self.obj_modelo = BaseDeDatos()
        self.obj_valid = Validation()

        self.selected_id = 0

        self.root = ventana
        self.root.title("Control de Personal")
        self.root.geometry("633x450")

        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.root.iconbitmap(f"{dir_path}/img/icono.ico")

        # self.root.resizable(0, 0)

        # ------------------ ROW 0 ---------------------------------------------------------

        # Entry Options Label
        Label(
            self.root,
            text="INGRESO DE PERSONAL",
            background="purple3",
            foreground="white",
            width=80,
        ).grid(row=0, column=0, columnspan=6, sticky="nsew")

        # ------------------ ROW 1 ---------------------------------------------------------

        # Name Data Entry
        self.name_text = "ej: Fulano"
        Label(self.root, text="Nombre", width=15).grid(row=1, column=0, sticky=W)
        self.entry_name = Entry(self.root, textvariable=self.name_text, width=25)
        self.entry_name.grid(row=1, column=1)
        self.name_text = StringVar()
        self.entry_name.config(textvariable=self.name_text)
        self.name_text.set("ej: Fulano")
        self.entry_name.focus_set()

        # Surname Data Entry
        Label(self.root, text="Apellido", width=15).grid(row=1, column=2, sticky=W)
        self.entry_surname = Entry(self.root, width=25)
        self.entry_surname.grid(row=1, column=3)
        self.surname_text = StringVar()
        self.entry_surname.config(textvariable=self.surname_text)
        self.surname_text.set("ej: Pérez")

        # ------------------ ROW 2 ---------------------------------------------------------

        # Document Data Entry
        Label(self.root, text="Documento", width=15).grid(row=2, column=0, sticky=W)
        self.entry_dni = Entry(self.root, width=25)
        self.entry_dni.grid(row=2, column=1)
        self.dni_text = StringVar()
        self.entry_dni.config(textvariable=self.dni_text)
        self.dni_text.set("ej: 22222222")

        # Temperature Data Entry
        Label(self.root, text="Temperatura", width=15).grid(row=2, column=2, sticky=W)
        self.entry_temp = Entry(self.root, width=25)
        self.entry_temp.grid(row=2, column=3)
        self.temp_text = StringVar()
        self.entry_temp.config(textvariable=self.temp_text)
        self.temp_text.set("ej: 36.5")

        # ------------------ ROW 3 ---------------------------------------------------------

        # Phone Number Data Entry
        Label(self.root, text="Teléfono celular", width=15).grid(
            row=3, column=0, sticky=W
        )
        self.entry_phone = Entry(self.root, width=25)
        self.entry_phone.grid(row=3, column=1, columnspan=1)
        self.phone_text = StringVar()
        self.entry_phone.config(textvariable=self.phone_text)
        self.phone_text.set("ej: +5491134012500")

        # Email Data Entry
        Label(self.root, text="Email", width=15).grid(row=3, column=2, sticky=W)
        self.entry_mail = Entry(self.root, width=25)
        self.entry_mail.grid(row=3, column=3, columnspan=1)
        self.mail_text = StringVar()
        self.entry_mail.config(textvariable=self.mail_text)
        self.mail_text.set("ej: fulanoperez@gmail.com")

        # ------------------ ROW 4 ---------------------------------------------------------

        # Clear Data Entry Camps Button
        information_button = Button(
            self.root,
            command=lambda: self.info_window(),
            text="Ayuda",
            activebackground="green",
            activeforeground="white",
            padx=10,
        )
        information_button.grid(row=4, column=0, columnspan=1, sticky="ns")

        # Clear Data Entry Camps Button
        clear_data_entry_button = Button(
            self.root,
            command=lambda: self.clear_data(),
            text="Empezar denuevo",
            activebackground="green",
            activeforeground="white",
            padx=10,
        )
        clear_data_entry_button.grid(row=4, column=1, columnspan=1, sticky="ns")

        # Upload Data Button
        insert_data_button = Button(
            self.root,
            command=lambda: self.insert_data(),
            text="Cargar datos",
            activebackground="green",
            activeforeground="white",
            padx=15,
        )
        insert_data_button.grid(row=4, column=2, columnspan=1, sticky="ns")

        # Information Label
        Label(self.root, text="", width=15).grid(
            row=4, column=3, columnspan=6, sticky="w"
        )

        # ------------------ ROW 5 ---------------------------------------------------------

        # Database Label
        Label(
            self.root,
            text="BASE DE DATOS",
            background="purple3",
            foreground="white",
            width=80,
        ).grid(row=5, column=0, columnspan=6, sticky="nsew")

        # ------------------ ROW 6 ---------------------------------------------------------

        # ---------------------------- TREE VIEW -----------------------------------

        # Table
        columns = ("col0", "col1", "col2", "col3", "col4", "col5", "col6")
        self.data_table = ttk.Treeview(self.root, columns=columns, show="headings")

        self.data_table.column("col0", width=40, anchor=CENTER)
        self.data_table.column("col1", width=100, anchor=CENTER)
        self.data_table.column("col2", width=100, anchor=CENTER)
        self.data_table.column("col3", width=100, anchor=CENTER)
        self.data_table.column("col4", width=40, anchor=CENTER)
        self.data_table.column("col5", width=100, anchor=CENTER)
        self.data_table.column("col6", width=100, anchor=CENTER)

        self.data_table.heading("col0", text="Nº", anchor=CENTER)
        self.data_table.heading("col1", text="Nombre", anchor=CENTER)
        self.data_table.heading("col2", text="Apellido", anchor=CENTER)
        self.data_table.heading("col3", text="DNI", anchor=CENTER)
        self.data_table.heading("col4", text="Tº", anchor=CENTER)
        self.data_table.heading("col5", text="Celular", anchor=CENTER)
        self.data_table.heading("col6", text="Mail", anchor=CENTER)

        self.obj_modelo.actualizar_treeview(self.data_table)

        self.data_table.bind("<<TreeviewSelect>>", self.item_selected)

        self.data_table.grid(row=6, column=0, sticky="nsew", columnspan=5, rowspan=4)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(
            self.root, orient=VERTICAL, command=self.data_table.yview
        )
        self.data_table.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=6, column=5, sticky="ns", rowspan=6)

        # ------------------ ROW 13 ---------------------------------------------------------

        # Delete Row Button
        delete_register_button = Button(
            self.root,
            command=lambda: self.deleteData(),
            text="Eliminar fila",
            activebackground="green",
            activeforeground="white",
            padx=30,
        )
        delete_register_button.grid(row=13, column=1, columnspan=1, sticky="ns")

        # Modify Row Button
        modify_button = Button(
            self.root,
            command=lambda: self.setModifyID(),
            text="Modificar fila",
            activebackground="green",
            activeforeground="white",
            padx=30,
        )
        modify_button.grid(row=13, column=2, columnspan=1, sticky="ns")

        # ------------------ ROW 14 ---------------------------------------------------------

        Label(
            self.root,
            text="MODIFICAR INFORMACION DE PERSONAS",
            background="purple3",
            foreground="white",
            width=80,
        ).grid(row=14, column=0, columnspan=6, sticky="nsew")

        # ------------------ ROW 15 ---------------------------------------------------------

        Label(self.root, text="Nº a modificar", width=15).grid(
            row=15, column=0, sticky="w"
        )

        Label(self.root, text="Campo a modificar", width=15).grid(
            row=15, column=1, sticky="w"
        )

        Label(self.root, text="Nuevo valor", width=15).grid(
            row=15, column=2, sticky="w"
        )

        # ------------------ ROW 16 ---------------------------------------------------------

        self.entry_modify_before = Entry(self.root, width=25)
        self.entry_modify_before.grid(row=16, column=0, columnspan=1)

        self.entry_modify_after = Entry(self.root, width=25)
        self.entry_modify_after.grid(row=16, column=2, columnspan=1)

        self.combo_lsit = ttk.Combobox(self.root)
        self.combo_lsit.grid(row=16, column=1, columnspan=1)

        list_options = [
            "Nombre",
            "Apellido",
            "DNI",
            "Temperatura",
            "Teléfono",
            "email",
        ]

        self.combo_lsit["values"] = list_options
        self.combo_lsit.set("Nombre")
        # Modify Row Button
        modify_row_button = Button(
            self.root,
            command=lambda: self.updateData(),
            text="Modificar",
            activebackground="green",
            activeforeground="white",
            padx=30,
        )
        modify_row_button.grid(row=16, column=3, columnspan=1, sticky="ns")

    # ----------------------- DB COMMAND FUNCTIONS---------------------------------------------------
    def insert_data(self):
        if (
            self.obj_valid.valite_email(self.entry_mail.get())
            and self.obj_valid.valite_name(self.entry_name.get())
            and self.obj_valid.valite_name(self.entry_surname.get())
        ):
            self.obj_modelo.insertRegister(
                self.entry_name.get(),
                self.entry_surname.get(),
                self.entry_dni.get(),
                self.entry_temp.get(),
                self.entry_phone.get(),
                self.entry_mail.get(),
            )
            self.obj_modelo.actualizar_treeview(self.data_table)
            showinfo(
                title="Información alta de persona", message="Carga de datos exitosa!"
            )
            Label(self.root, text="Carga exitosa!", foreground="green", width=15).grid(
                row=4, column=3, columnspan=6, sticky="w"
            )
        else:
            if not self.obj_valid.valite_email(self.entry_mail.get()):
                showerror(
                    title="Error: mail ingresado incorrectamente",
                    message="El mail ingresado no es correcto, recuerde respetar el siguiente formato:\nejemplo@ejemplo.com",
                )
                Label(
                    self.root, text="Error en el mail", foreground="red", width=15
                ).grid(row=4, column=3, columnspan=6, sticky="w")
                return
            elif not self.obj_valid.valite_name(self.entry_name.get()):
                showerror(
                    title="Error: nombre ingresado incorrectamente",
                    message="El nombre ingresado no es correcto, recuerde respetar el siguiente formato:\nPrimera letra mayúscula\n Ejemplo: Agustín",
                )
                Label(
                    self.root, text="Error en el nombre", foreground="red", width=15
                ).grid(row=4, column=3, columnspan=6, sticky="w")
                return
            elif not self.obj_valid.valite_name(self.entry_surname.get()):
                showerror(
                    title="Error: apellido ingresado incorrectamente",
                    message="El apellido ingresado no es correcto, recuerde respetar el siguiente formato:\nPrimera letra mayúscula\n Ejemplo: Acevedo",
                )
                Label(
                    self.root, text="Error en el apellido", foreground="red", width=15
                ).grid(row=4, column=3, columnspan=6, sticky="w")
                return

    def deleteData(self):
        question_delete = askokcancel(
            title="Eliminar Persona",
            message="¿Esta seguro que desea eliminar todos los datos de la persona seleccionada?",
        )
        if question_delete == True:
            self.obj_modelo.deleteRegister(self.selected_id)
            self.obj_modelo.actualizar_treeview(self.data_table)
            Label(self.root, text="Fila eliminada", foreground="red", width=15).grid(
                row=4, column=3, columnspan=6, sticky="w"
            )

        elif question_delete == False:
            return

    def updateData(self):
        question_modify = askokcancel(
            title="Modificar Persona",
            message=f"¿Esta seguro que desea modificar el campo {self.combo_lsit.get()} de la persona seleccionada por {self.entry_modify_after.get()}?",
        )

        if question_modify == True:
            if self.combo_lsit.get() == "Nombre":
                if self.obj_valid.valite_name(self.entry_modify_after.get()):
                    self.obj_modelo.updateRegister(
                        self.entry_modify_before.get(),
                        self.combo_lsit.get(),
                        self.entry_modify_after.get(),
                    )
                    self.obj_modelo.actualizar_treeview(self.data_table)
                    Label(
                        self.root, text="Fila modificada", foreground="orange", width=15
                    ).grid(row=4, column=3, columnspan=6, sticky="w")

                else:
                    showerror(
                        title="Error: nombre ingresado incorrectamente",
                        message="El nombre ingresado no es correcto, recuerde respetar el siguiente formato:\nPrimera letra mayúscula\n Ejemplo: Agustin",
                    )
                    Label(
                        self.root, text="Error en el nombre", foreground="red", width=15
                    ).grid(row=4, column=3, columnspan=6, sticky="w")
                    return
            if self.combo_lsit.get() == "Apellido":
                if self.obj_valid.valite_name(self.entry_modify_after.get()):
                    self.obj_modelo.updateRegister(
                        self.entry_modify_before.get(),
                        self.combo_lsit.get(),
                        self.entry_modify_after.get(),
                    )
                    self.obj_modelo.actualizar_treeview(self.data_table)
                    Label(
                        self.root, text="Fila modificada", foreground="orange", width=15
                    ).grid(row=4, column=3, columnspan=6, sticky="w")

                else:
                    showerror(
                        title="Error: apellido ingresado incorrectamente",
                        message="El apellido ingresado no es correcto, recuerde respetar el siguiente formato:\nPrimera letra mayúscula\n Ejemplo: Acevedo",
                    )
                    Label(
                        self.root,
                        text="Error en el apellido",
                        foreground="red",
                        width=15,
                    ).grid(row=4, column=3, columnspan=6, sticky="w")
                    return

            if self.combo_lsit.get() == "email":
                if self.obj_valid.valite_email(self.entry_modify_after.get()):

                    self.obj_modelo.updateRegister(
                        self.entry_modify_before.get(),
                        self.combo_lsit.get(),
                        self.entry_modify_after.get(),
                    )
                    self.obj_modelo.actualizar_treeview(self.data_table)
                    Label(
                        self.root, text="Fila modificada", foreground="orange", width=15
                    ).grid(row=4, column=3, columnspan=6, sticky="w")

                else:
                    showerror(
                        title="Error: mail ingresado incorrectamente",
                        message="El mail ingresado no es correcto, recuerde respetar el siguiente formato:\nejemplo@ejemplo.com",
                    )
                    Label(
                        self.root, text="Error en el mail", foreground="red", width=15
                    ).grid(row=4, column=3, columnspan=6, sticky="w")
                    return
            else:
                self.obj_modelo.updateRegister(
                    self.entry_modify_before.get(),
                    self.combo_lsit.get(),
                    self.entry_modify_after.get(),
                )
                self.obj_modelo.actualizar_treeview(self.data_table)
                Label(
                    self.root, text="Fila modificada", foreground="orange", width=15
                ).grid(row=4, column=3, columnspan=6, sticky="w")

        elif question_modify == False:
            return

    # ----------------------- TK COMMAND FUNCTIONS----------------------------------------------------
    # clear data on data entry camps
    def clear_data(self):
        self.entry_name.config(textvariable=self.name_text)
        self.name_text.set("")
        self.entry_surname.config(textvariable=self.surname_text)
        self.surname_text.set("")
        self.entry_dni.config(textvariable=self.dni_text)
        self.dni_text.set("")
        self.entry_temp.config(textvariable=self.temp_text)
        self.temp_text.set("")
        self.entry_phone.config(textvariable=self.phone_text)
        self.phone_text.set("")
        self.entry_mail.config(textvariable=self.mail_text)
        self.mail_text.set("")
        self.entry_name.focus_set()

    def setModifyID(self):
        self.modify_id_text = StringVar()
        self.entry_modify_before.config(textvariable=self.modify_id_text)
        self.modify_id_text.set(self.selected_id)

    def item_selected(self, event):
        for selected_item in self.data_table.selection():
            item = self.data_table.item(selected_item)
            record = item["values"]
            self.selected_id = record[0]

    def info_window(
        self,
    ):

        child_w = Toplevel(self.root)
        child_w.grab_set()
        child_w.focus_set()

        child_w.geometry("480x395")
        child_w.title("Pestaña de ayuda")
        child_w.resizable(0, 0)

        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.python_image = PhotoImage(file=f"{dir_path}/img/help.PNG")
        ttk.Label(child_w, image=self.python_image).pack()
