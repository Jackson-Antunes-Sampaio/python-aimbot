import pyautogui
import time

# BOT TESTE COM PAIN
# pyautogui.keyDown("alt")
# pyautogui.press('tab')
# pyautogui.keyUp('alt')
# pyautogui.click(
#     'C:/Users/jaco_/AndroidStudioProjects/python/aimbot/Circulo.PNG')
# pyautogui.move(0, 100)
# pyautogui.drag(xOffset=200, yOffset=200, duration=5)
# ______________________________________________________________________________

# BOT TESTE COM EMULADOR
# pyautogui.keyDown("alt")
# pyautogui.press('tab')
# pyautogui.keyUp('alt')
# while True:
#     if pyautogui.locateOnScreen(
#             'C:/Users/jaco_/AndroidStudioProjects/python/aimbot/REPETIR.PNG'):
#         pyautogui.click(
#             'C:/Users/jaco_/AndroidStudioProjects/python/aimbot/VENDER_RUNAS.PNG')
#         time.sleep(0.5)
#         pyautogui.click()
#         time.sleep(0.5)
#         pyautogui.click(
#             'C:/Users/jaco_/AndroidStudioProjects/python/aimbot/SIM.PNG')
#         time.sleep(3)
#         pyautogui.click(
#             'C:/Users/jaco_/AndroidStudioProjects/python/aimbot/REPETIR.PNG')
#         time.sleep(1)
#         pyautogui.click(
#             'C:/Users/jaco_/AndroidStudioProjects/python/aimbot/X10.PNG')
#         quit()


# BOT ENVIAR MENSAGEM PRO GREAT
diretorio = "C:/Users/jaco_/AndroidStudioProjects/python/aimbot/WPP/"

pyautogui.click(f"{diretorio}chrome.PNG")

pyautogui.locateOnScreen(
    f"{diretorio}jackson.PNG")
pyautogui.click(
    f"{diretorio}jackson.PNG")

pyautogui.locateOnScreen(
    f"{diretorio}url.PNG")
pyautogui.press("F6")
pyautogui.write('https://web.whatsapp.com/')
pyautogui.press("ENTER")
pyautogui.locateOnScreen(
    f"{diretorio}webwpp.PNG")
pyautogui.sleep(1)
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')
pyautogui.press('tab')

pyautogui.write('great')
pyautogui.locateOnScreen(
    f"{diretorio}great.PNG")
pyautogui.click(
    f"{diretorio}great.PNG")
pyautogui.sleep(1)
pyautogui.write('MENSAGEM ENVIADA DE UM BOT PARA OUTRO (GUNZ)')
pyautogui.press("ENTER")
