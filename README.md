# SpanishDict-API
Automate Spanish-English translation using unoffical API for SpanishDict.com

## Using the API
First import the module and create an instance of the SpanishDictClient.
```
from SpanishDict-API.SpanishDictClient import SpanishDictClient

sd_client = SpanishDictClient()
```
To translate text use the translate() method to translate to and from English and Spanish.
```
# english to spanish
out = sd_client.translate('this is in english')  # translates to 'Esto es en ingles'

# spanish to english
out = sd_client.translate('esto es en ingles')  # translates to 'This is in English'
```
