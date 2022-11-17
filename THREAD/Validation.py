import threading
import time
import concurrent.futures
import multiprocessing
import requests
import statistics
import sys

img_urls = ['https://i.pinimg.com/564x/9b/cd/98/9bcd986b312668ddfec3202d22b073d9.jpg','https://i.pinimg.com/564x/48/30/6f/48306fb784cb718538efaff84be08dcd.jpg',
'https://i.pinimg.com/564x/d4/02/52/d4025245b5f8f188364f6af366ef4aab.jpg']

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[6]
    img_name = f'{img_name}.png'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'Image {img_name} téléchargée')


def task_threading():
    T.append(threading.Thread(target=download_image, args=(img_urls[0],)))
    T.append(threading.Thread(target=download_image, args=(img_urls[1],)))
    T.append(threading.Thread(target=download_image, args=(img_urls[2],)))
    for t in T:
        t.start()
    for t in T:
        t.join()

def pool_threading():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(download_image, img_urls)

def task_multiprocessing():
    T.append(multiprocessing.Process(target=download_image, args=(img_urls[0],)))
    T.append(multiprocessing.Process(target=download_image, args=(img_urls[1],)))
    T.append(multiprocessing.Process(target=download_image, args=(img_urls[2],)))
    for t in T:
        t.start()
    for t in T:
        t.join()



if __name__ == "__main__":
    print("")
    start = time.perf_counter()
    T = []
    task_threading()
    finish = time.perf_counter()
    print(f"Threading Finished in {round(finish-start, 6)} second(s)")
    print("")
    start = time.perf_counter()
    pool_threading()
    finish = time.perf_counter()
    print(f"POOL Finished in {round(finish-start, 6)} second(s)")
    print("")

    start = time.perf_counter()
    T = []
    task_multiprocessing()
    finish = time.perf_counter()
    
    print(f"Multiprocessing s'est terminé en {round(finish-start, 6)} second(s)")
    print("")
    sys.exit()
# Path: THREAD/Validation.py