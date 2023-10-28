import flet as ft


def main(page: ft.Page):
    # Размешнеие виджето
    page.title = "Admin Panel to access the server"
    page.window_width = 800
    page.window_height = 600
    page.bgcolor = "#272829"

    textSucces = ft.Text('You are logged in to the server', color=ft.colors.GREEN_400, size=14)

    img = ft.Image(
        src=f"img/video.png",
        width=200,
        height=200,
    )

    img1 = ft.Image(
        src=f"img/photo.png",
        width=100,
        height=100
    )

    images = ft.Row(
        controls=[
           img
        ],

    )

    images1 = ft.Row(
        controls=[
           img1
        ],

    )

    page.add(images, images1)
    # Обновление окна при
    page.update()

# Создаем окно приложения
ft.app(target=main)
