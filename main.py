from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

parse_file( 'script', edges, transform, screen, color )
'''
add_edge(edges, 50, 50, 0, 450, 50, 0)
add_edge(edges, 450, 50, 0, 450, 450, 0)
add_edge(edges, 450, 450, 0, 50, 450, 0)
add_edge(edges, 50, 450, 0, 50, 50, 0)

transform = make_scale(.5, .5, .5)
#transform = make_translate(50, 50, 50)
print_matrix(make_translate(50,50,50))
matrix_mult(make_translate(50, 50, 50), transform)
print_matrix(transform)
matrix_mult(transform, edges)

draw_lines(edges, screen, color)
display(screen)
'''
