import flet as ft
import time
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
    def Snackbar(message:str,color: str):
            page.snack_bar = ft.SnackBar(
                  ft.Text(message,
                          color="White",
                          font_family="Poppins"))
            page.snack_bar.open = True
            page.snack_bar.bgcolor = color
            page.update()
            time.sleep(3)

    def arquivo_selecionado(e):
            if e.files:  # Verifica se o usuário selecionou algum arquivo
                arquivo = e.files[0].path  # Pega o caminho do primeiro arquivo
                Snackbar(f"Arquivo selecionado: {arquivo}", "Green")
                
            else:
                Snackbar("Arquivo não selecionado","Red")
            page.update()

    def pesquisar(e):
          Snackbar(f"Você digitou: {search.value}","Teal")
          page.update()

    botao_pesquisar = ft.ElevatedButton("Pesquisar",on_click=pesquisar)
    search = ft.TextField(focused_border_color="Green")

    seletor_arquivo = ft.FilePicker(on_result=arquivo_selecionado)

    Title = ft.Text("Google API with my bro Pedro Forrosky",
                    font_family="Poppins",
                      size=30)
    botao_selecionar = ft.ElevatedButton(
            text="Selecionar Arquivo",
            on_click=lambda _: seletor_arquivo.pick_files()  # Abre o FilePicker quando clicado
        )
    
    page.add(
        ft.ResponsiveRow([Title]),
        ft.Row([seletor_arquivo,botao_selecionar,search,botao_pesquisar])
        )

    
ft.app(main)
