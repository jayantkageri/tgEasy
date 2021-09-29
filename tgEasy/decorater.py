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

import os
import tgEasy
import typing
import pyrogram
from .config import Config
from .helpers import *
from tgEasy.scaffold import Scaffold


class Command(Scaffold):
    def command(self, command: typing.Union[str, list], pm_only: typing.Union[bool, bool] = False, group_only: typing.Union[bool, bool] = False, self_admin: typing.Union[bool, bool] = False, self_only: typing.Union[bool] = False, filter: typing.Union[pyrogram.filters.Filter, pyrogram.filters.Filter] = None, *args, **kwargs):
        """
    ### `tgEasy.tgClient.command`
    - A decorater to Register Commands in simple way and manage errors in that Function itself, alternative for `@pyrogram.Client.on_message(pyrogram.filters.command('command'))`
    - Parameters:
    - command (str || list):
        - The command to be handled for a function

    - group_only (bool) **optional**:
        - If True, the command will only executed in Groups only, By Default False.

    - pm_only (bool) **optional**:
        - If True, the command will only executed in Private Messages only, By Default False.

    - self_only (bool) **optional**:
        - If True, the command will only excute if used by Self only, By Default False.

    - self_admin (bool) **optional**:
        - If True, the command will only executeed if the Bot is Admin in the Chat, By Default False

    - filter (`~pyrogram.filters`) **optional**:
        - Pyrogram Filters, hope you know about this, for Advaced usage. By Default `~pyrogram.filters.edited` and this can't be changed. Use `and` for seaperating filters.

    #### Example
    .. code-block:: python
        import pyrogram
        from tgEasy import tgClient

        app = tgClient(pyrogram.Client())

        @app.command("start", group_only=False, pm_only=False, self_admin=False, self_only=False, pyrogram.filters.chat("777000") and pyrogram.filters.text)
        async def start(client, message):
            await message.reply_text(f"Hello {message.from_user.mention}")
        """
        if filter:
            if self_only:
                filter = pyrogram.filters.command(command, prefixes=Config.HANDLERS) & ~pyrogram.filters.edited & filter & filters.me if self_only else pyrogram.filters.command(
                    command, prefixes=Config.HANDLER) & ~pyrogram.filters.edited & filter & pyrogram.filters.me
            else:
                filter = pyrogram.filters.command(command, prefixes=Config.HANDLERS) & ~pyrogram.filters.edited & filter & filters.me if self_only else pyrogram.filters.command(
                    command, prefixes=Config.HANDLER) & ~pyrogram.filters.edited & filter
        else:
            if self_only:
                filter = pyrogram.filters.command(
                    command, prefixes=Config.HANDLERS) & ~pyrogram.filters.edited & pyrogram.filters.me
            else:
                filter = pyrogram.filters.command(
                    command, prefixes=Config.HANDLERS) & ~pyrogram.filters.edited

        def wrapper(func):
            async def decorator(client, message: pyrogram.types.Message):
                if self_admin and message.chat.type != "supergroup":
                    return await message.reply_text("This command can be used in supergroups only.")
                if self_admin:
                    me = await client.get_me()
                    mee = await client.get_chat_member(message.chat.id, me.id)
                    if not mee.status == "admin":
                        return await message.reply_text("I must be admin to execute this Command")
                    pass
                if group_only and message.chat.type != "supergroup":
                    return await message.reply_text("This command can be used in supergroups only.")
                if pm_only and message.chat.type != "private":
                    return await message.reply_text("This command can be used in PMs only.")
                try:
                    await func(client, message)
                except pyrogram.errors.forbidden_403.ChatWriteForbidden:
                    await client.leave_chat(message.chat.id)
                except BaseException as exception:
                    return await handle_error(exception, message)
            self.__client__.add_handler(pyrogram.handlers.MessageHandler(
                callback=decorator, filters=filter))
            return decorator
        return wrapper


class Callback(Scaffold):
    def callback(self, data: typing.Union[str, list], self_admin: typing.Union[bool, bool] = False, filter: typing.Union[pyrogram.filters.Filter, pyrogram.filters.Filter] = None, *args, **kwargs):
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
                    me = await client.get_me()
                    mee = await client.get_chat_member(message.chat.id, me.id)
                    if not mee.status == "admin":
                        return await message.reply_text("I must be admin to execute this Command")
                    pass
                try:
                    await func(client, CallbackQuery)
                except pyrogram.errors.exceptions.forbidden_403.ChatAdminRequired:
                    pass
                except BaseException as e:
                    return await handle_error(e, CallbackQuery)
            self.__client__.add_handler(
                pyrogram.handlers.CallbackQueryHandler(decorator, filter))
            return decorator
        return wrapper


class AdminsOnly(Scaffold):
    def adminsOnly(self, permission: typing.Union[str, list], TRUST_ANON_ADMINS: typing.Union[bool, bool] = False):
        """
    ### `tgEasy.tgClient.adminsOnly`
    - A decorater for running the function only if the admin have the specified Rights.
    - We are still Working on this to make it to check Rights for Anonoymous Admins, Stay Tuned.
    - Parameters:
    - permission (str):
        - Permission which the User must have to use the Functions

    - TRUST_ANON_ADMIN (bool) **optional**:
        - If User is Anonymous Admin also, It Runs the Function, By Default False

    ### Example
    .. code-block:: python
        from tgEasy import tgClient
        import pyrogram

        app = tgClient(pyrogram.Client())

        @app.command("start")
        @app.adminsOnly("can_change_info")
        async def start(client, message):
            await message.reply_text(f"Hello Admin {message.from_user.mention}")
        """
        def wrapper(func):
            async def decorator(client, message):
                if not message.chat.type == "supergroup":
                    return await message.reply_text("This command can be used in supergroups only.")
                if message.sender_chat:
                    if not TRUST_ANON_ADMINS:
                        return await message.reply_text(
                            "The Right Check for Anonymous Admins is in Development. So you cannot perform this Action for Now, If you don't want this and want to Allow Anonymous Admins for performing Actions in this time Please Contact Bot Owner."
                        )
                if not await is_admin(message.chat.id, message.from_user.id, client=client):
                    return await message.reply_text("Only admins can execute this Command!")
                if not await check_rights(message.chat.id, message.from_user.id, permission, client=client):
                    return await message.reply_text(f"You are Missing the following Rights to use this Command:\n{permission}")
                try:
                    await func(client, message)
                except pyrogram.errors.exception.forbidden_403.ChatWriteForbidden:
                    await client.leave_chat(message.chat.id)
                except BaseException as exception:
                    await handle_error(exception, message)
            return decorator
        return wrapper
