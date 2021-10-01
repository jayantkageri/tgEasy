import asyncio
import os
import platform
import re
import sys

import pyrogram

import tgEasy


class Scaffold:
    def __init__(self):
        try:
            asyncio.get_event_loop()
        except RuntimeError:
            # This happens when creating Client instances inside different threads that don't have an event loop.
            # Set the main event loop in this thread.
            asyncio.set_event_loop(tgEasy.main_event_loop)

        self.__client__ = None

        def command(*args, **kwargs):
            pass

        def callback(*args, **kwargs):
            pass

        def adminsOnly(*args, **kwargs):
            pass

        async def check_rights(*args, **kwargs):
            pass

        async def is_admin(*args, **kwargs):
            pass
