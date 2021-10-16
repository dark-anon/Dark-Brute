#==================================================================================
# DarkBrute v1.0 ---- PDF CRACKER --------                                          
# Author: D4rK~4n0N
# Github: https://github.com/dark-anon/
# Telegram: https://t.me/DarkAn0n
#
# Written in python 3
# NOTE: IF you copy and paste my codes, give me the credits
#==================================================================================



#import necessary modules 

import pikepdf
import sys
import os
from datetime import datetime 

#colors to be used in the program

R = "\033[91m"
G = "\033[92m"
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
b = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'

# ------------ BANNER ----------------

def banner():
    os.system('clear')
    Ban =(
            G+'''
                 ________                __           __________                __
                \______ \ _____ _______|  | __       \______   \_______ _____ /  |_  ____  
                |    |   \\\__ \\\_ __  \   |/ / ______ |    |  _/\_  __ \  |  \   __\/ __ \ 
                |    `   \/ __ \|  | \/   <   /_____/ |    |   \ |  | \/  |  /|  | \  ___/ 
                /_______  (____ |__|   |__|_ \        |______  / |__|  |____/ |__|  \___  >
                        \/     \/           \/               \/                         \/ 
                                                                                         '''+b+'''V1.0
                                                                        
                                        '''+u+'------ Created by D4rk~4n0n -----\n')
                                                                                                            





                                                                                                     
    print(Ban)
    print(G+'╔════════════════════\n'+b+'║'+h+'〘 '+m+'OPTION '+h+'〙\n'+b+'╠════════════════════'+b+'\n║'+m+'『'+h+'0'+m+'』'+bm+' Exit\n'+b+'╠════════════════════'+b+'\n║'+m+'『'+h+'1'+m+'』 '+bm+'Crack PDF\n'+b+'║'+m+'『'+h+'2'+m+'』 '+bm+'Author\n')
    


    option = str(input(b+'╚══'+m+'〙'+u+'Select an option'+m+' ▶ '+h))

    if option == str(0):
        sys.exit()

    elif option == str(1):
        cracker()
    elif option == '':
        print(R+'\nDO not leave blank!!!\n'+G)

    elif option == str(2):
        print(G+'\n══>'+u+'Author: '+G+'Dark~anon')
        print(G+'\n══>'+u+'Github: '+G+'https://github.com/dark-anon\n')



def cracker():

    check = str(input(G+'\n╚══'+m+'〙'+u+'Enter file location'+m+' ▶ '+h))

    file = open("Dark-Brute/wordlist.txt").readlines()

    


    for password in file:
        try:


            with pikepdf.open(check ,password.strip()) as pdf:

                print(G+"=======> [+] password found: "+b+"{}\n".format(password))
                
                
                       
            break
               
            

                



                
                
        except PermissionError:


            print(R+'\nError!!! The file you provided does not exist or is not a pdf file\n')

            break

        except KeyboardInterrupt:

            print(R+'\nYou pressed Ctrl+C\n')


        except:

            print(R+"[~] trying password: {}\n".format(password))

            continue

            
    
if __name__ == '__main__':
        banner()    
