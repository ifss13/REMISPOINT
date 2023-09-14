#IMPORTACIONES DE KIVY
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivymd.uix.bottomnavigation import bottomnavigation
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import re

#IMPORTACION BSD

import sqlite3
miConexion = sqlite3.connect("bsd_remispoing.sqlite3")
miCursor = miConexion.cursor()

#IMPORTACION DE GOOGLE MAPS
import googlemaps

#Leer API Key desde un archivo externo
API = open("Google Maps Platform API Key.txt","r")
APIKey = API.read()
Maps = googlemaps.Client(key=APIKey)

Window.size = (300,580)


class LoginApp(MDApp):
    dialog = None #
    Label = None
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        #self.manager = ScreenManager(transition=NoTransition())
        screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("registro.kv"))
        screen_manager.add_widget(Builder.load_file("inicio.kv"))
        return screen_manager
    
    #TRANSICION DE PANTALLA DE INICIO
    def on_start(self):
        Clock.schedule_once(self.login, 3)

    #PANTALLA DE INICIO
    def login (self,*args):
        screen_manager.current = "login"

    #PANTALLA DE REGISTRO
    def registro(self,*args):
        screen_manager.current = "registro"

    #FUNCION PARA COMPARAR LOS VALORES DE LA PANTALLA CON LA BASE DE DATOS
    def completo (self,*args):
        email= screen_manager.get_screen('login').ids['mail'].text
        password = screen_manager.get_screen('login').ids['password'].text
        busca = f"SELECT email, password FROM Cliente WHERE email = '{email}' AND password = '{password}'; "
        miCursor.execute(busca)
        if miCursor.fetchone():
            screen_manager.current = "inicio"

    #FUNCION PARA EL BOTON REGISTRO DE LA PANTALLA REGISTRO Y AGREGADO A LA BASE DE DATOS
    def nuevo_usuario (self, *args):
        user = []
        nombre = screen_manager.get_screen('registro').ids['input_name'].text
        telefono = screen_manager.get_screen('registro').ids['input_phone'].text
        mail = screen_manager.get_screen('registro').ids['input_email'].text
        password = screen_manager.get_screen('registro').ids['input_password'].text
        password_c = screen_manager.get_screen('registro').ids['input_password_confirmation'].text
        lista = (nombre,telefono,mail,password)
        user.append(lista)
        if re.match('^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$',mail.lower()):
            long= len(telefono)
            if long >= 10:
                long_pass = len(password)
                if password != password_c:
                    self.dialog = MDDialog(
                    title = 'Contraseña Incorrecta',
                    text= 'Las contraseñas no coinciden o estan vacias, intete nuevamente',
                    buttons = [
                        MDFlatButton(
                            text= "Ok", text_color= self.theme_cls.accent_color,
                            on_release = self.close,
                            )
                        ]
                    )
                    self.dialog.open()
                elif long_pass < 5:
                    self.dialog = MDDialog(
                        title = 'Contraseña Incorrecta',
                        text= 'Las contraseñas deben tener 5 o mas caracteres de longitud',
                        buttons = [
                            MDFlatButton(
                                text= "Ok", text_color= self.theme_cls.accent_color,
                                on_release = self.close,
                            )
                        ]
                    )   
                    self.dialog.open()
                elif password == password_c:
                    registro_ejecucion = "INSERT INTO Cliente (id_cliente,Nombre,Telefono,email,password) VALUES (NULL,?,?,?,?)"
                    miCursor.executemany(registro_ejecucion,user)
                    miConexion.commit()
                    screen_manager.current = "login"
                    self.dialog = MDDialog(
                        title = 'Registro Exitoso',
                        text= 'Su cuenta a sido creada exitosamente',
                        buttons = [
                            MDFlatButton(
                                text= "Ok", text_color= self.theme_cls.accent_color,
                                on_release = self.close,
                            )
                        ]
                    )
                    self.dialog.open()
                else:
                    self.dialog = MDDialog(
                        title = 'Contraseña Incorrecta',
                        text= 'Las contraseñas deben tener 5 o mas caracteres de longitud',
                        buttons = [
                            MDFlatButton(
                                text= "Ok", text_color= self.theme_cls.accent_color,
                                on_release = self.close,
                            )
                        ]
                    )
            else:
                self.dialog = MDDialog(
                    title = 'Telefono',
                    text= 'Numero de telefono no valido, intente nuevamente',
                    buttons = [
                        MDFlatButton(
                            text= "Ok", text_color= self.theme_cls.accent_color,
                            on_release = self.close,
                            )
                        ]
                    )
                self.dialog.open()
        else:
            self.dialog = MDDialog(
                    title = 'Correo',
                    text= 'Correo no valido, intente nuevamente',
                    buttons = [
                        MDFlatButton(
                            text= "Ok", text_color= self.theme_cls.accent_color,
                            on_release = self.close,
                        )
                    ]
                )
            self.dialog.open()

    #FUNCION PARA EL BOTON DE LA SCREEN INICIO QUE CALCULA LAS DISTANCIAS
    def calculo(self):
        salida= screen_manager.get_screen('inicio').ids['salida'].text
        llegada= screen_manager.get_screen('inicio').ids['llegada'].text
        if salida != "" and llegada != "":
            Distancia=Maps.directions(salida,llegada)
            DistanciaKM = (Distancia[0]['legs'][0]['distance']['text'])
            HorasMinDuracion= (Distancia[0]['legs'][0]['duration']['text'])
            #if not self.dialog:
            self.dialog = MDDialog(
                title = 'Viaje',
                text= f'La distanncia entre {salida} y {llegada} es de {DistanciaKM} y la duracion del viaje es de {HorasMinDuracion} y el precio es de $!',
                buttons = [
                    MDFlatButton(
                        text= "Ok", text_color= self.theme_cls.accent_color,
                        on_release = self.close,
                    )
                ]
            )
            self.dialog.open()

    def close(self,*args):
        self.dialog.dismiss()               

if __name__ == '__main__':
    LoginApp().run()

miConexion.close()