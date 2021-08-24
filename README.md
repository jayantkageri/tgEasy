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
from tgEasy import tgClient, command
from pyrogram import Client

app = tgClient(Client("my_account"))

@command("start", group_only=True)
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
  

## Configuration

 Make an .env or set the Following in your Environment Variables.
  - `LOGS` - Log Group ID
  - `PLUGINS` - Plugins Directory Path where your Plugins are located, By Default it is `plugins` Directory
  - `HANDLERS` - The Command Handlers, By Default it is `/` and `!`

## Documatation
- Never name `tgEasy` for your any files/directory 

### `tgEasy.tgClient`
- A Class for Initialising the tgEasy and it's Methods, Types and Functions
- Parameters:
  - client (`pyrogram.Client`):
    - The Pyrogram Client

#### Example
```python
from tgEasy import tgClient
from pyrogram import Client

app = tgClient(Client("my_account"))
```
### `tgEasy.command`
- A decorater to Register Commands in simple way and manage errors in that Function itself, alternative for `@pyrogram.Client.on_message(pyrogram.filters.command('command'))`
- Parameters:
  - command (str || list):
    - The command to be handled for a function
  
  - group_only (bool) **optional**:
    - If True, the command will only executed in Groups only, By Default False.
  
  - pm_only (bool) **optional**:
    - If True, the command will only executed in Private Messages only, By Default False.

  - self_admin (bool) **optional**:
    - If True, the command will only executeed if the Bot is Admin in the Chat, By Default False

  - self_only (bool) **optional**:
    - If True, the command will only executeed if the Bot is Admin in the Chat, By Default False
  
  - filter (`~pyrogram.filters`) **optional**:
    - Pyrogram Filters, hope you know about this, for Advaced usage. By Default `~pyrogram.filters.edited` and this can't be changed. Use `and` for seaperating filters.

#### Example
```python
import pyrogram
from tgEasy import command

@command("start", group_only=False, pm_only=False, self_admin=False, self_only=False, pyrogram.filters.chat("777000") and pyrogram.filters.text)
async def start(client, message):
    await message.reply_text(f"Hello {message.from_user.mention}")
```

### `tgEasy.callback`

- A decorater to Register Callback Quiries in simple way and manage errors in that Function itself, alternative for `@pyrogram.Client.on_callback_query(pyrogram.filters.regex('^data.*'))`
- Parameters:
  - data (str || list):
    - The callback query to be handled for a function

  - self_admin (bool) **optional**:
    - If True, the command will only executeed if the Bot is Admin in the Chat, By Default False
  
  - filter (`~pyrogram.filters`) **optional**:
    - Pyrogram Filters, hope you know about this, for Advaced usage. Use `and` for seaperating filters.

#### Example
```python
import pyrogram
from tgEasy import command, callback

@command("start")
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

@callback("data")
async def data(client, CallbackQuery):
  await CallbackQuery.answer("Hello :)", show_alert=True)
```
### `tgEasy.adminsOnly`
- A decorater for running the function only if the admin have the specified Rights.
<!-- - If the admin is Anonymous Admin, it also checks his rights by making an Callback -->
- We are still Working on this to make it to check Rights for Anonoymous Admins, Stay Tuned.
- Parameters:
  - permission (str):
    - Permission which the User must have to use the Functions
- 
  - TRUST_ANON_ADMIN (bool) **optional**:
    - If User is Anonymous Admin also, It Runs the Function, By Default False

#### Example
```python
from tgEasy import command, adminsOnly

@command("start")
@adminsOnly("can_change_info")
async def start(client, message):
    await message.reply_text(f"Hello Admin {message.from_user.mention}")
```

### `tgEasy.tgClient.run()`
- Runs the `pyrogram.Client` by adding `tgEasy.tgClient.run()` in your main file and run [Not Recommended to use this], instead of running `python3 -m tgEasy`.

- This calls `pyrogram.Client.start()`, `pyrogram.idle()` and `pyrogram.Client.stop()`
#### Example
```python
from tgEasy import run

run()
```
### `tgEasy.get_user`
- Gets a User from Message/RepliedMessageFromUser
- Parameters:
  - m (`~pyrogram.types.Message` || `~pyrogram.types.CallbackQuery`)
