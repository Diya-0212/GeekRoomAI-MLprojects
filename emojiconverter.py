
def emo_con (msg):
    l=msg.split(' ')
    d={":)":"😊", ":(":"😒"}
    output=""
    for i in l:
        u=d.get(i,i)
        output+=u+ " "
    return output
msg=input(">")
print(emo_con(msg))