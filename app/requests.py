import urllib.request,json
from .models import Quote

def get_quote(): 
    with urllib.request.urlopen('http://quotes.stormconsultancy.co.uk/random.json') as url:
        quotesResponse = url.read()
        quote_get_response = json.loads(quotesResponse)
        
        results = []
        id = quote_get_response.get('id')
        author = quote_get_response.get('author')
        quote = quote_get_response.get('quote')

        quote = Quote(id,author,quote)
        results.append(quote)
        return results 