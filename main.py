import urllib3
import xml.dom.minidom

def getXML(url):
    '''Function that returns the XML from a specific url

    Parameters
    ----------
    url : string
        The direct url link to a .xml file

    Returns
    -------
    xml.dom.minidom.Document
        Returns the dom Document for the url
    '''
    http = urllib3.PoolManager()
    request = http.request('GET', url)
    print(request.status)
    dom = xml.dom.minidom.parseString(request.data)
    return dom

def saveToFile(filename, data):
    '''Function to save data to a file

    Parameters
    ----------
    filename : string
        The filename that will be used to save the data
    data : string
        The data that will be saved into the file
    '''    
    f = open(filename, 'w')
    f.write(data)
    f.close()

def handleXML(dom):
    handleXMLTitle(dom.getElementsByTagName('title')[0])
    pubDate = dom.getElementsByTagName('pubDate')[0]
    print(pubDate.firstChild.data)

def handleXMLTitle(titel):
    print(getText(titel.childNodes))

def getText(nodelist):
    rc = []
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            rc.append(node.data)
    return ''.join(rc)

if __name__ == '__main__':
    # XML Location of the NYTimes Home Page
    nytimes_url = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
    dom_ny = getXML(nytimes_url)
    saveToFile('nytimes.xml', dom_ny.toprettyxml())

    handleXML(dom_ny)

    items = dom_ny.getElementsByTagName('item')
    for item in items:
        title = item.getElementsByTagName('title')[0]
        print(title.firstChild.data)
        description = item.getElementsByTagName('description')[0]
        try:
            print(description.firstChild.data)
        except:
            print('NO DESCRIPTION!')
        categories = item.getElementsByTagName('category')
        for category in categories:
            print(category.firstChild.data)

    bbcnews_url = 'http://feeds.bbci.co.uk/news/world/rss.xml'
    dom_bbc = getXML(bbcnews_url)
    saveToFile('bbcworld.xml', dom_bbc.toprettyxml())

    redditnews_url = 'https://www.reddit.com/r/worldnews/.rss'
    dom_reddit = getXML(redditnews_url)
    saveToFile('redditWorldNews.xml', dom_reddit.toprettyxml())

    buzzfeedworld_url = 'https://www.buzzfeed.com/world.xml'
    dom_buzzfeed = getXML(buzzfeedworld_url)
    saveToFile('buzzfeednews.xml', dom_buzzfeed.toprettyxml())

    aljazeera_url = 'https://www.aljazeera.com/xml/rss/all.xml'
    dom_aljazeera = getXML(aljazeera_url)
    saveToFile('aljazeera.xml', dom_aljazeera.toprettyxml())

    yahooworld_url = 'https://www.yahoo.com/news/rss/world'
    dom_yahoo = getXML(yahooworld_url)
    saveToFile('yahoowold.xml', dom_yahoo.toprettyxml())