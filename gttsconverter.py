from gtts import gTTS
tts = gTTS(
	text=
	"""
Dozens of girls would storm up
I had to lock my door
Somehow I couldn't warm up
To one before
What was it that controlled me
What kept my love life lean
My intuition told me
You'd come on the scene
Lady listen to the rhythm of my heartbeat
And you'll get just what I mean
Embrace me, my sweet embraceable you
Embrace me, you irreplaceable you
Just one look at you my heart grew tipsy in me
You and you alone bring out the gypsy in me
I love all the many charms about you
Above all I want my arms about
Don't be a naughty baby,
Come to papa come to papa do
My sweet embraceable you

	""",
	lang='en',
	

)
tts.save("embraceableyou.mp3")
