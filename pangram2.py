## Solution 2 - O(n^2) (Quadratic) time

import time

def checkIfPangramSolutionTwo(n):
  start = time.time()
  
  # Check if it's a string
  if isinstance(n, str) != True:
    print('A pangram should start as a string!')
    return False

  removeSpaces = n.replace(' ','')
  toLowerCase = removeSpaces.lower()
  ## toLowerCase runs a For loop + if statement so O^n2 Quadratic time
  createList = list(toLowerCase)

  # Checked against both of these data sets - thought that a list sorted by frequency of alphabets used in the English language would return a quicker result
  fullAlphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  # alphabetByFrequency = ['e','t','a','o','i','n','s','h','r','d','l','u','c','m','f','w','y','p','v','b','g','k','j','q','x','z']

  # Check if createList contains all elements of fullAlphabet
  ## Nested for loop within the all. Under the hood, all is doing a for loop, then this is running a for loop within the all
  result = all(elem in createList for elem in fullAlphabet)
  print(result)
  
  end = time.time()
  print(end - start)

# Check against Full Alphabet
  # True
  # 5.79357147217e-05
  # False
  # 1.78813934326e-05

# Check against Alphabet list sorted by Frequency
  # True
  # 0.000185966491699
  # False
  # 2.40802764893e-05

checkIfPangramSolutionTwo('The Quick Brown Fox Jumps Over the Lazy Dog')
checkIfPangramSolutionTwo('The Brown Fox Jumps Over the Lazy Dog')

