from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext, ConversationHandler

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
import data.persistence as persistence
from functions.basic_functions import generate_id
from functions.characters_data import male_warrior_01, female_warrior_01, male_mage_01, female_mage_01
#from functions.characters_data import male_warrior, female_warrior, male_mage, female_mage





#Función que SOLO MUESTRA la galeria de personajes
async def show_characters(update:Update,context:CallbackContext):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)

    character_list = [male_warrior_01,female_warrior_01,male_mage_01,female_mage_01]

    keyboard = []

    #Se comprueba que el usuario existe, si existe, se le muestra la galeria
    if user_id not in persistence.REGISTERED_USERS:
        await context.bot.send_message(chat_id=chat_id, text=f"Debes registrarte primero")

    else:
        buttons = [
            InlineKeyboardButton("Previous", callback_data="Previous"),
            InlineKeyboardButton("Next", callback_data="NEXT")
        ]

        keyboard.append(buttons)
        reply_markup = InlineKeyboardMarkup(keyboard)

        for character in character_list:

            await context.bot.send_sticker(chat_id = chat_id, sticker = character)
            await update.message.reply_text(text=f"Hola",reply_markup=reply_markup)

