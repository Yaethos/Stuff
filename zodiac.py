import time

def waittime():
    print(" ")
def zodiac():
    name=input("Hi there! What's your name? ")
    if name in ("Carlotta", "Carly", "Totta", "carlotta", "totta", "carly"):
        print("We carly, provaci tu a fare sta roba e vediamo se ce la fai in meno righe")
    while 1:
        answ= input("Would you like to know your zodiac sign? " )
        if answ== "no" or answ== "nope" or answ== "No":
            print ("Ok, your loss")
            print ("Booting up...")
            time.sleep(2)
            for i in range (150):
                 print ("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            print (" You think you're funny, don't you?")
            print ("I'll give you one more chance")
            waittime()
            waittime()
            ascendent()
        elif answ== 'yes' or answ== 'yeah' or answ== 'yep' or answ== "Yes":
            while 1:
                try:
                    day,month,year = input("Okie dokie, I just need you to enter your birthdate like this: DD/MM/YYYY ").split("/")
                    if 1<=int(day)<=31 and 1<=int(month)<=12:
                     break
                    else:
                        print ("Hey, that's not a valid date!")
                except ValueError:
                     print ("Hey, that's not a valid date!")
            if month==("03") and int(day)>=21 or month==("04") and int(day)>0 and int(day)<=20:
                print ("Hey! You're an Aries!")
                print ("Famous Aries people: Robert Downey Jr, Lady Gaga, Emma Watson, Leonardo Da Vinci")
            elif month==("04") and int(day)>=21 or month==("05") and int(day)>0 and int(day)<=20:
                print ("Hey! You're a Taurus!")
                print ("Famous Taurus people: Dwayne Johnson, Wes Anderson, Salvador Dalì, William Shakespeare and the creator of this code!")
            elif month==("05") and int(day)>=21 or month==("06") and int(day)>0 and int(day)<=21:
                print ("Hey! You're a Gemini!")
                print ("Famous Gemini people: Marilyn Monroe, Johnny Depp, Morgan Freeman, Prince and John F. Kennedy")
            elif month==("06") and int(day)>=22 or month==("07") and int(day)>0 and int(day)<=22:
                print ("Hey! You're a Cancer!")
                print ("Famous Cancer people: Carlos Santana, Robin Williams, Kevin Hart, Franz Kafka and George Orwell")
            elif month==("07") and int(day)>=23 or month==("08") and int(day)>0 and int(day)<=23:
                print ("Hey! You're a Leo!")
                print ("Famous Leo people: Barack Obama, Neil Armstrong, Terry Crews, Stanley Kubrick and Jennifer Lawrence")
            elif month==("08") and int(day)>=24 or month==("09") and int(day)>0 and int(day)<=23:
                print ("Hey! You're a Virgo!")
                print ("Famous Virgo people: Michael Jackson, Our Lord and Savior Keanu Reeves, Tim Burton, Julian Casablancas and Paulo Coelho")
            elif month==("09") and int(day)>=24 or month==("10") and int(day)>0 and int(day)<=23:
                print ("Hey! You're a Libra!")
                print ("Famous Libra people: Will Smith, Snoop Dogg, Mahatma Gandhi, Vladimir Putin and Emilia Clarke")
            elif month==("10") and int(day)>=24 or month==("11") and int(day)>0 and int(day)<=22:
                print ("Hey! You're a Scorpio!")
                print ("Famous Scorpio people: Julia Roberts, Matthew McConaughey, Leonardo DiCaprio, Pablo Picasso and Emma Stone")
            elif month==("11") and int(day)>=23 or month==("12") and int(day)>0 and int(day)<=21:
                print ("Hey! You're a Sagittarius!")
                print ("Famous Sagittarius people: Scarlett Johansson, Ben Stiller, Brad Pitt, Jimi Hendrix and Samuel L. Jackson")
            elif month==("12") and int(day)>=22 or month==("01") and int(day)>0 and int(day)<=20:
                print ("Hey! You're a Capricorn!")
                print ("Famous Capricorn people: Kit Harrington, Jeff Bezos, Elvis Presley, Stephen Hawking and David Bowie")
            elif month==("01") and int(day)>=21 or month==("02") and int(day)>0 and int(day)<=18:
                print ("Hey! You're an Aquarius!")
                print ("Famous Aquarius people: Jennifer Aniston, Bob Marley, Billie Joe Armstrong, John Travolta and Charles Darwin")
            elif month==("02") and int(day)>=19 or month==("03") and int(day)>0 and int(day)<=20:
                print ("Hey! You're a Pisces!")
                print ("Famous Pisces people: Steve Jobs, Albert Einstein, Kurt Cobain, Alan Rickman and Bryan Cranston")
            else:
                print ("Hey, that's not a valid date")
                    
            answ2= input("Would you like to know your chinese zodiac sign? ")
            if answ2 in ("yeah", "yes", "yep","Yes"):
                if (int(year)/12).is_integer():
                    print ("Hey, you're a Monkey!")
                elif ((int(year)-1)/12).is_integer():
                    print ("Hey, you're a Rooster!")
                elif ((int(year)-2)/12).is_integer():
                    print ("Hey, you're a Dog!")
                elif ((int(year)-3)/12).is_integer():
                    print ("Hey, you're a Pig!")
                elif ((int(year)-4)/12).is_integer():
                    print ("Hey, you're a Rat!")
                elif ((int(year)-5)/12).is_integer():
                    print ("Hey, you're a Ox!")
                elif ((int(year)-6)/12).is_integer():
                    print ("Hey, you're a Tiger!")
                elif ((int(year)-7)/12).is_integer():
                    print ("Hey, you're a Rabbit!")
                elif ((int(year)-8)/12).is_integer():
                    print ("Hey, you're a Dragon!")
                elif ((int(year)-9)/12).is_integer():
                    print ("Hey, you're a Snake!")
                elif ((int(year)-10)/12).is_integer():
                    print ("Hey, you're a Horse!")
                elif ((int(year)-11)/12).is_integer():
                    print ("Hey, you're a Goat!")
            elif answ2== "no" or answ== "nope" or answ== "No":
                print ("Ok, your loss")
            
            print("Bye!")
            waittime()
            waittime()
            break
            
            

            

        else:
            print ("Sorry, didn't really get that")

def ascendent():
    zodiac()
    waittime()
    waittime()
    waittime()
    waittime()
    fascia1=[6,7]
    fascia2=[8,9]
    fascia3=[10,11]
    fascia4=[12,13]
    fascia5=[14,15]
    fascia6=[16,17]
    fascia7=[18,19]
    fascia8=[20,21]
    fascia9=[22,23]
    fascia10=[24,1,0,00]
    fascia11=[2,3]
    fascia12=[4,5]
    name= input("Hey there, what's your name again? ")
    while 1:
        answ= input("Would you like now to know your zodiac ascendent? " )
        if answ== "no" or answ== "nope" or answ== "No":
            print ("Well, your loss")
            waittime()
            waittime()
            ascendent()
        elif answ== 'yes' or answ== 'yeah' or answ== 'yep' or answ== "Yes":
            while 1:
                try:
                    hour = int(input("Ok, I just need the hour you were born in (24 Hours format) "))
                    if 0<=hour<=24:
                        break
                    else:
                        print ("Hey, that's not a valid input")
                except ValueError:
                        print ("Hey, that's not a valid input!")
            while 1:
                try:
                    sign = input ("Hey, I don't remember your zodiac sign. Can you tell me what it is? ")
                    if sign in ("aries", "taurus", "gemini", "cancer", "leo", "virgo", "libra", "scorpio", "sagittarius", "capricorn", "aquarius", "pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"):
                     break
                    else:
                        print ("Hey, that's not a valid input")
                except ValueError:
                        print ("Hey, that's not a valid sign!")
            if sign in ("aries", "Aries"):
                        if hour in fascia1:
                            print ("Hey "+name+" you're a "+sign+" ascendent Taurus")
                        elif hour in fascia2:
                            print ("Hey "+name+" you're a "+sign+" ascendent Gemini")
                        elif hour in fascia3:
                            print ("Hey "+name+" you're a "+sign+" ascendent Cancer")
                        elif hour in fascia4:
                            print ("Hey "+name+" you're a "+sign+" ascendent Leo")
                        elif hour in fascia5:
                            print ("Hey "+name+" you're a "+sign+" ascendent Virgo")
                        elif hour in fascia6:
                            print ("Hey "+name+" you're a "+sign+" ascendent Libra")
                        elif hour in fascia7:
                            print ("Hey "+name+" you're a "+sign+" ascendent Scorpio")
                        elif hour in fascia8:
                            print ("Hey "+name+" you're a "+sign+" ascendent Sagittarius")
                        elif hour in fascia9:
                            print ("Hey "+name+" you're a "+sign+" ascendent Capricorn")
                        elif hour in fascia10:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aquarius")
                        elif hour in fascia11:
                            print ("Hey "+name+" you're a "+sign+" ascendent Pisces")
                        elif hour in fascia12:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aries")
            elif sign in ("taurus", "Taurus"):
                        if hour in fascia1:
                            print ("Hey "+name+" you're a "+sign+" ascendent Gemini")
                        elif hour in fascia2:
                            print ("Hey "+name+" you're a "+sign+" ascendent Cancer")
                        elif hour in fascia3:
                            print ("Hey "+name+" you're a "+sign+" ascendent Leo")
                        elif hour in fascia4:
                            print ("Hey "+name+" you're a "+sign+" ascendent Virgo")
                        elif hour in fascia5:
                            print ("Hey "+name+" you're a "+sign+" ascendent Libra")
                        elif hour in fascia6:
                            print ("Hey "+name+" you're a "+sign+" ascendent Scorpio")
                        elif hour in fascia7:
                            print ("Hey "+name+" you're a "+sign+" ascendent Sagittarius")
                        elif hour in fascia8:
                            print ("Hey "+name+" you're a "+sign+" ascendent Capricorn")
                        elif hour in fascia9:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aquarius")
                        elif hour in fascia10:
                            print ("Hey "+name+" you're a "+sign+" ascendent Pisces")
                        elif hour in fascia11:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aries")
                        elif hour in fascia12:
                            print ("Hey "+name+" you're a "+sign+" ascendent Taurus")
            elif sign in ("Gemini", "gemini"):
                        if hour in fascia1:
                            print ("Hey "+name+" you're a "+sign+" ascendent Cancer")
                        elif hour in fascia2:
                            print ("Hey "+name+" you're a "+sign+" ascendent Leo")
                        elif hour in fascia3:
                            print ("Hey "+name+" you're a "+sign+" ascendent Virgo")
                        elif hour in fascia4:
                            print ("Hey "+name+" you're a "+sign+" ascendent Libra")
                        elif hour in fascia5:
                            print ("Hey "+name+" you're a "+sign+" ascendent Scorpio")
                        elif hour in fascia6:
                            print ("Hey "+name+" you're a "+sign+" ascendent Sagittarius")
                        elif hour in fascia7:
                            print ("Hey "+name+" you're a "+sign+" ascendent Capricorn")
                        elif hour in fascia8:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aquarius")
                        elif hour in fascia9:
                            print ("Hey "+name+" you're a "+sign+" ascendent Pisces")
                        elif hour in fascia10:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aries")
                        elif hour in fascia11:
                            print ("Hey "+name+" you're a "+sign+" ascendent Taurus")
                        elif hour in fascia12:
                            print ("Hey "+name+" you're a "+sign+" ascendent Gemini")
            elif sign in ("Cancer", "cancer"):
                        if hour in fascia1:
                            print ("Hey "+name+" you're a "+sign+" ascendent Leo")
                        elif hour in fascia2:
                            print ("Hey "+name+" you're a "+sign+" ascendent Virgo")
                        elif hour in fascia3:
                            print ("Hey "+name+" you're a "+sign+" ascendent Libra")
                        elif hour in fascia4:
                            print ("Hey "+name+" you're a "+sign+" ascendent Scorpio")
                        elif hour in fascia5:
                            print ("Hey "+name+" you're a "+sign+" ascendent Sagittarius")
                        elif hour in fascia6:
                            print ("Hey "+name+" you're a "+sign+" ascendent Capricorn")
                        elif hour in fascia7:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aquarius")
                        elif hour in fascia8:
                            print ("Hey "+name+" you're a "+sign+" ascendent Pisces")
                        elif hour in fascia9:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aries")
                        elif hour in fascia10:
                            print ("Hey "+name+" you're a "+sign+" ascendent Taurus")
                        elif hour in fascia11:
                            print ("Hey "+name+" you're a "+sign+" ascendent Gemini")
                        elif hour in fascia12:
                            print ("Hey "+name+" you're a "+sign+" ascendent Cancer")
            elif sign in ("Leo", "leo"):
                        if hour in fascia1:
                            print ("Hey "+name+" you're a "+sign+" ascendent Virgo")
                        elif hour in fascia2:
                            print ("Hey "+name+" you're a "+sign+" ascendent Libra")
                        elif hour in fascia3:
                            print ("Hey "+name+" you're a "+sign+" ascendent Scorpio")
                        elif hour in fascia4:
                            print ("Hey "+name+" you're a "+sign+" ascendent Sagittarius")
                        elif hour in fascia5:
                            print ("Hey "+name+" you're a "+sign+" ascendent Capricorn")
                        elif hour in fascia6:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aquarius")
                        elif hour in fascia7:
                            print ("Hey "+name+" you're a "+sign+" ascendent Pisces")
                        elif hour in fascia8:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aries")
                        elif hour in fascia9:
                            print ("Hey "+name+" you're a "+sign+" ascendent Taurus")
                        elif hour in fascia10:
                            print ("Hey "+name+" you're a "+sign+" ascendent Gemini")
                        elif hour in fascia11:
                            print ("Hey "+name+" you're a "+sign+" ascendent Cancer")
                        elif hour in fascia12:
                            print ("Hey "+name+" you're a "+sign+" ascendent Leo")
            elif sign in ("Virgo", "virgo"):
                        if hour in fascia1:
                            print ("Hey "+name+" you're a "+sign+" ascendent Libra")
                        elif hour in fascia2:
                            print ("Hey "+name+" you're a "+sign+" ascendent Scorpio")
                        elif hour in fascia3:
                            print ("Hey "+name+" you're a "+sign+" ascendent Sagittarius")
                        elif hour in fascia4:
                            print ("Hey "+name+" you're a "+sign+" ascendent Capricorn")
                        elif hour in fascia5:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aquarius")
                        elif hour in fascia6:
                            print ("Hey "+name+" you're a "+sign+" ascendent Pisces")
                        elif hour in fascia7:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aries")
                        elif hour in fascia8:
                            print ("Hey "+name+" you're a "+sign+" ascendent Taurus")
                        elif hour in fascia9:
                            print ("Hey "+name+" you're a "+sign+" ascendent Gemini")
                        elif hour in fascia10:
                            print ("Hey "+name+" you're a "+sign+" ascendent Cancer")
                        elif hour in fascia11:
                            print ("Hey "+name+" you're a "+sign+" ascendent Leo")
                        elif hour in fascia12:
                            print ("Hey "+name+" you're a "+sign+" ascendent Virgo")
            elif sign in ("Libra", "libra"):
                        if hour in fascia1:
                            print ("Hey "+name+" you're a "+sign+" ascendent Scorpio")
                        elif hour in fascia2:
                            print ("Hey "+name+" you're a "+sign+" ascendent Sagittarius")
                        elif hour in fascia3:
                            print ("Hey "+name+" you're a "+sign+" ascendent Capricorn")
                        elif hour in fascia4:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aquarius")
                        elif hour in fascia5:
                            print ("Hey "+name+" you're a "+sign+" ascendent Pisces")
                        elif hour in fascia6:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aries")
                        elif hour in fascia7:
                            print ("Hey "+name+" you're a "+sign+" ascendent Taurus")
                        elif hour in fascia8:
                            print ("Hey "+name+" you're a "+sign+" ascendent Gemini")
                        elif hour in fascia9:
                            print ("Hey "+name+" you're a "+sign+" ascendent Cancer")
                        elif hour in fascia10:
                            print ("Hey "+name+" you're a "+sign+" ascendent Leo")
                        elif hour in fascia11:
                            print ("Hey "+name+" you're a "+sign+" ascendent Virgo")
                        elif hour in fascia12:
                            print ("Hey "+name+" you're a "+sign+" ascendent Libra")
            elif sign in ("Scorpio", "scorpio"):
                        if hour in fascia1:
                            print ("Hey "+name+" you're a "+sign+" ascendent Sagittarius")
                        elif hour in fascia2:
                            print ("Hey "+name+" you're a "+sign+" ascendent Capricorn")
                        elif hour in fascia3:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aquarius")
                        elif hour in fascia4:
                            print ("Hey "+name+" you're a "+sign+" ascendent Pisces")
                        elif hour in fascia5:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aries")
                        elif hour in fascia6:
                            print ("Hey "+name+" you're a "+sign+" ascendent Taurus")
                        elif hour in fascia7:
                            print ("Hey "+name+" you're a "+sign+" ascendent Gemini")
                        elif hour in fascia8:
                            print ("Hey "+name+" you're a "+sign+" ascendent Cancer")
                        elif hour in fascia9:
                            print ("Hey "+name+" you're a "+sign+" ascendent Leo")
                        elif hour in fascia10:
                            print ("Hey "+name+" you're a "+sign+" ascendent Virgo")
                        elif hour in fascia11:
                            print ("Hey "+name+" you're a "+sign+" ascendent Libra")
                        elif hour in fascia12:
                            print ("Hey "+name+" you're a "+sign+" ascendent Scorpio")
            elif sign in ("Sagittarius", "sagittarius"):
                        if hour in fascia1:
                            print ("Hey "+name+" you're a "+sign+" ascendent Capricorn")
                        elif hour in fascia2:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aquarius")
                        elif hour in fascia3:
                            print ("Hey "+name+" you're a "+sign+" ascendent Pisces")
                        elif hour in fascia4:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aries")
                        elif hour in fascia5:
                            print ("Hey "+name+" you're a "+sign+" ascendent Taurus")
                        elif hour in fascia6:
                            print ("Hey "+name+" you're a "+sign+" ascendent Gemini")
                        elif hour in fascia7:
                            print ("Hey "+name+" you're a "+sign+" ascendent Cancer")
                        elif hour in fascia8:
                            print ("Hey "+name+" you're a "+sign+" ascendent Leo")
                        elif hour in fascia9:
                            print ("Hey "+name+" you're a "+sign+" ascendent Virgo")
                        elif hour in fascia10:
                            print ("Hey "+name+" you're a "+sign+" ascendent Libra")
                        elif hour in fascia11:
                            print ("Hey "+name+" you're a "+sign+" ascendent Scorpio")
                        elif hour in fascia12:
                            print ("Hey "+name+" you're a "+sign+" ascendent Sagittarius")
            elif sign in ("Capricorn", "capricorn"):
                        if hour in fascia1:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aquarius")
                        elif hour in fascia2:
                            print ("Hey "+name+" you're a "+sign+" ascendent Pisces")
                        elif hour in fascia3:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aries")
                        elif hour in fascia4:
                            print ("Hey "+name+" you're a "+sign+" ascendent Taurus")
                        elif hour in fascia5:
                            print ("Hey "+name+" you're a "+sign+" ascendent Gemini")
                        elif hour in fascia6:
                            print ("Hey "+name+" you're a "+sign+" ascendent Cancer")
                        elif hour in fascia7:
                            print ("Hey "+name+" you're a "+sign+" ascendent Leo")
                        elif hour in fascia8:
                            print ("Hey "+name+" you're a "+sign+" ascendent Virgo")
                        elif hour in fascia9:
                            print ("Hey "+name+" you're a "+sign+" ascendent Libra")
                        elif hour in fascia10:
                            print ("Hey "+name+" you're a "+sign+" ascendent Scorpio")
                        elif hour in fascia11:
                            print ("Hey "+name+" you're a "+sign+" ascendent Sagittarius")
                        elif hour in fascia12:
                            print ("Hey "+name+" you're a "+sign+" ascendent Capricorn")
            elif sign in ("Aquarius", "aquarius"):
                        if hour in fascia1:
                            print ("Hey "+name+" you're a "+sign+" ascendent Pisces")
                        elif hour in fascia2:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aries")
                        elif hour in fascia3:
                            print ("Hey "+name+" you're a "+sign+" ascendent Taurus")
                        elif hour in fascia4:
                            print ("Hey "+name+" you're a "+sign+" ascendent Gemini")
                        elif hour in fascia5:
                            print ("Hey "+name+" you're a "+sign+" ascendent Cancer")
                        elif hour in fascia6:
                            print ("Hey "+name+" you're a "+sign+" ascendent Leo")
                        elif hour in fascia7:
                            print ("Hey "+name+" you're a "+sign+" ascendent Virgo")
                        elif hour in fascia8:
                            print ("Hey "+name+" you're a "+sign+" ascendent Libra")
                        elif hour in fascia9:
                            print ("Hey "+name+" you're a "+sign+" ascendent Scorpio")
                        elif hour in fascia10:
                            print ("Hey "+name+" you're a "+sign+" ascendent Sagittarius")
                        elif hour in fascia11:
                            print ("Hey "+name+" you're a "+sign+" ascendent Capricorn")
                        elif hour in fascia12:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aquarius")
            elif sign in ("Pisces", "pisces"):
                        if hour in fascia1:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aries")
                        elif hour in fascia2:
                            print ("Hey "+name+" you're a "+sign+" ascendent Taurus")
                        elif hour in fascia3:
                            print ("Hey "+name+" you're a "+sign+" ascendent Gemini")
                        elif hour in fascia4:
                            print ("Hey "+name+" you're a "+sign+" ascendent Cancer")
                        elif hour in fascia5:
                            print ("Hey "+name+" you're a "+sign+" ascendent Leo")
                        elif hour in fascia6:
                            print ("Hey "+name+" you're a "+sign+" ascendent Virgo")
                        elif hour in fascia7:
                            print ("Hey "+name+" you're a "+sign+" ascendent Libra")
                        elif hour in fascia8:
                            print ("Hey "+name+" you're a "+sign+" ascendent Scorpio")
                        elif hour in fascia9:
                            print ("Hey "+name+" you're a "+sign+" ascendent Sagittarius")
                        elif hour in fascia10:
                            print ("Hey "+name+" you're a "+sign+" ascendent Capricorn")
                        elif hour in fascia11:
                            print ("Hey "+name+" you're a "+sign+" ascendent Aquarius")
                        elif hour in fascia12:
                            print ("Hey "+name+" you're a "+sign+" ascendent Pisces")
            
            waittime()
            waittime()
            print("Bye!")
            break
        else:
            print ("Sorry, didn't really get that")
ascendent()

