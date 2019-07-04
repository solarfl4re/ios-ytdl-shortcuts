# coding: utf-8
from __future__ import unicode_literals
import webbrowser
import ui
from os import remove
from os.path import splitext
from zipfile import ZipFile
import youtube_dl
import clipboard
import sys
from base64 import b64encode

files = []

def main(argv):
	if len(argv) > 1:
		url = argv[1]
		mode = argv[2]
		
		# Should we download videos or just audio?
		if mode == 'audio':
			format = 'bestaudio[ext!*=webm]/best'
		else: # video
			format = 'best'
			
		# https://youtu.be/f0uHpasSpq0
		if url:
			ydl_opts = {
				'progress_hooks': [postdownload],
				# 'writethumbnail': True,
				'format': format,
				'ignoreerrors': True
			}
			
			with youtube_dl.YoutubeDL(ydl_opts) as ydl:
					ydl.download([url])

			# Make zip file with video(s)
			with ZipFile('yt.zip', 'x') as z:
				for file in files:
					z.write(file)
					remove(file)

			# Save ZIP file to clipboard
			with open('yt.zip', 'rb') as f:
				f64 = b64encode(f.read())
				clipboard.set(f64.decode())
		
			# Remove the ZIP, as it's on the clipboard
			remove('yt.zip')
			
			# Call Shortcuts
			url = "shortcuts://run-shortcut?name=yt_save3&input=clipboard"
			webbrowser.open(url)

def postdownload(d):
	if d['status'] == 'finished':
		# Get filename of json info saved by yt-dl
		base_filename = splitext(d['filename'])[0]
		#json_filename = "{}.info.json".format(base_filename)
		#thumbnail = "{}.jpg".format(base_filename)
		
		# Add to list
		files.append(d['filename'])

# class download:
#	def __init__(self):
#		self.d = ""
#		
#	def postd(self, d):
#		self.d = d
		

if __name__ == '__main__':
	main(sys.argv)
