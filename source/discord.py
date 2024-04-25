import random
import string

import requests

from source.styles import Color, log

URL = 'https://discord.com/api/v8/entitlements/gift-codes/'


def request(token: str) -> None:
    request = requests.get(url=URL + token)

    if request.status_code != 200:
        log(f'{Color.dark_gray}[{Color.corn_silk} {token} {
            Color.dark_gray}{Color.reset}] Invalid', Color.indian_red, ' × ')

    if request.status_code == 200:
        log(f'{Color.dark_gray}[{Color.corn_silk} {token} {
            Color.dark_gray}{Color.reset}] Invalid', Color.light_green, ' ✓ ')


def check() -> dict[str, bool]:
    while True:
        request(''.join(random.choices(
            string.ascii_letters + string.digits, k=16)))
