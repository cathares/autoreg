import json
from json import JSONDecodeError
from time import sleep

import requests as requests

TOKEN = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MjcyMTkyMzQsImlhdCI6MTY5NTY4MzIzNCwicmF5IjoiYmMzNjY0MWIyM2E0MmU3MTFkZGFhNDM5ZDMyNWQ4OTkiLCJzdWIiOjE4NzY5NTV9.I7zefjvgDnGE7BNJ1Pi_YCyx8DXGXNSdyBbQ13Sm5p69cexcZKRZgiPQU69rpPNBr9CdU0xRj0wgOQeHVyIvVwT6wNntk_674pOrR61bWez9QKT2DWJ1YEj0cnjWssUSV_WEVeBOuqJ5ZTpOwULfznYlE6ON10kUYsa_cryWB_H2gjArgL_MEo7DobAjsQ7-Fh5EkAZ8vx5Xtsgpg-6Tqe2lg4Ny8dyVAAPHxVYFyeUp1upt1AIdaUP4KMTp693aZUtPBqTyQX991_SyuIChnF3YF3_3VnF-qx6hX1De5FStG6w760_5DmlSpOucm0AeoH3Zx8EuFMLyEMXjwzA2uQ"

headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {TOKEN}'
}
data = requests.get("https://5sim.biz/v1/user/profile", headers=headers)
print(data.content)

"""
def getPurchaseData():
    pricesResponse = requests.get("https://5sim.biz/v1/guest/prices?product=tiktok")
    priceList = json.loads(pricesResponse.content)

    validNumbers = dict.fromkeys(['Country', 'Operator'])
    for country in priceList['tiktok']:
        for operator in priceList['tiktok'][country]:
            if priceList['tiktok'][country][operator]['cost'] == 1 and priceList['tiktok'][country][operator][
                'count'] > 1:
                validNumbers['Country'] = country
                validNumbers['Operator'] = operator
                print(validNumbers)
                break
            if validNumbers['Country'] is not None:
                break
        if validNumbers['Country'] is not None:
            break
    return validNumbers
"""

def purchaseNumber(token, validNumbers):
    country = validNumbers['Country']
    operator = validNumbers['Operator']
    product = 'tiktok'

    headers = {
        'Authorization': 'Bearer ' + token,
        'Accept': 'application/json',
    }
    response = requests.get(
        'https://5sim.biz/v1/user/buy/activation/' + country + '/' + operator + '/' + product,
        headers=headers
    )
    try:
        numberInfo = json.loads(response.content)
        result = dict.fromkeys(['number', 'country', 'id'])
        result['number'] = numberInfo['number']
        result['country'] = numberInfo['country']
        result['id'] = numberInfo['id']
        return result
    except JSONDecodeError:
        print(f'Invalid server response when trying to buy number. Json code is {response}')


def getSMS(token, id):
    headers = {
        'Authorization': 'Bearer ' + token,
        'Accept': 'application/json',
    }
    response = requests.get('https://5sim.biz/v1/user/check/' + id, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.content)
        return data["sms"]["code"]
        """"
        while data["sms"]["code"] is None:
            print("Код пока не пришел")
            sleep(30)
            response = requests.get('https://5sim.biz/v1/user/check/' + id, headers=headers)
            data = json.loads(response.content)
            """
    else:
        print(f"Error during receiving sms. JSON code is {response.status_code}")



#x = purchaseNumber(TOKEN, getPurchaseData())
