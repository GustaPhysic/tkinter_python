import pyautogui
from time import sleep


#APERTAR O ARQUIVO
pyautogui.click(219,168, duration=1)
pyautogui.press('enter')
sleep(2)
#APERTAR E LOGAR 
pyautogui.click(969,617, duration=1)
pyautogui.write('gus123')
pyautogui.press('enter')
sleep(2)
pyautogui.press('enter')
#ADICIONAR NOVO PRODUTO
pyautogui.click(55,43, duration=1)

with open('itens.txt', 'r') as arquivo:
    for linha in arquivo:
        id_prod = linha.split(',')[0]
        nome = linha.split(',')[1]
        qntd = linha.split(',')[2]
        preco = linha.split(',')[3]

        pyautogui.click(200,85, duration=2)
        pyautogui.write(id_prod)
        pyautogui.click(205,148, duration=2)
        pyautogui.write(nome)
        pyautogui.click(179,217, duration=2)
        pyautogui.write(qntd)
        pyautogui.click(158,280, duration=2)
        pyautogui.write(preco)
        #CLICAR NO SALVAR
        pyautogui.click(227,324, duration=2)
        sleep(2)
        pyautogui.press('enter')





