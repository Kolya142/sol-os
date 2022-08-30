from replit import db
import os
username = os.environ['REPL_OWNER']
if not username in list(db):
  db[username] = 0
score = db[username]
c = True
while True:
  os.system("clear")
  d = []
  for p in list(db):
    d.append(db[p])
  ms = max(d)
  print(f'your score: {score}')
  print(f'max score: {ms}')
  print(f'all players: {db.keys()}')
  i = input('"c"-->score+1, "exit"-->quit\n')
  if i == "c" and not c:
    score += 1
    db[username] = score
    c = True
  elif i == "exit":
    quit()
  else:
    c = False
