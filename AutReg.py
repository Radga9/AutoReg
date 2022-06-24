from colorama import Fore, Back, Style
import pyautogui
import random
import pyperclip
import keyboard
import os
from time import sleep
from colorama import init
init()


hello = """
███████╗████████╗ █████╗ ██████╗
██╔════╝╚══██╔══╝██╔══██╗██╔══██╗
███████╗   ██║   ███████║██████╔╝
╚════██║   ██║   ██╔══██║██╔══██╗
███████║   ██║   ██║  ██║██║  ██║
╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝
██╗    ██╗ █████╗ ██████╗ ███████╗
██║    ██║██╔══██╗██╔══██╗██╔════╝
██║ █╗ ██║███████║██████╔╝███████╗
██║███╗██║██╔══██║██╔══██╗╚════██║
╚███╔███╔╝██║  ██║██║  ██║███████║
 ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝


Deezer AutoRegistration | V0.1.0 | Dev by Radga9 |

Версия специально создна для теста

██████╗ ██╗     ███████╗███████╗███████╗███████╗██████╗
██╔══██╗██║     ██╔════╝██╔════╝██╔════╝██╔════╝██╔══██╗
██████╔╝██║     █████╗  ███████╗███████╗█████╗  ██║  ██║
██╔══██╗██║     ██╔══╝  ╚════██║╚════██║██╔══╝  ██║  ██║
██████╔╝███████╗███████╗███████║███████║███████╗██████╔╝
╚═════╝ ╚══════╝╚══════╝╚══════╝╚══════╝╚══════╝╚═════╝

"""


def mail_rand_gen():
    Abc_list = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s",
                "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
    Num_list = ["0", "7", "4", "1", "2", "5", "8", "9", "6", "3"]

    G_Mail = ""
    for i in range(random.randint(2, 3)):
        G_Mail = G_Mail + Num_list[random.randint(0, len(Num_list)-1)]
        for j in range(random.randint(2, 3)):
            G_Mail = G_Mail + Abc_list[random.randint(0, len(Abc_list)-1)]
    return G_Mail


def deezer_page_clicker(num_of_acc):
    deezer_icon = pyautogui.locateOnScreen('deezer.png', confidence=0.9)
    if deezer_icon:
        cntr_deezer = pyautogui.center(deezer_icon)
        x_cntr_deezer, y_cntr_deezer = cntr_deezer
        pyautogui.rightClick(x_cntr_deezer, y_cntr_deezer)
        pyautogui.press(['down']*2)
        pyautogui.hotkey('right')
        pyautogui.press(['down']*num_of_acc)
        pyautogui.hotkey('enter')
        while True:
            cancel_button = pyautogui.locateOnScreen(
                'cancel.png', confidence=0.9)
            if cancel_button:
                cntr_cancel = pyautogui.center(cancel_button)
                x_cntr_cancel, y_cntr_cancel = cntr_cancel
                pyautogui.click(x_cntr_cancel, y_cntr_cancel)
                break
        return True
    else:
        print("Не найден Дизер ссылка в углу")
        sleep(2)
        return False


def reger(eye_x, eye_y, num_to_mail):
    pyautogui.click(eye_x-100, eye_y)
    sleep(0.1)
    temp_mail = mail_rand_gen()+"A"+str(num_to_mail+1)+"@gmail.com"
    pyperclip.copy(temp_mail)
    print(temp_mail)
    sleep(0.1)
    keyboard.write(temp_mail)
    sleep(0.1)
    pyautogui.hotkey('shift', 'tab')
    keyboard.write(temp_mail)
    sleep(0.1)
    pyautogui.hotkey('shift', 'tab')
    keyboard.write(temp_mail)
    sleep(0.1)
    pyautogui.press(['tab']*3)
    keyboard.write(str(random.randint(17, 23)))
    pyautogui.hotkey('tab')
    for i in range(random.randint(1, 2)):
        pyautogui.hotkey('down')
    pyautogui.press(['tab']*3)
    pyautogui.hotkey('enter')


