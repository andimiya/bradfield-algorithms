import heapq
import collections

def networkDelayTime(times, N, K):
  
  # Are any of the w values negative?
  # return -1

  graph = collections.defaultdict(list)
  for src, tgt, time in times:
    graph[src].append((tgt, time))
  print(graph, 'graph')
  distances = {vertex: float('infinity') for vertex in graph}
  distances[K] = 0

  entry_lookup = {}
  pq = []

  for vertex, distance in distances.items():
    entry = [distance, vertex]
    entry_lookup[vertex] = entry
    heapq.heappush(pq, entry)
  while len(pq) > 0:
    current_distance, current_vertex = heapq.heappop(pq)
    for neighbor, neighbor_distance in graph[current_vertex]:
      
      distance = distances[current_vertex] + neighbor_distance
      if distance < distances[neighbor]:
        distances[neighbor] = distance
        entry_lookup[neighbor][0] = distance
  return distances

print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1],[4,5,1]],5,2))