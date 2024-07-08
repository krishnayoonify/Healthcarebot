import pyautogui
import time
import pyperclip


# Function to open the Windows Start menu and search for an application
def search_application(application_name):
    # Press the Windows key to open the Start menu
    pyautogui.press("win")
    time.sleep(1)  # Wait for the Start menu to open

    # Type the application name
    pyautogui.typewrite(application_name)
    time.sleep(1)  # Wait for the search results to appear

    # Press Enter to open the application
    pyautogui.press("enter")


# Function to handle admin rights prompt
def handle_admin_prompt():
    time.sleep(35)  # Wait for the admin prompt to appear

    # Temporarily disable the fail-safe feature
    pyautogui.FAILSAFE = False

    # Move the mouse to the "Yes" button and click it
    # Replace (x, y) with the actual coordinates of the "Yes" button
    # pyautogui.moveTo(1100, 590, 1)
    yes_button_coords = (1100, 590)
    pyautogui.click(yes_button_coords)
    time.sleep(5)

    yes_button_coords = (890, 437)
    pyautogui.click(yes_button_coords)

    pyautogui.typewrite("Welcome@123")
    time.sleep(5)
    yes_button_coords = (900, 520)
    pyautogui.click(yes_button_coords)

    # select persdon
    time.sleep(5)
    pyautogui.click(40, 60)

    # select auto search
    # time.sleep(5)
    # pyautogui.click(650, 290)

    # search user
    time.sleep(5)
    pyautogui.click(700, 270)
    pyautogui.typewrite("Abbott")

    # click first user
    time.sleep(5)
    pyautogui.doubleClick(650, 445)

    # close alert box
    time.sleep(5)
    pyautogui.click(950, 620)

    # select first name
    pyautogui.click(650, 265)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)  # Wait for the clipboard to update
    first_name = pyperclip.paste()
    print("First name:", first_name)

    # select last name
    pyautogui.click(650, 285)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.5)  # Wait for the clipboard to update
    last_name = pyperclip.paste()
    print("Last name:", last_name)

    # Re-enable the fail-safe feature
    pyautogui.FAILSAFE = True


def main():
    application_name = "Patterson Eaglesoft"
    search_application(application_name)
    handle_admin_prompt()


if __name__ == "__main__":
    # import pdb

    # pdb.set_trace()
    main()
