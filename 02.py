import turtle
def koch_line(n, l):
    if n == 0:
        turtle.forward(l)
    else:
        koch_line(n - 1, l/3.0)
        turtle.left(60)
        koch_line(n - 1, l/3.0)
        turtle.right(120)
        koch_line(n - 1, l/3.0)
        turtle.left(60)
        koch_line(n - 1, l/3.0)

def koch_flake(n,l):
    if n == 0:
        turtle.forward(l)
    else:
        koch_line(n,l)
        turtle.right(120)
        koch_line(n,l)
        turtle.right(120)
        koch_line(n,l)


koch_flake(3,100)