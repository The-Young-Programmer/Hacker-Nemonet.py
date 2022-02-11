"""
 Python 3.7
 I'm a Curious beginner  in python,
 This is basically a Hacking simulator
 
 Created by Nemonet aka The Young Programmer.
 Your feedbacks are appreciated
 Give me a star if you like this project
"""

# Import
import time
import random
from time import sleep as time_per_word
import sys

# Welcome logo

print("                                             ")
print(" _   _                                 _     ")
print("| \ | | ___ _ __ ___   ___  _ __   ___| |_   ")
print("|  \| |/ _ \ '_ ` _ \ / _ \| '_ \ / _ \ __|  ")
print("| |\  |  __/ | | | | | (_) | | | |  __/ |_   ")
print("|_| \_|\___|_| |_| |_|\___/|_| |_|\___|\__|  ")
print("                                             ")
                                                              "

print("Hacker  TYP-tool".upper().center(50))
time.sleep(0.3)
print(">>>Nemonet\n".center(63))
time.sleep(1)

# Description
time_per_word(0.03)
desc = ("//Description: This programme is used to\nsimulate brute-force/dictionary attack.\n")
des_c = ("It doesn't really work. No need to enter\nyour own username or password,No problem\nif gave,I'm not collecting anything,©2022")
full_desc = desc + des_c
for info in list(full_desc):
    print(info, end="",flush=True)
    time_per_word(0.03)

# Login/signup info
time.sleep(2)
print("\n\n>>> create/log-in account <<<".upper())
time.sleep(0.6)
print("[*] login to free Hacker asf account")
time.sleep(0.6)
print("[*] no email or phone number needed\n")
time.sleep(0.6)

# Username input and availability
username=input("[-] username:")
time.sleep(1)
print ("[*] username:available")
time.sleep(0.6)
print ("[+] username:saved as",username)
time.sleep(0.6)

# Usercode generation
user_random = random.randint(1,1000)
user_code = sys.getsizeof(username) * user_random
print ("[*] usercode:hasfcd"+str(user_code))
time.sleep(0.6)

# Password input
password=input("\n[-] password:")
time.sleep(2)
print("[+] password:saved as",password)
time.sleep(0.6)

# Password length and strength
leng =(len(password))
print("[*] Length  :",leng)
time.sleep(0.6)
if leng < 8 :
  print ("[*] Password:not strong")
elif leng >= 12:
  print("[*] Password:very strong")
else :
  print ("[*] Strength:strong")
time.sleep(0.6)
print ("[*] saved succesful")

# Welcome to Hacker  TYP server
time.sleep(1)
print("\n// welcome".upper())
time.sleep(0.6)
TYP_ping = random.randint(70,999)
print ("[$] Hacker  TYP")
time.sleep(0.6)
print ("[$] Server ping:"+str(TYP_ping)+"+")
time.sleep(1)
# Server ping speed
if TYP_ping < 100 :
  print("[+] server speed:very fast")
elif TYP_ping < 200 :
  print("[+] server speed:fast")
elif TYP_ping < 300 :
  print("[+] server speed:bit slow")
elif TYP_ping < 400 :
  print("[+] server speed:average")
elif TYP_ping < 500 :
  print("[+] server speed:below average")
elif TYP_ping < 600 :
  print("[+] server speed:slow")
elif TYP_ping < 700 :
  print("[+] server speed:very slow")
elif TYP_ping < 800 :
  print("[+] server almost unreachable")
else :
  print("[+] server details not found!")

# A short time delay when ping is high or low
if TYP_ping < 300 :
  time.sleep(2)
elif TYP_ping > 300 :
  time.sleep(4)
else :
  time.sleep(3)

# Choosing a proxy server
print("[+] connecting to proxy server...")
time.sleep(3)
random_proxy = random.randint(0,15)
if random_proxy == 0 :
  print("[$] Proxy:Thunder VPN")
elif random_proxy == 1 :
  print("[$] Proxy:Blazing SEO")
elif random_proxy == 2 :
  print("[$] Proxy:VPN Tomato")
elif random_proxy == 3 :
  print("[$] Proxy:Smart proxy")
elif random_proxy == 4 :
  print("[$] Proxy:Solo VPN")
elif random_proxy == 5 :
  print("[$] Proxy:GeoSurf VPN")
elif random_proxy == 6 :
  print("[$] Proxy:Proton VPN")
elif random_proxy == 7 :
  print("[$] Proxy:Tunnel bear")
elif random_proxy == 8 :
  print("[$] Proxy: Secure VPN")
elif random_proxy == 9 :
  print("[$] Proxy:Turbo VPN")
elif random_proxy == 10 :
  print("[$] Proxy:SurFree VPN")
