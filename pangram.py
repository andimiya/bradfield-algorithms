# Write a function which determines if a given string is a pangram.

# Questions:
# Each time I run the timer, it gives me a different result for the same problem. That makes sense because my computer is probably running different things at different times, but how can I use the timer as an accurate way to compare different solutions to each other?


import time

def checkIfPangramSolutionOne(n):
  start = time.time()

# Check to make sure n is a string
  if isinstance(n, str) != True:
    return False

  removeSpaces = n.replace(' ','')
  toLowerCase = removeSpaces.lower()
  createList = list(toLowerCase)
  sortedList = sorted(createList)
  
  fullAlphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];
  alphabetByFrequency = ['e','t','a','o','i','n','s','h','r','d','l','u','c','m','f','w','y','p','v','b','g','k','j','q','x','z'];

  for i in xrange(len(fullAlphabet)):
    for y in xrange(len(sortedList)):
      if fullAlphabet[i] == sortedList[y]:
        print(fullAlphabet[i])
        break
        
    print('not pangram')
    return False

    end = time.time()
    print(end - start)

checkIfPangramSolutionOne('The Quick Brown Fox Jumps Over the Lazy Dog')

# // Make a note of how you came to that strategy and what the time and space complexity are.

