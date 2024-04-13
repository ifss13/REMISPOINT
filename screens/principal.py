from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
import googlemaps

# Leer API Key desde un archivo externo
API = open("./Google Maps Platform API Key.txt", "r")
APIKey = API.read()
Maps = googlemaps.Client(key=APIKey)

def remis_confirmar(screen_manager):
    # Create the dialog instance and store it in a variable
    dialog = MDDialog(
        title='Confirmacion',
        text='¿Confirma que quiere realizar el pedido?',
        buttons=[
            MDFlatButton(
                text="Si",
                on_release=lambda *args: callback_yes(screen_manager, dialog),
            ),
            MDFlatButton(
                text="No",
                on_release=lambda *args: callback_no(dialog),
            )
        ]
    )

    dialog.open()

def callback_yes(screen_manager, dialog, *args):
    # Actions to perform when "Si" is pressed
    dialog.dismiss()
    screen_manager.current = "base"  # Change to another screen

def callback_no(dialog, *args):
    # Actions to perform when "No" is pressed
    dialog.dismiss()  # Close the dialog

def calculo(screen_manager):
    #'FUNCION PARA EL BOTON DE LA SCREEN INICIO QUE CALCULA LAS DISTANCIAS'
    salida = screen_manager.get_screen('inicio').ids['salida'].text
    llegada = screen_manager.get_screen('inicio').ids['llegada'].text
    if salida != "" and llegada != "":
        Distancia = Maps.directions(salida, llegada)
        DistanciaKM = Distancia[0]['legs'][0]['distance']['text']
        HorasMinDuracion = Distancia[0]['legs'][0]['duration']['text']
        screen_manager.get_screen('inicio').ids['l_salida'].text = f'{salida}'
        screen_manager.get_screen('inicio').ids['l_llegada'].text = f'{llegada}'
        screen_manager.get_screen('inicio').ids['l_distancia'].text = f'{DistanciaKM}'
        screen_manager.get_screen('inicio').ids['l_duracion'].text = f'{HorasMinDuracion}'
