import requests
import json
from main import logger


# Задача 1 Кто самый умный супергерой


def supaheroes_list():
    url = requests.get(
        "https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json"
    )
    superheroes_list = json.loads(url.text)

    supaheroes = {}
    for i in superheroes_list:
        supa_name = i.get("name")
        supa_stats = i.get("powerstats")
        supaheroes.update({supa_name: supa_stats.get("intelligence")})

    return supaheroes


@logger
def smart_hero(list_0):
    smartest_hero = []
    supahero = ["Hulk", "Captain America", "Thanos"]
    supaheroes = list_0
    for x in supaheroes.items():
        name, intellect = x
        if name in supahero:
            smartest_hero.append(list(x))
    smartest_hero.sort(reverse=True)

    return f"Вывод задачи №1:\nСамый умный герой из троицы, это - {smartest_hero[0][0]}"
