import requests
import local


def fetch_input(day: int, test: bool = False):
    text = read_test_data(day) if test else fetch_data(day)
    input_values = text.splitlines()
    return input_values


def read_test_data(day: int) -> str:
    return open(f'./test_data/day{day}.txt').read()



def fetch_data(day: int) -> str:
    url = f'https://adventofcode.com/2024/day/{day}/input'
    headers = {
        'cookie': 'session={0}'.format(local.session)
    }
    return requests.get(url, headers=headers).text