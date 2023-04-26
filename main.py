import os
import requests
from bs4 import BeautifulSoup
import pyperclip
import html2text
import re
import textwrap
class TelegramScraper:
    
    def __init__(self, post_links, author = "", content = "", postDate = "", bulkData = ""):
        self.post_links = post_links
        self.author = author
        self.content = content
        self.postDate = postDate
        self.bulkData = bulkData
        self.imgUrls = []
        self.hasImg = None

    def clear_console(self):
        # Windows
        if os.name == 'nt':
            os.system('cls')
        # Unix/Linux/MacOS
        else:
            os.system('clear')

    def html_to_text(self, html):
        h = html2text.HTML2Text()
        h.body_width = 0  # Disable line wrapping
        h.ignore_links = True  # Ignore hyperlinks
        h.ignore_emphasis = True  # Ignore bold and italic formatting
        h.ignore_images = True  # Ignore images
        h.protect_links = True  # Protect hyperlinks from being stripped out
        h.unicode_snob = True  # Use Unicode characters instead of ASCII
        h.wrap_links = False  # Disable link wrapping
        h.wrap_lists = False  # Disable list wrapping
        h.decode_errors = 'ignore'  # Ignore Unicode decoding errors

        text = h.handle(html)
        text = re.sub(r'\*+', '', text)  # Remove asterisks
        text = re.sub(r'^[ \t]*[\\`]', '', text, flags=re.MULTILINE)  # Remove leading \ or `
        return text

    def downloadImages(self):
        self.clear_console()
        dlImg = input(f"Would you like to download [{len(self.imgUrls)}] images from the post?\n[Y] - Download {len(self.imgUrls)} images from {self.author}\n[Enter] - Skip Downloads")
        if dlImg:
            urlData = post_link.split('/')
            mainFolder = urlData[-2]
            postID = urlData[-1]
            if not os.path.exists(f"{mainFolder}"):
                os.makedirs(f"{mainFolder}")
            for img_num, url in enumerate(self.imgUrls, start=1):
                fp = f"{mainFolder}-{urlData[-1]}"
                fn = f"{mainFolder}-{img_num}.jpg"
                if not os.path.exists(f"{mainFolder}\{fp}"):
                    os.makedirs(f"{mainFolder}\{fp}")
                if os.path.exists(os.path.join(f"{mainFolder}\{fp}", fn)):
                    print(f"Image {img_num} already exists at {os.path.dirname(os.path.abspath(__file__))}\{mainFolder}")
                else:
                    response = requests.get(url)
                    with open(os.path.join(f"{mainFolder}\{fp}", fn), 'wb') as f:
                        f.write(response.content)
                    print(f"Image {img_num} downloaded to {os.path.dirname(os.path.abspath(__file__))}\{mainFolder}")

        
    def copyData(self):
        self.clear_console()
        copyData = input("Would you like to copy the content to your clipboard?\n[Y - Copy Content | A - Copy All Data]\n('Enter' to skip) Selection: ").lower()
        match(copyData):
            case 'y':
                pyperclip.copy(self.content)
            case 'a':
                pyperclip.copy(self.bulkData)
            case _:
                print("Skipping!")
        if(self.hasImg):
            self.downloadImages()
    def doit(self):
        try:
            for link in self.post_links:
                response = requests.get(link)
                soup = BeautifulSoup(response.text, 'html.parser')
                requiresApp = soup.find('div', {'class': 'message_media_not_supported_label'})
                if requiresApp:
                    input("This Telegram post is unavailable through GET requests.\nIt must be viewed in the Telegram app.\nSorry! ♥\n\nPress 'Enter' to exit")
                    exit()

                htmlBody = soup.find('div', {'class': 'tgme_widget_message_text js-message_text', 'dir': 'auto'})
                author = soup.find('div', {'class': 'tgme_widget_message_author accent_color'}).find('a', {'class': 'tgme_widget_message_owner_name'}).find('span', {'dir': 'auto'})
                datetime = soup.find('span', {'class': 'tgme_widget_message_meta'}).find('time', {'class': 'datetime'})
                # Find all the a elements with the specified class
                imgUrls = soup.findAll('a', {'class': 'tgme_widget_message_photo_wrap'})
                if imgUrls:
                    for div in imgUrls:
                        style = div['style']
                        match = re.search(r"background-image:url\('(.*)'\)", style)
                        if match:
                            bg_image_url = match.group(1)
                            self.hasImg = True
                            self.imgUrls.append(bg_image_url)
                if htmlBody:
                    self.content = self.html_to_text(str(htmlBody))
                if author:
                    self.author = self.html_to_text(str(author))
                if datetime:
                    self.postDate = self.html_to_text(str(datetime))
                match(self.hasImg):
                    case True:
                        info = f"URL: {link}\nImages: [{len(self.imgUrls)}]\n\nAuthor: {self.author}Date: {self.postDate}\nTelegram Content:\n\n{self.content.strip()}\n"
                    case None:
                        info = f"URL: {link}\nAuthor: {self.author}\nDate: {self.postDate}\nTelegram Content:\n\n{self.content.strip()}\n"
                self.bulkData = info
                wrapped_info = textwrap.indent(info, ' ' * 12)
                print(wrapped_info)
        except AttributeError as e: 
            print(e)
if __name__ == '__main__':
    post_link = input("Enter your post URL: ")
    post_links = post_link + "?embed=1&mode=tme"
    scraper = TelegramScraper(post_links.split('|'))
    scraper.doit()
    input("Press Enter to continue")
    scraper.copyData()
    
    
    