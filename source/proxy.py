from source.styles import log, Color


def parse(file: str):
    data = {'https': [], 'http': []}
    with open(file, encoding='utf8', mode='r') as fr:
        for proxy in fr.readlines():
            split = proxy.replace('"', '').split(',')
            if len(split) <= 1:
                log('Bad proxy format, leaving', Color.red, ' ¡ ')
                exit(1)

            ip = split[0]
            port = split[7]
            protocol = split[8]

            if (protocol == 'http'):
                http_list = data['http']
                http_list.append(f'http://{ip}:{port}')

                data['http'] = http_list
    return data
