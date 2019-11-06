import time
def name():
    name=input("Hahoy! What's your name? ")
    if name in ("Carlotta", "Carly", "Totta", "carlotta", "totta", "carly"):
        print("We carly è tardi ma ce l'ho fatta, visto?")    
def sort():
    a=[]
    b=[]
    n=0
    f=0
    while n<10:
        try:
            z= int(input("Give me a number! (I'll need 10 of them but i'll just ask them one by one): "))
            a.append(z)
            n+=1
        except ValueError:
            print ("Hey dude, that's not a valid number!")
    print (a)
    while 1:
        answ= input("Are you satisfied with this list? ")
        if answ in ("no", "No", "nope", "Nope"):
            print ("Ok, no problem, just give me a second!")
            time.sleep(1)
            sort()
        elif answ in ("yeah", "yes", "yep","Yes"):
            print ("Very good ^.^")
            print ("I'll now sort this list!")
            time.sleep(2)
            while len(b)<10:
                if f in a:
                    b.append(f)
                else:
                    pass
                f+=1
            print (b)
            time.sleep(1)
            print ("Ta-duh!!")
            time.sleep(1)
            print ("Hope you liked it! See ya!")
            break
        else:
            print ("Sorry man, didn't really catch that")
name()
sort()