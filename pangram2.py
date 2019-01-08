import time

def checkIfPangramSolutionTwo(n):
  start = time.time()
  if isinstance(n, str) != True:
    return False

  removeSpaces = n.replace(' ','')
  toLowerCase = removeSpaces.lower()
  createList = list(toLowerCase)

  fullAlphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  alphabetByFrequency = ['e','t','a','o','i','n','s','h','r','d','l','u','c','m','f','w','y','p','v','b','g','k','j','q','x','z']

  ## Nested for loop within the all. Under the hood, all is doing a for loop, then this is running a for loop within the all

  # Check if createList contains all elements of fullAlphabet
  result = all(elem in createList for elem in fullAlphabet)
  print(result)
  
  end = time.time()
  print(end - start)


checkIfPangramSolutionTwo('The Quick Brown Fox Jumps Over the Lazy Dog')
checkIfPangramSolutionTwo('The Brown Fox Jumps Over the Lazy Dog')