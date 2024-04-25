from threading import Thread
from psutil import cpu_count

from source.discord import check
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
    Thread(target=check).start()
    Thread(target=check).start()
    Thread(target=check).start()
    Thread(target=check).start()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit(0)
