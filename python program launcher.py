import pyfiglet as fig # 100% organic free range human made code
import os
import time
import random
while True:
    print("-h for help")
    user = input("type start to begin> ") # user is the first used input, this controls the power on/off and first help menu
    if user == "-h":
        print("this is the help menu type in start to run or powerdown to exit")
    elif user == "powerdown":
        exit()
    elif user == "hello":
        print(fig.figlet_format("HI", font="dos_rebel"))
    elif user == "-i":
        print("info menu made by INABOT#8377 all code made by INABOT#8377")
    if user == "start":
        print(fig.figlet_format("HELLO", font="dos_rebel"))
        time.sleep(0.5)
        print("write -h for help")
        print(fig.figlet_format("LOADING", font="small"))
        time.sleep(2)
        while True:
                usrinput = input("please write the name of your application or a menu> ") # usrinput controls the booting up of programs, this is the main part of the script
                if usrinput == "powerdown":
                    break
                if usrinput == "clear":
                    os.system("cls") # cls is windows only, linux version maybe
                    continue
                elif usrinput == "ip":
                    os.system("ipconfig")
                    continue
                elif usrinput == "steam":
                    steampath = input("write in you path to steam> ")
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
                    elif usrinput == "file maker":
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
                                    time.sleep(4)
                                    continue
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
                    elif usrinput == "free":
                        usrfree = input("write anything here or type end to stop> ")
                        if usrfree == "end":
                            break
                    elif usrinput== "-h":
                        print('type in "file maker" for a notepad, "coinflip" for a game, "steam" to open steam or "calculator" to open a calculator')
                        print('or "powerdown" to close, IMPORTANT, "end" is allwase the code to end a program')
                        time.sleep(6)
                        break
                    else:
                        print(fig.figlet_format("ERROR INPUT A NAME ", font="small"))
                        break

                    # error fixed from the clear command with continue at the end
                    # new code goes here, dont forget to add a break at the end and the program will automatically restart so core while Trues do nothing
