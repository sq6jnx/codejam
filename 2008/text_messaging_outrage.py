import sys

in_file=open(sys.argv[1])


number_of_cases=int(in_file.readline())

for case_no in xrange(number_of_cases):
    line=in_file.readline().split()
    letters_per_key=int(line[0])
    keys_available=int(line[1])
    number_of_letters=int(line[2])

    letter_frequency= in_file.readline()
    letter_frequency=[int(f) for f in letter_frequency.split()]

    cost=0

    for i,f in enumerate(sorted(letter_frequency)[::-1]):
        cost=cost+f*((i//keys_available)+1)

    print "Case #%d: %d"%(case_no+1, cost)

