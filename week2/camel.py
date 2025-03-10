def camel(camel_case):
    snake_case = ""
    for char in camel_case:
        if char .isupper():
            snake_case += "_" + char.lower()
        else:
            snake_case += char


   
    return snake_case        


camel_case = input("Enter a variable name in camelCase: ")
snake_case = camel(camel_case)
print(f"The variable name in snake_case is: {snake_case} ")
  
