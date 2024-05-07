#IMPORTACIONES DE KIVY 
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window

#IMPORTACION KIVYMD

from kivymd.app import MDApp



#IMPORTACION DE FUNCIONES
from screens.login import completo as login_completo
from screens.conectar_db import conectar_db
from screens.registro import nuevo_usuario
from screens.principal import calculo
from screens.principal import remis_confirmar
from screens.registro import verificar_codigo


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
        screen_manager.add_widget(Builder.load_file("kv/verificar_remiseria.kv"))
        screen_manager.add_widget(Builder.load_file("kv/inicio_chofer.kv"))
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
        nuevo_usuario (screen_manager, *args)

    def calculo(self):
        #'FUNCION PARA EL BOTON DE LA SCREEN INICIO QUE CALCULA LAS DISTANCIAS'
        calculo(screen_manager)

    def remis_confirmar(self,*args):
        remis_confirmar(screen_manager, *args)

    def inicio(self):
        screen_manager.current="inicio"

    def close(self, *args):
        self.dialog.dismiss()

    def verificar_codigo(self):
        verificar_codigo(screen_manager)


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