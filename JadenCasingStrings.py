def toJadenCase(string):
#split up the entire quote "string" into individual words separated by a space " "
    indv_words = string.split(" ")
#Open a list to store the new quote with capital letters
    quote_with_caps = []
#Capitlize the first letter word[0] of each element in the indv_words list 
    for word in indv_words:
        first_let_caps = word[0].upper() + word[1:]
#Store the new words that include caps in the quote_with_caps list 
        quote_with_caps.append(first_let_caps)
#Separate the elements of the list by a space 
    return " ".join(quote_with_caps)
