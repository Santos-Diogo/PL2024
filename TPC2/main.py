import sys

#returns rest of the line
def parseFirstMark(line):
    if (line[0]== '#'):
        i= 1
        while (line[i]== '#'):
            i++
        insertTag(line[i:], "h"+ i)
    

def parseRest(rest_line):

def parse (line):
    res= parseRest(parseFirstMark(line))


def main ():
    result= list()
    for line in sys.stdin:
        html_line= parse(line)
        result.add(html_line)

    print result
