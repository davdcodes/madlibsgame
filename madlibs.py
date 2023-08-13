import random

bookNum = random.randint(0,1)

# possible rework: combine items into a list, prompt user for each item and append to list.
# systen would be aware of what prompt each index was assigned and insert into the story appropriately

adj1 = input("(1/13) Enter an adjective: ")
adj2 = input("(2/13) Enter an adjective: ")
adj3 = input("(3/13) Enter an adjective: ")
adj4 = input("(4/13) Enter an adjective: ")
pnoun1 = input("(5/13) Enter a plural noun: ")
pnoun2 = input("(6/13) Enter a plural noun: ")
pnoun3 = input("(7/13) Enter a plural noun: ")
pnoun4 = input("(8/13) Enter a plural noun: ")
verb1 = input("(9/13) Enter a -ing verb: ")
name1 = input("(10/13) Enter a name: ")
name2 = input("(11/13) Enter a name: ")
num = input("(12/13) Enter a number: ")
weather = input("(13/13) Enter a type of weather: ")

if bookNum == 1:
    print("The Great Treasure Hunt")
    print("In a world of boundless sea, the " + adj1 + " Pirates, led by the valiant Captain " + name1 + ", embark on a legendary quest for the fabled " + num + " Piece!")
    print("Together with his crew, Captain " + name1 + " will sail the many islands and become the King of Pirates.")
    print("Their indomitable ship, the Thousand " + weather + " will sail through tumultuous seas, braving " + adj2 + " waves and perilous " + pnoun1 + " while exploring the Grand Line.")
    print("The " + adj3 + " sea would show them countless " + pnoun2 + " that defy the laws of nature, " + verb1 + " their senses and sparking their boundless curiosity.")
    print("As their odyssey unfolds, the bonds between the " + adj1 + " Pirates grow stronger, tested by fierce " + pnoun3 + " and forged in the crucible of battle.")
    print("As a decisive battle against pirate " + name2 + " and their " + adj4 + " crew draws near, the ultimate destiny of the " + num + " Piece awaits, ready to reshape the world in an era of " + pnoun4 + " and harmony!")


elif bookNum == 2:
    print("The Daring Rescue")

elif bookNum == 3:
    print("The Gigantic Party")

elif bookNum == 4:
    print("The Magical Quest")

else:
    print("No book for you!")