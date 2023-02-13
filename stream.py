import requests

with requests.get('', stream=True) as response:
    # for line in response.iter_lines(decode_unicode=True):
    for byte in response.iter_content():
        if byte:
            print(byte)