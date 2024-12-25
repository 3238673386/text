import re
import requests
from urllib import parse
from tqdm import tqdm

filename = 'dir/php.txt'
url = 'http://07401565-92fb-4368-b838-50db95cf4e8b.challenge.ctf.show/'

error = 0

respond_ks = requests.get(url=url)
text_ks = respond_ks.text

result = ''

with open(filename, 'r' ,encoding='utf-8') as file:
	lines = file.readlines()

total_lines = len(lines)
with tqdm(total=total_lines,desc="Processing lines") as pbar:

	for index,line in enumerate(lines,start=1):
		pbar.update(1)
		true_url = url.rstrip('/')
		line = line.rstrip()
		if not line.startswith('/'):
			line = '/' + line
		encode_url = true_url + parse.quote(line)
		try:
			respond = requests.get(url = encode_url,timeout = 2)
			if respond.status_code == 200 and respond.text != text_ks:
				result = result + line + '\n'
		except Exception as err:
			error += 1
	pbar.close()

print(result)