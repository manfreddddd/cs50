def interpreter():
    expression=input("Expression: ")
    x,y,z = expression.split(" ")
    if y == "+":
        total = int(x) + int(z)
    elif y == "-":
        total = int(x) - int(z)
    elif y == "*":
        total = int(x) * int(z)
    elif y == "/":
        total = int(x) / int(z)
    f_total=float(total)
    print(round(f_total,1))
    
   
interpreter()