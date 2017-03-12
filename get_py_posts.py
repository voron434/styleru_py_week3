import json
import requests

def keyword_search():
    url = 'https://api.vk.com/method/newsfeed.search'
    params = {
            'q': 'python программирование -кожа -помогите -помощь',
            'count': 200,
            }
    all_news = json.loads(requests.get(url, params).text)
    return all_news

if __name__ == "__main__":
    py_posts = keyword_search()
    path = 'vk_py_groups.json'
    with open(path, mode="w", encoding='utf-8') as my_file:
        json.dump(py_posts, my_file)
