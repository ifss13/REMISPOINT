import asyncio
import websockets
from threading import Thread

# Importaciones de Kivy y KivyMD
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivymd.app import MDApp


#Variables y otros
Window.size = (300,580)

# Clase principal de la aplicación
class LoginApp(MDApp):
    def build(self):
        # Ejecutar el servidor de WebSockets en un hilo separado
        self.run_server_thread()

        # Configuración del ScreenManager y carga de pantallas
        global screen_manager
        screen_manager = ScreenManager()
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
        # Transición a la pantalla de login después de 3 segundos
        Clock.schedule_once(self.login, 3)

    def login(self, *args):
        # Cambiar a la pantalla de login
        screen_manager.current = "login"

    # Aquí añadimos el servidor de WebSockets
    def start_websockets_server(self):
        async def echo(websocket, path):
            async for message in websocket:
                await websocket.send(f"Echo: {message}")

        server = websockets.serve(echo, "localhost", 8765)

        asyncio.get_event_loop().run_until_complete(server)
        asyncio.get_event_loop().run_forever()

    def run_server_thread(self):
        ws_thread = Thread(target=self.start_websockets_server)
        ws_thread.daemon = True
        ws_thread.start()

# Punto de entrada de la aplicación
if __name__ == "__main__":
    LoginApp().run()
