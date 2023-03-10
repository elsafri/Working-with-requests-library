import requests
from datetime import datetime, timedelta
import time


def get_questions(url):
    fromdate = datetime.now() + timedelta(days=-2)
    fromdate_unix = int(time.mktime(fromdate.timetuple()))
    todate_unix = int(time.mktime(datetime.now().timetuple()))
    params = {'fromdate': fromdate_unix, 'todate': todate_unix}
    content = requests.get(url, params=params).json()
    counter = 0
    for value in content['items']:
        print(value['title'])
        counter += 1


if __name__ == '__main__':
    link = 'https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&tagged=python&site=stackoverflow'
    get_questions(link)
