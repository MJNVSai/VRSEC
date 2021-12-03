'''
GOOGLE NEWS
'''

from GoogleNews import GoogleNews

googlenews = GoogleNews()

googlenews = GoogleNews(period = '7d')

googlenews.search('INDIA')

result = googlenews.result()
print("\n\n answer: \n\n",result)

for x in result:
    print("-"*50)
    print()

    print("Title--",x['title'])
    print("Date/Time--",x['date'])
    print("Description--",x['desc'])
    print("Link--",x['link'])
    print()