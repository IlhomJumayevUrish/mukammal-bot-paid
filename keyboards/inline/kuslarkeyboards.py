from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
kursMenu=InlineKeyboardMarkup(
    inline_keyboard=[
       [
           InlineKeyboardButton(text="Web Backend",callback_data="backend"),

       ],
        [
            InlineKeyboardButton(text="Web Frontend",callback_data="frontend"),
        ],
        [

            InlineKeyboardButton(text="Foundation",callback_data="foundation"),
        ],
        [
            InlineKeyboardButton(text="Graphic Design",callback_data="grafik"),
        ],
    ],
    resize_keyboard=True
)
bizBotton=InlineKeyboardMarkup(
    inline_keyboard=[
       [
           InlineKeyboardButton(text="Instagram",url="https://www.instagram.com/opens_digital_school/"),
           InlineKeyboardButton(text="Facebook", url="https://www.facebook.com/Opensschool/"),
       ],
        [

           InlineKeyboardButton(text="Web sayt", url="http://opens.uz/"),
           InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/channel/UCZDcVLSG4CJnBD9p85DkGYg"),

        ],
    ],
    resize_keyboard=False
)
kursMenuBotton=InlineKeyboardMarkup(row_width=1)
python=InlineKeyboardButton(text="Kursga yozilish",callback_data="ruyxat")
kursMenuBotton.insert(python)