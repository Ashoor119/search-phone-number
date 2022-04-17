import phonenumbers
from phonenumbers import geocoder, carrier
import time
import sys   

def ashoor(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 1000)
ashoor('_____________________________________________________')
ashoor(" Welcome to tool ashoor_information to location number SIM ")
ashoor('To help you use the tool to follow the instructions' )
ashoor('[1] phone or run -> To run the tool')
ashoor('[2] help or h    -> The instructions show tools')
ashoor('[3] exit or x    -> To exit the tool')
# Parsing String to Phone number
def help ():
   print ("Key states > +967")
   print ("phone number > 77xxxxxxx")

#cmd =  input("ashoor > ")
while True:
 cmd =  input("ashoor > ")
 def ashor(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(5. / 1000)
 
 if(cmd == "h") or (cmd == "help"):
  help()
   
 elif(cmd =="exit") or (cmd == "x"):
  break
  
 elif(cmd =="phone") or (cmd =="run") :
  ashoor = input(" key states > ")
  ashoor1 = input("phone number > ")
  ashoor119 = str(ashoor + ashoor1)
  phoneNumber = phonenumbers.parse(ashoor119)
  Carrier = carrier.name_for_number(phoneNumber, 'en')
  Region = geocoder.description_for_number(phoneNumber, 'en')
  
  ashor("<•••_____________Information SIM______________•••>")
  
  print("      1- Telephone number : " + str(ashoor119))

  print("      2- Card Information Phone : " + Carrier)

  print("      3- Name of the state : " + Region)

