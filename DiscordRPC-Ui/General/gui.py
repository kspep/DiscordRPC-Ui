import flet as ft
import os
import time
from main import main_function

# Creating files
BASE_DIR = "files"
print(time.time())

def initialize_files():
    os.makedirs(f"{BASE_DIR}/List", exist_ok=True)
    for file_name in [
        "BotID", "DataState", "DataDetails", "DataStart",
        "DataEnd", "DataParty_size", "DataParty_sizeMax", "ButText", "ButLink", "ButText2", "ButLink2"
    ]:
        with open(f"{BASE_DIR}/{file_name}", "w") as f:
            f.write("")

initialize_files()

# General GUI
def main(page: ft.Page):
    page.title = "DiscordRPC-Ui"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 650
    page.window.height = 550

    # Define common styles
    container_style = {
        "padding": 10,
        "bgcolor": ft.colors.SECONDARY_CONTAINER,
        "border_radius": 15
    }

    input_style = {
        "width": 300,
        "border_radius": 10
    }

    # Input fields
    url_input = ft.TextField(label="URL Client ID (REQUIRED ENTRY)", border_color=ft.colors.RED_500, **input_style)
    state_input = ft.TextField(label="State (str)", **input_style)
    details_input = ft.TextField(label="Details (str)", **input_style)
    start_input = ft.TextField(label="Start Time (int)", width=200, keyboard_type=ft.KeyboardType.NUMBER, border_radius=10)
    end_input = ft.TextField(label="End Time (int)", width=200, keyboard_type=ft.KeyboardType.NUMBER, border_radius=10)
    party_size_input = ft.TextField(label="Party Size (int)", width=200, keyboard_type=ft.KeyboardType.NUMBER, border_radius=10)
    party_size_max_input = ft.TextField(label="Party Size Max (int)", width=200, keyboard_type=ft.KeyboardType.NUMBER, border_radius=10)
    but_text_input = ft.TextField(label="Button Text", **input_style)
    but_link_input = ft.TextField(label="Button Link", **input_style)
    but_text_input2 = ft.TextField(label="Button Text", **input_style)
    but_link_input2 = ft.TextField(label="Button Link", **input_style)

    # Save state button
    save_state_button = ft.ElevatedButton(
        text="Save State",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15),
            bgcolor=ft.colors.BLACK54,
            color=ft.colors.WHITE
        ),
        on_click=lambda e: save_state(
            url=url_input.value,
            state=state_input.value,
            details=details_input.value,
            start=start_input.value,
            end=end_input.value,
            party_size=party_size_input.value,
            party_size_max=party_size_max_input.value,
            but_text=but_text_input.value,
            but_link=but_link_input.value,
            but_text2=but_text_input2.value,
            but_link2=but_link_input2.value,
            page=page  # Pass the page object
        )
    )

    # Run main script button
    run_button = ft.ElevatedButton(
        text="Run Main Script",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=15),
            bgcolor=ft.colors.BLUE_500,
            color=ft.colors.WHITE
        ),
        on_click=lambda e: run_main_script()
    )

    # Information text
    info_text = ft.Text("Creator's Limnetic and Kspep", color=ft.colors.ON_SURFACE_VARIANT)

    # Structure blocks
    page.add(
        ft.Column([
            ft.Container(
                content=ft.Row([url_input], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                **container_style
            ),
            ft.Container(
                content=ft.Column([
                    ft.Row([state_input, details_input], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Row([start_input, end_input], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Row([party_size_input, party_size_max_input], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Row([but_text_input, but_link_input], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Row([but_text_input2, but_link_input2], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    save_state_button
                ]),
                **container_style
            ),
            ft.Container(
                content=ft.Row([run_button, info_text], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                **container_style
            )
        ])
    )

# Save state function
def save_state(url, state, details, start, end, party_size, party_size_max, but_text, but_link, but_text2, but_link2, page):
    with open(f"{BASE_DIR}/BotID", "w") as f:
        f.write(url)
    with open(f"{BASE_DIR}/DataState", "w") as f:
        f.write(state)
    with open(f"{BASE_DIR}/DataDetails", "w") as f:
        f.write(details)
    with open(f"{BASE_DIR}/DataStart", "w") as f:
        f.write(start)
    with open(f"{BASE_DIR}/DataEnd", "w") as f:
        f.write(end)
    with open(f"{BASE_DIR}/DataParty_size", "w") as f:
        f.write(party_size)
    with open(f"{BASE_DIR}/DataParty_sizeMax", "w") as f:
        f.write(party_size_max)
    with open(f"{BASE_DIR}/ButText", "w") as f:
        f.write(but_text)
    with open(f"{BASE_DIR}/ButLink", "w") as f:
        f.write(but_link)
    with open(f"{BASE_DIR}/ButText2", "w") as f:
        f.write(but_text2)
    with open(f"{BASE_DIR}/ButLink2", "w") as f:
        f.write(but_link2)

    # Show SnackBar
    snack = ft.SnackBar(content=ft.Text("State saved"), shape=ft.RoundedRectangleBorder(radius=0), duration=100,)
    page.overlay.append(snack)
    snack.open = True
    page.update()

# Run main script function
def run_main_script():
    main_function()

# Run app
if __name__ == "__main__":
    ft.app(target=main)
