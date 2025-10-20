import requests, sys, json
from ansi.colour import fg

def ip_api(link: str) -> dict[str: str]:
    base = 'http://ip-api.com/json/'
    r = requests.get(base + link)
    return r.json()

if __name__ =='__main__':
    result = ip_api(sys.argv[-1])
    print(f'Addres: {fg.green(result['country'])} {result['regionName']} {result['city']}')
    print(f'Coordinates: {fg.yellow(str(result['lat']))}, {fg.yellow(str(result['lon']))} (https://yandex.ru/maps/?ll={result['lon']}00%2C{result['lat']}00&z=16)')
    print(f'Organization: {result['isp']}, {fg.cyan(result['org'])}, {result['as']}')
