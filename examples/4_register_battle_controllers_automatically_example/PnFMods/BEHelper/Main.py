# coding=utf-8
from battlelib import BattleElementsHelper
from fabric import ActionsFabric

API_VERSION = 'API_v1.0'
MOD_NAME = '_USS_HELPER_MOD_'

BE_MODS_DIRECTORY = 'FMods/battle_elements/'

from xml.dom import minidom
try:
    from API_v_1_0 import *
    from typing import Generator
except:
    pass


def _iter_mods_documents():
    for filename in _iter_uss_xml_specs():
        try:
            with open(filename, 'r') as f:
                document = minidom.parse(f)
        except:
            print('[ERROR]: unable to load battle elements file {}'.format(filename))
        else:
            yield filename, _iter_actions(document)


def _iter_actions(document):
    uss_list = document.getElementsByTagName('action')
    for child in uss_list:
        yield child


def _iter_uss_xml_specs():
    for dir_, folders, files in utils.walk(BE_MODS_DIRECTORY, True, False):
        for filename in files:
            if not filename.endswith('.xml'):
                print('[WARNING]: extra file in FMods/uss directory {}'.format(filename))
                continue
            yield BE_MODS_DIRECTORY + filename


b = BattleElementsHelper()

# just iter over all .xml's and register items specified there
for mod_name, actions in _iter_mods_documents():
    print('[INFO]: processing %s' % mod_name)
    document = b.get_xml_document()
    fabric = ActionsFabric()
    for action in actions:
        if not fabric.get_action(action)(document, action).run():
            print('[ERROR]: an error happened during loading mod %s' % mod_name)
            print('This mod will not be loaded into battle_elements.xml')
            break
    else:
        b.save()
