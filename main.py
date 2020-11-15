try:
    from consolemenu import *
    from consolemenu.items import *
    from consolemenu.format import *
    import subprocess
    from math_res import math_res as mr
    from text_res import text_res as tres
    from net_res import net_res as netres
except:
    print("An error occurred importing application modules")
    print("Possible solutions: try reinstalling the required modules and checking the integrity of the application files (in development)")

current_version=str("ver: dev branch") # onfy for official releases, if you want to add your own apps, use your version

# ---- APPS ----
# ---- APPS ----

# MATH APPs
math_menu = ConsoleMenu("Math apps."+current_version,"by MichaelODeli on https://github.com/MichaelODeli/py_microapps")
math_easy = FunctionItem("Easy operations", mr.math_menu_easy)
math_money = FunctionItem("Money operations", mr.math_menu_money)
math_menu.append_item(math_easy)
math_menu.append_item(math_money)
def math_menu_main_show():
    math_menu.show()

# TEXT APPs
text_menu = ConsoleMenu("Text apps. "+current_version,"by MichaelODeli on https://github.com/MichaelODeli/py_microapps")
text_menu_item = MenuItem("Menu Item")
text_menu_item1 = FunctionItem("Transcriptor", tres.transcript)
text_menu.append_item(text_menu_item1)
def text_menu_show():
    text_menu.show()

# NETWORK APPs

# Consolemenu and matplotlib has threading problem. Untill i will fix it, launch graphping using this method
def netpinglauncher():
    subprocess.Popen(r'cmd.exe /c start python.exe net_res/graphping_launcher.py')
network_menu = ConsoleMenu("Network apps. "+current_version,"by MichaelODeli on https://github.com/MichaelODeli/py_microapps")
network_menu_item = MenuItem("Menu Item")
network_menu_item1 = FunctionItem("FTP Monitor (need fix from github.com/MichaelODeli/py_ftp-manager)", netres.ftpmonitor)
network_menu_item2 = FunctionItem("Graph Ping", netpinglauncher)
network_menu.append_item(network_menu_item1)
network_menu.append_item(network_menu_item2)
def network_menu_show():
    network_menu.show()



# ---- MAIN MENU ----
# ---- MAIN MENU ----
main_menu = ConsoleMenu("MicroApps. "+current_version,"by MichaelODeli on https://github.com/MichaelODeli/py_microapps")
main_menu_item = MenuItem("Menu Item")
main_item_tomath = FunctionItem("Math", math_menu_main_show)
main_item_totext = FunctionItem("Text", text_menu_show)
main_item_tonet = FunctionItem("Network", network_menu_show)
main_menu.append_item(main_item_tomath)
main_menu.append_item(main_item_totext)
main_menu.append_item(main_item_tonet)
def main_menu_show():
    main_menu.show()

main_menu_show()