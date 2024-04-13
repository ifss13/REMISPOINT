from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from screens import conectar_db

def open_dialog(screen_manager):
    # Create the dialog instance and store it in a variable
    dialog = MDDialog(
        title='Contraseña Incorrecta',
        text='El usuario o la contraseña no son correctos',
        buttons=[
            MDFlatButton(
                text="Ok",
                on_release=lambda *args: close_dialog(dialog),
            )
        ]
    )
    dialog.open()  # Open the dialog after creating it

def close_dialog(dialog_instance):
    # Dismiss the dialog instance that is passed as an argument
    if dialog_instance:
        dialog_instance.dismiss()

def completo(app, screen_manager, miCursor, close_dialog_callback, *args):
    miConexion = conectar_db.conectar_db()  # Establish database connection
    miCursor = miConexion.cursor()
    if miConexion:
        try:
            email = screen_manager.get_screen('login').ids['mail'].text
            password = screen_manager.get_screen('login').ids['password'].text
            busca = f'SELECT correo, password FROM public."Clientes" WHERE correo = \'{email}\' AND password = \'{password}\''
            c_nombre = f'SELECT Nombre FROM public."Clientes" WHERE correo = \'{email}\' AND password = \'{password}\''
            c_email = f'SELECT correo FROM public."Clientes" WHERE correo = \'{email}\' AND password = \'{password}\''
            c_tel = f'SELECT Telefono FROM public."Clientes" WHERE correo = \'{email}\' AND password = \'{password}\''
            c_direc = f'SELECT direccion FROM public."Clientes" WHERE correo = \'{email}\' AND password = \'{password}\''
            miCursor.execute(busca)
            if miCursor.fetchone():
                miCursor.execute(c_nombre)
                nombrelogin = miCursor.fetchone()
                nombrelogin = str(nombrelogin)
                nombrelogin = nombrelogin.strip("()").replace("'", "").replace(",", "")
                screen_manager.get_screen('inicio').ids['bienvenido'].text = f'Bienvenido/a {nombrelogin}'
                screen_manager.get_screen('inicio').ids['l_nombre'].text = f'{nombrelogin}'

                miCursor.execute(c_email)
                mail = miCursor.fetchone()
                mail = str(mail)
                mail = mail.strip("()").replace("'", "").replace(",", "")
                screen_manager.get_screen('inicio').ids['email'].text = f'{mail}'

                miCursor.execute(c_tel)
                tel = miCursor.fetchone()
                tel = str(tel)
                tel = tel.strip("()").replace("'", "").replace(",", "")
                screen_manager.get_screen('inicio').ids['telefono'].text = f'{tel}'

                miCursor.execute(c_direc)
                dire = miCursor.fetchone()
                dire = str(dire)
                dire = dire.strip("()").replace("'", "").replace(",", "")
                screen_manager.get_screen('inicio').ids['direccion'].text = f'{dire}'
                screen_manager.current = "inicio"
            else:
                open_dialog(screen_manager)
        except Exception as e:
            print(f"Error with database operations: {e}")
            miConexion.close()  # Close database connection on error
    else:
        print("Error: Unable to connect to database")

