import pyautogui
import time


def display_mouse_coordinates():
    print("Press Ctrl-C to quit.")
    try:
        while True:
            x, y = pyautogui.position()
            position_str = f"X: {x} Y: {y}"
            print(position_str, end="")
            print("\b" * len(position_str), end="", flush=True)
            time.sleep(3)
    except KeyboardInterrupt:
        print("\nDone.")


if __name__ == "__main__":
    display_mouse_coordinates()
