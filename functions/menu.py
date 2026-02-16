from telegram import BotCommand

async def menu(application):
    commands = [
        BotCommand("start", "Registrarse en el sistema"),
        BotCommand("characters", "Elige a un personaje"),
        BotCommand("status", "Comprueba el estado del personaje"),
        BotCommand("addtask", "Añade una nueva tarea"),
        BotCommand("showtasks", "Lista de tareas pendientes"),
        BotCommand("comtask", "Muestra la lista de tareas pendientes y permite marcar las tareas realizadas como completadas"),
        BotCommand("deltask", "Borra una tarea de la lista de tareas pendientes"),
        BotCommand("deluser", "Elimina tu usuario del sistema")       
    ]

    await application.bot.set_my_commands(commands)

