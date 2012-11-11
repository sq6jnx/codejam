import sys

#
# Dunno why, but Google does not accept solutions form this script...
#

in_file=open(sys.argv[1]).readlines()

def solve_problem(n):
    rv=str(int((3+5**0.5)**n))
    return rv[max(len(rv)-3,0):].rjust(3,'0')

for case_no, n in enumerate(in_file[1:],1):
    print 'Case #%d: %s'%(case_no, solve_problem(int(n)))


