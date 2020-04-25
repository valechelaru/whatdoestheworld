import urllib3
import xml.dom.minidom



if __name__ == '__main__':
    # XML Location of the NYTimes Home Page
    url = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
    http = urllib3.PoolManager()
    request = http.request('GET', url)
    print(request.status)

    dom = xml.dom.minidom.parseString(request.data)
    category = dom.getElementsByTagName('category')