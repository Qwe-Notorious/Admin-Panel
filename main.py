# импортируем фреймоврк
import flet as ft
import pandas as pd
import os

# Инцелизация - функции Main
def main(page: ft.Page):
    # Настройка окна программы
    page.title = "Admin Panel to access the server"
    page.window_width = 800
    page.window_height = 600
    page.bgcolor = "#272829"

    # Функции обработки
    def login(e):
        userData = pd.read_csv('accaunts.csv')
        df = pd.DataFrame(userData)

        matching_creds = (len(df[(df.username == textinputUsername.value) & (df.password == textinputPassword.value)]) > 0)
        textSucces = ft.Text('You are logged in to the server', color=ft.colors.GREEN_400, size=14)
        textNosucces = ft.Text('There is no such account', color=ft.colors.GREEN_400, size=14)


        if matching_creds:
            succes = ft.Row(
                controls=[
                    ft.Column(
                        [
                            textSucces
                        ],
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
            page.add(succes)
            os.system("python adminPanelMain.py")
            page.window_destroy()
        else:
            succesNo = ft.Row(
                controls=[
                    ft.Column(
                        [
                            textNosucces
                        ],
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
            page.add(succesNo)
            page.window_destroy()
        page.update()

    # Создвние втджетов на странице
    textInfo = ft.Text('To connect to the server, log in to your account', color=ft.colors.GREEN_400, size=25)
    textinputUsername = ft.TextField(label="Username", width=200, color=ft.colors.GREEN_400)
    textinputPassword = ft.TextField(label="Password", width=200, color=ft.colors.GREEN_400, password=True,
                                     can_reveal_password=True)
    loginBnt = ft.ElevatedButton(text="Log in server", color=ft.colors.GREEN_400, width=200, on_click=login)

    # Разметака виджетов на странице
    markupWidgetsRowText = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    ft.Container(
                        textInfo,
                        margin=ft.margin.symmetric(vertical=20),
                        padding=ft.padding.symmetric(horizontal=20)
                    ),
                ],
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    markupWidgetsRow = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    textinputUsername,
                    textinputPassword,
                    loginBnt
                ],
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Добавление объектов на страницу
    page.add(markupWidgetsRowText, markupWidgetsRow)
    # Обновление окна
    page.update()



# Создаем окно приложения
ft.app(target=main)