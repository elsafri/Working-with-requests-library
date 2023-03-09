import requests


def get_questions(url):
    content = requests.get(url).json()
    counter = 0
    for value in content['items']:
        print(value['title'])
        counter += 1


if __name__ == '__main__':
    link = 'https://api.stackexchange.com/2.3/questions?fromdate=1678147200&todate=1678320000' \
               '&order=desc&sort=activity&tagged=python&site=stackoverflow'
    get_questions(link)
