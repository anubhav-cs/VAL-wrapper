# VAL-wrapper
A python wrapper over KCL-VAL binary executables compiled from [source](https://github.com/KCL-Planning/VAL).


LICENSE
-------

This pypi release, which redistributes the VAL binaries, carries the original [3-Clause BSD License](https://github.com/KCL-Planning/VAL/blob/3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4/LICENSE) under which VAL source code was released.


USAGE
-----

- Command line 

    `validate.py` is installed as a python script, a wrapper around `Validate` executable, which can be run from the command line. The pypi script installation directory is generally in system `PATH`, if not, it should be added manually.

        validate.py -h

- From another python module

    You can import `val_main` from `val_wrapper` and use it to run VAL binaries. 
    
    SYNTAX: `val_main("<executable name>", [<arg1>, <arg2>])`

        from val_wrapper import val_main
        
        val_main("Validate", ["-h"])

- Google colab notebook

        !pip install val-wrapper wurlitzer --upgrade

        from val_wrapper import val_main

        from wurlitzer import sys_pipes

        with sys_pipes():
            val_main("Validate", ["-h"])
