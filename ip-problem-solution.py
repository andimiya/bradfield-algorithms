def restore_ip_addresses(s):
  res = []
  path = []

  def dfs(i):
    if len(path) == 4:
      if i == len(s):
        res.append('.'.join(path))
      return
    for di in range(1, 4):
      if i + di <= len(s):
        path.append(s[i:i+di])
        if di == 1:
          dfs(i + di)
        elif di == 2 and s[i] != "0":
          dfs(i + di)
        elif di == 3 and s[i] != "0" and int(s[i:i+3]) <= 255:
          dfs(i + di)
        path.pop()
  
  dfs(0)
  return res

print(restore_ip_addresses("521522"))