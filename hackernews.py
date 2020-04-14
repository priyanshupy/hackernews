import requests
from bs4 import BeautifulSoup

import pprint
res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
result=res.text + res2.text
soup = BeautifulSoup(result,'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')
def sort_stories_by_votes(hlist):
    return sorted(hlist, key=lambda k: k['points'], reverse=True)


def create_custom_hn(links,subtext):
    hn = []

    for idx,item in enumerate(links): # enumerate is being used to provide index for links as they don't have
        title = links[idx].getText()   # getText() is used to get text between html elements eg:<a>this</a>
        link = links[idx].get('href',None)
        vote = subtext[idx].select('.score')

        if(len(vote)):
            points = int(vote[0].getText().replace(' points', ''))
            if(points>100):
                hn.append({"title":title, "link": link, "points":points})

    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(links, subtext))











