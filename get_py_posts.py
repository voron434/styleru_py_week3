import json
import requests
import os

def get_new_py_posts():
    url = 'https://api.vk.com/method/newsfeed.search'
    params = {
        'q': 'python программирование -кожа -помогите -помощь',
        'count': 200,
        }
    new_py_posts = json.loads(requests.get(url, params).text)
    new_py_posts['response'].pop(0)
    return new_py_posts['response']

def chek_post(py_post, old_py_posts):
    for old_py_post in old_py_posts:
        if py_post['text'] == old_py_post['text']:
            return None
    return py_post

def get_old_posts(path):
    if not os.path.exists(path):
        return None
    with open(path, mode='r', encoding='utf-8') as my_file:
        data = json.load(my_file)
        return data

if __name__ == "__main__":
    #сценарий если файл уже есть
    path = input('Enter path to DataBase:')
    old_py_posts = get_old_posts(path)
    if not old_py_posts:
        print('File not found, sorry...')
        raise SystemExit
    py_posts = get_new_py_posts()
    for py_post in py_posts:
        if chek_post(py_post, old_py_posts):
            old_py_posts.append(py_post)
    path = 'vk_py_groups.json'
    with open(path, mode="w", encoding='utf-8') as my_file:
        json.dump(py_posts, my_file)

    #сценарий если файла еще нет
    py_posts = get_new_py_posts()
    posts_to_add = []
    #====================== вот это в функцию
    for py_post in py_posts:
        it_is_unic = True
        for another_py_post in py_posts:
            if ((py_post['text'] == another_py_post['text']) and (py_post['text'] is not another_py_post['text'])):
                it_is_unic = False
        if it_is_unic:
            posts_to_add.append(py_post)
    #=====================

    #dump
    path = 'vk_py_groups.json'
    with open(path, mode="w", encoding='utf-8') as my_file:
        json.dump(posts_to_add, my_file)
