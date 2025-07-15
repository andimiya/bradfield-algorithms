# Solution 3 - O^n2 Quadratic Time

# Question:
# Each time I run the timer, it gives me a different result for the same problem. That makes sense because my computer is probably running different things at different times, but how can I use the timer as an accurate way to compare different solutions to each other?

import time

def checkIfPangramSolutionOne(n):
  start = time.time()

# Check to make sure n is a string - constant time
  if isinstance(n, str) != True:
    return False

  removeSpaces = n.replace(' ','')
  toLowerCase = removeSpaces.lower()
  ## toLowerCase runs a For loop + if statement so O^n2 Quadratic time
  createList = list(toLowerCase)
  ## Sorted list O(nlogn) logarithmic time
  sortedList = sorted(createList)
  
  fullAlphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'];

  ## Iterating over elements required n steps so O(n) linear time
  for letter in fullAlphabet:
    ## If statement is O(n) linear time
    if not letter in sortedList:
      end = time.time()
      print(end - start)
      print('not a pangram')
      return False
  
  end = time.time()
  print(end - start)
  print('It is a pangram!')
  return True
  
checkIfPangramSolutionOne('The Quick Brown Fox Jumps Over the Lazy Dog')
checkIfPangramSolutionOne('The Brown Fox Jumps Over the Lazy Dog')

