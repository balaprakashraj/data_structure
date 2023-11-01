a=[1,2,3,'a','b']
def ls(a,k):
  for i in a:
    if i==k:
      return a.index(k)
  return 'notfound'
print(ls(a,3))
