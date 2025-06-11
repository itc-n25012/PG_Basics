correct_answer = [3, 5, 7, 11, 13, 17, 19, 23, 29]

# 数字当てプログラム、qを押したら終了
while True:
    answer = input("数字を入力してください[終了するときはqを押してください]:")
    if answer == "q":
        break
#例外処理
    try:
        answer = int(answer)
    except ValueError:
        print("数字を入力するか、qで終了します")
#入力された値が一致で正解、不一致で不正解
    if answer in correct_answer:
        print("正解")
    else:
        print("不正解")
