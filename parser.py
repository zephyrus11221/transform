from display import *
from matrix import *
from draw import *
from time import sleep

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 translate: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    comm = []
    f = open(fname)
    comm = f.readlines()
    i = 0
    while (i < len(comm)):
        print i
        comm[i] = comm[i].strip('\n')
        if (comm[i] == 'line'):
            i+=1
            args=[]
            args = comm[i].split()
            for n in range(len(args)):
                args[n] = int(args[n])
            add_edge(points, args[0], args[1], args[2], args[3], args[4], args[5])
            
        elif (comm[i] == 'ident'):
            ident(transform)

        elif (comm[i] == 'scale'):
            i+=1
            args=[]
            args = comm[i].split()
            for n in range(len(args)):
                args[n] = int(args[n])
            matrix_mult(make_scale(args[0], args[1], args[2]), transform)

        elif (comm[i] == 'move'):
            i+=1
            args=[]
            args = comm[i].split()
            for n in range(len(args)):
                args[n] = int(args[n])
            matrix_mult(make_translate(args[0], args[1], args[2]), transform)
            print_matrix(transform)

        elif (comm[i] == 'rotate'):
            i+=1
            args=[]
            args = comm[i].split()
            args[1] = int(args[1])
            if(args[0] == 'x'):
                matrix_mult(make_rotX(args[1]), transform)
            elif(args[0] == 'y'):
                matrix_mult(make_rotY(args[1]), transform)
            elif(args[0] == 'z'):
                matrix_mult(make_rotZ(args[1]), transform)

        elif (comm[i] == 'apply'):
            matrix_mult(transform, points)

        elif (comm[i] == 'display'):
            clear_screen(screen)
            sleep(.5)
            draw_lines(points, screen, color)
            display(screen)

        elif (comm[i] == 'save'):
            clear_screen(screen)
            sleep(.5)
            draw_lines(points, screen, color)
            i+=1
            save_extension(screen, comm[i])
        elif (comm[i] == 'quit'):
            i = len(comm)
        i+=1
        pass
