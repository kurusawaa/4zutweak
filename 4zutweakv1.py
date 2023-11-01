import os
import shutil
import time
import platform
import psutil

def banner():
    os.system('clear')
    print()
    print("""          \t\tCONFIG MENU
    
    \t\t\033[91m[\033[0m01\033[91m]  \033[95m>> \033[36mapp_process32 (60fps)
\t\t\033[91m[\033[0m02\033[91m]  \033[95m>> \033[36mapp_process64 (90fps)
\t\t\033[91m[\033[0m03\033[91m]  \033[95m>> \033[36mModule prop   (120fps)
\t\t\033[91m[\033[0m04\033[91m]  \033[95m>> \033[36mTerminal Info
\t\t\033[91m[\033[0m05\033[91m]  \033[95m>> \033[36mAbout
\t\t\033[91m[\033[0m00\033[91m]  \033[95m>> \033[36mExit
   """)

banner()
print()
print()
choice = str(input("\033[37m Select option : \033[91m"))
def sixtyfps():
# Build the download file
    print("\033[92m")
    os.chdir('..')
    os.system("wget https://www.mediafire.com/file/4k1ggg7rpph2nvd/app_process32")
   

# Move the file into the com.mobile.legends folder
    shutil.move("app_process32", "/storage/emulated/0/Android")
    
    os.system('clear')
    banner()
    print("Chossing => \033[93m", choice)
    print("\033[36mModule\033[0m : \033[93mapp_process32 ")
    print()
    time.sleep(1)
    print("\033[92m[\033[37m*\033[92m] \033[36madd Locked 60 Fps.")
    time.sleep(1)
    print("\033[92m[\033[37m*\033[92m] \033[36maddadd Reduce Lag config")
    time.sleep(1)
    print("\033[92m[\033[37m*\033[92m] \033[36madd Successfully add config to Mobile Legends.")
    
    
    
    
def menu():
    if choice == '1' or choice == '01':
        sixtyfps()
    elif choice == '2' or choice == '02':
        print()
    elif choice == '3' or choice == '03':
        print()
    elif choice == '4' or choice == '04':
        device_information()
    elif choice == '5' or choice == '05':
        print()
    elif choice == '0' or choice == '00':
        exit()
    else:
        print("Invalid options!")
        



def username():
      return psutil.Process().username()
def get_cpu_cores():
      return psutil.cpu_count()
      


def device_information():
    os.system('clear')
    system_info = platform.uname()
    device_name = system_info.system
    device_processor = system_info.processor
    device_version = system_info.release
    
    
    process = psutil.Process()
    
    print(f""" \t\t    
             \033[93m
                   ╭───────────────╮
                   │ TERMINAL INFO │
                   ╰───────────────╯
  
    \t\t\033[91m[\033[0m*\033[91m]  \033[36mUsername : \033[37m{username()}  
    \t\t\033[91m[\033[0m*\033[91m]  \033[36mSystem : \033[37m{device_name}
\t\t\033[91m[\033[0m*\033[91m]  \033[36mProcessor : \033[37m{device_processor}
\t\t\033[91m[\033[0m*\033[91m]  \033[36mCpu cores : \033[37m{get_cpu_cores()}
\t\t\033[91m[\033[0m*\033[91m]  \033[36mVersion : \033[37m{device_version}

 \t\t   Credits to 4ZU PH
""")
    
    
    

menu()
