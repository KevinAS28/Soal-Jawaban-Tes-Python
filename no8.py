import requests
from bs4 import BeautifulSoup

url = "https://academy.babastudio.com/login"



print("mendapatkan login endpoint, token security (dan input lainnya) secara otomatis... ")
page_source = BeautifulSoup(requests.get(url).content, "html.parser")
login_form = page_source.find("form", {"class": "form-signup", "method": "POST"})
login_endpoint = login_form["action"]
another_inputs = login_form.find_all("input")

#ubah another_inputs ke bentuk dictionary
login_data = dict()
for _input in another_inputs:
    try:
        login_data[_input["name"]] = _input["value"]
    except KeyError: 
        continue

print("login_data:", login_data)
print("login_endpoint:", login_endpoint)

email = input("email anda: ")
password = input("password anda: ")
login_data["email"] = email
login_data["password"] = password

result = requests.post(login_endpoint, login_data)
result_name = "result_no8.html"
with open(result_name, "wb+") as result_file:
    result_file.write(result.content)

print(result)
print("hasil tersimpan pada", result_name)