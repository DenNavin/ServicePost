# ========================================================================================================
# Создать сервис, который будет постить текстовое сообщение минимум в две социальные сети:
# ●     Сервис получает на вход текст поста (не более 140 символов) с помощью встроенной функции input()
# ●     Формирует запросы на API социальной сети ВКонтакте.
# ●     Сервис печатает в терминал сообщение об успешности публикации (получилось или нет).
# ●     Код сервиса выложен на github

# Критерии оценивания:
# -       сервис дает запостить текст из не более, чем 140 символов
# -       сервис авторизовывает пользователя в минимум двух соцсетях
# -       сервис отправляет пост на стену/другое публичное место соцсети
# -       сервис оповещает, что все прошло успешно или произошла ошибка
# ========================================================================================================
import requests
import sys


def vk_connection():
    """Connection VK"""
    url_vk = 'https://api.vk.com/method/wall.post'
    access_token = '______________' # Your token
    version_api_vk = 5.92

    try:
        my_request = requests.post(url_vk,
                                   params={
                                       'access_token': access_token,
                                       'message': message,
                                       'v': version_api_vk,
                                   })
    except:
        print("Error")

    else:
        sys.exit()
# ================================

def fb_connection():
    """Connection FB"""
    url_fb = 'https://graph.facebook.com/me/feed/?message='
    access_token2 = '______________' # Your token
    message.replace('', '+')

    try:
        my_request2 = requests.post(url_fb + message + "&access_token=" + access_token2)

    except:
        print('Error')

    else:
        sys.exit()
# =================================

while True:
    message = input('Введите сообщение не более, чем 140 символов: ')
    if len(message) > 140:
        message = ''
    else:
        choose_soc_network = input('Выберите социальную сеть, в которой хотите разместить пост:\n1 - VK\n2 - Facebook\n3 - Exit\n')
        if choose_soc_network == '1':
            vk_connection()
        elif choose_soc_network == '2':
            fb_connection()
        elif choose_soc_network == '3':
            sys.exit()
        else:
            continue


