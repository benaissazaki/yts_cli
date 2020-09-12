from handle_input import handle_input

if __name__ == "__main__":
    cmd = ""
    print("***YTS CLI***")

    while True:
        cmd = input("$ ")
        handle_input(cmd)