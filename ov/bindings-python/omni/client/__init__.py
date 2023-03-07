# fmt: off
import os
import platform
import sys
import asyncio
import concurrent.futures
from typing import Tuple, List, Callable

if hasattr(os, "add_dll_directory"):
    scriptdir = os.path.dirname(os.path.realpath(__file__))
    dlldir = os.path.abspath(os.path.join(scriptdir, "../../.."))
    with os.add_dll_directory(dlldir):
        from ._omniclient import *
else:
    from ._omniclient import *


def get_server_info(url: str) -> Tuple[Result, ServerInfo]:
    """Deprecated: Use :py:func:`omni.client.get_server_info_async` or :py:func:`omni.client.get_server_info_with_callback` instead.
    """

    ret = None

    def get_server_info_cb(result, info):
        nonlocal ret
        ret = (result, info)

    get_server_info_with_callback(url=url, callback=get_server_info_cb).wait()

    return ret


async def get_server_info_async(url: str) -> Tuple[Result, ServerInfo]:
    """Asynchronously Get Server Info

    See: :py:func:`omni.client.get_server_info_with_callback`
    """

    f = concurrent.futures.Future()

    def get_server_info_cb(result, info):
        if not f.done():
            f.set_result((result, info))

    get_server_info_with_callback(url=url, callback=get_server_info_cb)

    return await asyncio.wrap_future(f)


def list(url: str) -> Tuple[Result, Tuple[ListEntry]]:
    """Deprecated: Use :py:func:`omni.client.list_async` or :py:func:`omni.client.list_with_callback` instead.
    """

    ret = None

    def list_cb(result, entries):
        nonlocal ret
        ret = (result, entries)

    list_with_callback(url=url, callback=list_cb).wait()

    return ret


async def list_async(url: str) -> Tuple[Result, Tuple[ListEntry]]:
    """Asynchronously List contents of a folder

    See: :py:func:`omni.client.list_with_callback`
    """

    f = concurrent.futures.Future()

    def list_cb(result, entries):
        if not f.done():
            f.set_result((result, entries))

    list_with_callback(url=url, callback=list_cb)

    return await asyncio.wrap_future(f)


def stat(url: str) -> Tuple[Result, ListEntry]:
    """Deprecated: Use :py:func:`omni.client.stat_async` or :py:func:`omni.client.stat_with_callback` instead.
    """

    ret = None

    def stat_cb(result, entry):
        nonlocal ret
        ret = (result, entry)

    stat_with_callback(url=url, callback=stat_cb).wait()

    return ret


async def stat_async(url: str) -> Tuple[Result, ListEntry]:
    """Asynchronously Retrieve information about a single item

    See: :py:func:`omni.client.stat_with_callback`
    """

    f = concurrent.futures.Future()

    def stat_cb(result, entry):
        if not f.done():
            f.set_result((result, entry))

    stat_with_callback(url=url, callback=stat_cb)

    return await asyncio.wrap_future(f)


def delete(url: str) -> Result:
    """Deprecated: Use :py:func:`omni.client.delete_async` or :py:func:`omni.client.delete_with_callback` instead.
    """

    ret = None

    def delete_cb(result):
        nonlocal ret
        ret = result

    delete_with_callback(url=url, callback=delete_cb).wait()

    return ret


async def delete_async(url: str) -> Result:
    """Asynchronously Delete an item

    See: :py:func:`omni.client.delete_with_callback`
    """

    f = concurrent.futures.Future()

    def delete_cb(result):
        if not f.done():
            f.set_result(result)

    delete_with_callback(url=url, callback=delete_cb)

    return await asyncio.wrap_future(f)


def create_folder(url: str) -> Result:
    """Deprecated: Use :py:func:`omni.client.create_folder_async` or :py:func:`omni.client.create_folder_with_callback` instead.
    """

    ret = None

    def create_folder_cb(result):
        nonlocal ret
        ret = result

    create_folder_with_callback(url=url, callback=create_folder_cb).wait()

    return ret


async def create_folder_async(url: str) -> Result:
    """Asynchronously Create a folder

    See: :py:func:`omni.client.create_folder_with_callback`
    """

    f = concurrent.futures.Future()

    def create_folder_cb(result):
        if not f.done():
            f.set_result(result)

    create_folder_with_callback(url=url, callback=create_folder_cb)

    return await asyncio.wrap_future(f)


