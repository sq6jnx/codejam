import sys

in_file=open(sys.argv[1])

number_of_cases=int(in_file.readline())

for case_no in range(number_of_cases):
    start, end = [int(i) for i in in_file.readline().split()]
    count=0
    for number in xrange(start, end):
        s=str(number)
        l=len(s)
        for perm in range(l):
            s=s[1:l]+s[0]
            if s[0]<>'0' and start<=number and number<int(s) and int(s)<=end:
                count+=1
    print 'Case #%d: %d'%(case_no+1, count)


