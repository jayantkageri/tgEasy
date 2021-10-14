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
import typing

import pyrogram

import tgEasy

from .config import Config
from .scaffold import Scaffold


async def get_user(m: typing.Union[pyrogram.types.Message, pyrogram.types.CallbackQuery]):
    """
### `tgEasy.get_user`
- Gets a User from Message/RepliedMessage/CallbackQuery
- Parameters:
  - m (`~pyrogram.types.Message` || `~pyrogram.types.CallbackQuery`)
- Returns:
  - `pyrogram.types.User` on Success
  - `False` on Error

#### Example
    .. code-block:: python
        from tgEasy import get_user, command, adminsOnly

        @command("ban", group_only=True, self_admin=True)
        @adminsOnly("can_restrict_members")
        async def ban(client, message):
            user = await get_user(message)
            await message.chat.kick_member(user.id)
    """
    if isinstance(m, pyrogram.types.Message):
        message = m
        client = m._client
    if isinstance(m, pyrogram.types.CallbackQuery):
        message = m.message
        client = message._client
    if message.reply_to_message:
        if message.reply_to_message.sender_chat:
            return False
        return await client.get_users(message.reply_to_message.from_user.id)

    if len(message.command) > 1:
        command = message.command[1]
    else:
        command = None

    if command:
        if command.startswith("@") or command.isdigit():
            try:
                return await client.get_users(message.command[1])
            except pyrogram.errors.exceptions.bad_request_400.UsernameNotOccupied:
                pass
            except pyrogram.errors.exceptions.bad_request_400.UsernameInvalid:
                pass
            except pyrogram.errors.exceptions.bad_request_400.PeerIdInvalid:
                pass
            except IndexError:
                pass
    else:
        pass

    if message.entities:
        for mention in message.entities:
            if mention.type == "text_mention":
                user = mention.user.id
                break
        try:
            return await client.get_users(user)
        except:
            pass
    return False


async def get_user_adv(m: typing.Union[pyrogram.types.Message, pyrogram.types.CallbackQuery]):
    """
### `tgEasy.get_user_adv`
- A Function to Get the User from the Message/CallbackQuery, If there is None arguments, returns the From User.
- Parameters:
  - m (`pyrogram.types.Message` || `pyrogram.types.CallbackQuery`):
    - Message or Callbackquery.
- Returns:
  - `pyrogram.types.User` on Success
  - `False` on Error

#### Example
    .. code-block:: python
        from tgEasy import command, get_user_adv

        @command("id")
        async def id(client, message):
            user = await get_user_adv(message)
            await message.reply_text(f"Your ID is `{user.id}`")
    """
    if isinstance(m, pyrogram.types.Message):
        message = m
    if isinstance(m, pyrogram.types.CallbackQuery):
        message = m.message
    if message.sender_chat:
        return False
    try:
        if len(message.command) > 1:
            if message.command[1].startswith("@"):
                return await get_user(message)
            if message.command[1].isdigit():
                return await get_user(message)
            if "text_mention" in message.entities:
                return await get_user(message)
            if "from_user" in str(message.reply_to_message):
                return await get_user(message)
    except IndexError:
        pass
    except AttributeError:
        pass

    try:
        if "sender_chat" in str(message.reply_to_message):
            return False
        if "from_user" in str(message.reply_to_message):
            return await message._client.get_users(message.reply_to_message.from_user.id)
    except AttributeError:
        pass
    except Exception as e:
        pass

    return await message._client.get_users(message.from_user.id)


async def send_typing(m: typing.Union[pyrogram.types.Message, pyrogram.types.CallbackQuery]):
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


async def handle_error(error, m: typing.Union[pyrogram.types.Message, pyrogram.types.CallbackQuery]):
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

    from . import logging
    with open("crash.log", "w+", encoding="utf-8") as log:
        log.write(traceback.format_exc())
        log.close()
    if isinstance(m, pyrogram.types.Message):
        try:
            await m.reply_text("An Internal Error Occurred while Processing your Command, the Logs have been sent to the Owners of this Bot. Sorry for Inconvenience")
            await m._client.send_document(Config.LOGS, "crash.log", caption="Crash Report of this Bot")
        except:
            pass
    if isinstance(m, pyrogram.types.CallbackQuery):
        try:
            await m.message.delete()
            await m.message.reply_text("An Internal Error Occurred while Processing your Command, the Logs have been sent to the Owners of this Bot. Sorry for Inconvenience")
            await m.message._client.send_document(Config.LOGS, "crash.log", caption="Crash Report of this Bot")
        except:
            pass
    logging.exception(traceback.format_exc())
    os.remove('crash.log')


async def check_rights(chat_id: typing.Union[int, int], user_id: typing.Union[int, int], rights: typing.Union[str, str], client) -> bool:
    """
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

    - client (`pyrogram.Client`):
        - From which Client to Check the Rights.

    - Returns:
    - `True` if the User have the Right.
    - `False` if the User don't have the Right.

    #### Example
    .. code-block:: python
        from tgEasy import tgClient, check_rights, get_user
        import pyrogram

        app = tgClient(pyrogram.Client())

        @app.command("ban", group_only=True, self_admin=True)
        async def ban(client, message):
        if not await check_rights(message.chat.id, message.from_user.id, "can_restrict_members"):
            return await message.reply_text("You don't have necessary rights to use this Command.")
        user = await get_user(message)
        await message.chat.kick_member(user.id)
    """
    try:
        user = await client.get_chat_member(chat_id, user_id)
    except:
        return False
    if user.status == "user":
        return False
    if user.status in ("administrator", "creator"):
        permission = []
        if user.can_delete_messages:
            permission.append("can_delete_messages")
        if user.can_restrict_members:
            permission.append("can_restrict_members")
        if user.can_promote_members:
            permission.append("can_promote_members")
        if user.can_change_info:
            permission.append("can_change_info")
        if user.can_invite_users:
            permission.append("can_invite_users")
        if user.can_pin_messages:
            permission.append("can_pin_messages")
        if user.can_manage_voice_chats:
            permission.append("can_manage_voice_chats")
        if user.is_anonymous:
            permission.append("is_anonymous")
        if rights in permission:
            return True
        return False
    return False


async def is_admin(chat_id: typing.Union[int, str], user_id: typing.Union[int, str], client) -> bool:
    """
    ### `tgEasy.is_admin`
    - A Functions to Check if the User is Admin or not

    - Parameters:
        - chat_id (int):
            - The Chat ID of Which Chat have to check the Admin Status.

        - user_id (int):
            - The User ID of Whose Admin Status have to Check.

        - client (`pyrogram.Client`):
            - From which Client to Check the Admin Status.

    - Returns:
        - `True` if the User is Admin.
        - `False` if the User is't Admin.
    #### Example
    .. code-block:: python
        from tgEasy import tgClient, is_admin, adminsOnly
        import pyrogram

        app = tgClient(pyrogram.Client())

        @app.command("ban", group_only=True, self_admin=True)
        @app.adminsOnly("can_restrict_members")
        async def ban(client, message):
            if await is_admin(message.chat.id, (await get_user(mesasge)).id):
                return await message.reply_text("You can't Ban Admins.")
            await message.chat.kick_member((await get_user(message)).id)
            await message.reply_text("User has been Banned.")
    """
    try:
        user = await client.get_chat_member(chat_id, user_id)
    except:
        return False
    if user.status in ("administrator", "creator"):
        return True
    return False
