import pyautogui
import time
import pyperclip
import os
from PIL import ImageGrab, Image


def open_eaglesoft():
    print("Opening EagleSoft")
    # return True
    application_name = "Patterson Eaglesoft"

    # Press the Windows key to open the Start menu
    pyautogui.press("win")
    time.sleep(1)  # Wait for the Start menu to open

    # Type the application name
    pyautogui.typewrite(application_name)
    time.sleep(1)  # Wait for the search results to appear

    # Press Enter to open the application
    pyautogui.press("enter")

    time.sleep(25)
    # provider_box = (857, 449)
    # pyautogui.moveTo(provider_box)
    # pyautogui.click(provider_box)
    # pyautogui.typewrite("Silvana")

    # provider_box_close = (848, 772)
    # pyautogui.moveTo(provider_box_close)
    # pyautogui.click(provider_box_close)

    password_box = (853, 477)
    pyautogui.moveTo(password_box)
    pyautogui.click(password_box)
    pyautogui.typewrite("Cumani12345!")

    logon_box = (899, 544)
    pyautogui.moveTo(logon_box)
    pyautogui.click(logon_box)
    time.sleep(20)

    chart_option_screen_box = (1384, 665)
    pyautogui.moveTo(chart_option_screen_box)
    pyautogui.click(chart_option_screen_box)
    time.sleep(5)


