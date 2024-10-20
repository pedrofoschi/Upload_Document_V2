import flet as ft
from tkinter import filedialog

def main(page: ft.Page):
    page.title = 'New App'
    page.theme_mode = 'dark'
    # Fonts do aplicativo
    page.fonts = {
        "Poppins": "fonts/Poppins-Bold.ttf",
        "Poppins2": "fonts/Poppins-Light.ttf",
        "Poppins3": "fonts/Poppins-Regular.ttf",
        }

    # Efeito SnackBar
    def Snackbar(message: str, color: str = "green"):
            page.snack_bar = ft.SnackBar(ft.Text(message, color="White",style="Poppins"))
            page.snack_bar.open = True
            page.snack_bar.bgcolor = color
            page.update()

    def selecione(e):
        arquivo = ft.FilePicker()
        if not arquivo:
            Snackbar =('📁 Arquivos não selecionados !', 'Red')
        else:
            Snackbar =('📁 Arquivos selecionados com sucesso !','Green')
    

    selectArq = ft.ElevatedButton(
        "Teste",
        on_click=selecione,
        style=ft.ButtonStyle(
            color='white',
            bgcolor='Black',
            overlay_color='Red'
        )
    )

    page.add(
       ft.Row([selectArq])
        )


print('asas')

ft.app(main)