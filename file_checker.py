import subprocess
import hashlib
import configparser
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
    subprocess.Popen(r'cmd.exe /c start python.exe main.py')
    print("All files are valid. Have a nice day :)")