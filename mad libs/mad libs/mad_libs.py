import random

answer = "a"

words = []

print("Welcome to the Mad Libs game!")
print("The book you will write will be randomly selected, so do try to fill in the blanks and enjoy it!")
print()

while answer != "q":

    bookNum = random.randint(1,3)

    if bookNum == 1:

        for i in range(1,5):
            words.append(input("(" + str(i) + "/13) Enter an adjective: ")) # 4
        for i in range(5,9):
            words.append(input("(" + str(i) + "/13) Enter a plural noun: ")) # 4
        for i in range (9,10):
            words.append(input("(" + str(i) + "/13) Enter a verb: ")) # 1
        for i in range (10,12):
            words.append(input("(" + str(i) + "/13) Enter a name: ")) # 2
        for i in range (12,13):
            words.append(input("(" + str(i) + "/13) Enter a number: ")) # 1
        for i in range(13,14):
            words.append(input("(" + str(i) + "/13) Enter a weather condition: ")) # 1

        print()
        print("The Great Treasure Hunt")
        print()
        print("In a world of boundless sea, the " + words[0] + " Pirates, led by the valiant Captain " + words[9] + ", embark on a legendary quest for the fabled " + words[11] + " Piece!")
        print("Together with his crew, Captain " + words[9] + " will sail the many islands and become the King of Pirates.")
        print("Their indomitable ship, the Thousand " + words[11] + " will sail through tumultuous seas, braving " + words[1] + " waves and perilous " + words[4] + " while exploring the Grand Line.")
        print("The " + words[2] + " sea would show them countless " + words[5] + " that defy the laws of nature, " + words[8] + "ing their senses and sparking their boundless curiosity.")
        print("As their odyssey unfolds, the bonds between the " + words[0] + " Pirates grow stronger, tested by fierce " + words[7] + " and forged in the crucible of battle.")
        print("As a decisive battle against pirate " + words[10] + " and their " + words[3] + " crew draws near, the ultimate destiny of the " + words[11] + " Piece awaits, ready to reshape the world in an era of " + words[7] + " and harmony!")


    elif bookNum == 2:

        for i in range(1,3):
            words.append(input("(" + str(i) + "/12) Enter an adjective: ")) # 2
        for i in range(3,6):
            words.append(input("(" + str(i) + "/12) Enter a noun: ")) # 3
        for i in range (6,8):
            words.append(input("(" + str(i) + "/12) Enter a verb: ")) # 2
        for i in range (8,12):
            words.append(input("(" + str(i) + "/12) Enter a name: ")) # 4
        for i in range (12,13):
            words.append(input("(" + str(i) + "/12) Enter a number: ")) # 1

        print()
        print("Ninja Nonsense")
        print()
        print("In a world of wacky ninja antics and flying kunai, " + words[7] + ", a ninja wannabe, sets off on an adventure to become the most " + words[0] + " ninja ever.")
        print("Guided by their eccentric sensei, " + words[8] + ", and accompanied by their quirky sidekick, " + words[9] + ", they stumble through training, attempting to master bizarre " + words[2] + " tricks and hilariously failing at " + words[5] + "ing with style.")
        print("Amidst chaotic landscapes and oddball encounters, " + words[7] + " unlocks the mysteries of the ancient " + words[3] + ", a hidden secret rumored to unleash the ultimate power of the " + words[11] + "-tailed beast with a twist.")
        print("Armed with their mismatched ninja gear and a rubber " + words[4] + ", they face off against comically tough foes, showcasing their " + words[1] + " skills in the most uproarious ways.")
        print("In a final showdown against the ninja troublemaker " + words[10] + ", " + words[7] + " taps into their inner absurdity, channeling the mighty " + words[11] + "-tail to unleash a wave of slapstick chaos.")
        print("Their victory stands as a shining example of the true ninja spirit, inspiring laughter and others to embrace the zany world of " + words[1] + " hilarity and embark on their own laugh-filled escapades.")
    

    elif bookNum == 3:

        for i in range(1,6):
            words.append(input("(" + str(i) + "/15) Enter an adjective: ")) # 5
        for i in range(6,10):
            words.append(input("(" + str(i) + "/15) Enter a noun: ")) # 4
        for i in range (10,12):
            words.append(input("(" + str(i) + "/15) Enter a verb: ")) # 2
        for i in range (12,16):
            words.append(input("(" + str(i) + "/15) Enter a name: ")) # 4

        print()
        print("Soul Society Shenanigans") 
        print()
        print("In a realm of " + words[0] + " spirits and uproarious battles, the offbeat Soul Reaper " + words[11] + " leaps into a great adventure to protect the living from the wild " + words[5] + "s that haunt humans.")
        print("Under the guidance of their eccentric mentor " + words[12] + ", they journey to master the art of wielding " + words[1] + " techniques and battles, with just a hint of absurdity.")
        print("Amidst many " + words[2] + " landscapes and encounters, " + words[11] + " unravels mysteries of the peculiar " + words[13] + " Blade, a rare artifact rumored to unlock the ultimate power of " + words[9] + "ing.")
        print("Armed with a Soul Reaper badge and a comically large " + words[6] + ", they face off against " + words[5] + " monsters, showcasing their " + words[3] + " combat flairs that they've all learned.")
        print("In a showdown against the " + words[5] + " mastermind, " + words[14] + ", " + words[11] + " taps into their inner power, chanelling the " + words[4] + " energy of the " + words[13] + " Blade to deliver a final " + words[9] + " strike.")
        print("Their strength becomes a " + words[7] + " of true Soul Reaper strength, inspiring hope and " + words[10] + "ing others to embrace the power of " + words[8] + " and go off on their own escapades.") 

    print()
    answer = input("Enter any key to play again, or 'q' to quit! ")
    print()

print("Thank you for playing!")