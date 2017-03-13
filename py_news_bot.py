from telegram.ext import Updater, CommandHandler
from getpass import getpass
import logging
import json
import random
import os


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text('Hi!')


def help(bot, update):
    update.message.reply_text('Help!')


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def choose_post_from(path):
    with open(path, mode='r') as python_posts_file:
        python_posts = json.load(python_posts_file)
        random.choice(python_posts)
    return random.choice(python_posts)


def make_link(python_post):
    from_id = python_post['from_id']*(-1)
    id = python_post['id']
    return 'https://vk.com/wall-%s_%s' % (from_id, id)


def make_text(python_post):
    return (python_post['text'][:200]+'...').replace('<br>', '\n')


def load_random_python_post(bot, update):
    input_path = 'py_posts.json'
    python_post = choose_post_from(input_path)
    update.message.reply_text(make_text(python_post))
    update.message.reply_text(make_link(python_post))


if __name__ == '__main__':
    token = getpass('Enter your telegram token')
    path = 'py_posts.json'
    if not os.path.exists(path):
        print('database deleted or not created')
        raise SystemExit
    updater = Updater(token)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("python_news", load_random_python_post))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()