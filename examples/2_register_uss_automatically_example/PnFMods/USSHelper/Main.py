# coding=utf-8
API_VERSION = 'API_v1.0'
MOD_NAME = '_USS_HELPER_MOD_'

USS_MODS_DIRECTORY = 'FMods/uss/'

from xml.dom import minidom
from usslib import register_uss_expression_swf
try:
    from API_v_1_0 import *
    from typing import Generator
except:
    pass


def _iter_uss_mod_files():
    for filename in _iter_uss_xml_specs():
        try:
            with open(filename, 'r') as f:
                document = minidom.parse(f)
        except:
            print('[ERROR]: unable to load uss file {}'.format(filename))
        else:
            uss_list, = document.getElementsByTagName('uss')
            for child in uss_list.getElementsByTagName('file'):
                yield child.attributes['path'].value


def _iter_uss_xml_specs():
    for dir_, folders, files in utils.walk(USS_MODS_DIRECTORY, True, False):
        for filename in files:
            if not filename.endswith('.xml'):
                print('[WARNING]: extra file in FMods/uss directory {}'.format(filename))
                continue
            yield USS_MODS_DIRECTORY + filename


# just iter over all .xml's and register items specified there
for mod_path in _iter_uss_mod_files():
    register_uss_expression_swf(mod_path)
