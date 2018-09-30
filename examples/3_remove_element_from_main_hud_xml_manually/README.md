# Remove unneeded blocks from main_hud_pc.xml file

Place the xml file with following content into mods folder.
```
<?xml version="1.0" ?>
<main_hud_pc.xml>
    <remove tag="block" className="MainHUDPCContainer"/>
</main_hud_pc.xml>
```

Required filed is `tag`, others are compared to the target element attibutes.

BE CAREFULL, gui/unbound DIRECTORY MUST EXIST, BECAUSE MODAPI HAS NO ABILITY TO CREATE DIRECTORIES

## License
----
MIT
