import csv
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from supabase import create_client, Client
import time
import string

SUPABASE_URL = "https://cqakrownxujefhtmsefa.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNxYWtyb3dueHVqZWZodG1zZWZhIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIyNjMyMzMsImV4cCI6MjA0NzgzOTIzM30.E9jJxNBxFsVZsndwhsMZ_2hXaeHdDTLS7jZ50l-S72U"
SUPABASE_TABLE_NAME = "sp"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Rentang data yang diproses (misal dari baris 1 sampai 50)
start_row =0  # Baris pertama (0-based index)
end_row = 100  # Baris terakhir yang ingin diproses

# Deklarasi akun tunggal
email = "brendon_ferrer@sdn2duwet.ac.id"
password = "@@Masuk123#"


def random_string(count):
    string.ascii_letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    return "".join(random.choice(string.ascii_letters) for x in range(count))

    # return random.choice(string.ascii_letters)


# Fungsi membaca CSV dengan rentang baris tertentu
def read_csv_range(filename, start, end):
    with open(filename, newline='', encoding='utf-8') as f:
        rows = [row[0] for i, row in enumerate(csv.reader(f)) if start <= i < end]
    return rows



driver = webdriver.Chrome()

edit_mail = email.replace("@sdn2duwet.ac.id","")
username = edit_mail.replace("_","") 

fixusername = username+random_string(5)


driver.get("https://accounts.google.com/signin")
time.sleep(3)  # Tunggu halaman dimuat

# Temukan elemen input email dan masukkan email
driver.find_element(By.CSS_SELECTOR, "#identifierId").send_keys(email)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "#identifierId").send_keys(Keys.ENTER)
time.sleep(2)  # Tunggu untuk login dengan email

# Temukan elemen input password dan masukkan password
driver.find_element(By.CSS_SELECTOR, "input[name='Passwd']").send_keys(password)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR, "input[name='Passwd']").send_keys(Keys.ENTER)
time.sleep(5)  # Tunggu beberapa detik setelah login 



driver.get("https://aetherhub.com/Account/Register")
time.sleep(3)


driver.find_element(By.CSS_SELECTOR, "#Google").click()
time.sleep(3)

clickgoogle2 = f'div[data-identifier="{email}"]'

driver.find_element(By.CSS_SELECTOR, clickgoogle2).click()
time.sleep(3)

driver.find_element(By.XPATH, "//button[.//span[text()='Lanjutkan']]").click()
time.sleep(2)

driver.find_element(By.CSS_SELECTOR, "#UserName").send_keys(fixusername)
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '#Consent').click()
time.sleep(1)

driver.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()
time.sleep(5)

# Baca judul video sesuai rentang yang diinginkan
titles = read_csv_range("data.csv", start_row, end_row)


for title in titles:
    
    try:
        judul = title
        modif_kata = title.replace(' ', '_')
        kw = f'{title} Leaked Video New Files Update ++ '

        konten = f'''
        29 minutes ago - Access {title} Leaked Only-fans New Updaload FIles 2025<br><br>LINK ⏩⏩ https://topallfans.web.app?title={modif_kata}<br><br>{title} Leaked only-fans update pict  - you ll be able to download and preview all content from {title} Only-fans in just a few clicks.
        '''

            

        driver.get("https://aetherhub.com/Deck/MyDecks/")
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "#NewDeck_Name").send_keys(kw)
        time.sleep(2)
            

        driver.find_element(By.XPATH, "//button[.//b[text()='Create']]").click()
        time.sleep(5)

        try:
            driver.execute_script("document.getElementById('zone16-DesktopSticky').style.display = 'none';")
        except:
            pass

        element = driver.find_element(By.CSS_SELECTOR, "#editNotes")

        # Scroll 
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
        time.sleep(2)

        driver.find_element(By.CSS_SELECTOR, "#editNotes").click()
        time.sleep(3)

        driver.execute_script("tinymce.activeEditor.setContent(arguments[0]);", f'{judul} Leaked Video 2025 <br><br> LINK ⏩⏩ <a href="https://clipsfans.com/{modif_kata}&ref=aet">https://clipsfans.com/{modif_kata}</a> ')

            
        driver.find_element(By.CSS_SELECTOR, "#notesSubmit").click()
        time.sleep(5)
        driver.find_element(By.XPATH, "//a[@title='Visual View']").click()
        time.sleep(3)

        response = (
                supabase.table(SUPABASE_TABLE_NAME)
                .insert({"result": driver.current_url})
                .execute()
            )

        print("Berhasil Upload : "+title)
    except:
        print("Terjadi Error")

    

driver.quit()
