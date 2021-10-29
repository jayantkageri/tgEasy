<!--
tgEasy - Easy for a brighter Shine. A monkey pather add-on for Pyrogram
Copyright (C) 2021 Jayant Hegde Kageri <https://github.com/jayantkageri>

This file is part of tgEasy.

tgEasy is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

tgEasy is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with tgEasy.  If not, see <http://www.gnu.org/licenses/>.
-->

<p>
    <h1 align="center"><a href="https://github.com/jayantkageri/tgEasy"><img src="https://i.imgur.com/wfim4Jb.png" alt="tgEasy"></a></h1>
    <!-- <h3 align="center">Easy for a brighter Shine, A Monkey Patcher add-on for Pyrogram</h3><br> -->
</p>

# tgEasy
```python
from tgEasy import tgClient
from pyrogram import Client

app = tgClient(Client("my_account"))

@app.command("start", group_only=True)
async def start(client, message):
    await message.reply_text(f"Hello {message.from_user.mention}")

app.run()
```

## Featurs
- **Easy**: You can install tgEasy with pip and start building your applications right away.

- **Fast**: With the [Pyrogram](https://docs.pyrogram.org), tgEasy's speed is enhanced

- **Type-hinted**: Types and methods are all type-hinted, enabling excellent editor support.

- **Asynchronous**: With the Asynchronous, tgEasy can handle Multiple Requests at a time.

- **Documented**: All of the available methods, types and functions are well documented.

- **Comprehensive**: With the help of [Pyrogram](https://docs.pyrogram.org), Execute any advanced action an official client is able to do, and even more.

### Requirements

- Python 3.7 or higher.
- A [Telegram API key](https://docs.pyrogram.org/intro/setup#api-keys).

### Installing

``` bash
pip3 install tgEasy
```

### Resources

- The docs contain lots of resources to help you get started with tgEasy: https://github.com/jayantkageri/tgEasy/wiki.
- Seeking extra help? Come join and ask our community: https://t.me/tgEasyNews.
- For other kind of inquiries, you can send a [message](https://t.me/jayantkageri) or an [e-mail](mailto:jayantkageri@gmail.com)

## Copyright and Licence
- tgEasy is Licenced under the Terms and Conditions of OSI Approved GNU Lesser General Public License v3 or later (LGPLv3+).
- Copyright 2021 Jayant Hegde Kageri <https://github.com/jayantkageri>.
- This Projects Codes may contain snippets or codes of [Pyrogram](https://github.com/pyrogram/pyrogram).
- Pyrogram - Telegram MTProto API Client Library for Python. Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
- This Project uses [Pyromod](https://github.com/usernein) for making it more convenient.
- Pyromod - A monkeypatcher add-on for Pyrogram
- Copyright (C) 2020 - 2021 Cezar <https://github.com/usernein>
