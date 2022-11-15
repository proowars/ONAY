import locale
from datetime import datetime

import telebot
from PIL import Image, ImageDraw, ImageFont
from telebot import types

locale.setlocale(locale.LC_ALL, "")


token="5761540175:AAH4YDKufW2jI30kNYihUjxQfedq0egM36I"
bot=telebot.TeleBot(token)


img = Image.open('ABC.jpg')
img = img.copy()
text_position = (199, 715)
text_color = (0,0,0)
time = datetime.now().strftime("%A, %d %b. • %H:%M")
text = str(time)
fontsize = 20
font = ImageFont.truetype('font.ttf', fontsize)
img_draw = ImageDraw.Draw(img)
#  1слеваправа 2сверхкувниз 3праваправа 4снизувниз
img_draw.rectangle((190, 670, 400, 750), fill="#fcfcfe")
draw = ImageDraw.Draw(img)

draw.text(
    text_position,
    text,
    text_color,
    font,
    )

text_position2 = (138, 880)
fontsize2 = 23
timee = datetime.now(tzinfo= "UTC+2").strftime("%d/%m %H:%M")
draw2 = ImageDraw.Draw(img)
draw2.rectangle((138, 880, 400, 905), fill="#f0f1f3")
font2 = ImageFont.truetype('font.ttf', fontsize2)
qmg = ImageDraw.Draw(img)
qmg.text(
    text_position2,
    timee,
    text_color,
    font2
)

text_position4 = (25, 21)
time3 = datetime.now().strftime("%H:%M")
text3 = str(time3)
fontsize4 = 22
font4 = ImageFont.truetype('font.ttf', fontsize4)
img_draw = ImageDraw.Draw(img)
#  1слеваправа 2сверхкувниз 3праваправа 4снизувниз
img_draw.rectangle((20, 20, 82, 42), fill="#fcfcfe")
draw4 = ImageDraw.Draw(img)
draw4.text(
    text_position4,
    text3,
    text_color,
    font4,
    )


@bot.message_handler(content_types=['text', 'photo'],)
def start(message):
  bot.send_message(message.chat.id, "Введите код:" )
  bot.register_next_step_handler(message, bus)


  draw5 = ImageDraw.Draw(img)
  draw5.rectangle((101, 909, 300, 935), fill="#f0f1f3")

def bus(message):
  global kods
  fontsize1 = 25
  text_position1 = (463, 768)
  kods = message.text
  draw1 = ImageDraw.Draw(img)
  draw1.rectangle((460, 770, 550, 792), fill="#d0e6f3")
  font1 = ImageFont.truetype('font.ttf', fontsize1)
  amg = ImageDraw.Draw(img)
  amg.text(
      text_position1,
      kods,
      text_color,
      font1
      )

  bot.send_message(message.chat.id, "Введите номер автобуса:")
  bot.register_next_step_handler(message, kod)

def kod(message):
  busik = message.text

  text_position3 = (101, 909)
  fontsize3 = 25
  draw3 = ImageDraw.Draw(img)
  draw3.rectangle((100, 910, 127, 932), fill="#f0f1f3")
  font3 = ImageFont.truetype('font.ttf', fontsize3)


  num = ImageDraw.Draw(img)
  num.text(
      text_position3,
      busik+", #3023,80Т" ,
      text_color,
      font3
  )
  img.save('TESTTT.jpg')
  photo = "TESTTT.jpg"
  bot.send_photo(message.chat.id, open(photo, 'rb'))

print("START")
bot.infinity_polling()