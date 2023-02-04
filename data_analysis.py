#to be called on two sentences of nonzero length
def lev(a,b):
    if(len(a)==0):
        return len(b)
    elif(len(b)==0):
        return len(a)
    elif(a[0]==b[0]):
        return lev(a[1:], b[1:])
    else:
        return 1 + min(lev(a[1:],b), lev(a, b[1:]), lev(a[1:],b[1:]))
