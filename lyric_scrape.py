#%%
# Import packages

import os
import pandas as pd
from pyquery import PyQuery as pq
import requests
import numpy as np

#%%

# Step 1: Scraping the Lyrics

# define the artist
artist_i = 'Drake' # can expand to other or multiple artists
artist_i = artist_i.lower()
artist_i = artist_i.replace(" ","-")

# visit the artist's Metro Lyrics page
response = requests.get('http://www.metrolyrics.com/' + artist_i + '-lyrics.html')

# separate the different types of content
doc = pq(response.content)

# find the titles in the content
titles = doc('.title')

# create empty lists to store songs, artists, and lyrics
song_ = []
song_artist = []
song_lyrics = []

# visit each title, then stores song, artist, and lyrics
for title in titles:
  # visit each title
  response_title = requests.get(title.attrib['href'])
  # separate the content
  doc2 = pq(response_title.content)


  # find song name and lyrics, then reformat
  name_full = doc2('h1')
  song_full = str(name_full.text())
  song = song_full.lower()
  song = song[:-7]
  song = song.replace(" ","-")
  song = song.split("---")
  
  # filter out artists that are not requested artist
  artist = song[0]
  if artist == artist_i:
    name = song[1]
    song_.append(name)

    # append artist to list
    artist = song[0]
    song_artist.append(artist)

    # find the song lyrics
    verse = doc2('.verse')
    lyrics = verse.text()
    lyrics = lyrics.replace("\n","|-|")

    # append the lyrics to list
    song_lyrics.append(lyrics)
print('All done!')

#VALIDATION
#print(song_lyrics[0:2])
#print(song_[0:2])
#print(song_artist[0:2])

#%%

# Step 2: combine songs, artist, and lyrics lists into Data Frame

# change each list in step 1 to a numpy array
song = np.asarray(song_)
artist = np.asarray(song_artist)
lyrics = np.asarray(song_lyrics)

# create a data frame containing the three numpy arrays
lyrics_csv = pd.DataFrame(np.hstack((song.reshape(-1, 1), artist.reshape(-1, 1), lyrics.reshape(-1, 1))), columns=['song', 'artist', 'lyrics'])


#%%

# Step 3: export the lyrics to csv
# **Please chenge the directory to your own when running

# define directory to export csv file to
os.chdir(r'C:/Users/sjg27/OneDrive/Documents/GitHub/NLP-Project-Lyric-Generation')

# export csv file
lyrics_csv.to_csv('scraped_lyrics.csv', index=False)

#%%
