import pyautogui as pag

commands = {
    'mouse_up': lambda: pag.move(0, -10),
    'mouse_down': lambda: pag.move(0, 10),
    'mouse_right': lambda: pag.move(10, 0),
    'mouse_left': lambda: pag.move(-10, 0)

}
def get_command(command):

    if command:
        commands[command]()