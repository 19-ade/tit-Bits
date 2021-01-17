from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from cryptography.fernet import Fernet
import requests
from bs4 import BeautifulSoup

encryption = b'gAAAAABf-qFBQ1HyixWPcYpqmm4zBx22CVl1GzAFRsTd1cSr96e37JyGIxRPKDwxP2Fei3CB7quWHNKmZ0ezvU6cEipuc58xtcfuA6rXn25qvDmrN7-FL5g='
key_encrypt = b'y5-8tBbxdnTcJCCslXzGL65T8s26wdRdoJ4XU4CkH10='
enc1 = b'gAAAAABf-qTbgslFmbN--XYktZJ0o9LmrXkXEVMVr2xugjfkEKSkQxNs2Ddq6XbQF02ka3mnzsPTyqfOpFXrzKf0TWqsJQes8WXd-JgGCuKQfykouBd553-Q06cpbY0NCrD3sRQXn2soQ6vZ3-mylsfdUgdKu451T34m4b32MOnRH6Msx4PZ9Fc6ruoA38FWzlRkf51LvnojuD9YWwZqLBdk0jP6GsA_ZaBlDUbbczoZ_7bvLEL3c9fnXgLjCFoN1Tx_PeWRIjeB'
key1 = b'3T2mu3r5_d-e0SEQP-AZ0Uz7jnq6SpGgS9s4jWSkZVQ='


def firefox_driver(path):
    driver = webdriver.Firefox(executable_path=path)
    driver.maximize_window()
    return driver


def chrome_driver(path):
    driver_c = webdriver.Chrome(executable_path=path)
    driver_c.maximize_window()
    return driver_c


def getting_job_done(driver):
    driver.get(decrypt_code(encryption, key_encrypt))
    driver.find_element_by_xpath(
        decrypt_code(enc1, key1)).click()



def getting__job_done(links):
    for link in links:

        '''iterate through all links in video_links  
        and download them one by one'''

        # obtain filename by splitting url and getting
        # last string
        file_name = link.split("/")[-1]

        print("Downloading file:%s" % file_name)

        # create response object
        r = requests.get(link, stream=True, verify=False)

        # download started
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)

        print("%s downloaded!\n" % file_name)

    print("All pdf downloaded!")
    return


def decrypt_code(encryption, key):
    key = key
    f = Fernet(key)
    decrypted_message = f.decrypt(encryption)
    return decrypted_message.decode()


if __name__ == "__main__":
    r = requests.get(decrypt_code(encryption, key_encrypt))
    links = BeautifulSoup(r.content, "html5lib")
    print("Choose your webdrivers\n 1.Firefox Webdriver \n 2.Chrome webdriver")
    f = int(input("Enter 1 for Firefox 2 for chrome "))


    if f == 1:
        path = input("Enter path for geckodriver(pls avoid using spaces before input)")
        driver = firefox_driver(path)
        getting_job_done(driver)
    elif f == 2:
        path = input("Enter path for chromedriver(pls avoid using spaces before input)")
        driver = chrome_driver(path)
        getting_job_done(driver)
    else:
        print("wrong input \nHasta la Vista , baby")