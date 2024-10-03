import re
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from screens.conectar_db import conectar_db


miConexion = conectar_db()
if miConexion:
    miCursor = miConexion.cursor()
else:
    print("Error: Unable to connect to database")

def nuevo_usuario(screen_manager, verificar_datos=True, *args):
    if verificar_datos:
        switch_activado = screen_manager.get_screen('registro').ids['switch_activado']
        switch_estado = switch_activado.active

        if switch_estado:  # Si el switch está activado
            # Realizar verificación de datos antes de pasar a la próxima pantalla
            email_valido = validar_email(screen_manager)
            contraseñas_validas = validar_contraseñas(screen_manager)
            if email_valido and contraseñas_validas:
                datos_registro = obtener_datos_registro(screen_manager)
                screen_manager.datos_registro = datos_registro
                screen_manager.current = "verificar_remiseria"
            else:
                if not email_valido:
                    show_error_dialog(screen_manager, "Correo no válido, intente nuevamente")
                if not contraseñas_validas:
                    show_error_dialog(screen_manager, "Las contraseñas no coinciden o están vacías, intente nuevamente")
        else:
            # Realizar verificaciones y registro en la base de datos
            datos_registro = obtener_datos_registro(screen_manager)

            if miCursor and miConexion:
                # Ejecutar la consulta de inserción solo si la conexión es válida
                registro_ejecucion = 'INSERT INTO public."Clientes" (nombre,id_localidad,telefono,direccion,correo,password,tipo_cuenta) VALUES (%s,%s,%s,%s,%s,%s,%s)'
                miCursor.execute(registro_ejecucion, datos_registro)
                miConexion.commit()

                # Verificar si la inserción fue exitosa
                if miCursor.rowcount > 0:
                    screen_manager.current = "login"
                    show_success_dialog(screen_manager, "Su cuenta ha sido creada exitosamente")
                else:
                    show_error_dialog(screen_manager, "Error al crear la cuenta. Intente nuevamente.")
            else:
                show_error_dialog(screen_manager, "Error: No se pudo conectar a la base de datos")
    else:
        # Realizar verificaciones y registro en la base de datos sin verificar datos
        datos_registro = obtener_datos_registro(screen_manager)

        if miCursor and miConexion:
            # Ejecutar la consulta de inserción solo si la conexión es válida
            registro_ejecucion = 'INSERT INTO public."Clientes" (nombre,id_localidad,telefono,direccion,correo,password,tipo_cuenta) VALUES (%s,%s,%s,%s,%s,%s,%s)'
            miCursor.execute(registro_ejecucion, datos_registro)
            miConexion.commit()

            # Verificar si la inserción fue exitosa
            if miCursor.rowcount > 0:
                screen_manager.current = "login"
                show_success_dialog(screen_manager, "Su cuenta ha sido creada exitosamente")
            else:
                show_error_dialog(screen_manager, "Error al crear la cuenta. Intente nuevamente.")
        else:
            show_error_dialog(screen_manager, "Error: No se pudo conectar a la base de datos")



def validar_email(screen_manager):
    mail = screen_manager.get_screen('registro').ids['input_email'].text
    return re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$', mail.lower())


def validar_contraseñas(screen_manager):
    password = screen_manager.get_screen('registro').ids['input_password'].text
    password_c = screen_manager.get_screen('registro').ids['input_password_confirmation'].text
    return password == password_c and len(password) >= 5


def obtener_datos_registro(screen_manager):
    nombre = screen_manager.get_screen('registro').ids['input_name'].text
    direccion = screen_manager.get_screen('registro').ids['input_direc'].text
    localidad = screen_manager.get_screen('registro').ids['input_loc'].text
    telefono = screen_manager.get_screen('registro').ids['input_phone'].text
    mail = screen_manager.get_screen('registro').ids['input_email'].text
    password = screen_manager.get_screen('registro').ids['input_password'].text
    tipo_cuenta = 2 if screen_manager.get_screen('registro').ids['switch_activado'].active else 1
    localidad = str(localidad)

    busca_loc = f'SELECT id_localidad FROM public."Localidad" WHERE nombre = \'{localidad}\''
    miCursor.execute(busca_loc)
    id_localidad = miCursor.fetchone()

    return (nombre, id_localidad, telefono, direccion, mail, password, tipo_cuenta)


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


def verificar_codigo(screen_manager):
    codigo_verificacion = screen_manager.get_screen('verificar_remiseria').ids['verificacion'].text

    if codigo_verificacion == "R3M1S":
        print("Código correcto, llamando a nuevo_usuario")
        screen_manager.get_screen('registro').ids['switch_activado'].active = True  # Cambiar el tipo de cuenta a 2
        nuevo_usuario(screen_manager, verificar_datos=False)
    else:
        show_error_dialog(screen_manager, "Código incorrecto")
