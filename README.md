# Telegram Post Scraper via Python

Telegram-Post-Scraper is a Python program designed to scrape posts from Telegram channels using HTTP requests and HTML parsing, rather than Telegram's API. This program is useful when creating bots or using Telegram's API is not feasible or against Telegram's terms of service.
TG-Post-Scraper also has the capabilities to download multimedia, videos and images from a Telegram post. Atop of this, it offers the ability to save posts and the bulk data to text files for ease of access.

## Changelog
```
Version 3:
Release Date: Sept 21, 2023

Rewrote the base. Again.
Added better error handling.
Converted from async back to sync.
Added CLI support.
py(thon)(3) main.py --link / -l https://t.me/somegroup/420

Version 4 will include a graphical user interface as well as a settings handler.
Much love, enjoy y'all ♥
```


## Features

- Scrapes posts from Telegram channels using HTTP requests and HTML parsing.
- Can copy the content of the posts, and download media such as images and videos.
- Supports scraping multiple links in one session. Seperate links at the beginning of the program with commas. (t.me/groupID/333,t.me/someotherID/444,t.me/anotherOne/555)
- Does not require a bot or an API key.
- Useful for situations where using Telegram's API or creating a bot is not feasible or against Telegram's terms of service.

## Requirements

To use Telegram-Post-Scraper, you need to have Python 3 installed on your system, as well as the following Python packages:
This program was built on Python 3.10.10 64bit

- beautifulsoup4==4.11.1
- html2text==2020.1.16
- pyperclip==1.8.2
- Requests==2.28.2

You can install these packages using pip by running the following command:

```
pip install -r requirements.txt
```

## Usage

To use Telegram-Post-Scraper, you just provide it with a URL of a Telegram post.
```
1. Open Command Prompt, Powershell, or Terminal.
2. Run "py(thon3) main.py"
2a. (For CLI usage) py(thon3) main.py -l OR --link http://t.me/somegroup/ID
3. Enter your Telegram post URL. (Format: https://t.me/SOMEGROUP/NUMERICID)
3a. You can find the link of a Telegram post by right clicking it and pressing "Copy Link".
4. Follow through the prompts in the console window.

```

## Contributing

If you find any bugs or have suggestions for improvements, feel free to create an issue or submit a pull request.


## Donations
Was this program useful to you? 
If you want to donate ♥:
 > BTC: bc1q0rp3740t3hjrpuc3dzhme30rupwcffet7jndux
