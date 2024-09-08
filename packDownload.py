#imports
import requests
import re
import os

# user enter variables
#url = 'https://dailyaudiobooks.co/j-r-r-tolkien-the-lord-of-the-rings-audiobook/2/'
#fileName = 'the lord of the rings'
url = input('Enter the url of the file to download: ')
fileName = input('Enter the name of the file to download: ')

# get content
r = requests.get(url)
print (r.content)
htmlContent = r.content.decode('utf-8')

match = re.findall(r'https?://[^\s"]+\.mp3', htmlContent)  #find all files
numberOfFilesOnThePage = len(match)  # calculate the number of all files
print(f'files found:{numberOfFilesOnThePage/3}')  # /3 because in the HTML file on the dailyaudiobooks.co there are 3 same links in a row
URLnumber = 0
fileNumber = 0
os.makedirs(f"/Users/levtysh/Downloads/{fileName}")  # creates a folder with the downloaded files
while numberOfFilesOnThePage > URLnumber:
    fileNumber = fileNumber + 1  # writes the number of a chapter into the filename
    downloadURL = match[URLnumber]

    # download
    path = os.path.join(f"/Users/levtysh/Downloads/{fileName}", f'{fileName} {fileNumber}.mp3')
    response = requests.get(downloadURL)
    if response.status_code == 200:
        # save to the location
        with open(path, 'wb') as file:  # wb = write binary
            file.write(response.content)
        print("File downloaded successfully")
    else:
        print(f"Failed to download file. Status code: {response.status_code}")
    URLnumber = URLnumber+3
