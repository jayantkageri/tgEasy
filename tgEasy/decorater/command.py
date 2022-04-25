# tgEasy - Easy for a brighter Shine. A monkey pather add-on for Pyrogram
# Copyright (C) 2021 - 2022 Jayant Hegde Kageri <https://github.com/jayantkageri>

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

from ..config import Config
from ..helpers import handle_error


class Command(Scaffold):
    def command(
        self,
        command: typing.Union[str, list],
        pm_only: typing.Union[bool, bool] = False,
        group_only: typing.Union[bool, bool] = False,
        self_admin: typing.Union[bool, bool] = False,
        self_only: typing.Union[bool, bool] = False,
        handler: typing.Optional[list] = Config.HANDLERS,
        filter: typing.Union[pyrogram.filters.Filter, pyrogram.filters.Filter] = None,
        *args,
        **kwargs
    ):
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

        - handler (list) **optional**:
            - If set, the command will be handled by the specified Handler, By Default `Config.HANDLERS`.

        - self_admin (bool) **optional**:
            - If True, the command will only executeed if the Bot is Admin in the Chat, By Default False

        - filter (`~pyrogram.filters`) **optional**:
            - Pyrogram Filters, hope you know about this, for Advaced usage. Use `and` for seaperating filters.

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
                filter = (
                    pyrogram.filters.command(command, prefixes=handler)
                    & filter
                    & pyrogram.filters.me
                )
            else:
                filter = (
                    pyrogram.filters.command(command, prefixes=handler)
                    & filter
                    & pyrogram.filters.me
                )
        else:
            if self_only:
                filter = (
                    pyrogram.filters.command(command, prefixes=handler)
                    & pyrogram.filters.me
                )
            else:
                filter = pyrogram.filters.command(command, prefixes=handler)

        def wrapper(func):
            async def decorator(client, message: pyrogram.types.Message):
                if (
                    self_admin
                    and message.chat.type != pyrogram.enums.ChatType.SUPERGROUP
                ):
                    return await message.reply_text(
                        "This command can be used in supergroups only."
                    )
                if self_admin:
                    me = await client.get_chat_member(
                        message.chat.id, (await client.get_me()).id
                    )
                    if not me.status in (
                        pyrogram.enums.ChatMemberStatus.OWNER,
                        pyrogram.enums.ChatMemberStatus.ADMINISTRATOR,
                    ):
                        return await message.reply_text(
                            "I must be admin to execute this Command"
                        )
                    pass
                if (
                    group_only
                    and message.chat.type != pyrogram.enums.ChatType.SUPERGROUP
                ):
                    return await message.reply_text(
                        "This command can be used in supergroups only."
                    )
                if pm_only and message.chat.type != pyrogram.enums.ChatType.PRIVATE:
                    return await message.reply_text(
                        "This command can be used in PMs only."
                    )
                try:
                    await func(client, message)
                except pyrogram.errors.exceptions.forbidden_403.ChatWriteForbidden:
                    await client.leave_chat(message.chat.id)
                except BaseException as exception:
                    return await handle_error(exception, message)

            self.__client__.add_handler(
                pyrogram.handlers.MessageHandler(callback=decorator, filters=filter)
            )
            return decorator

        return wrapper
