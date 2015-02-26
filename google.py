import requests
from bs4 import BeautifulSoup


def google_calc_addition(num1, num2):

    problem = '{0}+{1}'.format(num1, num2)

    response = requests.get(
        'http://google.com/search', params={'q': problem})

    if response.status_code != 200:
        print response.headers
        print response.text
        raise ValueError("google sucks")

    google_soup = BeautifulSoup(response.content)
    search_results = google_soup.select('h2.r')
    return search_results[0].text


if __name__ == '__main__':
    print google_calc_addition(1, 1)
