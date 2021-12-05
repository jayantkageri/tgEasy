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

from ..helpers import check_rights, handle_error, is_admin


class AdminsOnly(Scaffold):
    def adminsOnly(
        self,
        permission: typing.Union[str, list],
        TRUST_ANON_ADMINS: typing.Union[bool, bool] = False,
    ):
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
                permissions = ""
                if not message.chat.type == "supergroup":
                    return await message.reply_text(
                        "This command can be used in supergroups only."
                    )
                if message.sender_chat and not TRUST_ANON_ADMINS:
                    return await message.reply_text(
                        "The Right Check for Anonymous Admins is in Development. So you cannot perform this Action for Now, If you don't want this and want to Allow Anonymous Admins for performing Actions in this time Please Contact Bot Owner."
                    )
                if not await is_admin(
                    message.chat.id, message.from_user.id, client=client
                ):
                    return await message.reply_text(
                        "Only admins can execute this Command!"
                    )
                if isinstance(permission, str):
                    if not await check_rights(
                        message.chat.id, message.from_user.id, permission, client=client
                    ):
                        return await message.reply_text(
                            f"You are Missing the following Rights to use this Command:\n{permission}"
                        )
                if isinstance(permission, list):
                    for perm in permission:
                        if not await check_rights(
                            message.chat.id, message.from_user.id, perm, client=client
                        ):
                            permissions += f"\n{perm}"
                    if not permissions == "":
                        return await message.reply_text(
                            f"You are Missing the following Rights to use this Command:{permissions}"
                        )
                try:
                    await func(client, message)
                except pyrogram.errors.exceptions.forbidden_403.ChatWriteForbidden:
                    await client.leave_chat(message.chat.id)
                except BaseException as exception:
                    await handle_error(exception, message)

            return decorator

        return wrapper
