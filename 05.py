import turtle
def symbol_recipe(n):
    if n == 0:
        return "F"
    else:
        symbols = symbol_recipe(n - 1)
        return symbols.replace("F", "+F--F+")

def levy(n,l):
    for character in symbol_recipe(n):
        if character == 'F':
            turtle.forward(l)
        elif character == '+':
            turtle.right(45)
        elif character == '-':
            turtle.left(45)


levy(6,30)