import os
import socket as pysocket


def pipe() -> tuple[int, int]:
    a, b = os.pipe2(0)
    os.set_inheritable(a, True)
    os.set_inheritable(b, True)
    return a, b


def socket(*args, **kwargs) -> pysocket.socket:
    s = pysocket.socket(*args, **kwargs)
    s.set_inheritable(True)
    return s


def socketpair(*args, **kwargs) -> tuple[pysocket.socket, pysocket.socket]:
    a, b = pysocket.socketpair(*args, **kwargs)
    a.set_inheritable(True)
    b.set_inheritable(True)
    return a, b


def fromfd(*args, **kwargs) -> pysocket.socket:
    s = pysocket.fromfd(*args, **kwargs)
    s.set_inheritable(True)
    return s
