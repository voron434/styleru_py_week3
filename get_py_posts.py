import json
import requests
import os


def fetch_python_posts_from_vk():
    url = 'https://api.vk.com/method/newsfeed.search'
    params = {
        'q': 'python программирование -кожа -помогите -помощь',
        'count': 200
        }
    new_python_posts = json.loads(requests.get(url, params).text)
    new_python_posts['response'].pop(0)
    return new_python_posts['response']


def load_existing_python_posts(input_path):
    with open(input_path, mode='r') as input_file:
        existing_python_posts = json.load(input_file)
        return existing_python_posts


def is_post_unique(python_post, existing_python_posts):
    for existing_python_post in existing_python_posts:
        if (python_post['text'] == existing_python_post['text'])\
                and (python_post is not existing_python_post):
            return False
    return True


if __name__ == "__main__":
    path = 'py_posts.json'
    if os.path.exists(path):
        existing_python_posts = load_existing_python_posts(path)
    else:
        existing_python_posts = []
    python_posts = fetch_python_posts_from_vk()
    for py_post in python_posts:
        if is_post_unique(py_post, python_posts):
            existing_python_posts.append(py_post)
    with open(path, mode="w") as output_file:
        json.dump(existing_python_posts, output_file)
    print("posts added into file %s" % path)


