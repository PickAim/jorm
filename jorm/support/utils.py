import json
from typing import TypeVar, Iterable

import aiohttp
import requests

T = TypeVar("T")


def intersection(it_a: Iterable[T], it_b: Iterable[T]) -> list[T]:
    return [element for element in it_a if element in it_b]


async def get_async_request_json(url: str, session: aiohttp.ClientSession):
    async with session.get(url=url) as request:
        if request.status == 200:
            data = await request.read()
            if len(data) > 0:
                return json.loads(data)
        return ""


def get_request_json(url: str, session: requests.Session, headers=None):
    if headers is None:
        headers = {}
    with session.get(url, headers=headers) as request:
        if request.status_code == 200:
            request.raise_for_status()
            return request.json()
        return ""
