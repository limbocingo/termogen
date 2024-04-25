import random
import string

import requests

from source.styles import Color, log

URL = 'https://discord.com/api/v8/entitlements/gift-codes/'


def generate(amount: int) -> list[str]:
    return [''.join(random.choices(
        string.ascii_letters + string.digits, k=16)) for _ in range(32)]


def request(token: str) -> None:
    request = requests.get(url=URL + token)

    if request.status_code != 200:
        log(f'{Color.dark_gray}[{Color.corn_silk} {token} {
            Color.dark_gray}{Color.reset}] Invalid', Color.indian_red, ' × ')

    if request.status_code == 200:
        log(f'{Color.dark_gray}[{Color.corn_silk} {token} {
            Color.dark_gray}{Color.reset}] Invalid', Color.light_green, ' ✓ ')


def check(tokens: list[str] = None) -> dict[str, bool]:
    for token in tokens:
        request(token)
