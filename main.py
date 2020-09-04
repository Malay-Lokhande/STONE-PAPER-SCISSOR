import random

chance = 0
no_of_chances = 10

c = 0
pl = 0

s = "STONE"
p = "PAPER"
si = "SCISSOR"
lis = [s, p, si]

print('---------------------------------------\n'
      'Welcome to STONE, PAPER & SCISSOR Game.\n'
      '---------------------------------------\n')

Name = input('Please Enter Name: \n')
print('Please select \n'
      '---------------\n'
      's for STONE \n'
      'p for PAPER \n'
      'si for SCISSOR \n')

while chance < no_of_chances:

      comp = random.choice(lis)
      player = input('-------------------\n'
                     'ENTER YOUR CHOICE: \n'
                     '-------------------\n').lower()


      if player == "s":
            print("COMPUTER: ", comp)



            if comp == s:
                  print("STONE vs STONE = MATCH TIED!..\n"
                        "--------------------------------\n")

            elif comp == p:
                  print("Your STONE was raped under the the Computer's PAPER..  \n"
                        "------------------------------------------------------\n"
                        "YOU LOSE!..\n"
                        "------------\n")
                  c = c + 1
                  print(f"Computer point = {c} & Your points = {pl} \n"
                        f"-------------------------------------------\n")

            elif comp == si:
                  print("Your STONE brakes the COMPUTEr's SCISSOR... \n"
                        "--------------------------------------------\n"
                        'YOU WON!!...\n'
                        '------------\n')
                  pl = pl + 1
                  print(f"Computer point = {c} & Your points = {pl} \n"
                        f"------------------------------------------\n")




      elif player == "p":
            print("COMPUTER: ", comp)


            if comp == s:
                  print("The STONE caught in Your PAPER..\n"
                        "--------------------------------\n"
                        "You win!.. \n"
                        "-----------\n")
                  pl = pl + 1
                  print(f"Computer point = {c} & Your points = {pl} \n"
                        f"------------------------------------------\n")

            elif comp == p:
                  print("Both of your PAPERS where transformed into a plane and flown away...\n"
                        "---------------------------------------------------------------------\n"
                        "So... no one WON!\n"
                        "-----------------\n"
                        "MATCH TIED... \n"
                        "--------------\n")

            elif comp == si:
                  print("Ooh!.....\n"
                        "---------\n"
                        "COMPUTER divide Your PAPER in half with the help of his SCISSOR. \n"
                        "-----------------------------------------------------------------\n"
                        "Sorry!.. You Lose...\n"
                        "--------------------\n")
                  c = c + 1
                  print(f"Computer point = {c} & Your points = {pl} \n"
                        f"------------------------------------------\n")


      elif player == "si":
            print("COMPUTER: ", comp)


            if comp == s:
                  print("YOU Tried to cut the STONE BUT...\n"
                        "---------------------------------\n"
                        "YOU lose!...\n"
                        "-------------\n")
                  c = c + 1
                  print(f"Computer point = {c} & Your points = {pl} \n"
                        f"------------------------------------------\n")

            elif comp == p:
                  print("YOU made a paper cutout out of COMPUTER's PAPER.\n"
                        "-------------------------------------------------\n"
                        "YOU WON!... \n"
                        "-------------\n")
                  pl = pl + 1
                  print(f"Computer point = {c} & Your points = {pl} \n"
                        f"------------------------------------------\n")


            elif comp == si:
                  print("Both of YOU take your SCISSORS & Battle for very long time BUT.....\n"
                        "-------------------------------------------------------------------\n"
                        "MATCH TIED...\n"
                        "-------------\n")


            else:
                  print("****************\n"
                        "INVALID OPTION..\n"
                        "****************\n")


      else:
            print("****************\n"
                  "INVALID OPTION..\n"
                  "****************\n")

      chance =  chance + 1
      print("**********************************************************************\n "
            f"No of chances {no_of_chances - chance} is left out of {no_of_chances}\n"
            f"*********************************************************************\n")
print("~~~~~~~~~~~~~\n"
      "<<GAME OVER>>\n"
      "~~~~~~~~~~~~~\n")




if pl < c:
      print("----------------------------\n"
            "SORRY!...YOU LOSE THE GAME.\n"
            "----------------------------\n"
            "BETTER LUCK NEXT TIME.\n"
            "------------------------\n")
elif pl == c:
      print("MATCH TIED!\n"
            "TRY AGAIN...")
elif pl > c:
      print("------------------------------------------\n"
            f"CONGO!.........YOU WON! *|*{Name}*|*\n"
            "------------------------------------------\n")
print(f"YOUR POINT = {pl} & COMPUTER POINT = {c}\n"
      f"****************************************")