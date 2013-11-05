# coding: utf-8
import requests
import json


madmimi_apikey = ''
madmimi_email = ''


def carrega(url, method, body={}, HEADERS_APP=None):

    url = 'http://api.madmimi.com/%s&username=%s&api_key=%s' % (url, madmimi_email, madmimi_apikey)

    if method == "get":
        data = requests.get(
            url, data=json.dumps(body), headers=HEADERS_APP
        )
    else:
        data = requests.post(
            url, data=json.dumps(body), headers=HEADERS_APP
        )

    try:
        data = json.loads(data.text)
        return data
    except:
        return False

def nova_lista(nome):
    data = carrega('audience_lists/?name=%s' % nome, 'POST')
    if data:
        return data['success']
    return False

def alterar_lista(lista_antiga, lista_nova):
    data = carrega('audience_lists/%s/rename?name=%s' % (lista_antiga, lista_nova), 'POST')
    if data:
        return data['success']
    return False

def remover_lista(nome):
    data = carrega('audience_lists/%s?_method=delete' % nome, 'POST', { '_method': 'delete' })
    if data:
        return data['success']
    return False

def novo_email(lista, email):
    data = carrega('audience_lists/%s/add?email=%s' % (lista, email), 'POST')
    if data:
        return data['success']
    return False

def remover_email(lista, email):
    data = carrega('audience_lists/%s/remove?email=%s' % (lista, email), 'POST')
    if data:
        return data['success']
    return False

def remover_email_todas_listas(lista, email):
    data = carrega('audience_lists/remove_all?email=%s' % email, 'POST')
    if data:
        return data['success']
    return False

if __name__ == "__main__":
    nova_lista('newsletter')
    novo_email('newsletter', 'email1@email.com')
    novo_email('newsletter', 'email2@email.com')
    novo_email('newsletter', 'email3@email.com')
    nova_lista('newsletter2')
    novo_email('newsletter2', 'email1@email.com')
    novo_email('newsletter2', 'email2@email.com')
    novo_email('newsletter2', 'email3@email.com')

    remover_email('newsletter', 'email2@email.com')
    remover_email_todas_listas('newsletter', 'email1@email.com')

    alterar_lista('newsletter2', 'newsletter10')
    remover_lista('newsletter10')

    nova_lista('FDP')
    # remover_lista('FDP')
