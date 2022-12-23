import requests

correct_response = []
incorrect_response = []

def get_check_websites():
    with open("websites.txt", "r", encoding="UTF-8") as file:
        websites = file.read().splitlines()
        for url in websites:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    correct_response.append(url)

            except requests.exceptions.ConnectionError:
                incorrect_response.append(url)

def save_file (file, correct_urls, incorrect_urls):
    with open("correct_response.txt", "w", encoding="UTF-8") as file:
        for url in correct_urls:
            file.write(url + "\n")
            
    with open("incorrect_response.txt", "w", encoding="UTF-8") as file:
        for url in incorrect_urls:
            file.write(url + "\n")

save_file(get_check_websites(), correct_response, incorrect_response)