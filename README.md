# val-wrapper
A python wrapper over KCL-VAL binaries compiled from [source](https://github.com/KCL-Planning/VAL)

Install
-------

        python3 -m pip install val-wrapper

How does it work?
=================

The entire build and python packaging is handled by cmake. The VAL github source is added as an external project which is compiled on the target system. The python wrapper is a script which calls the Validate executable.

LICENSE
-------
The *wrapper* source code in this repository is released under MIT license. On the other hand, the pypi release, which redistributes the VAL binaries, carries the original [license](https://github.com/KCL-Planning/VAL/blob/3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4/LICENSE) under which VAL source is released.

# BUILD Commands

        cmake -B<build_dir> -S<this repo's root path> -DCMAKE_INSTALL_PREFIX=<installation dir>
        cmake --build <build_dir> --target install

# PIP install using locally built binaries

        cd <installation dir>
        python3 -m pip install .

# Build a platform specific wheel
        python3 setup.py bdist_wheel --plat-name=<platform tag>

  - Platform tags are based on the platform on which the binaries were built, for example:
    - win_amd64
    - manylinux1_x86_64
    - ... many more, lookup the documentation

# USAGE

- Command line 

    `validate.py` is installed as a python script, a wrapper around `Validate` executable, which can be run from the command line. The pypi script installation directory is generally in system `PATH`, if not, it should be added manually.

        validate.py -h

- From another python module

    You can import `val_main` from `val_wrapper` and use it to run VAL binaries. 
    
    SYNTAX: `val_main("<executable name>", [<arg1>, <arg2>, ...])`

        from val_wrapper import val_main
        val_main("Validate", ["-h"])

- Google colab notebook

        !pip install val-wrapper wurlitzer --upgrade

        from val_wrapper import val_main
        from wurlitzer import sys_pipes

        with sys_pipes():
            val_main("Validate", ["-h"])