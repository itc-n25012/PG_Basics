def hangman(word):
    wrong = 0
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\\     ",
             "|       / \\     ",
             "|               "
              ]

    rletters = list(word)  # 正解の文字列をリスト化し、変数に代入。
    board = ["__"] * len(word)
    win = False
    print("ハングマンへようこそ")
    print(" ".join(board)) # joinメソッドを使って、リストの"__"と"__"の間にスペースを追加。

    while wrong < len(stages) - 1:
        print("\n")
        msg = "１文字を予想してね："
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char) # 正解した文字のインデックス番号を変数に代入
            # 文字列に同じ文字が複数ある場合、当たった文字を伏せ字$にする
            board[cind] = char 
            rletters[cind] = '$'
        else:
            wrong += 1

        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0: e]))

        # ゲームクリアの処理
        if "__" not in board:
            print("あなたの勝ち！")
            print(" ".join(board))
            win = True
            break

    #ゲームオーバーの処理
    if not win:
        print("\n".join(stages[0:wrong]))
        print("あなたの負け！正解は{}.".format(word))

hangman("cat")
