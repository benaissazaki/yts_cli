from YtsAPI import YtsAPI
import sys

commands = {
    "list": {"fct": YtsAPI.display_list, "arg": False},
    "detail": {"fct": YtsAPI.display_detail, "arg": True},
    'exit': {"fct": sys.exit, "arg": False}
}

def handle_input(inp):
    inp = inp.split(" ")
    resp = commands.get(inp[0], 0)

    if resp == 0:
        print("Unknown command")
    elif resp["arg"]:
        resp["fct"](inp[1])
    else:
        resp["fct"]()
