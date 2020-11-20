import hashlib
import configparser
# generate MD5
main=hashlib.md5(open('main.py','rb').read()).hexdigest()
mymodule_res=hashlib.md5(open('mymodule_res/sample.py','rb').read()).hexdigest()
# WRITE MD5 TO CONFIG FILE
config = configparser.ConfigParser()
config.read('hashes.ini')
config.set("hashes_store", "main", main)
config.set("hashes_store", "mymodule_res", mymodule_res)
with open("hashes.ini", "w") as config_file:
    config.write(config_file)
print("Success!")