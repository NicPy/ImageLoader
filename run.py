import urllib.request
import os
print('Beginning file download with urllib2...')
path = os.getcwd()

def get_img_name(full_name):
	name = '' 
	for i in reversed(full_name):
		if i == '/':
			break
		else:
			name += i
	return(''.join(reversed(name)))

def download(img_url, path, img_name):
	urllib.request.urlretrieve(img_url, path + '/images/' + img_name)  
	print('Download completed')	

def start():

	with open('images.txt', 'r') as urls:
		for url in urls:
			download(url, path, get_img_name(url))

start()