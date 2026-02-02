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

    keyboard = []

    #Se comprueba que el usuario existe, si existe, se le muestra la galeria
    if user_id not in persistence.REGISTERED_USERS:
        await context.bot.send_message(chat_id=chat_id, text=f"Debes registrarte primero")

    #Botones de Anterior, Siguiente y Seleccionar
    else:

        
        buttons = [
            InlineKeyboardButton("Previous", callback_data="PREVIOUS"),
            InlineKeyboardButton("Next", callback_data="NEXT")
        ]

        select_character = [InlineKeyboardButton("Select", callback_data="SELECT")]


        keyboard.append(buttons)
        keyboard.append(select_character)
        reply_markup = InlineKeyboardMarkup(keyboard)


        #Se muestra el primer personaje de la lista, y con los botones pasaremos a los demás
        await context.bot.send_sticker(chat_id = chat_id, sticker = male_warrior_01)
        await update.message.reply_text(text=f"Guerrero",reply_markup=reply_markup)


async def show_characters_buttons(update:Update,context:CallbackContext):
    chat_id = update.effective_chat.id
    user_id = generate_id(chat_id)

    query = update.callback_query
    await query.answer()

    data = query.data

    character_list = [male_warrior_01,female_warrior_01,male_mage_01,female_mage_01]

    
    
