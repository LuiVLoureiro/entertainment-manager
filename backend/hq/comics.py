# Aumentar a Velocidade de Download
# Disponibilizar para Acesso Via Flask
# Transformar Fotos em PDF para Poder Baixar

import requests as r
import os

class Url:
    def __init__(self, url):
        self.url = url
    
    def build(self, number_c, number_p):
        return "/".join(self.url.split("/")[:7] + [str(number_c), f"{number_p:02d}.{self.url.split('/')[-1].split('.')[-1]}"])

class Files:
    @staticmethod
    def create_directory(path):
        if(not os.path.exists(path)):
            os.makedirs(path)
    
    @staticmethod
    def save_file(path, content):
        with open(path, "wb") as f:
            f.write(content)

class Downloader:
    def __init__(self, url, files):
        self.url = url
        self.files = files

    def download_img(self, url):
        try:
            response = r.get(url)
            if response.status_code == 200:
                return response.content
            else:
                (f"Error on Request -> {response.status_code}")
                return 404
        except:
            ("Error in Download...")
            return 404

    def download_chapter(self, chapter, max_pages=200):
        for page in range(1, max_pages):
            url = self.url.build(chapter, page)
            print(f"Trying: {url}")
            content = self.download_img(url)
            if content == 404:
                break
            hq_name = self.url.url.split("/")[5]
            chapter_path = os.path.join(hq_name, str(chapter))
            self.files.create_directory(chapter_path)
            file_path = os.path.join(chapter_path, f"{page:02d}.png")
            self.files.save_file(file_path, content)
            print(f"Saved: {file_path}")

    
    def download_all(self, max_chapters=48):
        for chapter in range(1, max_chapters+1):
            test_chapter = self.url.build(chapter, 1)
            test_content = self.download_img(test_chapter)
            if test_content == 404:
                break
            print(f"Downloading Chapter {chapter}...")
            self.download_chapter(chapter)
        
url = input("URL -> ").strip()
url = Url(url)
files = Files()
download = Downloader(url, files)
download.download_all()
        
        



#Criar Pagina -> 6 item da lista sempre e o nome


("Finished...")
