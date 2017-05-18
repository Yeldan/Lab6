import requests

url = 'https://api.vk.com/method/newsfeed.get?source_gids=newsbarca'
response = requests.get(url)
data = response.json()
communities = data['response'][0]['groups']
print(communities)
