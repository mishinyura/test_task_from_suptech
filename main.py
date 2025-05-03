import json

def parse(response: dict) -> list[str]:
    logins = []
    try:
        for obj in response.get('people').get('result'):
            logins.append(obj['login'])
    except AttributeError as ex:
        print(f'Bad Response. Message: {ex}')

    return logins


with open('data2.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
    parse(data)