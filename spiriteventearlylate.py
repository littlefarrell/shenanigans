import pyautogui
import time
import keyboard
import threading
import os
import win32api
import win32con

#other variables
loop_running = False
flag_var = True
flag_var2 = True
retry_flag = False
target_pos = (633, 568)
target_col = (232, 208, 0)
alternative_pos = (621, 567)
alternative_col = (231, 212, 0)
time_lim = 5
image_path_startercards = r'C:\ImagesForMacro\StarterCards.png'
image_path_additivecards = r'C:\ImagesForMacro\AdditiveCards.png'
image_path_endwisp = r'C:\ImagesForMacro\EndWisp.png'
image_path_desired = r'C:\ImagesForMacro\Desired.png'
image_path_wave1 = r'C:\ImagesForMacro\Wave1.png'
image_path_wave28 = r'C:\ImagesForMacro\Wave28.png'
image_path_ability = r'C:\ImagesForMacro\Ability.png'
harvest = r'C:\ImagesForMacro\Harvest.png'
loot = r'C:\ImagesForMacro\Loot.png'
commonloot = r'C:\ImagesForMacro\CommonLoot.png'
damage = r'C:\ImagesForMacro\Damage.png'
range = r'C:\ImagesForMacro\Range.png'
cooldown = r'C:\ImagesForMacro\Cooldown.png'
slayer = r'C:\ImagesForMacro\Slayer.png'
strong = r'C:\ImagesForMacro\Strong.png'
dodge = r'C:\ImagesForMacro\Dodge.png'
press = r'C:\ImagesForMacro\Press.png'
champions = r'C:\ImagesForMacro\Champions.png'
precise = r'C:\ImagesForMacro\Precise.png'
# Change the order of the cards to match your desired priority
arrayearly = [harvest, loot, commonloot, damage, range, cooldown, slayer, champions, dodge, strong, press, precise]
arraylate = [harvest, champions, dodge, loot, commonloot, damage, range, cooldown, slayer, strong, press, precise]

def move_mouse_relative(dx, dy):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy, 0, 0)

def killswitch():
    # Check if the 'm' key is pressed to stop the program
    global flag_var
    while True:
        if keyboard.is_pressed('m'):
            print("Kill switch activated. Exiting program.")
            flag_var = False  # Exit the loop if 'm' is pressed
            break
        
thread = threading.Thread(target=killswitch)  # Create a thread
thread.start()  # Start the thread

time.sleep(0.05)
print("Script Started: press ; to start the script, and m to stop it")

