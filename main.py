import telebot
from telebot import types
import time

TOKEN = '5016368803:AAFYeZ98QuL5HnRgTL30Xxl-JFB33kjsCtA'
telebot.TeleBot(TOKEN)


@bot.inline_handler(lanbda query: query.query == 'test')
def test(inline_query):
    r = types.InlineQueryResultArticle(
        #The id our inline result
        id='1',
        title='test',
        input_message_content=types.InputTextMessageContent(
            'I am a message'
        )
    )
    bot.answer_inline_query(inline_query.id, [r])

    @bot.inline_handler(lanbda query: query.query == 'image')
    def image(inline_query):
        r = types.InlineQueryResultPhoto(
            id='11'
            photo_url='https://yt3.ggpht.com/3kmvsf3NNYy4XLy3hKc2ZVF8O-XkSaahtwUr3KW-YzJKMJsy-g2HePIayrh-JnXWbilYQ6n_=s900-c-k-c0x00ffffff-no-rj'
            thumb_url='http://assets.stickpng.com/images/580b57fcd9996e24bc43c4c4.png'
        )

        bot.answer_inline_query(inline_query.id, [r])

while True:
    try:
        bot.polling(True)
    except:
        time.sleep(5)