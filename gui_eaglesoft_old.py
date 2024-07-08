import pyautogui
import json
import time


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


def gui_eaglesoft():
    # Example GUI automation
    pyautogui.moveTo(100, 100)
    pyautogui.click()
    time.sleep(1)
    result = {"message": "GUI task completed successfully"}
    return result


if __name__ == "__main__":
    import pdb

    pdb.set_trace()
    application_name = "Patterson Eaglesoft"
    search_application(application_name)
    # gui_eaglesoft()
