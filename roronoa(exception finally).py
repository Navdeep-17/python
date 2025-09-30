def menu(item):
    try:
        if item == "idly":
            print("idly is Ready")
        elif item == "dosa":
            print("dosa is Ready")
        elif item == "Puri":
            print("Puri is Ready")
        except Exception as e:
        print(e)
    else:
        print("NameError")
    finally:
        print("items over")
        
def main():
    item = input()
    menu(item)
    
main()