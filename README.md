FFMPEG Python bindings
----------------------
Python Ctypes bindings for FFMPEG LibAV libraries

Example
-------
An optional path to the FFMPEG library files can be provided by setting the environment variable LIBAV_PATH.
If a path is not provided python will try to load the FFMPEG library files from the system folders.
```
	import os
	os.environ['LIBAV_PATH'] = os.path.dirname(os.path.realpath(__file__)).replace('\\','/') + '/include/ffmpeg'
	import libav
```
