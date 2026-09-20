import pyfiglet as fig # 100% organic free range human made code
import os
import time
import random
while True:
    user = input("type start to begin> ") # user is the first used input this controls the power on/off and first help menu
    if user == "-h":
        print("this is the help menu type in start to run")
    elif user == "powerdown":
        exit()
    elif user == "hello":
        print(fig.figlet_format("HI", font="dos_rebel"))
    elif user == "-i":
        print("info menu made by INABOT#8377 all code made by INABOT#8377")
    if user == "start":
        print(fig.figlet_format("HELLO", font="dos_rebel"))
        while True:
                usrinput = input("please write the name of your application> ") # usrinput controls the booting up of programs, this is the main part of the script
                if usrinput == "powerdown":
                    break
                if usrinput == "clear":
                    os.system("cls") # cls is windows only, linux version maybe
                    continue
                elif usrinput == "steam":
                    steampath = input("write in you path to steam")
                    if os.path.exists(steampath): # os startfile is windows only, linux version maybe
                        os.startfile(steampath)
                        print("steam starting")
                        continue
                    else:
                        print("FILEPATH ERROR")
                        continue
                while True: # main loop for all of the programs
                    if usrinput == "calculator":
                        try:
                            calc = float(input("type in your numbers> "))
                            opp = input("+, -, *, /, %,") # literally just exits the calculator if you type a operator in wrong- 
                            #couldnt be bothered to make an error message while im still adding things
                            calc2 = float(input("now write your second number> "))
                            if opp == "+":
                                print(calc + calc2)
                            elif opp == "-":
                                print(calc - calc2)
                            elif opp == "*":
                                print(calc * calc2)
                            elif opp == "/":
                                print(calc / calc2)
                            elif opp == "%":
                                print(calc % calc2)
                            usr = input('type "end" to exit or enter to write again ')
                            if usr == "end":
                                break
                        except ZeroDivisionError:
                            print(fig.figlet_format("BRO TRIED TO DIVIDE BY ZERO", font="small"))
                            break
                        except ValueError:
                            print(fig.figlet_format("ERROR INPUT A NUMBER ", font="small"))
                            break
                    elif usrinput == "coinflip":
                        coin = random.randint(1, 2)
                        print(fig.figlet_format("heads or tails", font="dos_rebel"))
                        guess = input()
                        if coin == 1:
                            print(fig.figlet_format("IT WAS HEADS", font="mini"))
                        else:
                            print(fig.figlet_format("IT WAS TAILS", font="mini"))
                        if guess == "heads" and coin == 1:
                            print(fig.figlet_format("YAY", font="mini"))
                        elif guess == "tails" and coin == 2:
                            print(fig.figlet_format("YAY", font="mini"))
                        else: print(fig.figlet_format("BOO", font="mini"))
                        usrcoin = input("press enter to play again or type end to go back> ")
                        if usrcoin == "end":
                            print(fig.figlet_format("Restart", font="dos_rebel")) # dev note, this is outdated but still works
                            break
                    if usrinput == "file maker":
                        select_mode = input("plese sellect a mode> ")
                        if select_mode == "write new":
                            usr_write_name = input("please write your file name> ")
                            usrwrite = input("now write the contents of this file")
                            with open(usr_write_name, "w") as file:
                                file.write(usrwrite)
                        elif select_mode == "read":
                            try:
                                nameing = input("please type in the name of the file you wish to read> ")
                                with open(nameing, "r") as file:
                                    contents = file.read()
                                    print(fig.figlet_format("LOADING", font="mini"))
                                    time.sleep(1)
                                    print(fig.figlet_format("DONE", font="mini"))
                                    time.sleep(0.2)
                                    print(contents)
                            except FileNotFoundError:
                                print("ERROR")
                                time.sleep(1)
                                os.system("cls")
                                time.sleep(1)
                                break
                            else:
                                print(fig.figlet_format("DONE", font="dos_re"))
                            usrend = input("type end to stop or enter to write again> ")
                            if usrend == "end":
                                break
                        else:
                            break
                    else:
                        print(fig.figlet_format("ERROR INPUT A NAME ", font="small"))
                        break # error fixed from the clear command with continue at the end
                    # new code goes here, dont forget to add a break at the end and the program will automatically restart so core while Trues do nothing