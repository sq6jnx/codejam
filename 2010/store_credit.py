

in_file=open('A-large-practice.in').readlines()

def solve_problem(credit, elements):
    credit=int(credit)
    elements=[int(e) for e in elements]

    for i, e in enumerate(elements):
        if credit-e in elements[i+1:]:
            return sorted([i+1, i+1+elements[i+1:].index(credit-e)+1])



for case_no, task_start in enumerate(range(1, len(in_file),3),1):
    credit=in_file[task_start].replace('\n','')
    elements=in_file[task_start+2].replace('\n','').split()
    print 'Case #%d: %s'%(case_no, \
            ' '.join([str(e) for e in solve_problem(credit, elements)]))


