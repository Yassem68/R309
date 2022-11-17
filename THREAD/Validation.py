import threading
import time
import concurrent.futures
import multiprocessing
import requests
import statistics

img_urls = ['https://i.pinimg.com/564x/9b/cd/98/9bcd986b312668ddfec3202d22b073d9.jpg','https://i.pinimg.com/564x/48/30/6f/48306fb784cb718538efaff84be08dcd.jpg',
'https://i.pinimg.com/564x/d4/02/52/d4025245b5f8f188364f6af366ef4aab.jpg']

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[6]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

def task_threading(i):
    print(f"Task {i} started")
    time.sleep(1)
    print(f"Task {i} finished")



if __name__ == "__main__":
    start = time.perf_counter()
    threads 
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)
    finish = time.perf_counter()
    print(f'Finished in {round(finish-start, 2)} second(s)')



# Path: THREAD/Validation.py