que = input("好きな食べ物は？：")

with open("answer.txt", "w") as f:
    f.write(que)