while flag_var:
    
    # Check if the ';' key is pressed to start the loop
    if keyboard.is_pressed(';') and not loop_running:
        print("Loop started. Monitoring...")
        loop_running = True

    if loop_running:
        start_time = None
        while flag_var and loop_running:
            #Starter Card
            try:
                locationstart = pyautogui.locateOnScreen(image_path_startercards, confidence=0.8)
                try:
                    #click desired card
                    locationdesired = pyautogui.locateOnScreen(image_path_desired, confidence=0.8)
                    pyautogui.moveTo(locationdesired)
                    move_mouse_relative(0, 1)
                    pyautogui.click()
                    print("Desired card found")

                    #Start Macro
                    pyautogui.keyDown('f8')
                    time.sleep(0.09)
                    pyautogui.keyUp('f8')
                    time.sleep(0.01)
                    print("Macro Started")

                except:
                    #This part will open settings and restart stage if wrong card chosen
                    locationcard = (750, 500)
                    pyautogui.moveTo(locationcard)
                    move_mouse_relative(0,1)
                    pyautogui.click()
                    time.sleep(0.1)

                    locationvoteyes = (900, 185)
                    pyautogui.moveTo(locationvoteyes)
                    move_mouse_relative(0,1)
                    pyautogui.click()
                    time.sleep(7)

                    locationsettings = (30, 1000)
                    pyautogui.moveTo(locationsettings)
                    move_mouse_relative(0,1)
                    pyautogui.click()
                    time.sleep(0.1)

                    locationrestart = (1200, 500)
                    pyautogui.moveTo(locationrestart)
                    move_mouse_relative(0,1)
                    pyautogui.click()
                    time.sleep(0.1)

                    locationrestartvoteyes = (860, 555)
                    pyautogui.moveTo(locationrestartvoteyes)
                    move_mouse_relative(0,1)
                    pyautogui.click()
                    time.sleep(0.1)

                    locationrestartok = (960, 555)
                    pyautogui.moveTo(locationrestartok)
                    move_mouse_relative(0,1)
                    pyautogui.click()
                    time.sleep(0.1)

                    pyautogui.moveTo(locationsettings)
                    move_mouse_relative(0,1)
                    pyautogui.click()
                    time.sleep(0.1)

            except:
                #print("Starter Cards not detected")
                time.sleep(0.01)

            #Detects wave1 / wave28 and switches between early and late array accordingly
            try:
                locationwave1 = pyautogui.locateOnScreen(image_path_wave1, confidence=0.9)
                flag_var2 = True #if wave1 is detected, early array is used (prob will also detect wave10-19 but should be fine)
                #print("wave 1 detected")
                time.sleep(0.01)
            except:
                #print("wave 1 not detected")
                time.sleep(0.01)

            try:
                locationwave28 = pyautogui.locateOnScreen(image_path_wave28, confidence=0.95)
                flag_var2 = False #if wave28 is detected, late array is used
                #print("wave 28 detected")
                time.sleep(0.01)
            except:
                #print("wave 28 not detected")
                time.sleep(0.01)

            #AdditiveCards  
            try:
                #look for additive cards
                locationadditivecards = pyautogui.locateOnScreen(image_path_additivecards, confidence=0.8)
                time.sleep(0.05)
                x = 0
                if flag_var2: #flag_var2 = true means early array is used
                    while True:
                        print("Searching for: ", arrayearly[x])
                        time.sleep(0.01)
                        try:
                            locationtemp = pyautogui.locateOnScreen(arrayearly[x], confidence=0.8)
                            print("Found")
                            pyautogui.moveTo(locationtemp)
                            move_mouse_relative(0, 1)
                            pyautogui.click()
                            time.sleep(0.001)
                            break
                        except:
                            print("Not found")
                            time.sleep(0.001)
                        x += 1
                        if x > 11:
                            break
                else: #flag_var2 != true so late array is used
                    while True:
                        print("Searching for: ", arraylate[x])
                        time.sleep(0.01)
                        try:
                            locationtemp = pyautogui.locateOnScreen(arraylate[x], confidence=0.8)
                            print("Found")
                            pyautogui.moveTo(locationtemp)
                            move_mouse_relative(0, 1)
                            pyautogui.click()
                            time.sleep(0.001)
                            break
                        except:
                            print("Not found")
                            time.sleep(0.001)
                        x += 1
                        if x > 11:
                            break
            except:
                #print("Additive Cards not detected")
                time.sleep(0.01)     

            #Retry upon victory / loss
            pixel_color = pyautogui.screenshot().getpixel(target_pos)
            alternative_pixel_color = pyautogui.screenshot().getpixel(alternative_pos)

            try: #Detects end wisp and clicks twice then starts retry code segment
                locationendwisp = pyautogui.locateOnScreen(image_path_endwisp, confidence=0.8)
                pyautogui.moveTo(960,580)
                move_mouse_relative(0, 1)
                pyautogui.click()
                time.sleep(0.05)
                pyautogui.click()
                time.sleep(0.05)
                retry_flag = True
            except:
                time.sleep(0.001)
                
            try: #Detects if gojo messed up the macro -_-
                locationabilitycancel = pyautogui.locateOnScreen(image_path_ability, confidence=0.8)
                time.sleep(2.5)
                pyautogui.moveTo(955, 578)
                move_mouse_relative(0,1)
                pyautogui.click()
                time.sleep(0.05)
                pyautogui.click()
                time.sleep(0.05)
                retryflag = True
            except:
                time.sleep(0.001)

            if pixel_color == target_col or alternative_pixel_color == alternative_col or retry_flag:
                if not start_time:
                    start_time = time.time()

                elapsed_time = time.time() - start_time
                if elapsed_time >= time_lim:
                    #turn off macro
                    pyautogui.keyDown('f8')
                    time.sleep(0.1)
                    pyautogui.keyUp('f8')
                    time.sleep(0.05)
                    print("Rewards detected, macro stopped")

                    #retry
                    locationcancel = (960, 580)
                    pyautogui.moveTo(locationcancel)
                    move_mouse_relative(0, 1)
                    pyautogui.click()
                    time.sleep(0.05)

                    locationretry = (1170, 820)
                    pyautogui.moveTo(locationretry)
                    move_mouse_relative(0, 1)
                    pyautogui.click()
                    time.sleep(0.05)
                    print("Run restarted")
                    retry_flag = False
