import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import numpy as np
import warnings

warnings.filterwarnings('ignore')

data = pd.read_csv('spotify_songs.csv')

# Histogram
pop_score = data['track_popularity']
plt.hist(pop_score, bins=25, histtype='bar', edgecolor='black')
plt.title("Count of Song Popularity Scores")
plt.xlabel("Popularity Score")
plt.ylabel("Count")
plt.savefig('histo.png')

# Bar Graph
colors = ['red', 'blue', 'green', 'orange', 'yellow', 'purple']
ax = data['playlist_genre'].value_counts().plot(kind='barh', color=colors)
ax.set_ylabel("Genres")
ax.set_xlabel("Number of Songs")
ax.set_title("Number of Songs In Each Genre")
plt.savefig('bar.png')

# Line Plot
pop_df = data.loc[:, ['track_popularity', 'track_album_release_date', 'playlist_genre']]
pop_df["Year"] = pop_df['track_album_release_date'].str.split('-').str[0].astype(int)
pop_df = pop_df.loc[:, ['track_popularity', 'Year', 'playlist_genre']]

rock = pop_df.loc[pop_df['playlist_genre'] == 'rock']
rock_count = rock.groupby(['Year'])['track_popularity'].mean()

rap = pop_df[(pop_df['playlist_genre'] == 'rap')]
rap_count = rap.groupby(['Year'])['track_popularity'].mean()

country = pop_df[(pop_df['playlist_genre'] == 'country')]
country_count = country.groupby(['Year'])['track_popularity'].mean()

latin = pop_df[(pop_df['playlist_genre'] == 'latin')]
latin_count = latin.groupby(['Year'])['track_popularity'].mean()

pop = pop_df[(pop_df['playlist_genre'] == 'pop')]
pop_count = pop.groupby(['Year'])['track_popularity'].mean()

edm = pop_df[(pop_df['playlist_genre'] == 'edm')]
edm_count = edm.groupby(['Year'])['track_popularity'].mean()

fig = plt.figure(figsize=(15, 5))
plt.plot(rock_count, label='Rock', linewidth=3)
plt.plot(rap_count, label='Rap', linewidth=3)
plt.plot(country_count, label='Country', linewidth=3)
plt.plot(latin_count, label='Latin', linewidth=3)
plt.plot(pop_count, label='Pop', linewidth=3)
plt.plot(edm_count, label='EDM', linewidth=3)
plt.ylabel("Popularity")
plt.xlabel("Year")
plt.title("Popularity of Genre by Year")
plt.legend(loc='lower right')
plt.savefig('line.png')

# Scatterplot
dance = data['danceability']
tempo = data['tempo']
sizes = 100 * np.random.rand(300)
colors = np.random.rand(300)

fig = plt.figure(figsize=(10, 5))
plt.scatter(tempo[0:300], dance[0:300], s=sizes, c=colors)
plt.ylabel("Danceability")
plt.xlabel("Tempo")
plt.title("Impact of Tempo on Danceability")
plt.savefig('scatter.png')