def copy(src_url: str, dst_url: str, behavior: CopyBehavior = CopyBehavior.ERROR_IF_EXISTS, message: str = "") -> Result:
    """Deprecated: Use :py:func:`omni.client.copy_async` or :py:func:`omni.client.copy_with_callback` instead.
    """

    ret = None

    def copy_cb(result):
        nonlocal ret
        ret = result

    copy_with_callback(src_url=src_url, dst_url=dst_url, behavior=behavior, message=message, callback=copy_cb).wait()

    return ret


async def copy_async(src_url: str, dst_url: str, behavior: CopyBehavior = CopyBehavior.ERROR_IF_EXISTS, message: str = "") -> Result:
    """Asynchronously Copy an item from ``src_url`` to ``dst_url``

    See: :py:func:`omni.client.copy_with_callback`
    """

    f = concurrent.futures.Future()

    def copy_cb(result):
        if not f.done():
            f.set_result(result)

    copy_with_callback(src_url=src_url, dst_url=dst_url, behavior=behavior, message=message, callback=copy_cb)

    return await asyncio.wrap_future(f)


def move(src_url: str, dst_url: str, behavior: CopyBehavior = CopyBehavior.ERROR_IF_EXISTS, message: str = "") -> Tuple[Result, bool]:
    """Deprecated: Use :py:func:`omni.client.move_async` or :py:func:`omni.client.move_with_callback` instead.
    """

    ret = None

    def move_cb(result, copied):
        nonlocal ret
        ret = (result, copied)

    move_with_callback(src_url=src_url, dst_url=dst_url, behavior=behavior, message=message, callback=move_cb).wait()

    return ret


async def move_async(src_url: str, dst_url: str, behavior: CopyBehavior = CopyBehavior.ERROR_IF_EXISTS, message: str = "") -> Tuple[Result, bool]:
    """Asynchronously Move an item from ``src_url`` to ``dst_url``

    See: :py:func:`omni.client.move_with_callback`
    """

    f = concurrent.futures.Future()

    def move_cb(result, copied):
        if not f.done():
            f.set_result((result, copied))

    move_with_callback(src_url=src_url, dst_url=dst_url, behavior=behavior, message=message, callback=move_cb)

    return await asyncio.wrap_future(f)


def get_local_file(url: str) -> Tuple[Result, str]:
    """Deprecated: Use :py:func:`omni.client.get_local_file_async` or :py:func:`omni.client.get_local_file_with_callback` instead.
    """

    ret = None

    def get_local_file_cb(result, local_file_path):
        nonlocal ret
        ret = (result, local_file_path)

    get_local_file_with_callback(url=url, callback=get_local_file_cb).wait()

    return ret


async def get_local_file_async(url: str) -> Tuple[Result, str]:
    """Asynchronously Get local file path from a URL

    See: :py:func:`omni.client.get_local_file_with_callback`
    """

    f = concurrent.futures.Future()

    def get_local_file_cb(result, local_file_path):
        if not f.done():
            f.set_result((result, local_file_path))

    get_local_file_with_callback(url=url, callback=get_local_file_cb)

    return await asyncio.wrap_future(f)


def read_file(url: str) -> Tuple[Result, str, Content]:
    """Deprecated: Use :py:func:`omni.client.read_file_async` or :py:func:`omni.client.read_file_with_callback` instead.
    """

    ret = None

    def read_file_cb(result, version, content):
        nonlocal ret
        ret = (result, version, content)

    read_file_with_callback(url=url, callback=read_file_cb).wait()

    return ret


async def read_file_async(url: str) -> Tuple[Result, str, Content]:
    """Asynchronously Read a file

    See: :py:func:`omni.client.read_file_with_callback`
    """

    f = concurrent.futures.Future()

    def read_file_cb(result, version, content):
        if not f.done():
            f.set_result((result, version, content))

    read_file_with_callback(url=url, callback=read_file_cb)

    return await asyncio.wrap_future(f)


def write_file(url: str, content: bytes, message: str = "") -> Result:
    """Deprecated: Use :py:func:`omni.client.write_file_async` or :py:func:`omni.client.write_file_with_callback` instead.
    """

    ret = None

    def write_file_cb(result):
        nonlocal ret
        ret = result

    write_file_with_callback(url=url, content=content, message=message, callback=write_file_cb).wait()

    return ret


