from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import time
import lxml
from datetime import datetime, timezone, timedelta

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/79.0.3945.88 Safari/537.36 '
}

def main():
    while True:
        try:
            r = requests.get('https://store.steampowered.com/stats/Steam-Game-and-Player-Statistics?l=schinese',headers = headers ,timeout=15)
            if r.status_code == 200:
                soup = BeautifulSoup(r.text, 'lxml')
                a = soup.findAll(class_="player_count_row")
                NOW =[]
                MAX=[]
                ID=[]
                Name = []
                for i in a:
                    Nownum = i.contents[1].span.string
                    MAXnum = i.contents[3].span.string
                    NOW.append(Nownum)
                    MAX.append(MAXnum)
                    ID.append(re.search('\d+', str(i.contents[7].a.attrs['href'])).group())
                    name = str(i.contents[7].text)
                    name = name.replace('\n', '').replace('\r', '')
                    Name.append(name)
                df = pd.DataFrame(list(zip(ID, Name, NOW, MAX)),
                               columns =[ 'ID', 'Name', 'now','max'])
                df1 = df.set_index('ID')
                path_stats = str(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()))+'.csv'

                dt0 = datetime.utcnow().replace(tzinfo=timezone.utc)
                dt8 = dt0.astimezone(timezone(timedelta(hours=8)))  # 转换时区到东八区
                dtime = str(dt8)
                mat = re.search(r"(\d{4}-\d{1,2}-\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2})",dtime)
                dtime = mat.group()

                df1.to_csv(path_stats)
                print(dtime)

                time.sleep(1)
        except:
            print('Error')
            pass

if __name__ == '__main__':
    main()