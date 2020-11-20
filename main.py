try:
    from consolemenu import *
    from consolemenu.items import *
    from consolemenu.format import *
    import subprocess
    from math_res import math_res as mr
    from text_res import text_res as tres
    from net_res import net_res as netres
    import hashlib
    import configparser
    import platform
except:
    print("An error occurred importing application modules")
    print("Possible solutions: try reinstalling the required modules and checking the integrity of the application files (in development)")
    exit(0)
thisos=platform.system()
# file checking
print("Please wait, checking MD5...")
config = configparser.ConfigParser()
config.read('hashes.ini')
main=config.get("hashes_store", "main")
text_res=config.get("hashes_store", "text_res")
math_res=config.get("hashes_store", "math_res")
net_res=config.get("hashes_store", "net_res")
graph=config.get("hashes_store", "graphping_launcher")
fix=config.get("hashes_store", "fix")
current_hash1=hashlib.md5(open('main.py','rb').read()).hexdigest()
current_hash2=hashlib.md5(open('text_res/text_res.py','rb').read()).hexdigest()
current_hash3=hashlib.md5(open('math_res/math_res.py','rb').read()).hexdigest()
current_hash4=hashlib.md5(open('net_res/net_res.py','rb').read()).hexdigest()
current_hash5=hashlib.md5(open('net_res/graphping_launcher.py','rb').read()).hexdigest()
current_hash6=hashlib.md5(open('fix/__init__.py','rb').read()).hexdigest()
if current_hash1!=main:
    print("main.py has non-valid md5. Reinstall app.")
    exit(0)
elif current_hash2!=text_res:
    print("text_res/text_res.py has non-valid md5. Reinstall app.")
    exit(0)
elif current_hash3!=math_res:
    print("math_res/math_res.py has non-valid md5. Reinstall app.")
    exit(0)
elif current_hash4!=net_res:
    print("net_res/net_res.py has non-valid md5. Reinstall app.")
    exit(0)
elif current_hash5!=graph:
    print("net_res/graphping_launcher.py has non-valid md5. Reinstall app.")
    exit(0)
elif current_hash6!=fix:
    print("fix/__init__.py has non-valid md5. Reinstall app.")
    exit(0)
else:
    current_version=str("ver: dev branch") # onfy for official releases, if you want to add your own apps, use your version
    # ---- APPS ----
    # ---- APPS ----

    # MATH APPs
    math_menu = ConsoleMenu("Math apps."+current_version,"by MichaelODeli on https://github.com/MichaelODeli/py_microapps")
    math_easy = FunctionItem("Easy operations", mr.math_menu_easy)
    math_money = FunctionItem("Money operations", mr.math_menu_money)
    math_subj = FunctionItem("Subject calculators", mr.math_menu_subj) # phys, IT, build
    math_unit = FunctionItem("Unit conversion", mr.math_menu_unit)
    math_menu.append_item(math_easy)
    math_menu.append_item(math_money)
    math_menu.append_item(math_subj)
    math_menu.append_item(math_unit)
    def math_menu_main_show():
        math_menu.show()

    # TEXT APPs
    text_menu = ConsoleMenu("Text apps. "+current_version,"by MichaelODeli on https://github.com/MichaelODeli/py_microapps")
    text_menu_item = MenuItem("Menu Item")
    text_transcriptor = FunctionItem("Transcriptor", tres.transcript)
    text_counter = FunctionItem("Words and symbols calculator", tres.dev)
    text_menu.append_item(text_transcriptor)
    text_menu.append_item(text_counter)
    def text_menu_show():
        text_menu.show()

    # NETWORK APPs
    def netpinglauncher():
        if thisos=='Windows':
            subprocess.Popen(r'cmd.exe /c start python.exe net_res/graphping_launcher.py')
        if thisos=='Linux':
            netres.graph_ping()
    def ftpmonlauncher():
        if thisos=='Windows':
            subprocess.Popen(r'cmd.exe /c start python.exe net_res/ftpmon_launcher.py')
        if thisos=='Linux':
            # subprocess.Popen(r'python3 net_res/ftpmon_launcher.py') - NOT SUPPORTED
            print("Linux OS does not suuport this application. Press Enter to back in menu")
            input()
    network_menu = ConsoleMenu("Network apps. "+current_version,"by MichaelODeli on https://github.com/MichaelODeli/py_microapps")
    network_menu_item = MenuItem("Menu Item")
    network_ftpmon = FunctionItem("FTP Monitor (fix it from 'fix' folder)", ftpmonlauncher)
    network_graphping = FunctionItem("Graph Ping", netpinglauncher)
    network_calc = FunctionItem("You can use IT calculator in Math APPs", netres.dev)
    network_menu.append_item(network_ftpmon)
    network_menu.append_item(network_graphping)
    network_menu.append_item(network_calc)
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
    main_menu.show()