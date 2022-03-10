from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton

API_TOKEN = 'Bot token here'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

main_button = KeyboardButton('Barchasi')
button1 = KeyboardButton('Dushanba')
button2 = KeyboardButton('Seshanba')
button3 = KeyboardButton('Chorshanba')
button4 = KeyboardButton('Payshanba')
button5 = KeyboardButton('Juma')
button6 = KeyboardButton('Shanba')

keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False).add(main_button).add(button1).add(button2).add(button3).add(button4).add(button5).add(button6)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum!\nMen Kitob tumani 1-IDUM 8-'A' sinf ning dars jadvalini chiqarib beraman", reply_markup=keyboard1)


@dp.message_handler()
async def kb_answer(message: types.Message):

    if message.text == "Barchasi":
        await message.answer(""" 
Dushanba: 
    Jismoniy Tarbiya
    Tarbiya 
    Biologiya
    Rus tili
    Ona tili
    Iqtisodiyot

Seshanba:
    Informatika
    Biologiya
    Geografiya
    Chizmachilik
    Texnologiya
    O'zbekiston Tarixi

Chorshanba:
    Adabiyot
    Rus tili
    O'zbekiston tarixi
    Ingliz tili
    Ona tili

Payshanba:
    Kimyo
    Adabiyot
    Fizika
    Ingliz tili
    Algebra
    Geometriya

Juma:
    Sinf Soati
    Huquq
    Jaxon Tarixi
    Geografiya
    Algebra
    Geometriya

Shanba: 
    Kimyo
    Ona Tili
    Fizika
    Ingliz Tili
    Jismoniy Tarbiya
    Algebra """)
        
        image = open("images/all.png", 'rb')
        await message.answer_photo(image)

    elif message.text == "Dushanba":
        await message.answer("Jismoniy Tarbiya\nTarbiya\nBiologiya\nRus tili\nOna tili\nIqtisodiyot")
        
        image1 = open("images/1.png", 'rb')
        await message.answer_photo(image1)

    elif message.text == 'Seshanba':
        await message.answer("Informatika\nBiologiya\nGeografiya\nChizmachilik\nTexnologiya\nO'zbekiston Tarixi")

        image2 = open("images/2.png", 'rb')
        await message.answer_photo(image2)

    elif message.text == 'Chorshanba':
        await message.answer("Adabiyot\nRus tili\nO'zbekiston tarixi\nIngliz tili\nOna tili")
        
        image3 = open("images/3.png", 'rb')
        await message.answer_photo(image3)

    elif message.text == 'Payshanba':
        await message.answer("Kimyo\nAdabiyot\nFizika\nIngliz tili\nAlgebra\nGeometriya")
        
        image4 = open("images/4.png", 'rb')
        await message.answer_photo(image4)

    elif message.text == 'Juma':
        await message.answer("Sinf Soati\nHuquq\nJaxon Tarixi\nGeografiya\nAlgebra\nGeometriya")

        image5 = open("images/5.png", 'rb')
        await message.answer_photo(image5)

    elif message.text == 'Shanba':
        await message.answer("Kimyo\nOna Tili\nFizika\nIngliz Tili\nJismoniy Tarbiya\nAlgebra")

        image6 = open("images/6.png", 'rb')
        await message.answer_photo(image6)

    else:
        await message.answer(f'Uzr {message.text} degan ma\'lumot topilmadi')

# @dp.message_handler()
# async def echo(message: types.Message):
#     await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
