import requests

print("mendapatkan halaman shopee...")

url = "https://shopee.co.id/"

page_source = requests.get(url).content

shopee_name = "shopee.html"

with open(shopee_name, "wb+") as shopee_file:
    shopee_file.write(page_source)

print("hasil tersimpan pada", shopee_name)