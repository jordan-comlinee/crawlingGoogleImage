from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
chrome_options.binary = './chromedriver-win64/chromedriver.exe'  # 드라이버 실행파일 경로
query = '사탕 식품영양정보'


driver = webdriver.Chrome(options=chrome_options)
driver.get(f'https://www.google.com/imghp')
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys(query)
search_bar.submit()

PAUSE_TIME = 2
last_hegiht = driver.execute_script("return document.body.scrollHeight")
new_height = 0

while True:
    driver.execute_script("window.scrollBy(0,5000)")
    time.sleep(PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height - last_hegiht > 0:
        last_hegiht = new_height
        continue
    else:
        break

img_elements = driver.find_elements(By.CSS_SELECTOR, ".rg_i")
imgs = []

for idx, img in enumerate(img_elements):
    print(f"{query} : {idx + 1}/{len(img_elements)} proceed...")
    try:
        img.click()
        time.sleep(PAUSE_TIME)
        # 이부분에서 에러나면, 직접 개발자 도구 활용해서 XPATH 추출한 뒤에 변경
        img_element = driver.find_element(By.XPATH,
                                          '//*[@id="Sva75c"]/div[2]/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img')
        img_src = img_element.get_attribute('src')
        img_alt = img_element.get_attribute('alt')
        imgs.append({
            'alt': img_alt,
            'src': img_src
        })

    except:
        print(f'err in {idx}')
        pass

driver.close()

save_path = f'./{query}'
import os

if not os.path.exists(save_path):
    os.mkdir(save_path)

total_N = len(imgs)
for idx, one in enumerate(imgs):
    src = one['src']
    alt = one['alt']
    headers = {
        "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
        "Accept":
            "image/avif,image/webp,image/apng,image/*,*/*;q=0.8"
    }
    try:
        # Request 객체를 생성하여 headers를 설정합니다.
        request = urllib.request.Request(src, headers=headers)

        # 생성한 Request 객체를 사용하여 이미지를 다운로드
        response = urllib.request.urlopen(request)

        # 이미지를 지정된 경로에 저장
        with open(f"{save_path}/{query}_{idx}.png", 'wb') as f:
            f.write(response.read())

        print(idx, alt)
    except Exception as e:
        print(f"Error downloading image {idx}: {e}")
        # 일정 시간을 대기
        time.sleep(1)



print('done')