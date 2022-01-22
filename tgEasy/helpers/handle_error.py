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

import os
import typing

import pyrogram

from ..config import Config


async def handle_error(
    error, m: typing.Union[pyrogram.types.Message, pyrogram.types.CallbackQuery]
):
    """
    ### `tgEasy.handle_error`
    - A Function to Handle the Errors in Functions.
    - This Sends the Error Log to the Log Group and Replies Sorry Message for the Users.
    - This is Helper for all of the functions for handling the Errors.

    - Parameters:
      - error:
        - The Exceptation.

      - m (`pyrogram.types.Message` or `pyrogram.types.CallbackQuery`):
        - The Message or Callback Query where the Error occurred.

    #### Exapmle
        .. code-block:: python
            from tgEasy import tgClient, handle_error
            import pyrogram

            app = tgClient(pyrogram.Client())

            @app.command("start")
            async def start(client, message):
            try:
                await message.reply_text("Hi :D') # I intentionally made an bug for Example :/
            except Exceptation as e:
                return await handle_error(e, message)
    """
    import traceback

    from .. import logging

    with open("crash.log", "w+", encoding="utf-8") as log:
        log.write(traceback.format_exc())
        log.close()
    if isinstance(m, pyrogram.types.Message):
        try:
            await m.reply_text(
                "An Internal Error Occurred while Processing your Command, the Logs have been sent to the Owners of this Bot. Sorry for Inconvenience"
            )
            await m._client.send_document(
                Config.LOGS, "crash.log", caption="Crash Report of this Bot"
            )
        except:
            pass
    if isinstance(m, pyrogram.types.CallbackQuery):
        try:
            await m.message.delete()
            await m.message.reply_text(
                "An Internal Error Occurred while Processing your Command, the Logs have been sent to the Owners of this Bot. Sorry for Inconvenience"
            )
            await m.message._client.send_document(
                Config.LOGS, "crash.log", caption="Crash Report of this Bot"
            )
        except:
            pass
    logging.exception(traceback.format_exc())
    os.remove("crash.log")
    return True
