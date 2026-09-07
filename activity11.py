#import demo
import getpass

username = "davez-bot"
password = "Pogisi_davez123"

u = input("input USERNAME --->")
p = getpass.getpass("input PASSWORD --->")

if u == username and p == password:
	print("username amd password correct")
else:
	print("access denied")