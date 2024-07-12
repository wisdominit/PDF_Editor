import os
import time
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def download_pdfs(pdf_urls, download_folder):
    # Set up Chrome options
    chrome_options = Options()
    prefs = {
        "download.default_directory": download_folder,  # Change default directory for downloads
        "download.prompt_for_download": False,  # Disable download prompt
        "plugins.always_open_pdf_externally": True  # Automatically download PDFs
    }
    chrome_options.add_experimental_option("prefs", prefs)

    # Ensure ChromeDriver is installed
    chromedriver_autoinstaller.install()

    # Initialize ChromeDriver
    service = Service()
    driver = webdriver.Chrome(service=service, options=chrome_options)

    for url in pdf_urls:
        try:
            driver.get(url)
            time.sleep(5)  # Wait for download to complete (adjust as necessary)
            print(f"Downloaded: {url}")
        except Exception as e:
            print(f"Failed to download {url}: {e}")

    driver.quit()

# List of PDF URLs to download
pdf_urls = [
    "http://www.example.com/file1.pdf",
    "http://www.example.com/file2.pdf",
    "http://www.example.com/file3.pdf",
]

# Folder to save the downloaded PDFs
download_folder = os.path.abspath("downloaded_pdfs")

# Create download folder if it doesn't exist
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Download the PDFs
download_pdfs(pdf_urls, download_folder)