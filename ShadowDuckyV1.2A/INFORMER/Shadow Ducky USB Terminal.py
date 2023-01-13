# Shadow Ducky USB Terminal
# This will be the terminal to activate and run the programs on the shadow ducky USB
# password(key) activated

print("You must sign in to use ShadowDucky\n")

def get_key():
  key = -1
  correct = 7331
  while key != correct:
    key = input("please enter key: \n")
    try:
      if int(key) != correct:
        raise
      else:
        key = int(key)
    except:
      print("Access Denied Inavlid Key")
      
get_key()
print("Access Granted..Welcome")

print(" \n" +
"|//+----------------------------------Shadows-Bag-Of-Holding----------------------------------------------+\n" +
"|//|======================================================================================================|\n" +
"|//|       ___         ___           ___           ___           ___            ___                   |//|\n" +
"|//|      /\  \       /\__\         /\  \         /\  \         /\  \          /\__\                  |//|\n" +
"|//|     /::\  \     /:/  /        /::\  \       /::\  \       /::\  \        /:/ _/_                 |//|\n" +
"|//|  _\:\~\ \  \   /::\  \ ___   /::\~\:\  \   /:/  \:\__\   /:/  \:\  \    /:/ /:/ _/_               |//|\n" +
"|//| /\ \:\ \ \__\ /:/\:\  /\__\ /:/\:\ \:\__\ /:/__/ \:|__| /:/__/ \:\__\  /:/_/:/ /\__\              |//|\n" +
"|//| \:\ \:\ \/__/ \/__\:\/:/  / \/__\:\/:/  / \:\  \ /:/  / \:\  \ /:/  /  \:\/:/ /:/  /              |//|\n" +
"|//|  \:\ \:\__\        \::/  /       \::/  /   \:\  /:/  /   \:\  /:/  /    \::/_/:/  /               |//|\n" +
"|//|   \:\/:/  /        /:/  /        /:/  /     \:\/:/  /     \:\/:/  /      \:\/:/  /                |//|\n" +
"|//|    \::/  /        /:/  /        /:/  /       \::/__/       \::/  /        \::/  /                 |//|\n" +
"|//|     \/__/         \/__/         \/__/         ~~            \/__/          \/__/                  |//|\n" +
"|//|           ___           ___           ___           ___             ___                           |//|\n" +
"|//|          /\  \         /\__\         /\  \         /\__\           |\__\                          |//|\n" +
"|//|         /::\  \       /:/  /        /::\  \       /:/  /           |:|  |                         |//|\n" +
"|//|        /:/\:\  \     /:/  /        /:/\:\  \     /:/__/            |:|  |                         |//|\n" +
"|//|       /:/  \:\__\   /:/  /  ___   /:/  \:\  \   /::\__\____        |:|__|__                       |//|\n" +
"|//|      /:/__/ \:|__| /:/__/  /\__\ /:/__/ \:\__\ /:/\:::::\__\      /::::\__\                       |//|\n" +
"|//|      \:\  \ /:/  / \:\  \ /:/  / \:\  \  \/__/ \/_|:|~~|~        /:/~~/~                          |//|\n" +
"|//|       \:\  /:/  /   \:\  /:/  /   \:\  \          |:|  |        /:/  /                __          |//|\n" +
"|//|        \:\/:/  /     \:\/:/  /     \:\  \         |:|  |       /:/  /             ___( o)>        |//|\n" +
"|//|         \::/__/       \::/  /       \:\__\        |:|  |      /:/  /              \ <_. )         |//|\n" +
"|//|          ~~            \/__/         \/__/         \|__|      \/__/                `---'          |//|\n" +
"|//|                                                                                                   |//|\n" +
"|//|                                                                                                   |//|\n" +
"|//|                                                                                                   |//|\n" +
"|//|                                                                                                   |//|\n" +
"|//|                                                                                                   |//|\n" + 
"|//|                                                                                                   |//|\n" +
"|//|                                                                                                   |//|\n" +
"|//|                                                                                                   |//|\n" +
"|//|                                                                                                   |//|\n" +
"|//|======================================================================================================|\n" +
"|//+------------------------------------------------------------------------------------------------------+\n" +
"\n" + "Welcome to ShadowDucky\n") 
 
menu = "-I" , "-S"
print("please choose from one of our option\n" + "1. -I : will start the informer\n" + "2. -S : will start and run Shadow Ducky,\n" + "after using this option please restart the computer\n" + "befor unplugging the ShadowDucky USB\n")

import os # imports always go at the top
routines = {
  "-I": "Informer",
  "-S": "ShadowDucky"
}
def exec_routine(inpt):
  if inpt in routines.keys():
    os.system("D:\\"+f"{routines[inpt]}.lnk")
    print(f"{routines[inpt]} has finished")

def get_input():
  command = ""
  while command not in routines.keys():
    command = input("Please enter command:\n> ")
    try:
      if command not in routines.keys():
        raise
      else:
        return command
    except:
      print("Invalid Command")

exec_routine(get_input())
print("Thank you for using ShadowDucky")


wait = input()





















