import pickle as pk
count = 1
while True:
    with open('users.bin', 'wb') as f:
        c = input("do you wanna continue enter y or n ")
        if (c == 'y'):
            a = input("enter data "+str(count))
            pk.dump(a,f)
            count += 1
            pk.close()
        else:
            break
