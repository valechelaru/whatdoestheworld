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
    dom = getXML(nytimes_url)
    saveToFile('test.xml', dom.toprettyxml())

    handleXML(dom)

    items = dom.getElementsByTagName('item')
    for item in items:
        title = item.getElementsByTagName('title')[0]
        print(title.firstChild.data)
        description = item.getElementsByTagName('description')[0]
        try:
            print(description.firstChild.data)
        except:
            print('NO DESCRIPTION!')
        categorys = item.getElementsByTagName('category')
        for category in categorys:
            print(category.firstChild.data)