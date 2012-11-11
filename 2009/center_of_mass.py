#NOTE: this solution is incorrect.

import sys

in_file=open(sys.argv[1])

# some constants
X, Y, Z, VX, VY, VZ = range(0,6)

for case_no in xrange(int(in_file.readline())):
    fireflies=[]
    number_of_fireflies=int(in_file.readline())
    for f in range(number_of_fireflies):
        fireflies.append([int(i) for i in in_file.readline().split()])

    t=0
    d_min=None
    t_of_d_min=0
    while True:
        t=t+1
        x_c, y_c, z_c = 0,0,0
        for i in xrange(number_of_fireflies):
            fireflies[i][X]+=fireflies[i][VX]
            fireflies[i][Y]+=fireflies[i][VY]
            fireflies[i][Z]+=fireflies[i][VZ]
            x_c+=fireflies[i][X]
            y_c+=fireflies[i][Y]
            z_c+=fireflies[i][Z]

        x_c/=float(number_of_fireflies)
        y_c/=float(number_of_fireflies)
        z_c/=float(number_of_fireflies)
        d=(x_c**2+y_c**2+z_c**2)**0.5

        if d_min>d or d_min is None:
            d_min=d
            t_of_d_min=t
        elif d_min is not None and t_of_d_min+1000<t:
            print "Case #%d: %0.8f %0.8f"%(case_no+1, d_min, t_of_d_min)
            break

