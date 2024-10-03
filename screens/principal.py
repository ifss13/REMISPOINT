import googlemaps.directions
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivy_garden.mapview import MapView
import googlemaps
from screens import conectar_db

kivy_garden = MapView

from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

def remis_confirmar(screen_manager):
    dialog = MDDialog(
        title='Confirmación',
        text='¿Confirma que quiere realizar el pedido?',
        buttons=[
            MDFlatButton(
                text="Sí",
                on_release=lambda *args: callback_yes(screen_manager, dialog),
            ),
            MDFlatButton(
                text="No",
                on_release=lambda *args: callback_no(dialog),
            )
        ]
    )
    dialog.open()

def callback_yes(screen_manager, dialog):
    try:
        miConexion = conectar_db.conectar_db()  # Conectar a la base de datos
        miCursor = miConexion.cursor()

        # Obtener el email del cliente logueado
        email = screen_manager.get_screen('inicio').ids['email'].text
        
        # Buscar el id_cliente basado en el email
        query_id_cliente = 'SELECT id_cliente FROM public."Clientes" WHERE correo = %s'
        miCursor.execute(query_id_cliente, (email,))
        result = miCursor.fetchone()

        if result is not None:
            id_cliente = result[0]

            # Obtener dir_salida y dir_destino del archivo KV
            dir_salida = screen_manager.get_screen('remises').ids['dir_salida'].text
            dir_destino = screen_manager.get_screen('remises').ids['dir_destino'].text
            datos_insertar = (id_cliente,dir_salida,dir_destino)
            print(datos_insertar)

            # Insertar el pedido en la base de datos
            query_insert = 'INSERT INTO public."PedidoCliente" (id_cliente, dir_salida, dir_destino) VALUES (%s, %s, %s)'
            miCursor.execute(query_insert, datos_insertar)
            miConexion.commit()

            print("Pedido confirmado y registrado en la base de datos.")
        else:
            print(f"No se encontró un cliente con el correo: {email}")

    except Exception as e:
        print(f"Error al realizar el pedido: {e}")
    finally:
        if miConexion:
            miConexion.close()
        dialog.dismiss()

def callback_no(dialog):
    print("Pedido cancelado.")
    dialog.dismiss()


def calcular_y_mostrar_ruta(screen_manager):
    salida = screen_manager.get_screen('inicio').ids['salida'].text
    llegada = screen_manager.get_screen('inicio').ids['llegada'].text
    google_maps_api_key = 'AIzaSyADCWdmWSSVPDQwFbjx7smd92mgKq7fzFQ'

    if not salida or not llegada:
        return

    gmaps = googlemaps.Client(key=google_maps_api_key)
    direcciones = gmaps.directions(salida, llegada, mode="driving")

    if direcciones:
        mapview = kivy_garden.map
        points = direcciones[0]['overview_polyline']['points']


def demora(screen_manager):
    miConexion = conectar_db.conectar_db()  # Establish database connection
    miCursor = miConexion.cursor()
    miCursor.execute('SELECT COUNT(*) FROM public."PedidoCliente";')
    cantidad_registros = miCursor.fetchone()[0]
    if cantidad_registros == 0:
        screen_manager.get_screen('remises').ids['demora'].text = f'No posee demoras'
    else:
        minutos_demoras = cantidad_registros * 15
        screen_manager.get_screen('remises').ids['demora'].text = f'Demora aproximada: {minutos_demoras} minutos.'

        