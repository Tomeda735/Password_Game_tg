import asyncio
import os
import random

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Message
from telegram.ext import Application, ContextTypes, CommandHandler, CallbackQueryHandler, InlineQueryHandler

from bot import bot_messages as bm


class Bot:

    def __init__(self):
        self.bot = Application.builder() \
            .token(os.getenv("BOT_TOKEN")) \
            .build()
        self.bot.add_handler(CommandHandler(bm.START_CMD, self.start))
        self.bot.add_handler(CommandHandler(bm.PLAY_CMD, self.play))
        self.bot.add_handler(CommandHandler(bm.TURN_CMD, self.turn))
        self.bot.add_handler(CommandHandler(bm.HELP_CMD, self.help))

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=bm.START)

    async def game(self, arg: str, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if context.user_data.get("code"):
            attempts = context.user_data["code"][1]
            code = context.user_data["code"][0]
            if attempts == bm.ATTEMPTS:
                await context.bot.send_message(chat_id=update.effective_chat.id, text=bm.MOREATTEMPTS)
                context.user_data.pop("code")
                return

            h = []
            for i in arg:
                try:
                    h.append(int(i))
                except ValueError:
                    await context.bot.send_message(chat_id=update.effective_chat.id, text=bm.ONLYNUM)
                    return

            arg = h
            if len(arg) != bm.LENPASSWORD:
                await context.bot.send_message(chat_id=update.effective_chat.id,
                                               text=bm.ONLYLENNUM)
                return
            b = 0
            if (arg[0] == code[0]) and (arg[1] == code[1]) and (arg[2] == code[2]) and (arg[3] == code[3]):
                await context.bot.send_message(chat_id=update.effective_chat.id, text=bm.WIN)
                context.user_data.pop("code")
                return

            for i in range(len(arg)):
                if arg[i] == code[i]:
                    await context.bot.send_message(chat_id=update.effective_chat.id,
                                                   text=bm.coincidencesposicion(i))

            for i in range(len(code)):
                if code[i] in arg:
                    b += 1

            await context.bot.send_message(chat_id=update.effective_chat.id,
                                           text=bm.coincidences(b))
            attempts += 1
            context.user_data["code"] = code, attempts
        else:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=bm.HELPSTART)

    async def turn(self, update: Update, context: ContextTypes.DEFAULT_TYPE):

        if len(context.args) == 0:
            await context.bot.send_message(chat_id=update.effective_chat.id, text=bm.HELPTURN)
            return
        args = context.args[0]
        await self.game(args, update, context)

    async def play(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        code = str(random.randint(1111, 9999))
        code = [int(i) for i in code]
        context.user_data["code"] = code, 0
        await context.bot.send_message(chat_id=update.effective_chat.id, text=bm.INPUTRASSWORD)

    async def help(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await context.bot.send_message(chat_id=update.effective_chat.id, text=bm.HELPRULES)