elif random_proxy == 11 :
  print("[$] Proxy:NetCapsule")
elif random_proxy == 12 :
  print("[$] Proxy:CyberGhost")
elif random_proxy == 13 :
  print("[$] Proxy:Nord VPN")
elif random_proxy == 14 :
  print("[$] Proxy:VPN 365")
else :
  print("[$] Proxy:none")
time.sleep(0.6)

# #Asking other details about social media
print("\n[+] Select options\n >(Type number)")
time.sleep(0.3)
print("[1] Instagram\n[2] Facebook\n[3] Twitter\n[4] Tiktok\n")
smedia = int(input("[-] "))
instagram = "Instagram"
facebook = "Facebook"
twitter = "Twitter"
tiktok = "Tiktok"
public = "Public"
if smedia == 1:
  social_media = instagram
elif smedia == 2:
  social_media = facebook
elif smedia == 3:
  social_media = twitter
elif smedia == 4:
  social_media = tiktok
else :
  social_media = public
time.sleep(0.5)
print("[*] type:social media")
time.sleep(0.3) 
print("[*] loading details...")
time.sleep(2)
print("[*] loading resources...")
time.sleep(2)
print("[*] connecting to",social_media,"server...")
time.sleep(0.5)
print("[*] waiting for server response...")
time.sleep(3)

# Server ping for social media
ser_ping = random.randint(80,999)
print("[$]",social_media,"server ping:"+str(ser_ping)+"+")

# Another time delay when ping is high or low
if ser_ping < 100 :
  time.sleep(1)
elif ser_ping > 100 :
  time.sleep(3)
elif ser_ping > 200 :
  time.sleep(6)
else :
  time.sleep(4)

# Connecting to server in random %
ran1 = random.randint(5,10)
print("[*] connecting...             ",ran1,"%")
time.sleep(0.3)
ran2 = random.randint(15,20)
print("[*] connecting...             ",ran2,"%")
time.sleep(0.3)
ran3 = random.randint(25,30)
print("[*] connecting...             ",ran3,"%")
time.sleep(0.3)
ran4 = random.randint(35,40)
print("[*] connecting...             ",ran4,"%")
time.sleep(0.3)
ran5 = random.randint(45,50)
print("[*] connecting...             ",ran5,"%")
time.sleep(0.3)
ran6 = random.randint(55,60)
print("[*] connecting...             ",ran6,"%")
time.sleep(0.3)
ran7 = random.randint(65,70)
print("[*] connecting...             ",ran7,"%")
time.sleep(0.3)
ran8 = random.randint(75,80)
print("[*] connecting...             ",ran8,"%")
time.sleep(0.3)
ran9 = random.randint(85,90)
print("[*] connecting...             ",ran9,"%")
time.sleep(0.3)
ran10 = random.randint(95,98)
print("[*] connecting...             ",ran10,"%")
time.sleep(0.3)
ran11 = random.randint(100,100)
print("[*] connecting...            ",ran11,"%")
time.sleep(1)
print("[*] cloud syncing...")
time.sleep(1)
print("[*] waiting for API response...")
time.sleep(3)
print("[*] connection successful")
time.sleep(0.6)
print("[*] server status:active")
time.sleep(0.6)
print("[$] recent logs:null\n")
time.sleep(1.2)

# Asking Target details and starting attack
print("//Target details")
time.sleep(0.3)
target_id=input("[-] Target id/username:")
time.sleep(0.2)
print("[*] collecting info. from",target_id.lower())
time.sleep(0.3)
print("[*] saved to kalie/home/Hacker/Nemonet/target/username/"+str(target_id)+".txt")
time.sleep(4)
print("[*] setting python...")
time.sleep(2)
print("[*] setting python2...")
time.sleep(0.4)
print("[*] file name: word-list.txt")
time.sleep(0.4)
print("[*] total file contains:55020 lists")
time.sleep(0.4)
print("[*] path://kali.org/kali/home/Hacker /Nemonet/word-list.txt")
time.sleep(0.7)
print("[*] un-zipping local word-list.txt")
time.sleep(0.5)
print("[*] word-list count:00100/55020")
time.sleep(3)
print("[*] loading word-list.txt")
time.sleep(0.7)
print("[*] please wait...")
time.sleep(1)
print("[*] opening word-list.txt")
time.sleep(1)
print("[*] clearing cache...")
time.sleep(2)
cookies = random.randint(0,1)
if cookies == 0 :
  print("[*] cookies not cleared!")
else :
  print("[*] clearing cookies...")
time.sleep(1)
print("[*] brute-forceing...\n")
time.sleep(3)

