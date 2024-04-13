# Import necessary modules
import re
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from screens import conectar_db

def nuevo_usuario(screen_manager, miCursor, dialog, theme_cls, close):
    miConexion = conectar_db.conectar_db()
    miCursor = miConexion.cursor()
    user = []
    nombre = screen_manager.get_screen('registro').ids['input_name'].text
    direccion = screen_manager.get_screen('registro').ids['input_direc'].text
    localidad = screen_manager.get_screen('registro').ids['input_loc'].text
    telefono = screen_manager.get_screen('registro').ids['input_phone'].text
    mail = screen_manager.get_screen('registro').ids['input_email'].text
    password = screen_manager.get_screen('registro').ids['input_password'].text
    password_c = screen_manager.get_screen('registro').ids['input_password_confirmation'].text
    tipo_cuenta = 1  # Assuming this is a default value
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
                dialog = MDDialog(
                    title='Contraseña Incorrecta',
                    text='Las contraseñas no coinciden o están vacías, intente nuevamente',
                    buttons=[
                        MDFlatButton(
                            text="Ok",
                            text_color=theme_cls.accent_color,
                            on_release=close,
                        )
                    ]
                )
                dialog.open()
            elif long_pass < 5:
                dialog = MDDialog(
                    title='Contraseña Incorrecta',
                    text='Las contraseñas deben tener 5 o más caracteres de longitud',
                    buttons=[
                        MDFlatButton(
                            text="Ok",
                            text_color=theme_cls.accent_color,
                            on_release=close,
                        )
                    ]
                )
                dialog.open()
            elif password == password_c:
                registro_ejecucion = 'INSERT INTO public."Clientes" (nombre,id_localidad,telefono,direccion,correo,password,tipo_cuenta) VALUES (%s,%s,%s,%s,%s,%s,%s)'
                miCursor.executemany(registro_ejecucion, user)
                miConexion.commit()
                screen_manager.current = "login"
                dialog = MDDialog(
                    title='Registro Exitoso',
                    text='Su cuenta ha sido creada exitosamente',
                    buttons=[
                        MDFlatButton(
                            text="Ok",
                            text_color=theme_cls.accent_color,
                            on_release=close,
                        )
                    ]
                )
                dialog.open()
            else:
                dialog = MDDialog(
                    title='Contraseña Incorrecta',
                    text='Las contraseñas deben tener 5 o más caracteres de longitud',
                    buttons=[
                        MDFlatButton(
                            text="Ok",
                            text_color=theme_cls.accent_color,
                            on_release=close,
                        )
                    ]
                )
                dialog.open()
        else:
            dialog = MDDialog(
                title='Telefono',
                text='Número de teléfono no válido, intente nuevamente',
                buttons=[
                    MDFlatButton(
                        text="Ok",
                        text_color=theme_cls.accent_color,
                        on_release=close,
                    )
                ]
            )
            dialog.open()
    else:
        dialog = MDDialog(
            title='Correo',
            text='Correo no válido, intente nuevamente',
            buttons=[
                MDFlatButton(
                    text="Ok",
                    text_color=theme_cls.accent_color,
                    on_release=close,
                )
            ]
        )
        dialog.open()