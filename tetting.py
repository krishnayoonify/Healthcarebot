import pyautogui
import pytesseract
from PIL import Image
import time

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"  # Adjust this path if necessary
)


def ocr_from_coordinates(left, top, width, height):
    # Capture the screenshot of the specific area
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    # Perform OCR on the screenshot
    text = pytesseract.image_to_string(screenshot)
    return text.strip()


def find_proposed_and_get_code(start_x, start_y, row_height, code_offset_x):
    while True:
        # Define the region for the status column
        status_region = (start_x, start_y, 100, row_height)  # Adjust width if necessary
        status_text = ocr_from_coordinates(*status_region)
        print(f"Status text: {status_text}")

        if "Proposed" in status_text:
            # If the status is "Proposed", define the region for the code column
            code_region = (
                start_x + code_offset_x,
                start_y,
                100,
                row_height,
            )  # Adjust width if necessary
            code_text = ocr_from_coordinates(*code_region)
            print(f"Found code: {code_text}")
            break

        # Move to the next row
        start_y += row_height

        # If reached the bottom of the view, scroll down and reset y coordinate
        if start_y > pyautogui.size().height - row_height:
            pyautogui.scroll(-500)  # Adjust scroll amount if needed
            start_y = start_y - pyautogui.size().height + row_height
            time.sleep(1)  # Give time for the screen to update


# Constants (Adjust based on your application's layout)
START_X = 1115  # X coordinate to start from
START_Y = 735  # Y coordinate to start from
ROW_HEIGHT = 60  # Height of each row in pixels
CODE_OFFSET_X = 15  # Horizontal offset to the code column from the status column

# Execute the function
find_proposed_and_get_code(START_X, START_Y, ROW_HEIGHT, CODE_OFFSET_X)
