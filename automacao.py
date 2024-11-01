import pyautogui as pa
import time #PARA DEFINIR O TEMPO DAS AÇOES
import pyperclip #PODER ESCREVER COM ACENTUAÇÃO 
pa.PAUSE = 0.5 #DEFINIR O TEMPO PARA EXECUTAR 

pa.press('win')
pa.write('chrome')
pa.press('ENTER')
pa.write("https://www.youtube.com")
pa.press('ENTER')
time.sleep(4)
pa.click(x=696, y=118)
pyperclip.copy("Programação")
pa.hotkey('ctrl' , 'v')
pa.press('ENTER')
time.sleep(2)
pa.click(x=1007, y=557)
