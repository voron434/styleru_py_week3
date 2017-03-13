import json
import requests
import os


def fetch_python_posts_from_vk():
    url = 'https://api.vk.com/method/newsfeed.search'
    params = {
        'q': 'python программирование -кожа -помогите -помощь',
        'count': 200,
        }
    new_python_posts = json.loads(requests.get(url, params).text)
    new_python_posts['response'].pop(0)
    return new_python_posts['response']


def load_old_posts(path):
    with open(path, mode='r') as my_file:
        data = json.load(my_file)
        return data


def is_post_unique(python_post, old_python_posts):
    for old_python_post in old_python_posts:
        if (python_post['text'] == old_python_post['text'])\
                and (python_post is not old_python_post):
            return False
    return True


if __name__ == "__main__":
    path = input('Enter path to database:')
    if os.path.exists(path):
        old_py_posts = load_old_posts(path)
    else:
        old_py_posts = []
    python_posts = fetch_python_posts_from_vk()
    for py_post in python_posts:
        if is_post_unique(py_post, python_posts):
            old_py_posts.append(py_post)
    with open(path, mode="w") as my_file:
        json.dump(old_py_posts, my_file)

