# ?éß Calls Music 2 ?? The first open-source project based on [PyTgCalls](https://github.com/pytgcalls/pytgcalls)

## ?çÔ? Requirements

- FFmpeg
- Node.JS 15+
- Python 3.7+

## ?? Deployment

### ?? Config

Copy `example.env` to `.env` and fill it with your credentials.

### ?? The good way

1. Install Python requirements:
   ```bash
   pip install -U -r requirements.txt
   ```
2. Run:
   ```bash
   python -m callsmusic
   ```

### ?ê¨ Docker

1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```

### ?íµ Heroku

[Click here](https://heroku.com/deploy?template=https://github.com/mrnitric/music-robo_heroku/)

## ?πÔ? Commands

| Command | Description                                  |
| ------- | -------------------------------------------- |
| /play   | play the replied audio file or YouTube video |
| /pause  | pause the audio stream                       |
| /resume | resume the audio stream                      |
| /skip   | skip the current audio stream                |
| /stop   | clear the queue and stop the audio stream    |

## ?? License

### GNU Affero General Public License v3.0

[Read more](https://www.gnu.org/licenses/#AGPL)
