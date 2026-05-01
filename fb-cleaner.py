import pyautogui
import time

# --- GLOBAL SETTINGS ---
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 1.0

# Set to True if using a Mac with a Retina display, otherwise False (e.g., Windows)
IS_RETINA = True 

# --- SCROLL CONFIGURATION ---
ARROWS_AFTER_EDIT = 10  
ARROWS_SEARCH = 4         
SCROLL_PRIVACY_MENU = -1000  

print("The bot starts in 5 seconds! Switch to the Facebook window...")
print("⚠️ TO STOP IT: Throw your mouse to one of the screen corners or press Ctrl+C!")
time.sleep(5)

# Automatically calculate the center of the screen
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

def click_image(file_name, confidence_level=0.7):
    """Searches for an image on the screen and clicks it."""
    try:
        position = pyautogui.locateCenterOnScreen(file_name, confidence=confidence_level, grayscale=True)
        if position is not None:
            if IS_RETINA:
                pyautogui.click(position.x / 2, position.y / 2)
            else:
                pyautogui.click(position.x, position.y)
            return True
    except Exception as e:
        print(f"Error while searching for {file_name}: {e}")
    return False

counter = 1

# --- MAIN FLOW ---
while True:
    print(f"--- Analyzing post {counter} ---")
    
    # 1. Search and click the three dots button
    if click_image('./icons/options.png'):
        time.sleep(1) 
        
        # 2. Click on "Edit audience" / "Edit privacy"
        if click_image('./icons/modify.png'):
            time.sleep(0.5) 
            
            # 3. Move the cursor exactly to the center of the screen
            pyautogui.moveTo(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
            
            # 4. Scroll down (inside the privacy dropdown menu)
            pyautogui.scroll(SCROLL_PRIVACY_MENU)
            
            # 5. Move the cursor to the right to avoid the hover effect
            pyautogui.move(300, 0) 
            
            # 6. Click on "Only me"
            if click_image('./icons/only_me.png'):
                time.sleep(0.5)
                
                # 7. Click on "Save" (with 90% confidence to avoid false positives)
                if click_image('./icons/save.png', confidence_level=0.9):
                    time.sleep(1)
                    print(f"✅ Post {counter} set to 'Only me'!")
                    
                    # 8. Scroll down the timeline using arrow keys
                    pyautogui.press('down', presses=ARROWS_AFTER_EDIT, interval=0.1)
                    time.sleep(2)
                    
                    # 9. Loop again
                    counter += 1
                    continue

    # 10. If the three dots are not found, scroll down a bit and search again
    print("Looking for the three dots... scrolling down a bit...")
    pyautogui.press('down', presses=ARROWS_SEARCH, interval=0.1)
    time.sleep(2)