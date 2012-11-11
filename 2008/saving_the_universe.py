# NOTE: this solution is incorrect.

import sys

in_file=open(sys.argv[1])

number_of_cases=int(in_file.readline())

def solve(search_engines, queries):
    return min( [queries.count(se) for se in search_engines] )


for case_no in xrange(number_of_cases):
    search_engines=[]
    queries=[]

    number_of_search_engines=int(in_file.readline())
    for se in range(number_of_search_engines):
        search_engines.append(in_file.readline())

    number_of_queries=int(in_file.readline())
    for q in range(number_of_queries):
        queries.append(in_file.readline())

    print 'Case #%d: %d'%(case_no+1, solve(search_engines, queries))

