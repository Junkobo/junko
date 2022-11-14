from playsound import playsound
print ("you find a bridge that's broken what are you gonna do")
choice1 = input ("(1) Jump over, (2) Build a ladder, (3) Jump down ")
if choice1 == "1":
    print("you jump over adn dident fall but there is a horde of pyro jacks on the other side of the brige what do you do")
    choice2 = input ("(1) you use fire attack, (2) you use a ice attack (3) you use a wind attack.")
    if choice2 == "1":
        print("you stupid twat you that did nothing and you die")
    elif choice2 == "2":
         print("you got a crit on the hord and they die. you never got hit and yo safe and sound. you keep going further in the forset beyond the briged and you find the matador standing there waiting for you.")
         speech1 = input (" you hear a voice *only one of us will escape this forest alive. The victor shall claim the loser's menorah, and return in  triumph. You hold a menorah... Then, like me you must be seeking supreme power. That i cannot allow* !prees f too contineu.")
         if speech1 == "f":
            print("*Only the greatest warrior is worthy of such authority. It is meant for a master swordsman... One who, amidst blood and applause, has put an end to countless lives. That warrior is I, Matador. I'm sorry to say, but you seem rather week to be in a possession of a menorah. You should hand it to one more deserving, such as I. But since it's unlikely that you'll head my advice... I challenge you to a duel. We shall determine which of us is truly worthy of the menorha. I Swear, by my sword and capote, that i will once again prove victorious! Now, let the battle begin!*")
            BattleMetador = input("prees f to countineu")
            if BattleMetador == "f":
             playsound("C:\\Users\\elias.sellgren\\Pictures\\2020-10\\music for rpg\\Shin-Megami-Tensei-V-OST-Battle-Demifiend-.wav")
            print("Metador use red Capote. hes Evasion/ Hit Rate increased by 4 stages and then uses Mazan to hit you with a medium wind attack but it did nothing")
            BattleMetador2 = input(" (1) Attack, (2) fire breath, (3) mabufu (4) Lunge")
            if BattleMetador2 == "1":
                print("You did lite dmg")
            elif BattleMetador2 == "2":
                print("you did lite dmg") 
    elif choice2 == "3":
        print("you hit them but it didnt do that much dmg")
elif choice1 == "2":
    print("you build a ladder and made it over same but there is a horde of abaddon on the otherside")
elif choice1 == "3":
    print("you jump down in to the water and made it safe you go up on the chore and find a hordes of Mot")
