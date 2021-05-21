# chapter 10 hangman

def hangman(word):
    wrong = 0
    stages = ["",
              "_______        ",
              "|              ",
              "|      |       ",
              "|      0       ",
              "|     /|\      ",
              "|     / \      ",
              "|              "
              ]
    rletters = list(word)
    board = ["_"]*len(word)
    win = False
    print("ハングマンへようこそ！")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字を予想してね:"
        char = input(msg)
        if char in rletters:
            # rletters内のcharに一致する数
            number = rletters.count(char)
            # char に一致した回数だけ、boardを書き換え
            for i in range(number):
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("あなたの負け！正解は {}.".format(word))

hangman("letter")