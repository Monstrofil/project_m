# [Example 1] Uss register using ModAPI

This example shows how to register your custom uss expressions file using modAPI. All you need is to import special method named 'register_uss_expression_swf' from usslib and pass your path as an argument.
```# coding=utf-8
API_VERSION = 'API_v1.0'
MOD_NAME = 'USS_DEMO_MOD'
from usslib import register_uss_expression_swf
register_uss_expression_swf('../../unbound/flash/mycooluss.swf')
```

Once your game client starts, all your files will be added to USSExpressionsLoader.xml.

BE CAREFULL, gui/flash DIRECTORY SHOULD EXIST, BECAUSE MODAPI HAS NO ABILITY TO CREATE DIRECTORIES

## License
----
MIT
