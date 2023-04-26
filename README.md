# Telegram-Post-Scraper

Telegram-Post-Scraper is a Python program designed to scrape posts from Telegram channels using HTTP requests and HTML parsing, rather than Telegram's API. This program is useful when creating bots or using Telegram's API is not feasible or against Telegram's terms of service.

## Features

- Scrapes posts from Telegram channels using HTTP requests and HTML parsing.
- Can copy the content of the post, including text and images. (#TODO: Video download support)
- Downloads images and other media attached to the post.
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
3. Enter your Telegram post URL.
3a. You can find the link of a Telegram post by right clicking it and pressing "Copy Link".
4. Follow through the prompts in the console window.

```

## Contributing

If you find any bugs or have suggestions for improvements, feel free to create an issue or submit a pull request.

## License

Telegram-Post-Scraper is released under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license. This means that you are free to use the program, but you may not use it for commercial purposes.