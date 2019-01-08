# Solution 3 - O^n2 Quadratic Time

# Solution where a complete alphabet array is not needed to check against

# I *think* that the alphabet array would change the amount of time it takes for the computer to solve the problem, based on the order of alphabets. So tried to take that array out of the equation.

import time

def checkIfPangramSolutionThree(n):
  start = time.time()

  # Make sure it's a string
  if isinstance(n, str) != True:
    return False

  # Clean up the string of spaces and turn it into an array, sorted A-Z
  ## O(1) Constant operations
  removeSpaces = n.replace(' ','')
  toLowerCase = removeSpaces.lower()
  ## toLowerCase runs a For loop + if statement so O^n2 Quadratic time
  createList = list(toLowerCase)
  sortedList = sorted(createList)

  # Remove duplicates
  ## Set appears to be an O(1) Constant operation
  checkIfPangram = list(set(sortedList))

  # Check if 26 letters. If there are no duplicates and no spaces and contained every letter, it would have to be a list of 26.
  ## len() and check if equals appear to be an O(1) Constant operation - 
  if (len(checkIfPangram) == 26):
    print('It is a pangram!')
    end = time.time()
    print(end - start)
    return True
  else:
    end = time.time()
    print(end - start)
    print('Is not pangram')
    return False

## Time: 4.31537628174e-05
checkIfPangramSolutionThree('The Quick Brown Fox Jumps Over the Lazy Dog')