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


async def send_typing(
    m: typing.Union[pyrogram.types.Message, pyrogram.types.CallbackQuery],
):
    """
    ### `tgEasy.send_typing`
    - A Function to Send the Typing Status to the Chat.

    - Parameters:
      - m (`pyrogram.types.Message` || `pyrogram.types.CallbackQuery`):
        - Message or Callbackquery.

    #### Example
        .. code-block:: python
            from tgEasy import tgClinet, send_typing
            import pyrogram

            app = tgClient(pyrogram.Client())

            @app.command("start")
            async def start(client, message):
            await send_typing(message)
            await message.reply_text("Hello")
    """
    if isinstance(m, pyrogram.types.Message):
        message = m
    if isinstance(m, pyrogram.types.CallbackQuery):
        message = m.message
    for i in range(3):
        return await message._client.send_chat_action(message.chat.id, "typing")
