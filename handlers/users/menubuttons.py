import logging

from aiogram.dispatcher import FSMContext

import Image
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, KeyboardButtonPollType, KeyboardButton
from keyboards.inline.kuslarkeyboards import kursMenu, bizBotton, kursMenuBotton
from keyboards.default.menuBottom import menuAsosiy, topmenu
from aiogram import types, bot
from loader import dp
import logging
from data.config import ADMINS
from states.userData import PersonalData
from aiogram.dispatcher.filters import Regexp

@dp.message_handler(Command('menu'),state=PersonalData.phoneNum)
@dp.message_handler(Command('menu'),state=PersonalData.fullName)
@dp.message_handler(Command('start'),state=PersonalData.phoneNum)
@dp.message_handler(Command('start'),state=PersonalData.fullName)
async def bot_menu(message: Message, state: FSMContext):
    await state.finish()
    await message.answer("Asosiy menu", reply_markup=menuAsosiy)

@dp.message_handler(Command('menu'))
@dp.message_handler(Command('start'))

async def bot_menu(message: Message, state: FSMContext):
    await message.answer("Asosiy menu", reply_markup=menuAsosiy)



@dp.message_handler(Command('chat'))
async def bot_chat(message: Message):
    await message.answer(f" User {message.from_user.first_name}")
    await message.answer("Chat hali ishlab chiqilmadi!")


@dp.message_handler(text="💻 Kurslar bilan tanishing!")
async def show_kurs(message: Message):
    await message.answer("Kurslar bilan tanishing!", reply_markup=kursMenu)
    # await message.answer("...", reply_markup=topmenu)


@dp.message_handler(text="📆 Ochiq darslar vaqti!")
async def show_darsvaqti(message: Message):
    await message.answer("Kerakli kurs uchun ochiq dars tanlang!", reply_markup=kursMenu)

#
# @dp.message_handler(text="🏢 Biz haqimizda!")
# async def show_info(message: Message):
#
#     await message.answer_photo(open('Image/imags.png', 'rb'),"👩‍💻 <b>Opens digital school</b> | Raqamli kasblar markazi \n 📞<b> Тел.:</b> (99) 644-08-80"
# ,reply_markup=bizBotton)


@dp.message_handler(text="📍 Location&Contact")
async def show_locationcontact(message: Message):
    await message.answer_location(41.27763, 69.20318)
    await message.answer_contact("+998996440880","Admin bilan bog'laning!")

@dp.callback_query_handler(text="frontend")
async def call_backend(call: CallbackQuery):
    global x
    x="Web backend"
    await call.message.answer_photo("https://t.me/opens_school/22","Dasturlashni o'rganmoqchisiz lekin qaysi yo'nalishdan va qanday boshlashni bilmayapsizmi? Unda Web dasturlash \"Frontend\" kursi aynan siz uchun!\
Ushbu kurs mentori tajribali dasturchi bo'lib, kurs ustoz shogird shaklida olib boriladi. Kursda talabar quyidagi texnologiyalarni o'rganadi va mustaqil to'laqonli web sayt yaratishni o'rganadi:\n\
- HTML\n\
- CSS\n\
- Bootstrap\n\
- SAS\n\
- JS\n\
- React\n\n\
📌Talaba kursni tamomlagandan so\'ng o\'z portfoliosi va CVsiga ega bo\'lishi ta\'minlanadi.\n\n\
💥Muvaffaqiyatli bitirgan talabalarga ishga joylashishda amaliy yordam ko\'rsatiladi. \n\n\
❗️Shoshiling joylar chegaralangan.\n\n\
Opens digital school | Центр диджитал профессий\n\n\
🤖 Бот: @opensuzbot\n\
📞 Тел.: (99) 644-08-80\n\
🏢 Офис: Метро Чиланзар.\n\
📍 Ориентир: Метро Чиланзар, Корзинка. Между Корзинки и кафе Loook",reply_markup=kursMenuBotton)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="backend")
async def call_frontend(call: CallbackQuery):
    global x
    x="Web frontend"
    await call.message.answer_photo("https://t.me/opens_school/24","🐍Python asoschisi Gvido van Rossumning asosiy maqsadi oddiy va odamlar uchun tushunarli bo'lgan dasturlash tilini yaratish edi.\n\
Har qanday tilni o'rganish qat'iyat va intizomni talab qiladi. Ammo Python bu ma'noda, ayniqsa, yangi boshlaganlar uchun eng qulaylaridan biri hisoblanadi. Oddiy sintaksis o'rganish, o'qish va amalda ishlatishni osonlashtiradi. Aynan shu taraflari uni juda mashhur qildi.\n\
📊Ohirgi 2 yillik ya'ni 2020-2021 yillarda ushbu til hatto Java dasturlash tillaridan ham ilgarilab ketti.\n\n\
🌐Hozirda dunyoning eng yirik IT kompaniyalari ham python tilini tanlashmoqda. Bularga misol qilib:\n\n\
- Google\n\
- Dropbox\n\
- Netscape\n\
- Facebook\n\
- Yandex\n\
- Microsoft\n\
- Intel\n\n\
👶Demak, siz ha siz python dasturlash tilini o’rganishni bugundan boshlashingiz munkin.\n\n\
Opens digital school | Центр диджитал профессий\n\n\
🤖 Бот: @opensuzbot\n\
📞 Тел.: (99) 644-08-80\n\
🏢 Офис: Метро Чиланзар.\n\
📍 Ориентир: Метро Чиланзар, Корзинка. Между Корзинки и кафе Loook",reply_markup=kursMenuBotton)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="foundation")
async def call_foundation(call: CallbackQuery):
    await call.message.answer_photo("https://www.instagram.com/p/CSMGlM8qrjs/","Ushbu yulduz futbolchiga avvalboshdan ikki asosiy da'vogar bor edi: faqat ikki klub - Messining yaqin do‘stlari to‘p suradigan va moliyaviy tomondan baquvvat bo‘lgan «PSJ» hamda arab shayxlarining yana bir klubi, Messining yoshlikdagi ustozi Xosep Gvardiola ishlayotgan «Manchester Siti». Ammo «shaharliklar» Messi «Barselona»dan ketishi e'lon qilinishi arafasida angliyalik yarimhimoyachi Jyek Grilishni 100 million funtga sotib oldi va poygadan chiqdi.")
    await call.answer(cache_time=60)
