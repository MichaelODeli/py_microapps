# this is main.py file, special edited for creating new modules and apps


#IMPORTING requied MODULES AND MD5 FILE CHECKERS
try:
    from consolemenu import *
    from consolemenu.items import *
    from consolemenu.format import *
    import subprocess
    import hashlib
    import configparser
    import platform
    # Here you can add your own module with its subfolder in root directory
    #Sample: 
    from mymodule_res import sample as smpl
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
# here you write your own module to check
text_res=config.get("hashes_store", "mymodule_res")
current_hash1=hashlib.md5(open('main.py','rb').read()).hexdigest()
current_hash2=hashlib.md5(open('mymodule_res/sample.py','rb').read()).hexdigest()
if current_hash1!=main:
    print("main.py has non-valid md5. Reinstall app.")
    exit(0)
elif current_hash2!=text_res:
    print("mymodule_res/sample.py has non-valid md5. Reinstall app.")
    exit(0)
else:
    current_version=str("ver: for developers) # onfy for official releases, if you want to add your own apps, use your version
    # ---- Creating APPS ----
    # ---- Creating APPS ----
    # Sample APPs
    sample_menu = ConsoleMenu("Sample apps."+current_version,"by MichaelODeli on https://github.com/MichaelODeli/py_microapps")
    sample_easy = FunctionItem("Open for test", smpl.test)
    sample_menu.append_item(sample_easy)
    def sample_menu_main_show():
        sample_menu.show()
    # ---- MAIN MENU ----
    # ---- MAIN MENU ----
    main_menu = ConsoleMenu("MicroApps. "+current_version,"by MichaelODeli on https://github.com/MichaelODeli/py_microapps")
    main_menu_item = MenuItem("Menu Item")
    main_item_tomath = FunctionItem("Sample", sample_menu_main_show)
    main_menu.append_item(main_item_tomath)
    main_menu.show()