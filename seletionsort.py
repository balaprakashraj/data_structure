a=[1,4,2,3]
def selesort(a):
  b=[]
  for i in range(len(a)):
    m=min(a)
    b.append(m)
    a.remove(m)
  return b
