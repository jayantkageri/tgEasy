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

import asyncio
import logging as logger
from datetime import datetime

import pyrogram
from pyrogram import client
from pyromod import listen
from pyromod.helpers import (array_chunk, bki, btn, force_reply, ikb, kb, kbtn,
                             ntb)
from pyromod.nav import Pagination

from .config import Config
from .decorater import *
from .helpers import *
from .scaffold import Scaffold

__version__ = "1.3.3"
__copyright__ = f"Copyright 2021 - {datetime.now().year} Jayant Hegde Kageri <github.com/jayantkageri>"
__license__ = "GNU Lesser General Public License v3 or later (LGPLv3+)"
logging = logger.getLogger("tgEasy")
main_event_loop = asyncio.get_event_loop()


class Methods(Command, Callback, AdminsOnly):
    pass


class tgClient(Methods, Scaffold):
    notice_displayed = False
    __client__ = None

    def __init__(self, client: pyrogram.Client):
        """
        ### `tgEasy.tgClient`
        - A Class for Initialising the tgEasy and it's Methods, Types and Functions
        - Parameters:
        - client (`pyrogram.Client`):
            - The Pyrogram Client

        #### Example
        .. code-block:: python
            from tgEasy import tgClient
            from pyrogram import Client

            app = tgClient(Client("my_account"))
        """
        super().__init__()
        self.__client__ = client
        tgClient.__client__ = self.__client__
        if not tgClient.notice_displayed:
            print(f"tgEasy v{__version__}, {__copyright__}")
            print(f"Licenced under the terms of {__license__}", end="\n\n")
            tgClient.notice_displayed = True

    def run(self):
        """
        ### `tgEasy.tgClient.run()`
        - Runs the `pyrogram.Client` by adding `tgEasy.tgClient.run()` in your main file.

        - This calls `pyrogram.Client.start()`, `pyrogram.idle()` and `pyrogram.Client.stop()`
        #### Example
        .. code-block:: python
            from tgEasy import tgClient
            from pyrogram import Client

            app = tgClient(Client)

            app.run()
        """
        if not Config.LOGS:
            logging.warning(
                "Log Group ID is't Set, Please set it else Bot will not able to Send Crash Logs"
            )
        logging.info("Starting the pyrogram.Client")
        try:
            self.__client__.start()
            self.__client__.send_message(
                Config.LOGS, "pyrogram.Client Started")
        except pyrogram.errors.exceptions.bad_request_400.PeerIdInvalid:
            logging.warning("Interact the Bot to your Log Chat Now")
        logging.info("Started the pyrogram.Client")
        logging.info("Idling the pyrogram.Client")
        pyrogram.idle()
        logging.info("Sending Message before Stopping the pyrogram.Client")
        try:
            self.__client__.send_message(
                Config.LOGS, "pyrogram.Client Stopped, If this is UnExpected check Logs"
            )
        except pyrogram.errors.exceptions.bad_request_400.PeerIdInvalid:
            logging.warning(
                "Unable to Send Message to Log Chat, Please Interact Bot with the Log Group while Running"
            )
        logging.info("Stopping the pyrogram.Client")
        self.__client__.stop()
        logging.info("Stopped the pyrogram.Client")

    def runClients(*args):
        """
        ### `tgEast.tgClint.runClients()`
        - Runs the Multiple `pyrogram.Client` of tgEasy by adding `tgEasy.tgClient.run()` in your main file and run.

        - This calls `pyrogram.Client.start()`, `pyrogram.idle()` and `pyrogram.Client.stop()`

        - Pass the tgEasy Clients in it.

        #### Example
        .. code-block:: python
            from tgEasy import tgClient
            import pyrogram

            app = tgClient(pyrogram.Client())
            app1 = tgClient(pyrogram.Client())

            tgClient.runClients(app, app1)
        """
        if not Config.LOGS:
            logging.warning(
                "Log Group ID is't Set, Please set it else Bot will not able to Send Crash Logs"
            )
        logging.info("Starting the pyrogram.Client")
        try:
            for clients in args:
                clients.__client__.start()
                try:
                    clients.__client__.send_message(
                        Config.LOGS, "pyrogram.Client Started"
                    ) if Config.LOGS else None
                except pyrogram.errors.exceptions.bad_request_400.PeerIdInvalid:
                    logging.warning("Interact the Bot to your Log Group Now")
                logging.info(f"Started the {client}")
        except pyrogram.errors.exceptions.bad_request_400.PeerIdInvalid:
            logging.warning("Interact with your Log Group Now")

        logging.info("Idling the pyrogram.Client")
        pyrogram.idle()

        for clients in args:
            try:
                logging.info(f"Sending Message before Stopping the {client}")
                clients.__client__.send_message(
                    Config.LOGS,
                    "pyrogram.Client Stopped, If this is UnExpected check Logs",
                ) if Config.LOGS else None

            except Exception:
                logging.warning(
                    "Unable to Send Message to Log Group, Please Interact Bot with the Log Group while Running"
                )

            clients.__client__.stop()
