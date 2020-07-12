import requests
from bs4 import BeautifulSoup as bs
import csv
user_agent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
header ={'user-agent':user_agent}
maoyanurl = "https://maoyan.com/films?showType=3"
#cookie1 = "__mta=50118041.1594197255465.1594198026010.1594198297082.11; uuid_n_v=v1; uuid=CD4CE2B0C0F511EA8A4527DE1893266B3172B01CC5C34D30BA95EF9A5DF13E34; _csrf=5fbcf0ed624f46cb1a09403ad10250ef58c43841aba4b41b6cd9db87ac044e84; mojo-uuid=ca80123c2a1981bbf8dec64a08bc6961; mojo-session-id={"id":"ce89068fa8a07f1e1258378a9b86f024","time":1594197255378}; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; _lxsdk_cuid=1732d8fa4f1c8-02d7cc7a26a114-396a4507-e1000-1732d8fa4f1c8; _lxsdk=CD4CE2B0C0F511EA8A4527DE1893266B3172B01CC5C34D30BA95EF9A5DF13E34; lt=z1Bd51CahCDAmze4nr_ShjTC-qgAAAAAAAsAABRnjCvLyn_gxgGOwmQk_5hElp2_0nd6z7O5DsD5Gfa4J918-2nr0_MA8QlwdZKB0A; lt.sig=I8GBsNwwQ5plDOtB3uRpDwDTaPQ; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1594197255,1594197413,1594198297; mojo-trace-id=27; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1594198382; __mta=50118041.1594197255465.1594198297082.1594198382062.12; _lxsdk_s=1732d8fa4f4-b60-e21-fd%7C%7C36"
res=requests.get(maoyanurl,headers = header)
#print(f'返回码:{res.status_code}')
bs_info = bs(res.text,'html.parser')
start = 0
list10 = []
for tags in bs_info.find_all('div', class_='movie-hover-info'):
    start += 1
    if start < 11: #指定电影的的范围是1-10
        info1 = tags.get_text(' ',strip = True)
        info2 = info1.split(' ')
        csv_1 = open('/Users/johnwang/Documents/pythoex/movie10.csv','a',newline='')
        writer1 = csv.writer(csv_1)
        print (info2[0] + '|' + info2[4] + '|' + info2[-1])
        writer1.writerow([info2[0],info2[4],info2[-1]])
        csv_1.close()