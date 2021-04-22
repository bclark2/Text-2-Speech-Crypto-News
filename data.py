#pip install mpyg321
import requests
import json
import re
import os
from gtts import gTTS
# Replace the tickers argument with the symbol of the Crypto Currency you want data for
# For example Bitcoin = BTC, Stellar = XLM, Iota = MIOTA
response = requests.get("https://cryptonews-api.com/api/v1?tickers=BTC&items=50&token"
                        "=YOUR_CRYPTONEWS-API.COM_API_KEY_HERE")

# Create branch logic here to check if the status code is 200
# if not exit and produce an error message
# Just printing the status for now

print(response.status_code)
data_dict = response.json()
my_list = data_dict.get('data')
# Empty lists for you to use for the various sentiments available 
list_of_positive_stories = []
list_of_negative_stories = []
list_of_neutral_stories = []
list_of_string_values_positive = []

# you can branch off of these counters
# if you want to filter by the counter of stories
counter_positive = 0
counter_negative = 0
counter_neutral = 0

for item in my_list:
    if item.get('sentiment') == 'Positive':
        counter_positive += 1
        list_of_positive_stories.append(item.get('title'))

print('Number of positive stories :', counter_positive)

for i in range(len(list_of_positive_stories)):
    list_of_string_values_positive.append(list_of_positive_stories[i])

# Wrangle the data
# Combine list elements into a single list
# Remove double quotes from the single list element
# So that it can be cleanly injected into the text to speech function
numList = list_of_positive_stories
separator = ', '
my_variable_raw = ('"' + separator.join(numList) + '"')
my_variable_clean = re.sub('"', '', my_variable_raw)

# This will show you the clean data output
# You can visually inspect it to make sure it is correct
print(my_variable_clean)

# The text that you want to convert to audio
mytext = '"' + my_variable_clean + '"'

# Language in which you want to convert
language = 'en'
 
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
 
# Saving the converted audio in a mp3 file named 
myobj.save("Path/To/Create/MP3/File/btc_positive_news.mp3")
