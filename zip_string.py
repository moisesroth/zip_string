def zip_string(s):
    r = ''
    f = [ord(x) for x in s] # convert string in array of ascii
    d = False # dash flag
    
    for i in range(len(f)):
        p = False # print flag
        if i == 0 or i == len(f)-1: # is first or last character
            p = True
        elif abs(f[i-1] - f[i]) != 1: # diference between last letter and this letter ir != 1, this indicates non sequencial letter
            p = True
        elif abs(f[i+1] - f[i]) != 1: # this verify non sequential letter
            p = True
        elif f[i-1] == f[i+1]: # verify if there is a change of sequential direction like "abcDcba"
            p = True
        else: # if no print was detected, print flag is seted to False and dash flag is seted to True
            p = False
            d = True

        if p: 
            if d: # if dash flag is True, this will make print a "-" before the next printed letter
                r += '-'
            r += chr(f[i])
            d = False

    return r
