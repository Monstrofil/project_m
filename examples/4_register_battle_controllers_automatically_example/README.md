# Register mods in battle_elements.xml using ModAPI, automatic mode

Just create <somename>.xml file in PnFMods/USSHelper/FMods/battle_elements directory and paste there something like following:
```
<?xml version="1.0" ?>
<battle_elements.xml>
    <action type="add" target="elementList" before="unboundCombatLog">
        <element class="my.test.Clip" name="my.test.Clip" url="fullscreen_effects.swf"/>
    </action>
    <action type="remove" target="elementList">
        <element name="fireScreenEffect"/>
    </action>

    <action type="update" target="controllers">
        <controller class="lesta.dialogs.battle_window_controllers.AchievementController" clips="+my.test.Clip2,-testClip"/>
    </action>
    <action type="add" target="controllers">
        <controller class="my.test.controller" clips="myclip"/>
    </action>
    <action type="remove" target="controllers">
        <controller class="lesta.dialogs.battle_window_controllers.InvitationController"/>
    </action>
    <action type="remove" target="controllers">
        <controller class="lesta.dialogs.battle_window_controllers.UnboundElementController" clips="unboundDogTagKillCam"/>
    </action>
</battle_elements.xml>
```

Xml spec is following
1. Add element
```
    <action type="add" target="elementList" [before="name_of_the_element"]>
        <!-- here we can add some elements that should be added -->
        <element class="my.test.Clip" name="my.test.Clip" url="fullscreen_effects.swf"/>
        <element class="my.test.Clip" name="my.test.Clip2" url="fullscreen_effects.swf"/>
    </action>
```
2. Remove element
```
    <action type="remove" target="elementList">
        <element name="name_of_the_element"/>
    </action>
```
3. Add controller; works same as 'add element'
```
    <action type="add" target="controllers">
        <controller class="my.test.controller" clips="myclip"/>
    </action>
```
4. Remove controller; clips parameter is required only for non-unicue controllers.
You can either specify all clips separated by coma, or just one of the.
```
    <action type="remove" target="controllers">
        <controller class="lesta.dialogs.battle_window_controllers.UnboundElementController" [clips="unboundDogTagKillCam"]/>
    </action>
```
5. Update controller; special action that allows you to add or remove clips in given controller.
Only unique controllers supported for now.
```
    <action type="update" target="controllers">
        <controller class="lesta.dialogs.battle_window_controllers.AchievementController" clips="+my.test.Clip2,-testClip"/>
    </action>
```

BE CAREFULL, gui/flash DIRECTORY SHOULD EXIST, BECAUSE MODAPI HAS NO ABILITY TO CREATE DIRECTORIES

## License
----
MIT
