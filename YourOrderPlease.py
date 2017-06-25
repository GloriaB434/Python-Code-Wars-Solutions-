def order(sentence):
  output = [ ]
  for word in sentence.split():
      for character in word:
          if character.isdigit():
              output.append([int(character),word])
  return " ".join([word[1] for word in sorted(output)])
  return
