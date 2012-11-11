import sys

# aliens won't start a number with zero, just like us
numbers = range(0,10+26)
numbers[0], numbers[1] = numbers[1], numbers[0]


in_file=open(sys.argv[1])

for case_no in xrange(int(in_file.readline())):
    case=in_file.readline().replace('\n','')

    # base is equal to number of different chars, but greater than 1
    base=max(len(set(case)),2)

    alien_digits=[]
    for d in case:
        if d not in alien_digits:
            alien_digits.append(d)

    translated_digits=[numbers[alien_digits.index(d)] for d in case]

    value=0
    for p,d in enumerate(translated_digits[::-1]):
        value=value+d*(base**p)

    print "Case #%d: %d"%(case_no+1, value)

