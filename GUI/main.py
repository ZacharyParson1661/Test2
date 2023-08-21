import os
import subprocess
import tkinter as tk
from tkinter import font
import GBA_roms
import N64_roms
import SNES_roms
import GAMECUBE_roms
import WII_roms
import DS_roms
import PS2_roms

selected_emulator_path = ""
cwd = os.getcwd()


def center_buttons(button):
    screen_width = root.winfo_screenwidth()
    button_width = button.winfo_reqwidth()  # Get the requested width of the button
    padding_x = (screen_width - button_width) // 2
    button.pack(padx=padding_x, pady=5, anchor="nw")


def launch_emulator_with_rom(emulator_path, rom_path):
    try:
        # Check if the emulator executable exists
        if not os.path.exists(emulator_path):
            print(f"Emulator not found at {emulator_path}. Please check the path.")
            return

        # Check if the ROM file exists
        if not os.path.exists(rom_path):
            print(f"ROM not found at {rom_path}. Please check the path.")
            return

        print("Launching emulator with the following paths:")
        print(f"Emulator Path: {emulator_path}")
        print(f"ROM Path: {rom_path}")

        # Launch the emulator with the ROM using subprocess
        subprocess.Popen([emulator_path, rom_path], shell=True)
        print(f"Emulator ({emulator_path}) launched with ROM ({rom_path}).")

    except Exception as e:
        print(f"Error: {e}")


