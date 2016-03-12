def zip_string(s):
    r = ''
    f = [ord(x) for x in s]
    d = False
    
    for i in range(len(f)):
        p = False
        if i == 0 or i == len(f)-1:
            p = True
        elif abs(f[i-1] - f[i]) != 1:
            p = True
        elif abs(f[i+1] - f[i]) != 1:
            p = True
        elif f[i-1] == f[i+1]:
            p = True
        else:
            p = False
            d = True

        if p:
            if d:
                r += '-'
            r += chr(f[i])
            d = False

    return r
