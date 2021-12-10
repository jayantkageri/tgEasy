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

import asyncio

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
