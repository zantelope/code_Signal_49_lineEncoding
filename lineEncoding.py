### import groupby object from itertools module
### splits string into list of like adjactent chars
from itertools import groupby

def lineEncoding(s):
    
    
    ###split string into groups of identical elements
    
    splitS = ["".join(grp) for e, grp in groupby(s)]

    
    ### count number of chars in each element, store in list "count"
    ### if count is one, append count with ""
    
    count = []
    for i in range(len(splitS)):
        if len(splitS[i]) == 1:
            count.append("")
        else:
            count.append(str(len(splitS[i])))

    ### list to store number of instanes concatenated with single instance of char
    
    numChars = []

    for i in range(len(splitS)):
        numChars.append(count[i] + splitS[i][0])
        
    ### join list into a string
    lineEncoded = "".join(numChars)

    ### return final string
    return (lineEncoded)
