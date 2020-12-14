import urllib.request,json
from .models import Quote

def get_quote():
    '''
    Function that gets the json responce to our url request
    '''
    get_quotes_url = 'http://quotes.stormconsultancy.co.uk/random.json'

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        id = get_quotes_response.get('id')
        author = get_quotes_response.get('author')
        quote = get_quotes_response.get('quote')
        permalink = get_quotes_response.get('permalink')

        quote_result = [id,author,quote, permalink]
    return quote_result