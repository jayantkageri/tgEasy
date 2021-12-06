# tgEasy - Easy for a brighter Shine. A monkey pather add-on for Pyrogram
# Copyright (C) 2021 Jayant Hegde Kageri <https://github.com/jayantkageri>

# This file is part of tgEasy.

# tgEasy is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# tgEasy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with tgEasy.  If not, see <http://www.gnu.org/licenses/>.

import typing

import pyrogram

from tgEasy.scaffold import Scaffold

from ..helpers import handle_error


class Callback(Scaffold):
    def callback(
        self,
        data: typing.Union[str, list],
        self_admin: typing.Union[bool, bool] = False,
        filter: typing.Union[pyrogram.filters.Filter, pyrogram.filters.Filter] = None,
        *args,
        **kwargs,
    ):
        """
        ### `tgEasy.tgClient.callback`

        - A decorater to Register Callback Quiries in simple way and manage errors in that Function itself, alternative for `@pyrogram.Client.on_callback_query(pyrogram.filters.regex('^data.*'))`
        - Parameters:
        - data (str || list):
            - The callback query to be handled for a function

        - self_admin (bool) **optional**:
            - If True, the command will only executeed if the Bot is Admin in the Chat, By Default False

        - filter (`~pyrogram.filters`) **optional**:
            - Pyrogram Filters, hope you know about this, for Advaced usage. Use `and` for seaperating filters.

        #### Example
        .. code-block:: python
            import pyrogram
            from tgEasy import tgClient

            app = tgClient(pyrogram.Client())

            @app.command("start")
            async def start(client, message):
                await message.reply_text(
                f"Hello {message.from_user.mention}",
                reply_markup=pyrogram.types.InlineKeyboardMarkup([[
                    pyrogram.types.InlineKeyboardButton(
                    "Click Here",
                    "data"
                    )
                ]])
                )

            @app.callback("data")
            async def data(client, CallbackQuery):
            await CallbackQuery.answer("Hello :)", show_alert=True)
        """
        if filter:
            filter = pyrogram.filters.regex(f"^{data}.*") & args["filter"]
        else:
            filter = pyrogram.filters.regex(f"^{data}.*")

        def wrapper(func):
            async def decorator(client, CallbackQuery: pyrogram.types.CallbackQuery):
                if self_admin:
                    me = await client.get_chat_member(
                        CallbackQuery.message.chat.id,
                        (await client.get_me()).id,
                    )
                    if not me.status in ("creator", "administrator"):
                        return await CallbackQuery.message.edit_text(
                            "I must be admin to execute this Command",
                        )
                    pass
                try:
                    await func(client, CallbackQuery)
                except pyrogram.errors.exceptions.forbidden_403.ChatAdminRequired:
                    pass
                except BaseException as e:
                    return await handle_error(e, CallbackQuery)

            self.__client__.add_handler(
                pyrogram.handlers.CallbackQueryHandler(decorator, filter),
            )
            return decorator

        return wrapper
