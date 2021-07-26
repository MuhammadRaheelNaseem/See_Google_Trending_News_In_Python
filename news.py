# pip3 install googlenews

from GoogleNews import GoogleNews

googlenews = GoogleNews() # Initialize method
googlenews = GoogleNews(period='7d',lang='urdu')
googlenews.search("pkr") # here you can enter your country code i.e USE,CAN,PKR,IND,SA 
result = googlenews.result() 

for x in result:
    print("-"*90)
    print("Title------>",x['title'])
    print("Date/Time------>",x['date'])
    print('Description------>',x['desc'])
    print('Link------>',x['link'])
