# ios-ytdl-shortcuts
Download video(s) from YouTube using Pythonista and Shortcuts

## Requirements:
- iOS
- Pythonista with StaSh and youtube-dl
- Shortcuts

## Usage
- Install [Pythonista](https://apps.apple.com/us/app/pythonista-3/id1085978097), [StaSh](https://github.com/ywangd/stash), and youtube-dl (using pip in StaSh).
- Save **shortcuts_ytdl.py** to Pythonista's root directory.
- Add the shortcuts to Shortcuts.
- Go to YouTube and share a URL, tap 'Shortcuts' and choose **Скачать аудио/видео с YouTube** (depending on if you want to download audio or video.

## Flow
__iOS share sheet__ (YouTube URL) > __Скачать ... с YouTube__ [Shortcuts] > __shortcuts_ytdl.py__ [Pythonista] > __yt_save3__ [Shortcuts]

## Files:
### shortcuts_ytdl.py
*Input*: a YouTube URL (video, playlist) and a string 'video' or 'audio', which determines what format we download from YouTube.

*Output*: a base64-encoded ZIP archive of the downloaded songs, on the clipboard.

> Uses youtube-dl to download videos as videos or audio files.
To pass files on to Shortcuts, it adds each file to a ZIP archive, encodes it with base64, and then puts it on the clipboard.

### Shortcuts
**Счачать видео с YouTube** ('Download video from YouTube')
**Счачать аудио с YouTube** ('Download audio from YouTube')

> Simple Shortcuts that take a URL-address as input (e.g. YouTube video > Share > Shortcuts > ...) and pass the URL and either 'video' or 'audio' to _shortcuts_ytdl_.

**yt_save3**

> Called by _shortcuts_ytdl_ when all videos are downloaded. Takes the archive off the clipboard, decodes it, and then offers to save the audio/video files on the device.
