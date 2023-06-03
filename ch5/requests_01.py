import requests

url = 'https://wallhaven.cc/w/z8lpww'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Referer': 'https://wallhaven.cc',
    'Cookie': 'wallhaven_session=eyJpdiI6InYzNmdzOVhhOUFRUFJRclhzN3lIR0E9PSIsInZhbHVlIjoiXC82Z0prT3piUWttVTFnWVVkN28ySU1hdGJQa0hjM1owVDdVcnZTamMzUUp2SFlIN1BZaGNiY3o4XC9sWklveHdIIiwibWFjIjoiMmVhZWJjODk3YTJjNjFjN2I4ZTE5Y2ZlNmEyMzhmZjhkNTg5M2NlNTQxZjk3NmNhODBiN2ZlOTIwNTU1ZjZmMyJ9'
}

response = requests.get(url=url, headers=headers)
print(response.text)