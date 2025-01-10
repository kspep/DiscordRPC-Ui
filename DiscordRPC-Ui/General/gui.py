import flet as ft
import os

#Create file
BASE_DIR = "files"

def initialize_files():
    os.makedirs(f"{BASE_DIR}/List", exist_ok=True)
    for file_name in [
        "BotID", "DataState", "DataDetails", "DataStart",
        "DataEnd", "DataParty_size", "DataParty_sizeMax", "ButText", "ButLink" #"DataEnd", "DataPaty_size", "DataPaty_sizeMax", "ButText", "ButLink"
    ]:
        with open(f"{BASE_DIR}/{file_name}", "w") as f:
            f.write("")

initialize_files()

#General GUI
def main(page: ft.Page):
    page.title = "Flet GUI Project"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 650 #redact size
    page.window_height = 450

    #Button and fild of enter
    url_input = ft.TextField(label="URL Client ID", width=300)
    save_url_button = ft.ElevatedButton(
        text="Save URL",
        on_click=lambda e: save_url(url_input.value)
    )

    state_input = ft.TextField(label="State (str)", width=300)
    details_input = ft.TextField(label="Details (str)", width=300)
    start_input = ft.TextField(label="Start Time (int)", width=150, keyboard_type=ft.KeyboardType.NUMBER)
    end_input = ft.TextField(label="End Time (int)", width=150, keyboard_type=ft.KeyboardType.NUMBER)

    party_size_input = ft.TextField(label="Party Size (int)", width=150, keyboard_type=ft.KeyboardType.NUMBER)
    party_size_max_input = ft.TextField(label="Party Size Max (int)", width=150, keyboard_type=ft.KeyboardType.NUMBER)

    but_text_input = ft.TextField(label="Button Text", width=300)
    but_link_input = ft.TextField(label="Button Link", width=300)

    save_state_button = ft.ElevatedButton(
        text="Save State",
        on_click=lambda e: save_state(
            state=state_input.value,
            details=details_input.value,
            start=start_input.value,
            end=end_input.value,
            party_size=party_size_input.value,
            party_size_max=party_size_max_input.value,
            but_text=but_text_input.value,
            but_link=but_link_input.value
        )
    )

    #Start main.py
    run_button = ft.ElevatedButton(
        text="Run Main Script",
        style=ft.ButtonStyle(bgcolor=ft.Colors.RED),
        on_click=lambda e: run_main_script()
    )

    #Text info
    info_text = ft.Text("Creators Limnetic and Kspep", color=ft.Colors.ON_SURFACE_VARIANT)

    #Block structure
    page.add(
        ft.Column([
            ft.Container(
                content=ft.Row([url_input, save_url_button], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                padding=10,
                bgcolor=ft.Colors.SECONDARY_CONTAINER,
                border_radius=5
            ),
            ft.Container(
                content=ft.Column([
                    ft.Row([state_input, details_input], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Row([start_input, end_input], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Row([party_size_input, party_size_max_input], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    ft.Row([but_text_input, but_link_input], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    save_state_button
                ]),
                padding=10,
                bgcolor=ft.Colors.SECONDARY_CONTAINER,
                border_radius=5
            ),
            ft.Container(
                content=ft.Row([run_button, info_text], alignment=ft.MainAxisAlignment.SPACE_EVENLY),
                padding=10,
                bgcolor=ft.Colors.SECONDARY_CONTAINER,
                border_radius=5
            )
        ])
    )

#Function load

def save_url(url):
    with open(f"{BASE_DIR}/BotID", "w") as f:
        f.write(url)
    with open(f"{BASE_DIR}/List/LogsList", "a") as log:
        log.write(url + "\n")


def save_state(state, details, start, end, party_size, party_size_max, but_text, but_link):
    with open(f"{BASE_DIR}/DataState", "w") as f:
        f.write(state)
    with open(f"{BASE_DIR}/DataDetails", "w") as f:
        f.write(details)
    with open(f"{BASE_DIR}/DataStart", "w") as f:
        f.write(start)
    with open(f"{BASE_DIR}/DataEnd", "w") as f:
        f.write(end)
    with open(f"{BASE_DIR}/DataParty_size", "w") as f: #with open(f"{BASE_DIR}/DataPaty_size", "w") as f:
        f.write(party_size)
    with open(f"{BASE_DIR}/DataParty_sizeMax", "w") as f: #with open(f"{BASE_DIR}/DataPaty_sizeMax", "w") as f:
        f.write(party_size_max)
    with open(f"{BASE_DIR}/ButText", "w") as f:
        f.write(but_text)
    with open(f"{BASE_DIR}/ButLink", "w") as f:
        f.write(but_link)


def run_main_script():
    os.system("Code/main.py")

#Start main.py
if __name__ == "__main__":
    ft.app(target=main)
