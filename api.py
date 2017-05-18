import requests

url = 'https://api.vk.com/method/users.get?user_ids=yeldan99&fields=bdate,blacklisted,lastseens,status'
response = requests.get(url)
data = response.json()
uid = data['response'][0]['uid']
status = data['response'][0]['status']
#university_name = data['response'][0]['occupation']['name']
url = 'https://api.vk.com/method/wall.get?owner_id=%d' % uid
response = requests.get(url)
data = response.json()
post_count = data["response"][0]
#likes_count = data["response"][0]
posts = data["response"][1:]
for post in posts:
	likes = post['likes']['count']
	print(likes)
#print(post_count)
#for post in posts:
	#text = post['text']
	#print(text)
#print(data)
#print(first_name)
#print(last_name)
#print(uid)