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

if __name__ == '__main__':
    # XML Location of the NYTimes Home Page
    url = 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
    dom = getXML(url)
    saveToFile('test.xml', dom.toprettyxml())