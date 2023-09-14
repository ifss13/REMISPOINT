#IMPORTACION DE KIVY
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy.core.window import Window



#IMPORTACION DE GOOGLE MAPS
import googlemaps

#Leer API Key desde un archivo externo
API = open("Google Maps Platform API Key.txt","r")
APIKey = API.read()
Maps = googlemaps.Client(key=APIKey)

#TAMAÑO DE VENTANA 
Window.size = (500,700)


#DISEÑO DE OBJETOS
KV='''
Screen:

    MDCard:
        size_hint: None, None
        size: 350, 650
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        elevation: 10
        padding: 65
        spacing: 35
        orientation: 'vertical'
        MDIcon:
            icon: 'car-clock'
            icon_color: 0,0,0,0
            halign: 'center'
            font_size: 180
        MDTextField:
            id: salida
            hint_text: "Salida"
            foreground_color: 1,0,1,1
            size_hint_x: None
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5}
        MDTextField:
            id: llegada
            hint_text: "Llegada"
            foreground_color: 1,0,1,1
            size_hint_x: None
            width: 220
            font_size: 20
            pos_hint: {"center_x": 0.5}
        MDFillRoundFlatButton
            text: "CALCULAR"
            font_size: 15
            pos_hint: {"center_x": 0.5}
            on_press: app.login()

'''

class LoginApp(MDApp):
    dialog = None #


    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Orange'
        self.theme_cls.accent_palette = 'Blue'



        return Builder.load_string(KV)
    
    
    def login(self):
        if self.root.ids.salida.text != "" and self.root.ids.llegada.text != "":
            Llegada = self.root.ids.llegada.text
            Salida = self.root.ids.salida.text
            Distancia = Maps.directions(Salida,Llegada)
            DistanciaKM = (Distancia[0]['legs'][0]['distance']['text'])
            HorasMinDuracion= (Distancia[0]['legs'][0]['duration']['text'])
            if not self.dialog:
                self.dialog = MDDialog(
                    title = 'Viaje',
                    text= f'La distancia entre {Salida} y {Llegada} es de {DistanciaKM} y la duracion del viaje es de {HorasMinDuracion} y el precio es de $!',
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


LoginApp().run()