def artists(Accs_Num_reg):
    for j in range(Accs_Num_reg):
        i = 0
        while i < 10:
            Srch = pyautogui.locateOnScreen(
                'Search.png', confidence=0.9)
            i += 1
        cntr_Srch = pyautogui.center(Srch)
        x_cntr_Srch, y_cntr_Srch = cntr_Srch
        pyautogui.click(x_cntr_Srch+200, y_cntr_Srch)
        keyboard.write("jared", delay=0.1)
        while True:
            sng = pyautogui.locateOnScreen(
                'jared song.png', confidence=0.9)
            print("search1")
            if sng:
                cntr_sng = pyautogui.center(sng)
                x_cntr_sng, y_cntr_sng = cntr_sng
                break
        pyautogui.click(x_cntr_sng, y_cntr_sng)
        while True:
            lov = pyautogui.locateOnScreen(
                'Love.png', confidence=0.9)
            print("Search2")
            if lov:
                cntr_lov = pyautogui.center(lov)
                x_cntr_lov, y_cntr_lov = cntr_lov
                break

        pyautogui.click(x_cntr_lov+200, y_cntr_lov)
        pyautogui.click(x_cntr_lov+400, y_cntr_lov)

        while True:
            don_reg = pyautogui.locateOnScreen(
                'done register.png', confidence=0.9)
            print("Search3")
            if don_reg:
                cntr_don_reg = pyautogui.center(don_reg)
                x_cntr_don_reg, y_cntr_don_reg = cntr_don_reg
                break
        pyautogui.click(x_cntr_don_reg, y_cntr_don_reg)
        pyautogui.hotkey('ctrl', 'tab')


def eye_finder(num_acc):
    eye = pyautogui.locateOnScreen('eye.png', confidence=0.9)
    if eye:
        print(eye)
        cntr_eye = pyautogui.center(eye)
        print(cntr_eye)
        x_cntr, y_cntr = cntr_eye
        reger(x_cntr, y_cntr, num_acc)
    else:
        print("Глаз не найден")


def solv_click():
    i = 0
    while i < 5:
        solv = pyautogui.locateOnScreen('solv.png', confidence=0.9)
        if solv:
            cntr_solv = pyautogui.center(solv)
            x_cntr_solv, y_cntr_solv = cntr_solv
            pyautogui.click(x_cntr_solv, y_cntr_solv)
            break
        else:
            print("ищу решатель")
        i += 1


def check_if_enter():
    i = 0
    while i < 5:
        sleep(0.2)
        wlcm = pyautogui.locateOnScreen('welcome.png', confidence=0.9)
        ok_b = pyautogui.locateOnScreen('capchaError.png', confidence=0.9)
        if ok_b:
            print("хуево!")
            pyautogui.hotkey('ctrl', 'r')
            sleep(5)
            eye_finder(1)
        if wlcm:
            print("Все ахуенно!")
            pyautogui.hotkey('shift', 'ctrl', 'tab')
            return True
        else:
            print("удачно введена?")
        i += 1


def retry_click():
    i = 0
    while i < 3:
        retry = pyautogui.locateOnScreen('retry.png', confidence=0.9)
        if retry:
            cntr_retry = pyautogui.center(retry)
            x_cntr_retry, y_cntr_retry = cntr_retry
            pyautogui.click(x_cntr_retry, y_cntr_retry)
            sleep(1)
            solv_click()
            break
        i += 1


def reCaptcha(reg_acc):
    reg = 0
    while reg != reg_acc:
        solv_click()
        if check_if_enter():
            reg += 1
        else:
            retry_click()
    return False


def starting():
    while True:
        try:
            Accs_Num = int(input("Сколько Аккаунтов? : "))
            break
        except:
            print("Введите Повторно")

    os.system('start firefox')
    sleep(5)
    for k in range(Accs_Num):
        if deezer_page_clicker(k):
            sleep(0.1)
        else:
            killer()

    for s in range(Accs_Num):
        eye_finder(s)
        pyautogui.hotkey('ctrl', 'shift', 'tab')
        sleep(1)
    pyautogui.hotkey('ctrl', 'w')

    print("Чекаю регистрацию аккаунтов")

    while reCaptcha(Accs_Num):
        print("===never give up===")

    print("Регистрация Окончена.")
    print("Ввод Артистов...")
    artists(Accs_Num)
    quit()


def killer():
    os.system("taskkill /f /im python.exe")


print(Fore.BLUE + Back.RED + Style.BRIGHT + hello + Style.RESET_ALL)
starting()
