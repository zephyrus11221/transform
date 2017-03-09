from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges1 = []
edges2 = []
edges3 = []
transform = new_matrix()

#parse_file( 'script', edges1, transform, screen, color )
'''
add_edge(edges1, -100, 100, 0, -100, -100, 0)
add_edge(edges1, -100, -100, 0, 100, -100, 0)
add_edge(edges1, 100, -100, 0, 100, 100, 0)
add_edge(edges1, 100, 100, 0, -100, 100, 0)

#transform = make_translate(50, 50, 50)
#matrix_mult(make_translate(50, 50, 50), transform)
print_matrix(transform)
matrix_mult(transform, edges)

transform = make_rotY(45)
matrix_mult(transform, edges1)
draw_lines(edges1, screen, color)
display(screen)
'''
for i in range(-75, 76):
    add_edge(edges1, i, 75, 75, i, -75, 75)
    add_edge(edges2, -75, 75, i, -75, -75, i)
    add_edge(edges3, i, -75, 75, i, -75, -75)
ident(transform)
matrix_mult(make_rotX(-45), transform)
#print_matrix(transform)
matrix_mult(make_rotZ(45), transform)
#print_matrix(transform)
matrix_mult(make_rotY(45), transform)
#print_matrix(transform)
print 'ugh'
matrix_mult(make_translate(100, 100, 0), transform)
#print_matrix(transform)

matrix_mult(transform, edges1)
matrix_mult(transform, edges2)
matrix_mult(transform, edges3)

color = [0, 100, 100]
draw_lines(edges2, screen, color)
color = [0, 50, 200]
draw_lines(edges3, screen, color)
color = [100, 20, 150]
draw_lines(edges1, screen, color)

matrix_mult(make_translate(300, 0 , 0), transform)

matrix_mult(transform, edges1)
matrix_mult(transform, edges2)
matrix_mult(transform, edges3)

color = [200, 0, 100]
draw_lines(edges2, screen, color)
color = [150, 50, 200]
draw_lines(edges3, screen, color)
color = [100, 0, 0]
draw_lines(edges1, screen, color)

matrix_mult(make_translate(0, 300, 0), transform)

matrix_mult(transform, edges1)
matrix_mult(transform, edges2)
matrix_mult(transform, edges3)

color = [0, 200, 0]
draw_lines(edges2, screen, color)
color = [0, 150, 100]
draw_lines(edges3, screen, color)
color = [30, 200, 150]
draw_lines(edges1, screen, color)

matrix_mult(make_translate(-300, 0, 0), transform)

matrix_mult(transform, edges1)
matrix_mult(transform, edges2)
matrix_mult(transform, edges3)

color = [100, 100, 100]
draw_lines(edges2, screen, color)
color = [150, 150, 150]
draw_lines(edges3, screen, color)
color = [200, 200, 200]
draw_lines(edges1, screen, color)


display(screen)
