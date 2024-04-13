import pyautogui

try:
    while True:
        x, y = pyautogui.position()
        print("\033[H\033[J", end="")
        print("Mouse position - X:", x, " Y:", y)
        pyautogui.sleep(0.1)

except KeyboardInterrupt:
    print("\nProgram terminated by user.")