async def write_file_async(url: str, content: bytes, message: str = "") -> Result:
    """Asynchronously Write a file

    See: :py:func:`omni.client.write_file_with_callback`
    """

    f = concurrent.futures.Future()

    def write_file_cb(result):
        if not f.done():
            f.set_result(result)

    write_file_with_callback(url=url, content=content, message=message, callback=write_file_cb)

    return await asyncio.wrap_future(f)


def get_acls(url: str) -> Tuple[Result, List[AclEntry]]:
    """Deprecated: Use :py:func:`omni.client.get_acls_async` or :py:func:`omni.client.get_acls_with_callback` instead.
    """

    ret = None

    def get_acls_cb(result, acls):
        nonlocal ret
        ret = (result, acls)

    get_acls_with_callback(url=url, callback=get_acls_cb).wait()

    return ret


async def get_acls_async(url: str) -> Tuple[Result, List[AclEntry]]:
    """Asynchronously Get the ACLs for an item

    See: :py:func:`omni.client.get_acls_with_callback`
    """

    f = concurrent.futures.Future()

    def get_acls_cb(result, acls):
        if not f.done():
            f.set_result((result, acls))

    get_acls_with_callback(url=url, callback=get_acls_cb)

    return await asyncio.wrap_future(f)


def set_acls(url: str, acls: List[AclEntry]) -> Result:
    """Deprecated: Use :py:func:`omni.client.set_acls_async` or :py:func:`omni.client.set_acls_with_callback` instead.
    """

    ret = None

    def set_acls_cb(result):
        nonlocal ret
        ret = result

    set_acls_with_callback(url=url, acls=acls, callback=set_acls_cb).wait()

    return ret


async def set_acls_async(url: str, acls: List[AclEntry]) -> Result:
    """Asynchronously Set the ACLs for an item

    See: :py:func:`omni.client.set_acls_with_callback`
    """

    f = concurrent.futures.Future()

    def set_acls_cb(result):
        if not f.done():
            f.set_result(result)

    set_acls_with_callback(url=url, acls=acls, callback=set_acls_cb)

    return await asyncio.wrap_future(f)


def send_message(join_request_id: int, content: bytes) -> Result:
    """Deprecated: Use :py:func:`omni.client.send_message_async` or :py:func:`omni.client.send_message_with_callback` instead.
    """

    ret = None

    def send_message_cb(result):
        nonlocal ret
        ret = result

    send_message_with_callback(join_request_id=join_request_id, content=content, callback=send_message_cb).wait()

    return ret


async def send_message_async(join_request_id: int, content: bytes) -> Result:
    """Asynchronously Send a message to a channel

    See: :py:func:`omni.client.send_message_with_callback`
    """

    f = concurrent.futures.Future()

    def send_message_cb(result):
        if not f.done():
            f.set_result(result)

    send_message_with_callback(join_request_id=join_request_id, content=content, callback=send_message_cb)

    return await asyncio.wrap_future(f)


def list_checkpoints(url: str) -> Tuple[Result, Tuple[ListEntry]]:
    """Deprecated: Use :py:func:`omni.client.list_checkpoints_async` or :py:func:`omni.client.list_checkpoints_with_callback` instead.
    """

    ret = None

    def list_checkpoints_cb(result, entries):
        nonlocal ret
        ret = (result, entries)

    list_checkpoints_with_callback(url=url, callback=list_checkpoints_cb).wait()

    return ret


async def list_checkpoints_async(url: str) -> Tuple[Result, Tuple[ListEntry]]:
    """Asynchronously List the checkpoints of an item

    See: :py:func:`omni.client.list_checkpoints_with_callback`
    """

    f = concurrent.futures.Future()

    def list_checkpoints_cb(result, entries):
        if not f.done():
            f.set_result((result, entries))

    list_checkpoints_with_callback(url=url, callback=list_checkpoints_cb)

    return await asyncio.wrap_future(f)


