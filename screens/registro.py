import re
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from screens.conectar_db import conectar_db

def nuevo_usuario(screen_manager, miCursor, *args):

    # Connect to the database
    miConexion = conectar_db()
    if miConexion:
        miCursor = miConexion.cursor()
    else:
        print("Error: Unable to connect to database")

    # 'FUNCION PARA EL BOTON REGISTRO DE LA PANTALLA REGISTRO Y AGREGADO A LA BASE DE DATOS'
    user = []
    nombre = screen_manager.get_screen('registro').ids['input_name'].text
    direccion = screen_manager.get_screen('registro').ids['input_direc'].text
    localidad = screen_manager.get_screen('registro').ids['input_loc'].text
    telefono = screen_manager.get_screen('registro').ids['input_phone'].text
    mail = screen_manager.get_screen('registro').ids['input_email'].text
    password = screen_manager.get_screen('registro').ids['input_password'].text
    password_c = screen_manager.get_screen('registro').ids['input_password_confirmation'].text
    tipo_cuenta = 1
    tipo_cuenta = int(tipo_cuenta)
    localidad = str(localidad)
    busca_loc = f'SELECT id_localidad FROM public."Localidad" WHERE nombre = \'{localidad}\''
    miCursor.execute(busca_loc)
    id_localidad = miCursor.fetchone()
    lista = (nombre, id_localidad, telefono, direccion, mail, password, tipo_cuenta)
    user.append(lista)
    if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', mail.lower()):
        long = len(telefono)
        if long >= 10:
            long_pass = len(password)
            if password != password_c:
                show_error_dialog(screen_manager, "Las contraseñas no coinciden o están vacías, intente nuevamente")
            elif long_pass < 5:
                show_error_dialog(screen_manager, "Las contraseñas deben tener 5 o más caracteres de longitud")
            elif password == password_c:
                registro_ejecucion = 'INSERT INTO public."Clientes" (nombre,id_localidad,telefono,direccion,correo,password,tipo_cuenta) VALUES (%s,%s,%s,%s,%s,%s,%s)'
                miCursor.executemany(registro_ejecucion, user)
                miConexion.commit()
                screen_manager.current = "login"
                show_success_dialog(screen_manager, "Su cuenta ha sido creada exitosamente")
        else:
            show_error_dialog(screen_manager, "Número de teléfono no válido, intente nuevamente")
    else:
        show_error_dialog(screen_manager, "Correo no válido, intente nuevamente")

def show_error_dialog(screen_manager, message):
    dialog = MDDialog(
        title='Error',
        text=message,
        buttons=[
            MDFlatButton(
                text="Ok",
                on_release=lambda *args: dialog.dismiss()
            )
        ]
    )
    dialog.open()

def show_success_dialog(screen_manager, message):
    dialog = MDDialog(
        title='Registro Exitoso',
        text=message,
        buttons=[
            MDFlatButton(
                text="Ok",
                on_release=lambda *args: dialog.dismiss(),
            )
        ]
    )
    dialog.open()

