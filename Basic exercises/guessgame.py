num=9
guess_count=1
while guess_count<=3:
    g=int(input("guess:"))
    if g== num:
        print("you win")
        break
    guess_count= guess_count + 1
else:
    print("you lost!!!")