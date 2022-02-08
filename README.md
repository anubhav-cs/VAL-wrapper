# VAL-wrapper
A python wrapper over KCL-VAL binaries compiled from [source](https://github.com/KCL-Planning/VAL)

How does it work?
=================

The entire build and python packaging is handled by cmake. The VAL github source is added as an external project which is compiled on the target system. The python wrapper is a script which calls the Validate executable.

LICENSE
The *wrapper* source code in this repository is released under MIT license. On the other hand, the pypi release, which redistributes the VAL binaries carries the original [license](https://github.com/KCL-Planning/VAL/blob/3c7a1f330bdab0ba28a4762bb45c3f06c27fb6d4/LICENSE) under which VAL source is released.