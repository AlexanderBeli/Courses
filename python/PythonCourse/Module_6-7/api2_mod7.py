import requests

#отработал доступ к api по паролю
#отработал закачку фалов по частям (chunk)
#усовершенствовал сохраность имени в скачиваемом файле

endpoint = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
# Замените DEMO_KEY ниже своим собственным ключом, если вы его сгенерировали.
api_key = "DEMO_KEY"
query_params = {"api_key": api_key, "earth_date": "2020-07-01"}
response = requests.get(endpoint, params=query_params)
print(response)
#print(response.json())
photos = response.json()["photos"]
print(f"Найдено {len(photos)} фотографий.")

for i in range(0, len(photos)):
	photo = requests.get(f'{photos[i]["img_src"]}', stream=True)
	head_photo = requests.head(f'{photos[i]["img_src"]}')
	photo_size = int(head_photo.headers['Content-Length'])
	print('Размер загружаемого файла: {0} кб'.format(photo_size/1024))
	name = photos[i]["img_src"].split('/')[-1]
	with open(f'NASA-pics/{name}', 'wb') as img: 
	#with open(f'NASA-pics/{i}.jpg', 'wb') as img:
		for chunk in photo.iter_content(chunk_size=1024):
			img.write(chunk)
	print(photos[i]["img_src"])

