def validate(mob):
    if len(mob)==10:
        print("valid")
    else:
        raise ValueError

def main():
    mob=input()
    validate(mob)
    
main()