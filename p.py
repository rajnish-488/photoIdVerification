def sum(a,b):
    try:
        return a+b
    except NameError:
        print("p")
    except TypeError:
        print("q")
    else:
        print("i")
sum(23,"3")        
        
