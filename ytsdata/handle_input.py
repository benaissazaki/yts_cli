from YtsAPI import YtsAPI
import sys

commands = {
    "list": YtsAPI.display_list,
    'exit': sys.exit
}

def handle_input(inp):
    resp = commands.get(inp, 0)

    if resp == 0:
        print("Unknown command")
    else:
        resp()
