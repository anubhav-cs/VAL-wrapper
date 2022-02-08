#!/usr/bin/env python3
import string
import sys
import subprocess
import os

def val_main(exec_name: string, args: list=[]):
    """A wrapper to execute KCL-VAL binaries

    :param exec_name: name of the binary [Exact]
    :type exec_name: String
    :param args: list of string arguments
    :type args: list
    """
    EXEC_PATH=os.path.join(os.path.dirname(__file__), "bin/"+exec_name)
    return subprocess.call([EXEC_PATH]+args)
