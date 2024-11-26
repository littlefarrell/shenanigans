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
target_pos = (633, 568)
target_col = (232, 208, 0)
time_lim = 8
image_path_startercards = r'C:\ImagesForMacro\StarterCards.png'
image_path_additivecards = r'C:\ImagesForMacro\AdditiveCards.png'
image_path_desired = r'C:\ImagesForMacro\Desired.png'
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
# Remove the Hashtag symbol of the set you want. The top set is "easy" whilst the bottom set is "hard but more loot"
#array = [harvest, loot, commonloot, damage, range, cooldown, slayer, strong, dodge, press, champions, precise] #Easy, less loot
#array = [harvest, loot, commonloot, dodge, damage, strong, range, cooldown, slayer, press, champions, precise] #Hard, more loot

def move_mouse_relative(dx, dy):
    """
    Move the mouse cursor relatively from its current position.
    
    :param dx: Distance to move horizontally (positive for right, negative for left).
    :param dy: Distance to move vertically (positive for down, negative for up).
    """
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

time.sleep(0.1)
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

                    #Start Macro
                    pyautogui.keyDown('f8')
                    time.sleep(0.1)
                    pyautogui.keyUp('f8')
                    time.sleep(0.1)

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
                print("Starter Cards not detected")
                time.sleep(0.1)

            #AdditiveCards  
            try:
                #look for additive cards
                locationadditivecards = pyautogui.locateOnScreen(image_path_additivecards, confidence=0.8)
                time.sleep(0.2)
                x = 0
                while True:
                    print("Searching for: ", array[x])
                    time.sleep(0.01)
                    try:
                        locationtemp = pyautogui.locateOnScreen(array[x], confidence=0.8)
                        print("Found")
                        pyautogui.moveTo(locationtemp)
                        move_mouse_relative(0, 1)
                        pyautogui.click()
                        time.sleep(0.01)
                        break
                    except:
                        print("Not found")
                        time.sleep(0.01)
                    x += 1
                    if x > 11:
                        break
            except:
                print("Additive Cards not detected")
                time.sleep(0.1)     

            #Retry upon victory / loss
            pixel_color = pyautogui.screenshot().getpixel(target_pos)
            if pixel_color == target_col:
                if not start_time:
                    start_time = time.time()

                elapsed_time = time.time() - start_time
                if elapsed_time >= time_lim:
                    #turn off macro
                    pyautogui.keyDown('f8')
                    time.sleep(0.1)
                    pyautogui.keyUp('f8')
                    time.sleep(0.1)

                    #retry
                    locationretry = (1170, 820)
                    pyautogui.moveTo(locationretry)
                    move_mouse_relative(0, 1)
                    pyautogui.click()
                    time.sleep(0.05)