- Returns:
  - `pyrogram.types.User` on Success
  - `False` on Error

#### Example
```python
from tgEasy import get_user, command, adminsOnly

@command("ban", group_only=True, self_admin=True)
@adminsOnly("can_restrict_members")
async def ban(client, message):
  user = await get_user(message)
  await message.chat.kick_member(user.id)
```
### `tgEasy.get_user_adv`
- A Function to Get the User from the Message/CallbackQuery, If there is None arguments, returns the From User.
- Parameters:
  - m (`pyrogram.types.Message` || `pyrogram.types.CallbackQuery`):
    - Message or Callbackquery.
- Returns:
  - `pyrogram.types.User` on Success
  - `False` on Error

#### Example
```python
from tgEasy import command, get_user_adv

@command("id")
async def id(client, message):
  user = await get_user_adv(message)
  await message.reply_text(f"Your ID is `{user.id}`")
```

### `tgEasy.check_rights`
- Checks the Rights of an User
- This is an Helper Function for `adminsOnly`

- Parameters:
  - chat_id (int):
    - The Chat ID of Which Chat have to check the Rights.

  - user_id (int):
    - The User ID of Whose Rights have to Check.

  - rights (str):
    - The Rights have to Check.

- Returns:
  - `True` if the User have the Right.
  - `False` if the User don't have the Right.

#### Example
```python
from tgEasy import command, check_rights, get_user

@command("ban", group_only=True, self_admin=True)
async def ban(client, message):
  if not await check_rights(message.chat.id, message.from_user.id, "can_restrict_members"):
    return await message.reply_text("You don't have necessary rights to use this Command.")
  user = await get_user(message)
  await message.chat.kick_member(user.id)
```
### `tgEasy.is_admin`
- A Functions to Check if the User is Admin or not

- Parameters:
    - chat_id (int):
        - The Chat ID of Which Chat have to check the Admin Status.

    - user_id (int):
        - The User ID of Whose Admin Status have to Check.

- Returns:
    - `True` if the User is Admin.
    - `False` if the User is't Admin.
 #### Example
```python
from tgEasy import command, is_admin, adminsOnly

@command("ban", group_only=True, self_admin=True)
@adminsOnly("can_restrict_members")
async def ban(client, message):
    if await is_admin(message.chat.id, (await get_user(mesasge)).id):
        return await message.reply_text("You can't Ban Admins.")
    await message.chat.kick_member((await get_user(message)).id)
    await message.reply_text("User has been Banned.")
```
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
```python
from tgEasy import command, handle_error

@command("start")
async def start(client, message):
  try:
    await message.reply_text("Hi :D') # I intentionally made an bug for Example :/
  except Exceptation as e:
    return await handle_error(e, message)
```

### `tgEasy.send_typing`
- A Function to Send the Typing Status to the Chat.

- Parameters:
  - m (`pyrogram.types.Message` || `pyrogram.types.CallbackQuery`):
    - Message or Callbackquery.

#### Example
```python
from tgEasy import command, send_typing

@command("start")
async def start(client, message):
  await send_typing(message)
  await message.reply_text("Hello")
```
### Smart Plugins
- The Smart Plugins Concept is't Implemented yes, It will be avaiable soon.

> Pro Tip: ```tgEasy imports all of the pyromod Functions, Methods and Types, use `from tgEasy import [pyromod function name]`, A Pyromod Function and make it More convenient to develop```
## Copyright and Licence
- tgEasy is Licenced under the Terms and Conditions of OSI Approved GNU Lesser General Public License v3 or later (LGPLv3+).
- Copyright 2021 Jayant Hegde Kageri <https://github.com/jayantkageri>.
- This Projects Codes may contain snippets or codes of [Pyrogram](https://github.com/pyrogram/pyrogram).
- Pyrogram - Telegram MTProto API Client Library for Python. Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
- This Project uses [Pyromod](https://github.com/usernein) for making it more convenient.
- Pyromod - A monkeypatcher add-on for Pyrogram
- Copyright (C) 2020 - 2021 Cezar <https://github.com/usernein>
