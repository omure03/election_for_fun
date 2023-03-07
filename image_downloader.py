import requests


url1 = "https://www.cumhuriyet.com.tr/Archive/2019/8/1/1514480_resource/canli.jpg"
response = requests.get(url1)
content = response.content
with open("rte.jpg", "wb") as img:
    img.write(content)

url2 = "https://indigodergisi.com/wp-content/uploads/2017/08/kilicdaroglu-atletli-fotografi.jpg"
response = requests.get(url2)
content = response.content
with open("kk.jpg", "wb") as img:
    img.write(content)

url3 = "https://64.media.tumblr.com/34bc567a70095725dd2455f233efddba/84c04db5ec535002-07/s1280x1920/bfe07d88c85f78a1e4ed700f2511ba414ae54dba.jpg"
response = requests.get(url3)
content = response.content
with open("mi.jpg", "wb") as img:
    img.write(content)
