import sys

encrypted= "ejpmysljylckdkxveddknmcrejsicpdrysi"\
        + "rbcpcypcrtcsradkhwyfrepkymveddknkmkrkcd"\
        + "dekrkdeoyakwaejtysrreujdrlkgcjv"\

decrypted="ourlanguageisimpossibletounderstand"\
        + "therearetwentysixfactorialpossibilities"\
        + "soitisokayifyouwanttojustgiveup"

decrypt={' ':' ', 'z':'q', 'q':'z'}
for i,char in enumerate(encrypted): 
    decrypt[char]=decrypted[i]


in_file=open(sys.argv[1])

number_of_cases=int(in_file.readline())

for case_no in range(number_of_cases):
    case=in_file.readline().replace('\n','')
    answer=''.join([decrypt[char] for char in case])
    print 'Case #%d: %s'%(case_no+1, answer)


