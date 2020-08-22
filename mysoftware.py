import os
import time
print()
print()

print("\t\t\t\t\t\tWELCOME to this program!!")
print()
print()


while True:
    print("HELLO!! how can I help you : \t"  , end='')
    
    p = input()
    
    if (("run" in p) or ("open" in p) or ("launch" in p))  and ("chrome" in p): 
        print()
        print("yaa sure!!")
        print()  
        time.sleep(1)
        os.system("\tchrome")
    elif (("run" in p) or  ("open" in p ) or ("launch" in p)) and  (("notepad" in p) or ("editor" in p) ):
        print()
        print("yaa sure!!")
        print() 
        time.sleep(1)
        os.system("notepad")
    elif (("run" in p) or ("open" in p))  and ("player" in p) and ("media" in p):
        print()
        print("yaa sure!!") 
        print()
        time.sleep(1)
        os.system("wmplayer")
    elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("mspowerpoint" in p) or ("powerpoint" in p)):
        print()
        print("yaa sure!!") 
        print()        
        time.sleep(1)
        os.system("powerpnt")
    elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("msword" in p) or ("word" in p)):
        print()
        print("yaa sure!!")
        print() 
        time.sleep(1)
        os.system("winword")
    elif (("run" in p) or ("open" in p) or ("launch" in p)) and (("msexcel" in p) or ("excel" in p)): 
        print()
        print("yaa sure!!") 
        print()
        time.sleep(1)
        os.system("excel!!")
    elif ("go" in p) and ("site" in p) and ("gaana" in p):
        print()
        print("yaa sure!!") 
        print()
        time.sleep(1)
        os.system("Start chrome www.gaana.com")
    elif (("launch" in p) or ("open" in p)) and ("whatsapp" in p):
        print()
        print("yaa sure!!") 
        print()
        time.sleep(1)
        os.system("Start chrome https://web.whatsapp.com/")
    elif ("open" in p)  and ("slack" in p):
        print()
        print("yaa sure!!") 
        print()
        time.sleep(1)
        os.system("slack")
    elif ("go" in p) and ("site" in p) and ("youtube" in p):
        print()
        print("yaa sure!!") 
        print()
        time.sleep(1)
        os.system("Start chrome www.youtube.com")
    elif (("launch" in p) or ("open" in p)) and ("facebook" in p):
        print()
        print("yaa sure!!") 
        print()
        time.sleep(1)
        os.system("Start chrome https://www.facebook.com/")
    elif (("launch" in p) or ("open" in p)) and ("instagram" in p):
        print()
        print("yaa sure!!") 
        print()
        time.sleep(1)
        os.system("Start chrome https://www.instagram.com/")
    elif (("launch" in p) or ("open" in p)) and ("linkedin" in p):
        print()
        print("yaa sure!!") 
        print()
        time.sleep(1)
        os.system("Start chrome https://www.linkedin.com/feed/")
    elif ("go" in p) and ("site" in p) and ("candy crush" in p):
        print()
        print("yaa sure!!") 
        print()
        time.sleep(1)
        os.system("Start chrome https://king.com/play/scrubbydubby")
    elif ("go" in p) and ("site" in p) and ("github.com" in p): 
        print()
        print("yaa sure!!")
        print()
        time.sleep(1) 
        os.system("Start chrome https://github.com/")
    elif  ("exit" in p)  or ("quit" in p):
        break
    else:
        print("  OOPS!!  Don't Support")

	
    
	

	