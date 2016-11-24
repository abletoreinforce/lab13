import turtle

def dragon(n, l, init, x, repl_x, y, repl_y):
    state = init

    if n == 0:
        return "F"

    for i in range(n):
        state2 = ''
        for character in state:
            if character == x:
             state2 += repl_x
            elif character == y:
             state2 += repl_y
            else:
             state2 += character
        state = state2

    for character in state:
        if character == 'F':
            turtle.forward(l)
        elif character == '+':
            turtle.right(90)
        elif character == '-':
            turtle.left(90)


dragon(15, 3, 'FX', 'X', 'X+YF+', 'Y', '-FX-Y')