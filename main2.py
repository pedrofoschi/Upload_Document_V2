import flet as ft
import time
def main(page: ft.Page):
    page.title = 'UploadDocument'
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
                result.value= f'{arquivo}' 
            else:
                Snackbar("Arquivo não selecionado","Red")
            page.update()

    
    selecao_local = ft.Dropdown(
        hint_text='Selecione uma opção...',
        options=[
            ft.dropdown.Option('1'),
            ft.dropdown.Option('2'),
            ft.dropdown.Option('3')
        ]
    )

    result = ft.TextField('',width=600,read_only=True)

    seletor_arquivo = ft.FilePicker(on_result=arquivo_selecionado)
    botao_selecionar = ft.ElevatedButton(
            text="Selecionar Arquivo",
            on_click=lambda _: seletor_arquivo.pick_files()  # Abre o FilePicker quando clicado
            
        )

    enviar_arquivo = ft.ElevatedButton(
          text='Enviar Arquivo'
    )

    conteudo = ft.Container(
            content=ft.Column(
                [
                    ft.ResponsiveRow(
                            [
                                seletor_arquivo,
                                selecao_local,
                                result,
                                botao_selecionar,
                                enviar_arquivo
                            ],
                        spacing=50
                    )
                ]
            ,alignment=ft.MainAxisAlignment.CENTER,
            )
    )

    table = ft.ListView(
          expand=True,
          controls=[
                ft.Dismissible(
                      content=ft.ListTile(title=ft.Text(f"Item {i}")),
                    dismiss_direction=ft.DismissDirection.HORIZONTAL,
                    background=ft.Container(bgcolor=ft.colors.GREEN),
                    secondary_background=ft.Container(bgcolor=ft.colors.RED),
                )
                for i in range(20)
          ]
    )


    Title = ft.Text("Google API with my bro Pedro Forrosky",
                    font_family="Poppins",
                      size=30)
    
    
    page.add(
        ft.Row([Title]),
        ft.ResponsiveRow([conteudo]),
        table
        )

    
ft.app(main)

# #def pesquisar(e):
#           Snackbar(f"Você digitou: {search.value}","Teal")
#           page.update()

#search = ft.TextField(focused_border_color="Green")