# Trying 100 Word-lists
print("*//Note: EACH WORD-LIST CONTAINS 10-100 PASSWORDS\n")
time.sleep(5)
print(">>> trying word-list = 00001")
time.sleep(0.3)
print(">>> trying word-list = 00002")
time.sleep(0.3)
print(">>> trying word-list = 00003")
time.sleep(0.3)
print(">>> trying word-list = 00004")
time.sleep(0.3)
print(">>> trying word-list = 00005")
time.sleep(0.4)
print(">>> trying word-list = 00006")
time.sleep(0.4)
print(">>> trying word-list = 00007")
time.sleep(0.5)
print(">>> trying word-list = 00008")
time.sleep(0.5)
print(">>> trying word-list = 00009")
time.sleep(0.5)
print(">>> trying word-list = 00010")
time.sleep(0.5)
print(">>> trying word-list = 00011")
time.sleep(0.5)
print(">>> trying word-list = 00012")
time.sleep(0.5)
print(">>> trying word-list = 00013")
time.sleep(0.5)
print(">>> trying word-list = 00014")
time.sleep(0.5)
print(">>> trying word-list = 00015")
time.sleep(0.5)
print(">>> trying word-list = 00016")
time.sleep(0.5)
print(">>> trying word-list = 00017")
time.sleep(0.5)
print(">>> trying word-list = 00018")
time.sleep(0.5)
print(">>> trying word-list = 00019")
time.sleep(0.5)
print(">>> trying word-list = 00020")
time.sleep(0.5)
print(">>> trying word-list = 00021")
time.sleep(0.5)
print(">>> trying word-list = 00022")
time.sleep(0.5)
print(">>> trying word-list = 00023")
time.sleep(0.5)
print(">>> trying word-list = 00024")
time.sleep(0.5)
print(">>> trying word-list = 00025")
time.sleep(0.5)
print(">>> trying word-list = 00026")
time.sleep(0.5)
print(">>> trying word-list = 00027")
time.sleep(0.5)
print(">>> trying word-list = 00028")
time.sleep(0.5)
print(">>> trying word-list = 00029")
time.sleep(0.5)
print(">>> trying word-list = 00030")
time.sleep(0.5)
print(">>> trying word-list = 00031")
time.sleep(0.5)
print(">>> trying word-list = 00032")
time.sleep(0.5)
print(">>> trying word-list = 00033")
time.sleep(0.5)
print(">>> trying word-list = 00034")
time.sleep(0.5)
print(">>> trying word-list = 00035")
time.sleep(0.5)
print(">>> trying word-list = 00036")
time.sleep(0.5)
print(">>> trying word-list = 00037")
time.sleep(0.5)
print(">>> trying word-list = 00038")
time.sleep(0.5)
print(">>> trying word-list = 00039")
time.sleep(0.5)
print(">>> trying word-list = 00040")
time.sleep(0.5)
print(">>> trying word-list = 00041")
time.sleep(0.5)
print(">>> trying word-list = 00042")
time.sleep(0.5)
print(">>> trying word-list = 00043")
time.sleep(0.5)
print(">>> trying word-list = 00044")
time.sleep(0.5)
print(">>> trying word-list = 00045")
time.sleep(0.5)
print(">>> trying word-list = 00046")
time.sleep(0.5)
print(">>> trying word-list = 00047")
time.sleep(0.5)
print(">>> trying word-list = 00048")
time.sleep(0.5)
print(">>> trying word-list = 00049")
time.sleep(0.5)
print(">>> trying word-list = 00050")
time.sleep(0.5)
print(">>> trying word-list = 00051")
time.sleep(0.5)
print(">>> trying word-list = 00052")
time.sleep(0.5)
print(">>> trying word-list = 00053")
time.sleep(0.5)
print(">>> trying word-list = 00054")
time.sleep(0.5)
print(">>> trying word-list = 00055")
time.sleep(0.5)
print(">>> trying word-list = 00056")
time.sleep(0.5)
print(">>> trying word-list = 00057")
time.sleep(0.5)
print(">>> trying word-list = 00058")
time.sleep(0.5)
print(">>> trying word-list = 00059")
time.sleep(0.5)
print(">>> trying word-list = 00060")
time.sleep(0.5)
print(">>> trying word-list = 00061")
time.sleep(0.5)
print(">>> trying word-list = 00062")
time.sleep(0.5)
print(">>> trying word-list = 00063")
time.sleep(0.5)
print(">>> trying word-list = 00064")
time.sleep(0.5)
print(">>> trying word-list = 00065")
time.sleep(0.5)
print(">>> trying word-list = 00066")
time.sleep(0.5)
print(">>> trying word-list = 00067")
time.sleep(0.5)
print(">>> trying word-list = 00068")
time.sleep(0.5)
print(">>> trying word-list = 00069")
time.sleep(0.5)
print(">>> trying word-list = 00070")
time.sleep(0.5)
print(">>> trying word-list = 00071")
time.sleep(0.5)
print(">>> trying word-list = 00072")
time.sleep(0.5)
print(">>> trying word-list = 00073")
time.sleep(0.5)
print(">>> trying word-list = 00074")
time.sleep(0.5)
print(">>> trying word-list = 00075")
time.sleep(0.5)
print(">>> trying word-list = 00076")
time.sleep(0.5)
print(">>> trying word-list = 00077")
time.sleep(0.5)
print(">>> trying word-list = 00078")
time.sleep(0.5)
print(">>> trying word-list = 00079")
time.sleep(0.5)
print(">>> trying word-list = 00080")
time.sleep(0.5)
print(">>> trying word-list = 00081")
time.sleep(0.5)
print(">>> trying word-list = 00082")
time.sleep(0.5)
print(">>> trying word-list = 00083")
time.sleep(0.5)
print(">>> trying word-list = 00084")
time.sleep(0.5)
print(">>> trying word-list = 00085")
time.sleep(0.5)
print(">>> trying word-list = 00086")
time.sleep(0.5)
print(">>> trying word-list = 00087")
time.sleep(0.5)
print(">>> trying word-list = 00088")
time.sleep(0.5)
print(">>> trying word-list = 00089")
time.sleep(0.5)
print(">>> trying word-list = 00090")
time.sleep(0.5)
print(">>> trying word-list = 00091")
time.sleep(0.5)
print(">>> trying word-list = 00092")
time.sleep(0.5)
print(">>> trying word-list = 00093")
time.sleep(0.5)
print(">>> trying word-list = 00094")
time.sleep(0.5)
print(">>> trying word-list = 00095")
time.sleep(0.5)
print(">>> trying word-list = 00096")
time.sleep(0.5)
print(">>> trying word-list = 00097")
time.sleep(0.5)
print(">>> trying word-list = 00098")
time.sleep(0.5)
print(">>> trying word-list = 00099")
time.sleep(0.5)
print(">>> trying word-list = 00100\n")
time.sleep(2)

