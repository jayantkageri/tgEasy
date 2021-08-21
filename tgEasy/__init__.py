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

import pyrogram
from .config import Config
from pyromod import listen
from pyromod.helpers import ikb, array_chunk, bki, btn, force_reply, kb, kbtn, ntb
from pyromod.nav import Pagination

from .decorater import *
from .helpers import *
import logging
logging.basicConfig(level=logging.INFO)
__version__ = "0.1.0"
__copyright__ = "Copyright 2021 Jayant Hegde Kageri <github.com/jayantkageri>"
__license__ = "GNU Lesser General Public License v3 or later (LGPLv3+)"

app = pyrogram.Client(
    session_name="pyrogram",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
    plugins={"root": Config.PLUGINS} if Config.PLUGINS else None
    )
app.__doc__ = "`~pyrogram.Client`"
client, client.__doc__ = app, app.__doc__

def run():
    """
### `tgEasy.run()`
- Runs the `pyrogram.Client` by adding `tgEasy.run()` in your main file and run.

- This calls `pyrogram.Client.start()`, `pyrogram.idle()` and `pyrogram.Client.stop()`
#### Example
.. code-block:: python
    from tgEasy import run

    run()
    """
    import logging
    print(f"tgEasy v{__version__}, {__copyright__}")
    print(f"Licenced under the terms of {__license__}", end='\n\n')
    if not Config.LOGS:
        raise NameError("Log Group ID is't Set, tgEasy Quitting")
    logging.info("Starting the pyrogram.Client")
    try:
        app.start()
        app.send_message(Config.LOGS, "pyrogram.Client Started")
    except pyrogram.errors.exceptions.bad_request_400.AccessTokenExpired:
        raise AccessTokenExpired("[400 ACCESS_TOKEN_EXPIRED]: The bot token has expired, Use Diffrent one or change it to the Correct one")
    except pyrogram.errors.exceptions.bad_request_400.PeerIdInvalid:
        logging.warning("Interact the Bot to your Log Group Now")
        pass
    if Config.PLUGINS and not os.path.exists(Config.PLUGINS):
        logging.warn(f"There is no directory named {Config.PLUGINS}, tgEasy Quitting")
        quit()
    logging.info("Started the pyrogram.Client")
    logging.info("Idling the pyrogram.Client")
    pyrogram.idle()
    logging.info("Sending Message before Stopping the pyrogram.Client")
    try:
        app.send_message(
            Config.LOGS, "pyrogram.Client Stopped, If this is UnExpected check Logs")
    except pyrogram.errors.exceptions.bad_request_400.PeerIdInvalid:
        logging.warning("Unable to Send Message to Log Group, Please Interact Bot with the Log Group while Running")
        pass
    logging.info("Stopping the pyrogram.Client")
    app.stop()
    logging.info("Stopped the pyrogram.Client")