def setup_rom_options_window(emulator_path, rom_paths, game_names):
    rom_options_window = tk.Toplevel(root)
    rom_options_window.title("ROM Options")


    custom_cursor_path = "Images\\cursor.cur"  # Update with your custom cursor file path
    custom_cursor_path = custom_cursor_path.replace("\\", "/")  # Replace backslashes with forward slashes
    rom_options_window.config(cursor=f"@{custom_cursor_path}")

    # Set the window attributes to maximize
    rom_options_window.state('zoomed')



    # Define the color scheme
    bg_color = "#2C2C2E"  # Dark gray
    button_color = "#2AA146"  # Green
    button_hover_color = "#264BCC"  # Blue


    # Load the TrueType font from the file
    custom_font = font.Font(family="Retro Gaming", size=12)
    rom_options_window.configure(bg=bg_color)  # Set the background color of the window



    # Create a canvas with a scrollbar
    canvas = tk.Canvas(rom_options_window, bg=bg_color,
                       highlightthickness=0)  # Set the background color and remove border
    scrollbar = tk.Scrollbar(rom_options_window, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Put the canvas and scrollbar in a frame
    rom_frame = tk.Frame(canvas, bg=bg_color)  # Set the background color of the frame

    # Bind the canvas to update the scrollable region
    rom_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Create a window inside the canvas to hold the ROM options

    # Create a window inside the canvas to hold the ROM options
    canvas.create_window(0, 0, anchor="nw", window=rom_frame)

    rom_button_styles = {
        "bg": button_color,
        "fg": "white",
        "activebackground": button_hover_color,
        "relief": "flat",
        "padx": 20,
        "pady": 10,
    }

    for i, (rom_path, game_name) in enumerate(zip(rom_paths, game_names)):
        rom_path = os.path.join(cwd, rom_path.replace("/", os.path.sep))  # Convert forward slashes to platform-specific separator
        rom_button = tk.Button(rom_frame, text=game_name,
                               command=lambda path=rom_path: launch_emulator_with_rom(emulator_path, path),
                               font=("Retro Gaming", 18), **rom_button_styles)
        center_buttons(rom_button)

    # Place the back button after the loop
    back_button = tk.Button(rom_frame, text="Back", command=rom_options_window.destroy, font=("Retro Gaming", 18),
                            **rom_button_styles)
    center_buttons(back_button)

    # Set the custom font for the ROM options window
    rom_options_window.option_add("*Font", custom_font)

    # Set the background color of the ROM options window
    rom_options_window.configure(bg=bg_color)
    rom_options_window.update_idletasks()



# Create your specific system functions using the setup_rom_options_window function
def show_rom_options_GAMEBOY():
    emulator_option1_path = os.path.join(cwd, "Emulators\\visualboyadvance-m.exe")
    rom_paths = GBA_roms.GBA_rom_paths
    game_names = GBA_roms.GBA_game_names
    setup_rom_options_window(emulator_option1_path, rom_paths, game_names)





def show_rom_options_N64():
    emulator_option_path = os.path.join(cwd, "Emulators", "Project64.lnk")
    rom_paths = N64_roms.N64_rom_path
    game_names = N64_roms.N64_game_names
    setup_rom_options_window(emulator_option_path, rom_paths, game_names)


def show_rom_options_SNES():
    emulator_option_path = os.path.join(cwd, "Emulators", "snes9x-x64.exe")
    rom_paths = SNES_roms.SNES_rom_path
    game_names = SNES_roms.SNES_game_names
    setup_rom_options_window(emulator_option_path, rom_paths, game_names)


def show_rom_options_GAMECUBE():
    emulator_option_path = os.path.join(cwd, "Emulators", "dolphin-master-5.0-19368-x64", "Dolphin-x64", "Dolphin.exe")
    rom_paths = GAMECUBE_roms.GAMECUBE_rom_path
    game_names = GAMECUBE_roms.GAMECUBE_game_names
    setup_rom_options_window(emulator_option_path, rom_paths, game_names)


def show_rom_options_WII():
    emulator_option_path = os.path.join(cwd, "Emulators", "dolphin-master-5.0-19368-x64", "Dolphin-x64", "Dolphin.exe")
    rom_paths = WII_roms.WII_rom_path
    game_names = WII_roms.WII_game_names
    setup_rom_options_window(emulator_option_path, rom_paths, game_names)


def show_rom_options_NINTENDODS():
    emulator_option_path = os.path.join(cwd, "Emulators", "DeSmuME_0.9.11_x64.exe")
    rom_paths = DS_roms.DS_rom_path
    game_names = DS_roms.DS_game_names
    setup_rom_options_window(emulator_option_path, rom_paths, game_names)


def show_rom_options_PS2():
    emulator_option_path = os.path.join(cwd, "Emulators", "PCSX2 1.6.0.lnk")
    rom_paths = PS2_roms.PS2_rom_path
    game_names = PS2_roms.PS2_game_names
    setup_rom_options_window(emulator_option_path, rom_paths, game_names)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Retro Game Emulator Launcher")
    root.geometry("800x600")
    root.state('zoomed')

    custom_cursor_path = "Images\\cursor.cur"  # Update with your custom cursor file path
    custom_cursor_path = custom_cursor_path.replace("\\", "/")  # Replace backslashes with forward slashes
    root.config(cursor=f"@{custom_cursor_path}")


    bg_color = "#2C2C2E"  # Dark gray
    label_color = "#B3B4B6"  # Light gray
    button_color = "#2AA146"  # Green
    button_hover_color = "#264BCC"  # Blue
    text_color = "#F8D034"  # Yellow
    error_color = "#E40027"  # Red

    # Load the TrueType font from the file
    font_path = "Images\\Retro Gaming.ttf"  # Update this with the actual path to your font file
    custom_font = font.Font(family="Retro Gaming", size=12)

    # Emulator selection label
    emulator_label = tk.Label(root, text="Select a System", font=("Retro Gaming", 24), bg=bg_color, fg="white")
    emulator_label.pack(pady=20)

    # Button styles
    button_styles = {
        "font": ("Retro Gaming", 18),
        "bg": button_color,
        "fg": "white",
        "activebackground": button_hover_color,
        "relief": "flat",  # Use flat relief for retro look
        "padx": 20,
        "pady": 10,
    }

    systems = [
        ("Gameboy Advance", show_rom_options_GAMEBOY),
        ("SNES", show_rom_options_SNES),
        ("N64", show_rom_options_N64),
        ("Gamecube", show_rom_options_GAMECUBE),
        ("Wii", show_rom_options_WII),
        ("Nintendo DS", show_rom_options_NINTENDODS),
        ("PS2", show_rom_options_PS2),
    ]

    for system, command in systems:
        button = tk.Button(root, text=system, command=command, **button_styles)
        button.pack(pady=5)

    # Set the custom font for the root window
    root.option_add("*Font", custom_font)

    # Set the background color of the root window
    root.configure(bg=bg_color)

    root.mainloop()