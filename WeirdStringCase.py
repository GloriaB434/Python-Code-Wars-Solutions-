def to_weird_case(string):
  s = [] #declare list
  string = string.split() #split the string
  for char in string:
    i = 0 #indexing variable
    new_string = '' #string to write the upper and lower case characters to
    while i < len(char):
      if i%2 == 0: #if the index divided by 2 leaves a remainder of zero
        new_string += char[i].upper()
      else:
        new_string += char[i].lower()
      i += 1
      s.append(new_string) #write the new string to a list
  return ' '.join(s)
      
    
  
