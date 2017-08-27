from collections import Counter
def scramble(s1,s2):
  l1 = counter(s1)
  l2 = counter(s2)
  nonoverlap = l2 - l1
  if len(nonoverlap)==0:
    return True
  else:
    return False
  
