


# go to https://serpapi.com/manage-api-key  to register for an api key
# go to https://platform.openai.com/account/api-keys to register for an api key
# go to https://platform.openai.com/docs/api-reference/completions/create for documentations
# go to https://serpapi.com/google-trends-related-queries for documentations
# pip install google-search-results
# pip install pandas

import pandas as pd
from serpapi import GoogleSearch
import openai
from dotenv import load_dotenv
import os


# load .env variables
load_dotenv()

chatgpt_api_key = os.environ.get('CHATGPT_API_KEY')
chatgpt_organization = os.environ.get('CHATGPT_ORGANIZATION')
if chatgpt_api_key is None or chatgpt_organization is None:
  print('CHATGPT keys and/or organization is not set in .env file')

serpapi_api_key = os.environ.get('SERPAPI_API_KEY')
if serpapi_api_key is None:
  print('SERPAPI key is not set in .env file')


params = {
  "engine": "google_trends",
  "cat":0,
  "date":"now 1-d",
  "geo":"US",
  "q": "ai",
  "data_type": "RELATED_QUERIES",
  "api_key": serpapi_api_key
}

search = GoogleSearch(params)
results = search.get_dict()

related_queries = results["related_queries"]
rising = related_queries["rising"]

df=pd.DataFrame(rising)
df = df.reset_index()  # make sure indexes pair with number of rows

for index, row in df.iterrows():
    print(row['query'], row['value'])