def create_checkpoint(url: str, comment: str, force: bool = False) -> Tuple[Result, str]:
    """Deprecated: Use :py:func:`omni.client.create_checkpoint_async` or :py:func:`omni.client.create_checkpoint_with_callback` instead.
    """

    ret = None

    def create_checkpoint_cb(result, query):
        nonlocal ret
        ret = (result, query)

    create_checkpoint_with_callback(url=url, comment=comment, force=force, callback=create_checkpoint_cb).wait()

    return ret


async def create_checkpoint_async(url: str, comment: str, force: bool = False) -> Tuple[Result, str]:
    """Asynchronously Create a checkpoint of an item

    See: :py:func:`omni.client.create_checkpoint_with_callback`
    """

    f = concurrent.futures.Future()

    def create_checkpoint_cb(result, query):
        if not f.done():
            f.set_result((result, query))

    create_checkpoint_with_callback(url=url, comment=comment, force=force, callback=create_checkpoint_cb)

    return await asyncio.wrap_future(f)


def get_groups(url: str) -> Tuple[Result, List[str]]:
    """Deprecated: Use :py:func:`omni.client.get_groups_async` or :py:func:`omni.client.get_groups_with_callback` instead.
    """

    ret = None

    def get_groups_cb(result, groups):
        nonlocal ret
        ret = (result, groups)

    get_groups_with_callback(url=url, callback=get_groups_cb).wait()

    return ret


async def get_groups_async(url: str) -> Tuple[Result, List[str]]:
    """Asynchronously Get a list of all groups

    See: :py:func:`omni.client.get_groups_with_callback`
    """

    f = concurrent.futures.Future()

    def get_groups_cb(result, groups):
        if not f.done():
            f.set_result((result, groups))

    get_groups_with_callback(url=url, callback=get_groups_cb)

    return await asyncio.wrap_future(f)


def get_group_users(url: str, group: str) -> Tuple[Result, List[str]]:
    """Deprecated: Use :py:func:`omni.client.get_group_users_async` or :py:func:`omni.client.get_group_users_with_callback` instead.
    """

    ret = None

    def get_group_users_cb(result, users):
        nonlocal ret
        ret = (result, users)

    get_group_users_with_callback(url=url, group=group, callback=get_group_users_cb).wait()

    return ret


async def get_group_users_async(url: str, group: str) -> Tuple[Result, List[str]]:
    """Asynchronously Get a list of all users in a group

    See: :py:func:`omni.client.get_group_users_with_callback`
    """

    f = concurrent.futures.Future()

    def get_group_users_cb(result, users):
        if not f.done():
            f.set_result((result, users))

    get_group_users_with_callback(url=url, group=group, callback=get_group_users_cb)

    return await asyncio.wrap_future(f)


def create_group(url: str, group: str) -> Result:
    """Deprecated: Use :py:func:`omni.client.create_group_async` or :py:func:`omni.client.create_group_with_callback` instead.
    """

    ret = None

    def create_group_cb(result):
        nonlocal ret
        ret = result

    create_group_with_callback(url=url, group=group, callback=create_group_cb).wait()

    return ret


async def create_group_async(url: str, group: str) -> Result:
    """Asynchronously Create a group

    See: :py:func:`omni.client.create_group_with_callback`
    """

    f = concurrent.futures.Future()

    def create_group_cb(result):
        if not f.done():
            f.set_result(result)

    create_group_with_callback(url=url, group=group, callback=create_group_cb)

    return await asyncio.wrap_future(f)


def rename_group(url: str, group: str, new_group: str) -> Result:
    """Deprecated: Use :py:func:`omni.client.rename_group_async` or :py:func:`omni.client.rename_group_with_callback` instead.
    """

    ret = None

    def rename_group_cb(result):
        nonlocal ret
        ret = result

    rename_group_with_callback(url=url, group=group, new_group=new_group, callback=rename_group_cb).wait()

    return ret


async def rename_group_async(url: str, group: str, new_group: str) -> Result:
    """Asynchronously Rename a group

    See: :py:func:`omni.client.rename_group_with_callback`
    """

    f = concurrent.futures.Future()

    def rename_group_cb(result):
        if not f.done():
            f.set_result(result)

    rename_group_with_callback(url=url, group=group, new_group=new_group, callback=rename_group_cb)

    return await asyncio.wrap_future(f)