@dp.callback_query_handler(text="grafik")
async def call_grafik(call: CallbackQuery):
    await call.message.answer_photo("https://t.me/opens_school/23",
    "Zamonaviy kasb bo'lmish \"Grafik dizayn\" kursiga start berildi. Ushbu kurs mentori tajribali grafik dizayner tomonidan ustoz shogird shaklida olib boriladi. Kursda talabar quyidagi dasturlarda ishlashni va san'at asarlarini yaratishni o'rganadi: \n\
    👨‍🎨Adobe Photoshop\n\
    🦸‍♂Adobe illustrator \n\
    ✍Figma \n\n"
    "📌Talaba kursni tamomlagandan so'ng o'z portfoliosi va CVsiga ega bo'lishi ta'minlanadi. \n\n"
    "👨‍💻Darslar haftasiga 3 marta 2 soatdan olib boriladi.\n\n"
    "💣Eng asosiysi Siz darslarni online yoki offline shaklini tanlashingiz mumkin.\n\n"
    "💥Muvaffaqiyatli bitirgan talabalarga ishga joylashishda amaliy yordam ko'rsatiladi. \n\n"
    "❗️Joylar soni cheklangan.\n\n"
    "Opens digital school | Raqamli kasblar markazi\n"
    "Tel.: (99) 644-08-80",reply_markup=kursMenuBotton)
    await call.answer(cache_time=60)

@dp.callback_query_handler(text="ruyxat")
async def call_back_ruyxat(call: CallbackQuery):
    await call.message.answer("<b>Ism, familiyangizni kiriting:</b>")
    await PersonalData.fullName.set()
    await call.answer(cache_time=60)
@dp.message_handler(state=PersonalData.fullName)
async def answer_fullname(message:types.Message,state:FSMContext):
    fullname=message.text
    await state.update_data(
        {"fullName":fullname}
    )
    await message.answer("<b>📞Aloqa:</b>\n\nBog`lanish uchun raqamingizni kiriting:\nMasalan, <i>+99890000000</i>")
    await PersonalData.phoneNum.set()



TelRegeX="^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
@dp.message_handler(Regexp(TelRegeX),state=PersonalData.phoneNum)
async def answer_phone(message: types.Message, state: FSMContext):
    phoneNum = message.text
    await state.update_data(
        {"phoneNum": phoneNum}
    )
    await state.update_data(
        {"kursName": x}
    )
    data=await state.get_data()
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, f"<b>Ism familiya:</b> {data.get('fullName')} \n<b>Kurs nomi:<b/> {data.get('kursName')} \n<b>Telefon:</>{data.get('phoneNum')}")
        except Exception as err:
            logging.exception(err)
    await state.finish()

    await message.answer(f"Tabriklaymiz {data.get('fullName')} siz {x} kursidan ro'yxatdan o'tdingiz! \n {x} uchun eng yaqin ochiqdars  shu xafta juma kuni soat 15:00 da bo'ladi.")

@dp.message_handler(state=PersonalData.phoneNum)
async def answer_phone(message: types.Message, state: FSMContext):
    text="<b>Telefon nomer xato! \n Misol:👉 +99890000000 👈</b>"
    await message.answer(text)



#
    # @dp.message_handler(content_types=types.ContentTypes.CONTACT)
    # async def show_contact(message: Message):
    #     for admin in ADMINS:
    #         try:
    #             await dp.bot.send_message(admin,message["contact"]["phone_number"])
    #
    #         except Exception as err:
    #             logging.exception(err)
