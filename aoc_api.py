import requests
import local


def fetch_input(day):
    url = f'https://adventofcode.com/2024/day/{day}/input'
    headers = {
        'cookie': 'session={0}'.format(local.session)
    }
    input_values = requests.get(url, headers=headers).text.splitlines()

    return input_values
