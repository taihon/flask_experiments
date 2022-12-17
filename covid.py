import random, requests

def get_covid_info():
  api_uri = 'https://api.covid19api.com/summary'
  data = requests.get(api_uri)
  get_json = data.json()
  covid = get_json.get('Countries')
  countries = [x for x in covid]
  countrydata = random.choice(countries)
  valuable_captions=["Country","NewConfirmed","TotalConfirmed","TotalRecovered"]
  return countrydata