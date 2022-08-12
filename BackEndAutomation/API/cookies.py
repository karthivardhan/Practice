import requests

cookie = requests.get('http://httpbin.org/cookies', allow_redirects=False, cookies={'visit-year': '2022'}, timeout=1)
print(cookie.history)
print(cookie.status_code)
print(cookie.text)
print(cookie.status_code)


######## Using Session manager ############
se = requests.session()
se.cookies.update({'visit-year': '2022'})
cookie2 = se.get('http://httpbin.org/cookies')
print(cookie2.text)

