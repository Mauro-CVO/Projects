from bs4 import BeautifulSoup  #del módulo bs4, necesitamos BeautifulSoup
import requests
import schedule
import web_scrapping
import my_criptos
import time

def bot_send_text(bot_message):
    
    bot_token = '1775951719:AAFixPpRGqcPSBwf9mosSVo4BLMFiou0ppo'
    bot_chatID = '1209865597'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response

def check():
    my_BTC = my_criptos.BTC
    my_ETH = my_criptos.ETH

    criptos =  web_scrapping.scrap()
    #criptos = [['BTC', 900000.4574825022], ['ETH', 55686.29116238187], ['DOGE', 6.73871583366395]]
    my_BTC_MXN = [criptos[i][1] for i in range(len(criptos)) if criptos[i][0] == 'BTC'][0] * my_BTC
    my_ETH_MXN = [criptos[i][1] for i in range(len(criptos)) if criptos[i][0] == 'ETH'][0] * my_ETH

    if my_BTC_MXN > 1550:
        bot_send_text(f'Precio de mis BTC: {my_BTC_MXN}, vender!!!')
    elif my_BTC_MXN < 1420:
        bot_send_text(f'Precio de mis BTC: {my_BTC_MXN}, comprar!!!')
    # else:
    #     bot_send_text(f'Precio de mis BTC: {my_BTC_MXN}')
    
    if my_ETH_MXN > 560:
        bot_send_text(f'Precio de mis ETH: {my_ETH_MXN}, vender!!!')
    elif my_ETH_MXN < 520:
        bot_send_text(f'Precio de mis ETH: {my_ETH_MXN}, comprar!!!')
    # else:
    #     bot_send_text(f'Precio de mis ETH: {my_ETH_MXN}')

if __name__ == '__main__':
    #check()  
    schedule.every(2).minutes.do(check)

    while True:
        schedule.run_pending()
        time.sleep(1)