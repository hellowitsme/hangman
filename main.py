import random

def hangman():
  words = ["google", "apple", "facebook", "apple", "microsoft", "alibaba"]
  word = words[random.randint(0, 5)]
  wrong = 0
  stages = ["",
            "___________         ",
            "|                   ",
            "|         |         ",
            "|         o         ",
            "|        /|\\       ",
            "|        / \\       ",
            "|                   ",
            "|__________         "
           ]
  letters = list(word)
  board = ["_"] * len(word)
  win = False
  print("Game Start!!")
  
  while wrong < len(stages) -1:
      print("\n")
      msg = "1文字を予想してね:"
      char = input(msg)
      if char in letters:
          ind = letters.index(char)
          board[ind] = char
          letters[ind] = '$'
      else:
          wrong += 1
      print(" ".join(board))
      e = wrong + 1
      print("\n".join(stages[0:e]))
      if "_" not in board:
          print("You win!! Answer was: {}.".format(word))
          print(" ".join(board))
          win = True
          break
  if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose!! Answer was: {}.".format(word))

hangman()
