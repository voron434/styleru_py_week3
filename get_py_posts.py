import json
import requests

def get_python_posts():
    url = 'https://api.vk.com/method/newsfeed.search'
    params = {
            'q': 'python программирование -кожа -помогите -помощь',
            'count': 200,
            }
    py_posts = json.loads(requests.get(url, params).text)
    return py_posts

if __name__ == "__main__":
    py_posts = get_python_posts()
    path = 'vk_py_groups.json'
    with open(path, mode="w", encoding='utf-8') as my_file:
        json.dump(py_posts, my_file)
