a=[1,2,3,4,5,23,34,45,65,667,999]

def bs(a,k,m,h):
    mid= m+(h-m)//2
    if a[mid]==k:
        return mid
    elif a[mid]>k:
        h=mid-1
        
        return bs(a,k,m,h)
    else:
        m=mid+1
        return bs(a,k,m,h)
print(bs(a,45,0,len(a)))
    
