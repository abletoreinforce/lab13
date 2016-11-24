import turtle
def min_line(n,l):
    if n == 0:
        turtle.forward(l)
    else:
        min_line(n - 1, l/4.0)
        turtle.left(90)
        min_line(n - 1, l/4.0)
        turtle.right(90)
        min_line(n - 1, l/4.0)
        turtle.right(90)
        min_line(n - 1, l/4.0)
        min_line(n - 1, l/4.0)
        turtle.left(90)
        min_line(n - 1, l/4.0)
        turtle.left(90)
        min_line(n - 1, l/4.0)
        turtle.right(90)
        min_line(n - 1, l/4.0)

min_line(3,200)