def process_request(user_name="Testa,Pa"):
    # return {"code": "E1232C", "fee": "24", "image": "image.png", "xray": "xray.png"}
    chart_box = (239, 67)
    pyautogui.moveTo(chart_box)
    pyautogui.click(chart_box)
    time.sleep(3)

    search_user_box = (676, 273)
    pyautogui.moveTo(search_user_box)
    pyautogui.click(search_user_box)
    pyautogui.typewrite(user_name)
    time.sleep(2)

    user_record_box = (630, 448)
    pyautogui.moveTo(user_record_box)
    pyautogui.click(user_record_box)
    pyautogui.doubleClick(user_record_box)
    time.sleep(3)

    alert_box = (960, 623)
    pyautogui.moveTo(alert_box)
    pyautogui.click(alert_box)

    ## get code ##

    def is_radio_button_selected(checked_image_path, region=None):
        """
        Check if the radio button is selected by comparing with checked and unchecked images.

        :param checked_image_path: Path to the checked radio button image.
        :param unchecked_image_path: Path to the unchecked radio button image.
        :param region: Region (left, top, width, height) to search within.
        :return: True if the radio button is selected, False otherwise.
        """
        try:
            checked_location = pyautogui.locateOnScreen(
                checked_image_path, region=region, confidence=0.8
            )
            if checked_location:
                return True
            else:
                return False
        except Exception as e:
            return False

    def get_popup_data(code, fee):
        edit_box = (922, 872)
        pyautogui.moveTo(edit_box)
        pyautogui.click(edit_box)
        time.sleep(1)
        checked_image_path = "radio_checked.png"
        # Get the full path to the current directory
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Define the path to the saved screenshot
        checked_image_path = os.path.join(current_directory, "radio_checked.png")
        region = (871, 330, 18, 17)
        is_selected = is_radio_button_selected(checked_image_path, region=region)
        if is_selected:
            pyperclip.copy("")
            code_box = (718, 363)
            pyautogui.moveTo(code_box)
            pyautogui.click(code_box)
            time.sleep(0.5)
            pyautogui.doubleClick(code_box)
            # pyautogui.hotkey('ctrl', 'a')
            pyautogui.hotkey("ctrl", "c")
            code = pyperclip.paste()
            print("C O D E ", code)

            time.sleep(0.5)
            pyperclip.copy("")
            fee_box = (1094, 385)
            pyautogui.moveTo(fee_box)
            pyautogui.click(fee_box)
            time.sleep(1)
            pyautogui.doubleClick(fee_box)
            pyautogui.hotkey("ctrl", "a")
            pyautogui.hotkey("ctrl", "c")
            fee = pyperclip.paste()
            print("F E E ", code)

        cancel_popup = (1193, 359)
        pyautogui.click(cancel_popup)
        time.sleep(0.5)
        return code, fee

    code = None
    fee = None
    table_box_cnt = 0
    for i in range(4):
        if not code:
            table_box = (922, 752 + table_box_cnt)
            table_box_cnt += 26
            pyautogui.moveTo(table_box)
            pyautogui.click(table_box)
            time.sleep(0.5)
            code, fee = get_popup_data(code, fee)

    for i in range(6):
        if not code:
            fee_box = (878, 848)
            pyautogui.moveTo(fee_box)
            pyautogui.click(fee_box)
            time.sleep(0.5)
            code, fee = get_popup_data(code, fee)
    ## get code done ##

    def save_clipboard_image(output_path):
        """
        Save the image from the clipboard to the specified file path.

        :param output_path: Path to save the image file.
        """
        # Grab the image from the clipboard
        image = ImageGrab.grabclipboard()
        if isinstance(image, Image.Image):
            # Save the image to the specified path
            image.save(output_path, "PNG")
            print(f"Image saved to {output_path}")
            return True
        else:
            print("No image found in clipboard.")
            return False

    ### GET DOC ###

    image_box = (1199, 868)
    pyautogui.moveTo(image_box)
    pyautogui.click(image_box)

    view_images_box = (1218, 705)
    pyautogui.moveTo(view_images_box)
    pyautogui.click(view_images_box)
    time.sleep(7)

    scanned_doc_box = (169, 195)
    pyautogui.moveTo(scanned_doc_box)
    pyautogui.click(scanned_doc_box)
    time.sleep(7)

    save_images_box = (468, 170)
    pyautogui.moveTo(save_images_box)
    pyautogui.rightClick(save_images_box)

    copy_image_box = (527, 518)
    pyautogui.moveTo(copy_image_box)
    pyautogui.click(copy_image_box)
    time.sleep(0.5)

    output_path = "image.png"
    if save_clipboard_image(output_path):
        # Send the image file to the API
        print("send_image_to_api")

    # # Clean up: Remove the saved image file if desired
    # if os.path.exists(output_path):
    #     # os.remove(output_path)
    #     print(f"Temporary image file {output_path} removed.")

    close_images_box = (1892, 9)
    pyautogui.moveTo(close_images_box)
    pyautogui.click(close_images_box)

    ### GET DOC DONE ###

    ### GET X-Rays ###
    time.sleep(0.5)
    xray_box = (1594, 812)
    pyautogui.moveTo(xray_box)
    pyautogui.click(xray_box)
    time.sleep(5)

    xray_copy_box = (818, 57)
    pyautogui.moveTo(xray_copy_box)
    pyautogui.click(xray_copy_box)
    time.sleep(1)

    xray_clipboard_box = (1029, 588)
    pyautogui.moveTo(xray_clipboard_box)
    pyautogui.click(xray_clipboard_box)

    output_path = "xray.png"
    if save_clipboard_image(output_path):
        # Send the image file to the API
        print("send_image_to_api")

    # Clean up: Remove the saved image file if desired
    # if os.path.exists(output_path):
    #     # os.remove(output_path)
    #     print(f"Temporary image file {output_path} removed.")

    close_xray_box = (333, 53)
    pyautogui.moveTo(close_xray_box)
    pyautogui.click(close_xray_box)
    ### GET X-Rays DONE ###

    # ### CLOSE Chart POPUP ###
    close_xray_box = (1438, 199)
    pyautogui.moveTo(close_xray_box)
    pyautogui.click(close_xray_box)

    # ### CLOSE Chart DONE ###

    # ### CLOSE Pateint ###
    close_patient_box = (107, 69)
    pyautogui.moveTo(close_patient_box)
    pyautogui.click(close_patient_box)

    # ### CLOSE Pateint DONE ###
    return {"code": code, "fee": fee, "image": "image.png", "xray": "xray.png"}


# open_eaglesoft()
# print(process_request())
