# Facebook Privacy Automator 🤖🔒

A Python script based on **Computer Vision** that automates the tedious process of changing the privacy of old posts on your Facebook timeline, setting them all to **"Only me"** in bulk.

This bot does not inject code or use Facebook APIs (which risks bans). Instead, it fully simulates human behavior: it "looks" at the screen pixels, moves the mouse, and uses the keyboard.

## 🛠 Requirements & Installation

1. Make sure you have **Python 3** installed.
2. Install the required libraries by running this command in your terminal:
   ```bash
   pip install pyautogui opencv-python pillow
   ```
3. If you use a Mac with a **Retina display**, ensure the `IS_RETINA = True` variable inside the script is active. If you're on Windows, change it to `False`.

## 📸 "Icons" Setup

For the bot to know where to click, you need to create a folder named `icons` in the same directory as the script and place 4 very precise screenshots of the Facebook buttons. 

**WARNING: The bot is color-sensitive. It is strictly required to set Facebook to DARK MODE before taking the screenshots and before running the bot.**

Rename your image snips exactly like this:
* `options.png` (The three dots icon at the top right of the post)
* `modify.png` (The "Edit audience" or "Edit privacy" option)
* `only_me.png` (The "Only me" icon with the padlock)
* `save.png` (The blue "Save" button / *attention: crop only the button itself, without outer margins*)

*Note: Try taking the screenshots without hovering your mouse over the buttons, otherwise you'll capture the 'hover' effect (the grey background) and the bot won't recognize them at rest.*

## 🚀 How to Use (The Flow)

1. Open your browser, go to your **Personal Profile** (Timeline), and scroll to the year/month of the posts you want to hide.
2. Make sure **Facebook is in Dark Mode**.
3. Run the script from your Terminal:
   ```bash
   python3 bot.py
   ```
4. **You have 5 seconds** to click on the Facebook window and bring it to the foreground.
5. Take your hands off the mouse and keyboard, and let the bot work! 

The bot will run this loop endlessly:
* Finds the post and opens the menu.
* Centers the mouse and scrolls to ensure "Only me" is visible.
* Makes a slight lateral movement to clear the view of graphical hover effects.
* Selects, Saves, and scrolls down the timeline to move to the next post.

## 🛑 Emergency Brake (Failsafe)

Since it's an infinite loop, to stop the bot when you're done (or if it does something unexpected), simply use the built-in failsafe:
**Throw your mouse cursor quickly to one of the 4 extreme corners of your screen.** The script will crash instantly, stopping safely. 
Alternatively, go back to the Terminal and press `Ctrl + C`.