import sys
import re

in_file=open(sys.argv[1])

line=in_file.readline().split()

letters_per_word=int(line[0])
words_in_language=int(line[1])
number_of_cases=int(line[2])

# Reading dictionary
dictionary=''

for i in xrange(words_in_language):
    dictionary=dictionary+in_file.readline().replace('\n','')+' '

for case_no in xrange(number_of_cases):
    case=in_file.readline().replace('\n','')+' '
    regexp=''
    alternative_mode=False
    for char in case:
        if char in '()':
            alternative_mode= not alternative_mode
            regexp=regexp+char
        else:
            regexp=regexp+char + '|'*alternative_mode

    regexp=regexp.replace('|)',')')

    print "Case #%d: %d"%(case_no+1, len(re.findall(regexp, dictionary)))

