#
# This file includes code from python-passfd (https://github.com/NightTsarina/python-passfd).
# Copyright (c) 2010 Martina Ferrari <tina@tina.pm>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import socket
import struct
from io import IOBase


def __check_socket(sock: socket.socket | IOBase):
    if hasattr(sock, 'family') and sock.family != socket.AF_UNIX:
        raise ValueError("Only AF_UNIX sockets are allowed")

    if hasattr(sock, 'fileno'):
        sock = socket.fromfd(sock.fileno(), family=socket.AF_UNIX, type=socket.SOCK_STREAM)

    if not isinstance(sock, socket.socket):
        raise TypeError("An socket object or file descriptor was expected")

    return sock

def __check_fd(fd):
    try:
        fd = fd.fileno()
    except AttributeError:
        pass
    if not isinstance(fd, int):
        raise TypeError("An file object or file descriptor was expected")

    return fd


def recvfd(sock: socket.socket | IOBase, msg_buf: int = 4096):
    size = struct.calcsize("@i")
    msg, ancdata, flags, addr = __check_socket(sock).recvmsg(msg_buf, socket.CMSG_SPACE(size))
    cmsg_level, cmsg_type, cmsg_data = ancdata[0]
    if not (cmsg_level == socket.SOL_SOCKET and cmsg_type == socket.SCM_RIGHTS):
        raise RuntimeError("The message received did not contain exactly one" +
                           " file descriptor")

    fd: int = struct.unpack("@i", cmsg_data[:size])[0]
    if fd < 0:
        raise RuntimeError("The received file descriptor is not valid")

    return fd, msg.decode("utf-8")


def sendfd(sock: socket.socket | IOBase, fd: int, message: bytes = b"NONE"):
    return __check_socket(sock).sendmsg(
        [message],
        [(socket.SOL_SOCKET, socket.SCM_RIGHTS, struct.pack("@i", fd))])