# Decoding process with a loading
print ("[*] password info:found!")
time.sleep(0.6)
print ("[*] salting analysis...")
time.sleep(3)
print ("[*] salting:not found!")
time.sleep(2)
print ("[*] fetching info...")
time.sleep(1)
print ("[*] process:Decrypting...")
time.sleep(3)
m = ("[+]")
rd1 = random.randint(0,3)
print (m,rd1,"%  "," █")
time.sleep(1)
rd2 = random.randint(5,9)
print (m,rd2,"%  "," ██")
time.sleep(0.4)
rd3 = random.randint(15,20)
print (m,rd3,"% "," ███")
time.sleep(0.6)
rd4 = random.randint(25,30)
print (m,rd4,"% "," ████")
time.sleep(0.8)
rd5 = random.randint(35,40)
print (m,rd5,"% "," █████")
time.sleep(0.3)
rd6 = random.randint(45,50)
print (m,rd6,"% "," ██████")
time.sleep(0.5)
rd7 = random.randint(55,60)
print (m,rd7,"% "," ███████")
time.sleep(0.3)
rd8 = random.randint(65,70)
print (m,rd8,"% "," ████████")
time.sleep(0.6)
rd9 = random.randint(75,80)
print (m,rd9,"% "," █████████")
time.sleep(0.8)
rd10 = random.randint(85,90)
print (m,rd10,"% "," ██████████")
time.sleep(0.4)
rd11 = random.randint(95,99)
print (m,rd11,"% "," ███████████")
time.sleep(2)
rd12 = random.randint(100,100)
print (m,rd12,"% ","████████████")
time.sleep(1)
print("[*] please wait...\n")
time.sleep(3)
print("[*] collecting keys...")
time.sleep(1)
print("[*] finding key match...")
time.sleep(3)
print("[+] key match found!\n")
time.sleep(2)

# Result + Showing username
print("[$] report".upper())
time.sleep(2)
work_rate = random.randint(20,100)
print("[$] task work rate:"+str(work_rate))
time.sleep(1)
print("[$] username:",target_id)
time.sleep(1)

# Password generation and showing
numbers = "0123456789"
letters = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
mix_num_let = numbers + letters
password_length = random.randint(8,16)
password_generated = "".join(random.sample(mix_num_let,password_length))
print("[$] password:",password_generated)

#Final info and Thanks
time.sleep(1)
print("\n\n[*] Thanks for using my nemonet-tool")
time.sleep(0.5)
print("[*] Follow me on github: @The Young Programmer Nemonet")
time.sleep(0.2)
print("[*] Give me a star\U0001F600")
time.sleep(0.2)
print("         THANK YOU ")
