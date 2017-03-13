# styleru_py_week3
This is result of my work with vk.com api and bot from telegram.
# 1. get_py_posts #
First script would find news posted in 24 hours from "run" moment about Python with no posts about helping someone or mabye shoes from python skin.    
After running result would be in file 'py_posts.json'.    
You could append new news into this file just running this script again    
#### example usage:
    $python get_py_posts.py.py   
    posts added into file 'py_posts.lson' 
***
# 2. py_news_bot #
Second script is a bot for telegram witch would send 1 random post from the first task after command "/python_news"
You need enter telegram bot token, wich you could get from another bot, just ask him [here](https://web.telegram.org/#/im?p=@BotFather). Print '/start' , than '/newbot', than follow his insructions.    
Whan your own bot wold be registrated - run this script and tell him telegram bot token, known from BotFather.    
Than print '/python_news' to your own bot.
#### example usage:  
    $python py_news_bot.py
than, in telegram:

    /python news
    
    Занимательное программирование на Python 
 
    1. Занимательное программирование на Python
    2. Переменные, строки ,числа 
    3. Математические операции. 
    4. Изменение типов данных 
    5. Ввод ...
    
    https://vk.com/wall-136721612_1001
