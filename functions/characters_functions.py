

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMedia
from telegram.ext import CallbackContext, ConversationHandler

from telegram.constants import ParseMode

#---------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------
import data.persistence as persistence
from functions.basic_functions import generate_id
from functions.characters_data import male_warrior_01, female_warrior_01, male_mage_01, female_mage_01
#from functions.characters_data import male_warrior, female_warrior, male_mage, female_mage



# 1. Asegúrate de que estos sean los IDs (Strings)
character_list = [male_warrior_01, female_warrior_01, male_mage_01, female_mage_01]

async def show_characters(update: Update, context: CallbackContext):
    # Usamos effective_chat para evitar errores de NoneType
    chat_id = update.effective_chat.id
    
    # ... aquí tu lógica de comprobación de usuario ...

    index = 0  # Empezamos por el primero
    
    keyboard = [
        [
            InlineKeyboardButton("Anterior", callback_data=f"PREV_{index}"),
            InlineKeyboardButton("Siguiente", callback_data=f"NEXT_{index}")
        ],
        [InlineKeyboardButton("Seleccionar", callback_data=f"SELECT_{index}")]
    ]
    
    # MANDAMOS EL STICKER CON EL TECLADO
    await context.bot.send_sticker(
        chat_id=chat_id,
        sticker=character_list[index],
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def characters_buttons(update: Update, context: CallbackContext):
    query = update.callback_query
    await query.answer() # Quita el reloj de arena del botón

    # SEPARAMOS LA ACCIÓN DEL ÍNDICE
    # Ejemplo: "NEXT_0" se convierte en ["NEXT", "0"]
    data = query.data.split("_")
    accion = data[0]
    indice_actual = int(data[1])

    # CALCULAMOS EL NUEVO ÍNDICE
    if accion == "NEXT":
        nuevo_indice = (indice_actual + 1) % len(character_list)
    elif accion == "PREV":
        nuevo_indice = (indice_actual - 1) % len(character_list)
    else:
        # Lógica para SELECT
        await query.edit_message_caption(caption="¡Personaje elegido!") # O lo que prefieras
        return

    # LA CLAVE: BORRAR Y ENVIAR EL SIGUIENTE
    try:
        await query.message.delete()
        
        # Creamos el nuevo teclado con el nuevo número
        nuevo_keyboard = [
            [
                InlineKeyboardButton("Anterior", callback_data=f"PREV_{nuevo_indice}"),
                InlineKeyboardButton("Siguiente", callback_data=f"NEXT_{nuevo_indice}")
            ],
            [InlineKeyboardButton("Seleccionar", callback_data=f"SELECT_{nuevo_indice}")]
        ]

        await context.bot.send_sticker(
            chat_id=query.message.chat_id,
            sticker=character_list[nuevo_indice],
            reply_markup=InlineKeyboardMarkup(nuevo_keyboard)
        )
    except Exception as e:
        print(f"Error al navegar: {e}")