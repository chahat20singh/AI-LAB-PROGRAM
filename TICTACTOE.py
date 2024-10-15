board = {1: &#39; &#39;, 2: &#39; &#39;, 3: &#39; &#39;,
4: &#39; &#39;, 5: &#39; &#39;, 6: &#39; &#39;,
7: &#39; &#39;, 8: &#39; &#39;, 9: &#39; &#39;}

def printBoard(board):
print(board[1] + &#39;|&#39; + board[2] + &#39;|&#39; + board[3])
print(&#39;-+-+-&#39;)
print(board[4] + &#39;|&#39; + board[5] + &#39;|&#39; + board[6])
print(&#39;-+-+-&#39;)
print(board[7] + &#39;|&#39; + board[8] + &#39;|&#39; + board[9])
print(&#39;\n&#39;)

def spaceFree(pos):
if board[pos] == &#39; &#39;:
return True
else:
return False

def checkWin():
if (board[1] == board[2] and board[1] == board[3] and board[1] != &#39; &#39;):
return True
elif (board[4] == board[5] and board[4] == board[6] and board[4] != &#39; &#39;):
return True
elif (board[7] == board[8] and board[7] == board[9] and board[7] != &#39; &#39;):
return True
elif (board[1] == board[5] and board[1] == board[9] and board[1] != &#39; &#39;):
return True
elif (board[3] == board[5] and board[3] == board[7] and board[3] != &#39; &#39;):
return True
elif (board[1] == board[4] and board[1] == board[7] and board[1] != &#39; &#39;):

return True
elif (board[2] == board[5] and board[2] == board[8] and board[2] != &#39; &#39;):
return True
elif (board[3] == board[6] and board[3] == board[9] and board[3] != &#39; &#39;):
return True
else:
return False

def checkMoveForWin(move):
if (board[1] == board[2] and board[1] == board[3] and board[1] == move):
return True
elif (board[4] == board[5] and board[4] == board[6] and board[4] == move):
return True
elif (board[7] == board[8] and board[7] == board[9] and board[7] == move):
return True
elif (board[1] == board[5] and board[1] == board[9] and board[1] == move):
return True
elif (board[3] == board[5] and board[3] == board[7] and board[3] == move):
return True
elif (board[1] == board[4] and board[1] == board[7] and board[1] == move):
return True
elif (board[2] == board[5] and board[2] == board[8] and board[2] == move):
return True
elif (board[3] == board[6] and board[3] == board[9] and board[3] == move):
return True
else:
return False

def checkDraw():
for key in board.keys():
if board[key] == &#39; &#39;:
return False
return True

def insertLetter(letter, position):
if spaceFree(position):
board[position] = letter
printBoard(board)

if checkDraw():
print(&#39;Draw!&#39;)
elif checkWin():
if letter == &#39;X&#39;:
print(&#39;Bot wins!&#39;)
else:
print(&#39;You win!&#39;)
return

else:
print(&#39;Position taken, please pick a different position.&#39;)
position = int(input(&#39;Enter new position: &#39;))
insertLetter(letter, position)
return

player = &#39;O&#39;
bot = &#39;X&#39;

def playerMove():
position = int(input(&#39;Enter position for O: &#39;))
insertLetter(player, position)
return

def compMove():
bestScore = -1000
bestMove = 0
for key in board.keys():

if board[key] == &#39; &#39;:
board[key] = bot
score = minimax(board, False)
board[key] = &#39; &#39;
if score &gt; bestScore:
bestScore = score
bestMove = key

insertLetter(bot, bestMove)
return

def minimax(board, isMaximizing):
if checkMoveForWin(bot):
return 1
elif checkMoveForWin(player):
return -1
elif checkDraw():
return 0

if isMaximizing:
bestScore = -1000

for key in board.keys():
if board[key] == &#39; &#39;:
board[key] = bot
score = minimax(board, False)
board[key] = &#39; &#39;
if score &gt; bestScore:
bestScore = score
return bestScore
else:
bestScore = 1000

for key in board.keys():
if board[key] == &#39; &#39;:
board[key] = player
score = minimax(board, True)
board[key] = &#39; &#39;
if score &lt; bestScore:
bestScore = score
return bestScore

while not checkWin():
compMove()
playerMove()