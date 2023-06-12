
#web scraping library request & parsing
#to give us access to the session object which we can use to create our requests
from requests_html import HTMLSession

#used to send HTTP requests and handle the response
s = HTMLSession()

#assign the string 'kuala lumpur' to the variable 'query', which represents the search query for weather information
query = 'kuala lumpur'
#constructs the URL for the Google search query by combining the base URL with the value of 'query'
url = f'https://www.google.com/search?q=weather+{query}'

#This line sends a GET request to the specified URL using the get method of the HTMLSession instance s. It includes a User-Agent header to mimic a web browser and avoid potential blocking or redirection.
r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'})


temp = r.html.find('span#wob_tm', first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
description = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

#prints the values of query, temp, unit, and description, providing information about the weather in Kuala Lumpur
print(query, temp, unit, description)
