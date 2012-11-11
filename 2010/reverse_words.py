

in_file=open('B-large-practice.in').readlines()

for case_no, line in enumerate(in_file[1:],1):
    print 'Case #%d: %s'%(case_no, ' '.join( line.split()[::-1] ))


