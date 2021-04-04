# Write a function that takes in a string of one or more words, and returns the
# same string, but with all five or more letter words reversed (Just like the 
# name of this Kata). Strings passed in will consist of only letters and spaces.
# Spaces will be included only when more than one word is present.

# Examples:

# spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"

# spinWords( "This is a test") => returns "This is a test"

# spinWords( "This is another test" )=> returns "This is rehtona test"


def spin_words(sentence):
    # Your code goes here
    if len(sentence) == 0:
        return None
    words = sentence.split(" ")
    for wordindex,word in enumerate(words):
        if len(word)>=5:
            words[wordindex] = reverse(word)
#     print words
    return " ".join(word for word in words)
          
    
def reverse(word):
  l = len(word)
  res = ""
  for index in range(1,l+1):
      res += word[-index]
#       print res
  return res
