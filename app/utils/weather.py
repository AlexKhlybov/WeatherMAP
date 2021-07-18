import json

import aiohttp

from app.config import WEATHER_LANG, YANDEX_KEY
from app.models.towns import Town


async def get_weater(db, items):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        head = {"X-Yandex-API-Key": YANDEX_KEY}
        for item in items:
            url = f'https://api.weather.yandex.ru/v2/forecast?lat={item["latitude"]}&lon={item["longitude"]}&[lang={WEATHER_LANG}]'
            async with session.get(url=url, headers=head) as r:
                town = db.query(Town).filter(Town.id == item["id"]).first()
                town.current_weather = (await r.json())["fact"]["temp"]
                town.forecast_weather = helper_forest((await r.json())["forecasts"])
                db.add(town)
                db.commit()


def helper_forest(items):
    forecast = {}
    for item in items:
        forecast[item["date"]] = item["parts"]["day"]["temp_avg"]
    return json.dumps(forecast)
