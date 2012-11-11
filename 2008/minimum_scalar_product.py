import sys

in_file=open(sys.argv[1]).readlines()

def solve_problem(v1, v2):
    v1=sorted([int(e) for e in v1.split()])
    v2=sorted([int(e) for e in v2.split()])[::-1]
    rv=0

    for i in range(0,len(v1)):
        rv=rv+v1[i]*v2[i]

    return rv

for case_no, task_start in enumerate(range(1, len(in_file),3),1):
    v1=in_file[task_start+1].replace('\n','')
    v2=in_file[task_start+2].replace('\n','')
    print 'Case #%d: %d'%(case_no, solve_problem(v1, v2))


