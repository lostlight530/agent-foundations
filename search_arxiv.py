import urllib.request
import urllib.parse
import json
import xml.etree.ElementTree as ET

url = "http://export.arxiv.org/api/query?search_query=all:%22multi-agent%22+AND+all:%22convergence%22+AND+all:%22tool%22&start=0&max_results=5&sortBy=submittedDate&sortOrder=descending"
req = urllib.request.urlopen(url)
response = req.read().decode('utf-8')
root = ET.fromstring(response)
ns = {'atom': 'http://www.w3.org/2005/Atom'}
for entry in root.findall('atom:entry', ns):
    title = entry.find('atom:title', ns).text.replace('\n', ' ')
    id = entry.find('atom:id', ns).text
    published = entry.find('atom:published', ns).text
    print(f"{id} - {published} - {title}")