def remove_group(url: str, group: str) -> Tuple[Result, int]:
    """Deprecated: Use :py:func:`omni.client.remove_group_async` or :py:func:`omni.client.remove_group_with_callback` instead.
    """

    ret = None

    def remove_group_cb(result, change_count):
        nonlocal ret
        ret = (result, change_count)

    remove_group_with_callback(url=url, group=group, callback=remove_group_cb).wait()

    return ret


async def remove_group_async(url: str, group: str) -> Tuple[Result, int]:
    """Asynchronously Remove a group

    See: :py:func:`omni.client.remove_group_with_callback`
    """

    f = concurrent.futures.Future()

    def remove_group_cb(result, change_count):
        if not f.done():
            f.set_result((result, change_count))

    remove_group_with_callback(url=url, group=group, callback=remove_group_cb)

    return await asyncio.wrap_future(f)


def get_users(url: str) -> Tuple[Result, List[str]]:
    """Deprecated: Use :py:func:`omni.client.get_users_async` or :py:func:`omni.client.get_users_with_callback` instead.
    """

    ret = None

    def get_users_cb(result, users):
        nonlocal ret
        ret = (result, users)

    get_users_with_callback(url=url, callback=get_users_cb).wait()

    return ret


async def get_users_async(url: str) -> Tuple[Result, List[str]]:
    """Asynchronously Get a list of all users

    See: :py:func:`omni.client.get_users_with_callback`
    """

    f = concurrent.futures.Future()

    def get_users_cb(result, users):
        if not f.done():
            f.set_result((result, users))

    get_users_with_callback(url=url, callback=get_users_cb)

    return await asyncio.wrap_future(f)


def get_user_groups(url: str, user: str) -> Tuple[Result, List[str]]:
    """Deprecated: Use :py:func:`omni.client.get_user_groups_async` or :py:func:`omni.client.get_user_groups_with_callback` instead.
    """

    ret = None

    def get_user_groups_cb(result, groups):
        nonlocal ret
        ret = (result, groups)

    get_user_groups_with_callback(url=url, user=user, callback=get_user_groups_cb).wait()

    return ret


async def get_user_groups_async(url: str, user: str) -> Tuple[Result, List[str]]:
    """Asynchronously Get a list of groups the user is in

    See: :py:func:`omni.client.get_user_groups_with_callback`
    """

    f = concurrent.futures.Future()

    def get_user_groups_cb(result, groups):
        if not f.done():
            f.set_result((result, groups))

    get_user_groups_with_callback(url=url, user=user, callback=get_user_groups_cb)

    return await asyncio.wrap_future(f)


def add_user_to_group(url: str, user: str, group: str) -> Result:
    """Deprecated: Use :py:func:`omni.client.add_user_to_group_async` or :py:func:`omni.client.add_user_to_group_with_callback` instead.
    """

    ret = None

    def add_user_to_group_cb(result):
        nonlocal ret
        ret = result

    add_user_to_group_with_callback(url=url, user=user, group=group, callback=add_user_to_group_cb).wait()

    return ret


async def add_user_to_group_async(url: str, user: str, group: str) -> Result:
    """Asynchronously Add a user to a group

    See: :py:func:`omni.client.add_user_to_group_with_callback`
    """

    f = concurrent.futures.Future()

    def add_user_to_group_cb(result):
        if not f.done():
            f.set_result(result)

    add_user_to_group_with_callback(url=url, user=user, group=group, callback=add_user_to_group_cb)

    return await asyncio.wrap_future(f)


def remove_user_from_group(url: str, user: str, group: str) -> Result:
    """Deprecated: Use :py:func:`omni.client.remove_user_from_group_async` or :py:func:`omni.client.remove_user_from_group_with_callback` instead.
    """

    ret = None

    def remove_user_from_group_cb(result):
        nonlocal ret
        ret = result

    remove_user_from_group_with_callback(url=url, user=user, group=group, callback=remove_user_from_group_cb).wait()

    return ret


async def remove_user_from_group_async(url: str, user: str, group: str) -> Result:
    """Asynchronously Remove a user from a group

    See: :py:func:`omni.client.remove_user_from_group_with_callback`
    """

    f = concurrent.futures.Future()

    def remove_user_from_group_cb(result):
        if not f.done():
            f.set_result(result)

    remove_user_from_group_with_callback(url=url, user=user, group=group, callback=remove_user_from_group_cb)

    return await asyncio.wrap_future(f)
