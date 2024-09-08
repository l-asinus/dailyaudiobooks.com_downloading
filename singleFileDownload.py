#imports
import requests
import re
import os

#user enter variables
url = 'https://dailyaudiobooks.co/j-r-r-tolkien-the-lord-of-the-rings-audiobook/2/'
fileNumber = 8

#get content
r = requests.get(url)
print (r.content)
htmlContent = r.content.decode('utf-8')

#chapter formula
matchNumber = (fileNumber-1)*3

#find the file
match = re.findall(r'https?://[^\s"]+\.mp3', htmlContent)
if len(match) >= 2:
    downloadURL = match[matchNumber]
else:
    print('not found')

#download
full_path = os.path.join("/Users/levtysh/Downloads", f'audio_file_{fileNumber}.mp3')
#headers, if the server wants them
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
response = requests.get(downloadURL, headers=headers, stream=True)
if response.status_code == 200:
    #save to the location
    with open(full_path, 'wb') as file:
        file.write(response.content)
    print("File downloaded successfully")
else:
    print(f"Failed to download file. Status code: {response.status_code}")