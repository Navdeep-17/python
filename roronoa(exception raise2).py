def menu(item):
    if item == "idli":
        print("Idli available")
    elif item == "dosa":
        print("dosa available")
    else:
        raise NameError
        

def main():
    item = input()
    menu(item)

main()
