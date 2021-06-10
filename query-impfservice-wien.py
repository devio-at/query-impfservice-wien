#!/usr/bin/env python3
import requests 
from pyquery import PyQuery 

response = requests.get('https://impfservice.wien/corona/')

pq = PyQuery(response.text)
print(pq('#termin-buchen .page strong').text())
