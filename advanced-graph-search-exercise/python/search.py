from constants import MOUNTAIN, COSTS

potentialDirections = ((-1, 0), (0, -1), (1, 0), (0, 1))

def exploreNeighbors(grid, location):
  # Return the set of co-ordinates that can be reached from the given location
  x,y = location

  return {(x+dx, y+dy) for dx, dy in potentialDirections
    if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]) # Remove out of bounds from potential neighbors
      and grid[x+dx][y+dy] != '^'} # Remove mountains from potential neighbors

exploreNeighbors([['s', ' ', ' ', ' '], [' ', '^', '^', '^'], [' ', '-', '-', '-'], [' ', ' ', ' ', 'x']], (0,0))


# Stack
def dfs (grid, start, goal):
  cost = 0
  start = (0, 0)
  visited = []
  visited.append(start)
  current = start
  # frontier params: coordinate, cost
  frontier = [(start, 0)]

  while not (len(frontier)) == 0: # As long as the queue is not empty, do all these things
    if current == goal: # If goal is reached, stop
      return visited

    # Explore all the possible neighbors
    neighbors = exploreNeighbors(grid, current)

    for neighbor in neighbors:
      if neighbor in visited:
        return
      else:
        print(neighbor, 'current')
        visited.append(neighbor)
        x = neighbor[0]
        y = neighbor[1]
        if (grid[x][y]):
          cost += COSTS[grid[x][y]]
          frontier.append((neighbor, cost))
        
    return visited
  print(frontier)  

  # for each square adjacent to the current square:
    # if (mountain is an obstacle), then cannot go to that square
      # continue
    # if (neighbor is not in visited)
      # path.add(neighbor)
      # Figure out the cost of the neighbor - Call a separate function with costs? 
      # search(path, visited, current) // Recursively visit all squares accessible from the neighbor
      # step back from neighbor to current, so you can visit the next neighbor of the current.
      # path.add(current)

dfs([['s', ' ', ' ', ' '], [' ', '^', '^', '^'], [' ', '-', '-', '-'], [' ', ' ', ' ', 'x']], (1, 1), (3, 3))

# BFS is nearly identical to DFS, the difference being which node you check next. With DFS you check the last node you discovered whereas with BFS you check the first one you discovered. 


# Queue
# Not all squares might be visited
# def bfs(path, visited, current):
#   costs = 0
#   startNode = (0, 0)

  
#   queue = []
#   visited = []

  # for each square adjacent to the current square:
    # if (mountain is an obstacle), then cannot go to that square
      # continue
    # if (neighbor is not in visited)

      # queue the current node
      
      # while there are thing in the queue:
        # Dequeue a vertex from it 
        # current = queue.pop(0)

      # search(path, visited, current) // Recursively visit all squares accessible from the neighbor

      # Figure out the cost of the neighbor - Call a separate function with costs? 