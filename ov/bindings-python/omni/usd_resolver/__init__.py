import os

from typing import Tuple, List, Callable

if hasattr(os, "add_dll_directory"):
    scriptdir = os.path.dirname(os.path.realpath(__file__))
    dlldir = os.path.abspath(os.path.join(scriptdir, "../../.."))
    with os.add_dll_directory(dlldir):
        from ._omni_usd_resolver import *
else:
    from ._omni_usd_resolver import *
