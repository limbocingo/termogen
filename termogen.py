from threading import Thread

from source.discord import check, generate
from source.styles import Color


def main():
    print(Color.red +
          r'''

                   _____                            ___
                  /__   \___ _ __ _ __ ___   ___   / _ \___ _ __
                    / /\/ _ \ '__| '_ ` _ \ / _ \ / /_\/ _ \ '_ \
                   / / |  __/ |  | | | | | | (_) / /_\\  __/ | | |
                   \/   \___|_|  |_| |_| |_|\___/\____/\___|_| |_|

                                  Made by: MrCingo
                               discord.gg/termostore


''',)
    text = f'{Color.dark_gray}[{Color.light_green} ⁕ {Color.dark_gray}] {
        Color.cadet_blue}Amount to generate: {Color.reset}'
    amount = int(input(text))

    if amount > 100:
        amount = int(amount/4)
        for _ in range(0, 4):
            Thread(target=check, kwargs={'tokens': generate(amount)}).start()
    else:
        Thread(target=check, kwargs={'tokens': generate(amount)}).start()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
