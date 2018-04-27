#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"


def register_battle_elements_controller(classname, clips):
    from ResMgr import PkgMgr

    ps = PkgMgr('gui').get_file_contents('gui/battle_elements.xml')

    from xml.dom import minidom

    dom = minidom.parseString(ps)
    controller = dom.createElement('controller')
    controller.setAttribute('class', classname)
    controller.setAttribute('clips', clips)
    controllers, = dom.getElementsByTagName('controllers')
    controllers.appendChild(controller)

    with open('../../gui/battle_elements.xml', 'wb') as f:
        f.write(dom.toprettyxml(newl=''))
