import requests

# some existing url with id
url = 'https://petstore.swagger.io/v2/pet/9843217/uploadImage'
files = {'file': open('/Users/apparaojajimoggala/PythonSelenium notes/test.json','rb')}
res = requests.post(url, files=files)
print(res.status_code)
print(res.text)
