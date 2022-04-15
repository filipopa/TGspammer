
import os, sys
from telethon.sync import TelegramClient
def requirements():
    os.system("""
			pip3 install cython numpy pandas
			python3 -m pip install cython numpy pandas
			""")
    print("[+] Installing requierments ...")
    os.system("""
		pip3 install telethon 
		python3 -m pip install telethon
		pip3 install puqt5
		python3 -m pip install pyqt5
		""")
    print("[+] requierments Installed.\n")


def config_setup():
    xid = input("[+] enter api ID : ")
    xhash = input("[+] enter hash ID : ")
    xphone = input("[+] enter phone number : ")
    setup = open(sys.path[0].replace('\\','/')+'/config.txt', 'w')
    setup.write(f'{xid} {xhash} {xphone}')
    setup.close()
    with TelegramClient(xphone, xid, xhash) as client:
        client.send_message('me','test')


    print("[+] setup complete !")
def main():
    requirements()
    config_setup()
    wait=input()
if __name__=='__main__':
    main()