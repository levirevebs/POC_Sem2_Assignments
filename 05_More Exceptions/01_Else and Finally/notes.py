def get_inverse(x):
    try:
        return 1 / x
    except: ZeroDivisionError00
    finally:
        print("I am printed!")

    
print(get_inverse(x))