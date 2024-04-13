#IMPORTACIONES DE KIVY 
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window

#IMPORTACION KIVYMD

from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


#IMPORTACION BSD
from screens.login import completo as login_completo
from screens.conectar_db import conectar_db
from screens.registro import nuevo_usuario

#IMPORTACION DE GOOGLE MAPS
import googlemaps

#Leer API Key desde un archivo externo
API = open("Google Maps Platform API Key.txt","r")
APIKey = API.read()
Maps = googlemaps.Client(key=APIKey)

#Variables y otros
Window.size = (300,580)

class LoginApp(MDApp):
    
    Label = None
    miCursor = None
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        #self.manager = ScreenManager(transition=NoTransition())
        screen_manager.add_widget(Builder.load_file("kv/pre-splash.kv"))
        screen_manager.add_widget(Builder.load_file("kv/login.kv"))
        screen_manager.add_widget(Builder.load_file("kv/registro.kv"))
        screen_manager.add_widget(Builder.load_file("kv/remises.kv"))
        screen_manager.add_widget(Builder.load_file("kv/inicio.kv"))
        screen_manager.add_widget(Builder.load_file("kv/base.kv"))
        return screen_manager
    
    def on_start(self):
        #TRANSICION DE PANTALLA DE INICIO'
        Clock.schedule_once(self.login, 3)

    def login (self,*args):
        #PANTALLA DE INICIO
        screen_manager.current = "login"

    def registro(self, *args):
        if self.miCursor:  # Check if miCursor is initialized
            busca = 'SELECT nombre FROM public."Localidad"'
            self.miCursor.execute(busca)
            valores = [row[0] for row in self.miCursor.fetchall()]
            lista_spinner = screen_manager.get_screen('registro').ids['input_loc']
            lista_spinner.values = valores
            screen_manager.current = "registro"
        else:
            print("Error: miCursor is not initialized.")
    
    def remises(self,*args):
        screen_manager.current = "remises"

    def completo(self, miCursor, *args):
        # FUNCION PARA COMPARAR LOS VALORES DE LA PANTALLA CON LA BASE DE DATOS
        login_completo(app=self, screen_manager=screen_manager, miCursor=miCursor, close_dialog_callback=self.close, *args)


    def nuevo_usuario(self, *args):
        # Call nuevo_usuario function from registro.py
        nuevo_usuario (screen_manager, self.miCursor, *args)

    def calculo(self):
    #'FUNCION PARA EL BOTON DE LA SCREEN INICIO QUE CALCULA LAS DISTANCIAS'
        salida= screen_manager.get_screen('inicio').ids['salida'].text
        llegada= screen_manager.get_screen('inicio').ids['llegada'].text
        if salida != "" and llegada != "":
            Distancia=Maps.directions(salida,llegada)
            DistanciaKM = (Distancia[0]['legs'][0]['distance']['text'])
            HorasMinDuracion= (Distancia[0]['legs'][0]['duration']['text'])
            screen_manager.get_screen('inicio').ids['l_salida'].text = f'{salida}'
            screen_manager.get_screen('inicio').ids['l_llegada'].text = f'{llegada}'
            screen_manager.get_screen('inicio').ids['l_distancia'].text = f'{DistanciaKM}'
            screen_manager.get_screen('inicio').ids['l_duracion'].text = f'{HorasMinDuracion}'

    def inicio(self):
        screen_manager.current="inicio"

    def close(self, *args):
        self.dialog.dismiss()


    def remis_confirmar(self,*args):
            self.dialog = MDDialog(
                    title = 'Confirmacion',
                    text= '¿Confirma que quiere realizar el pedido?',
                    buttons=[
                        MDFlatButton(
                            text="Si",
                            text_color=self.theme_cls.accent_color,
                            on_release=self.callback_yes
                        ),
                        MDFlatButton(
                            text="No",
                            text_color=self.theme_cls.accent_color,
                            on_release=self.callback_no
                        )
                    ]
                )

            self.dialog.open()      

    def callback_yes(self, *args):
        # Actions to perform when "Si" is pressed
        self.dialog.dismiss()
        screen_manager.current = "base"  # Change to another screen

    def callback_no(self, *args):
        # Actions to perform when "No" is pressed
        self.dialog.dismiss()  # Close the dialog

if __name__ == '__main__':
    app = LoginApp()
    app.miConexion = conectar_db()
    if app.miConexion:
        app.miCursor = app.miConexion.cursor()
        app.run()
        app.miConexion.close()
    else:
        print("Error: Unable to connect to database")

    # Close the connection outside the app's scope
    if app.miConexion:
        app.miConexion.close()