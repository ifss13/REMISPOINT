from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton


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
    pass
