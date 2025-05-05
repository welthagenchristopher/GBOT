# 🎉 GBOT 🎉

Family friendly gag bot, endlessly customisable and perfect for irritating your *friends*.

---

## 🤖 What It Does

1. **You** drop your target’s Discord user ID into an environment variable.  
2. **Bot** hops into their voice channel whenever they join or switch rooms.  
3. **Bot** plays `audio.mp3` on a tight loop (1 s delay by default) until they log off or flee.  
4. **Laughter ensues.** Or violence. Depends on how annoying your audio is.

---

## 🚀 Installation

1. **Clone the repo** 
   ```bash
   git clone https://github.com/you/annoyatron-3000.git
   cd annoyatron-3000

2. **create a virtual environment**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate , or .venv\scripts\activate on windows

3. **Install dependencies**
    ```bash
    pip install -r requirements.txt

4. **FFmpeg**
    ````bash
    Ensure you have FFmpeg on your PATH, otherwise
    download the excecutable and point the audiocog to it
    https://ffmpeg.org/

5. **Configuration**
    ```.env
    create your env file, with two arguments
    DISCORD_TOKEN=<your bot token>
    TARGET_USER_ID=<plain UID of any user>

6. **Audio**

    drop your chosen 'audio.mp3' file into the /src directory

7. **Navigate**
    ```bash
    to the project root cd .../gbot

8. **run**
    ```bash
    python main.py

9. **Sit back and enjoy**


### Warning and disclaimer:

Use responsibly. Victims may rage-quit, rage-ping, or rage-report you.

This is a prank bot. Do not deploy on servers without explicit consent.

You are solely responsible for any friendships (and EULAs) you break.

