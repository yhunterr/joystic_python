import hid
import time
import pyautogui

VID = 0x0810
PID = 0xE501

key_values = {
    "default": "01 80 80 7E 7F 0F 00 00",
    "LEFT_BTN": "01 80 80 7E 7F 0F 01 00",
    "RIGHT_BTN": "01 80 80 7E 7F 0F 02 00",
    "LEFT_ARROW": "01 80 80 00 7F 0F 00 00",
    "RIGHT_ARROW": "01 80 80 FF 7F 0F 00 00",
    "UP_ARROW": "01 80 80 7F 00 0F 00 00",
    "DOWN_ARROW": "01 80 80 7F FF 0F 00 00",
    "SELECT_KEY": "01 80 80 7F 7F 0F 10 00",
    "START_KEY": "01 80 80 7F 7F 0F 20 00",
    "X_KEY": "01 80 80 7F 7F 1F 00 00",
    "Y_KEY": "01 80 80 7F 7F 8F 00 00",
    "A_KEY": "01 80 80 7F 7F 2F 00 00",
    "B_KEY": "01 80 80 7F 7F 4F 00 00"
}

def main():
    print("MAIN START")

    try:
        dev = hid.device()
        dev.open(VID,PID)
        print("device open")
        
        while True:
            data = dev.read(64)
            hex_numbers = " ".join([f"{num:02X}" for num in data])
            #print(hex_numbers)

            if hex_numbers == key_values["LEFT_ARROW"]:
                pyautogui.write(['left'])
            elif hex_numbers == key_values["RIGHT_ARROW"]:
                pyautogui.write(['right'])
            elif hex_numbers == key_values["DOWN_ARROW"]:
                pyautogui.write(['down'])
            elif hex_numbers == key_values["UP_ARROW"]:
                pyautogui.write(['up'])
            elif hex_numbers == key_values["X_KEY"]:
                pyautogui.write('x')
            elif hex_numbers == key_values["Y_KEY"]:
                pyautogui.write('y')
            elif hex_numbers == key_values["A_KEY"]:
                pyautogui.write('a')
            elif hex_numbers == key_values["B_KEY"]:
                pyautogui.write('b')
            elif hex_numbers == key_values["SELECT_KEY"]:
                break
            print("Running ... ")
            time.sleep(0.1)
        print("END")
    except Exception as e:
        print("error : ",e)
        return

main()