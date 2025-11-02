# IBM MQ C libraries distributed as a Python package

This is a NOOP Python package designed to simplify the distribution of IBM MQ C
library files.
Designed to be used together with `ibmmq`.

They only support Windows X64 and Linux GLIC X64.

For all the other platforms, an empty wheel is generated.
This is designed to help unify the requirements for the dev tools.
You can then handle the empty wheel at the application level.


## Linux Usage

You need to use `LD_LIBRARY_PATH` to load the IBM C shared libraries.
They will be installed inside the virtual environment, at `lib/ibm-mq` path.

```
export LD_LIBRARY_PATH=YOUR_VENV/lib/ibm-mq/lib64/:YOUR_VENV/lib/ibm-mq/gskit9/lib64/
python your_ibm_mq_sample_code.py
```


## Windows Usage

The Microsoft Visual C++ 2013 Redistributable is required to build on
Windows systems.
This is a limitation of the IBM MQ C Client library.
The DLLs are copied in the wheel, so you don't need to install this on the
target systems.

The package copies the the IBM MQ libraries at `lib/ibm-mq` folder inside your
virtual environment.

You will need to setup Python to load the DLL from there.

```python
import os

if os.name == 'nt':
    base_dll_dir = os.path.join(os.path.dirname(sys.executable), 'ibm-mq')
    os.add_dll_directory(base_dll_dir)

import pymqi
```

## Licence

From the `licences/English.txt` found in the IBM MQ C redist archive:

> Redistributables may be distributed, in object-code form, only as part of Licensee's value-added application that was developed using the Program ("Licensee's Application") and only to support use of Licensee's Application.

I guess that this Python Package "application" adds some value, so the license is ok.
