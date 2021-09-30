import json
from pathlib import Path


def find_cols(table):
    cols = table.find('td', 'nmtt')
    trs = cols.find_all('tr')
    length = len(trs[-1])
    data_cols = [[] for _ in range(length)]
    for tr in trs:
        for k in tr.find_all('td'):
            if 'num_empty' in k.get('class'):
                continue
            cell_class = k.get('id')
            col = int(cell_class[3:].split('_')[0])
            data_cols[col].append(int(k.text))
    return data_cols


def find_rows(table):
    rows = table.find('td', 'nmtl')
    trs = rows.find_all('tr')
    data_rows = []
    for tr in trs:
        row = []
        for k in tr.find_all('td'):
            if 'num_empty' in k.get('class'):
                continue
            row.append(int(k.text))
        data_rows.append(row)
    return data_rows


def download_board(url):
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-setuid-sandbox")
    chrome_options.add_argument("--remote-debugging-port=9222")  # this
    chrome_options.add_argument("--disable-dev-shm-using")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("start-maximized")
    chrome_options.add_argument("disable-infobars")
    caps = DesiredCapabilities().CHROME
    # caps["pageLoadStrategy"] = "normal"  #  complete
    caps["pageLoadStrategy"] = "eager"  # interactive
    # caps["pageLoadStrategy"] = "none"
    driver = webdriver.Chrome(options=chrome_options, desired_capabilities=caps)
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', 'nonogram_table')
    rows = find_rows(table)
    cols = find_cols(table)
    return rows, cols


def get_board(url):
    filename = f'nonogram_folder/{url.split(r"/")[-1]}.json'
    if Path(filename).exists():
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            rows, cols = data[0], data[1]
    else:
        rows, cols = download_board(url)
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([rows, cols], f, ensure_ascii=False, indent=4)
    return rows, cols
