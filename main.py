import random
s=["rock","paper","seasors"]
print("welcome to stg's rps game 👊 📄 ✌️️")
flag=1;
while flag==1:
    print("chose rock paper or seasor")
    user = int(input("for rock press 0 for paper 1 for seasor 2"))
    comp = random.choice([0, 1, 2])
    print("u chose", s[user])
    print("i chose", s[comp])
    if (s[user] == s[comp]):
        print("draw")
        continue;
    elif(s[comp]=="rock"):
        if(s[user]=="seasors"):
            print("comp wins")
        else:
            print("user wins")
    elif(s[comp]=="seasors"):
        if (s[user] == "paper"):
            print("comp wins")
        else:
            print("user wins")
    elif (s[comp] == "paper"):

        if (s[user] == "seasor"):
            print("comp wins")
        else:
            print("user wins")
    s1=input("do u want to play again y or n")
    if(s1=="n"):
        flag=0