print(" ")
print(" ")
text = [
"  ███████╗ █████╗ ██╗   ██╗ ██████╗ ",
"  ██╔════╝██╔══██╗╚██╗ ██╔╝██╔═══██╗",
"  ███████╗███████║ ╚████╔╝ ██║   ██║",
"  ╚════██║██╔══██║  ╚██╔╝  ██║   ██║",
"  ███████║██║  ██║   ██║   ╚██████╔╝",
"  ╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ",
"",
"   ██████╗ ██████╗ ██╗",
"  ██╔═══██╗██╔══██╗██║",
"  ██║   ██║██████╔╝██║",
"  ██║   ██║██╔═══╝ ██║",
"  ╚██████╔╝██║     ██║",
"   ╚═════╝ ╚═╝     ╚═╝"
]

for line in text:
    print(line)

print(" ")
print("--------------------------------------------------------------------------")
print("|Made by: Artplay-git                                                    |")
print("|https://github.com/Artplay-git/Sayo-Geometry-Dash-program               |")
print("--------------------------------------------------------------------------")
print("|--------------------------------------------------------------------------|")
print("|HOW TO USE and HOW IT WORKS:                                              |")
print("|When you click 'o', 'p' or 'i' key on you keybord, program clicks 'w' key.|")
print("|To close the porgram click '1' on keyboard.                               |")
print("|--------------------------------------------------------------------------|")
print("----------------------------------")
print("| DISABLE CAPS LOCK BEFORE USING!|")
print("----------------------------------")
print("=====================OUTPUT=====================")

# sayo
import keyboard
import pydirectinput

pydirectinput.PAUSE = 0.01

is_pressed = False

def PressW(e):
    global is_pressed
    if e.name in ['o', 'p', 'i']:
        if e.event_type == keyboard.KEY_DOWN:
            if not is_pressed:
                pydirectinput.keyDown('w')
                is_pressed = True
                print("W pressed")
        
        elif e.event_type == keyboard.KEY_UP:
            if is_pressed:
                if not keyboard.is_pressed('o') and not keyboard.is_pressed('p') and not keyboard.is_pressed('i'):
                    pydirectinput.keyUp('w')
                    is_pressed = False
                    print("W released")

keyboard.hook(PressW)

keyboard.wait('1')
