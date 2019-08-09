from flask import render_template
from app import app
from MarkovModel import MarkovModel
from flask import request
import lyricsgenius, json

@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html', title='Home')

@app.route('/lyrics', methods=['POST'])
def lyrics():

	# Uncomment for RapGenius API
	get artist
	artist = request.form['artist']
	genius = lyricsgenius.Genius("Y_izF-J78Qf8qn1gqLTWyKj95b_sJuQwj7f4smPQq7zB1qnMp3mJ71jpB2tBu0Bb")
	artist = genius.search_artist(artist, max_songs=2, sort="title")

	# join lyrics into one document
	total_lyrics = []
	for song in artist.songs:
		total_lyrics.append(song.lyrics)
	total_lyrics = "".join(s for s in total_lyrics)

	# # test on bible
	# f = open('rapgod.txt',"r")
	# total_lyrics = f.read()

	model = MarkovModel()
	lyrics = model.textGenerator(total_lyrics, 5, 400)
	lyrics = model.stringLyrics(lyrics)

	# add line breaks
	lyrics = lyrics.split('\n')
	# lyrics = json.dump()
	# print(lyrics)

	return render_template('lyrics.html', lyrics=lyrics)