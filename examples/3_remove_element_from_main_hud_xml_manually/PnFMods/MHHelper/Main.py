# coding=utf-8
from ResMgr import PkgMgr
from xmllib1 import get_first_block_matching_params, remove_block_from_xml, get_pretty_xml_string

API_VERSION = 'API_v1.0'
MOD_NAME = '_MAIN_HUD_HELPER_MOD_'

from xml.dom import minidom
try:
    from API_v_1_0 import *
    from typing import Generator
except:
    pass

ME_MODS_DIRECTORY = 'mods/'
HUD_PATH = 'gui/unbound/main_hud_pc.xml'
REL_PATH = '../../'


def get_file_contents():
    # try:
    #     with open(REL_PATH + HUD_PATH, 'r') as f:
    #         return f.read()
    # except:
    #     return PkgMgr('gui').get_file_contents('gui/unbound/main_hud_pc.xml')

    # now users can use only xml way, so I can always regenerate file
    return PkgMgr('gui').get_file_contents('gui/unbound/main_hud_pc.xml')


def save_xml_file():
    with open(REL_PATH + HUD_PATH, 'w') as f:
        f.write(get_pretty_xml_string(dom))


def _iter_mods_documents():
    for filename in _iter_spec_files():
        try:
            with open(filename, 'r') as f:
                document = minidom.parse(f)
        except:
            print('[ERROR]: unable to load battle elements file {}'.format(filename))
        else:
            yield filename, _iter_remove(document)


def _iter_remove(document):
    uss_list = document.getElementsByTagName('remove')
    for child in uss_list:
        yield child


def _iter_spec_files():
    for dir_, folders, files in utils.walk(ME_MODS_DIRECTORY, True, False):
        for filename in files:
            if not filename.endswith('.xml'):
                print('[WARNING]: extra file in directory {}'.format(filename))
                continue
            yield ME_MODS_DIRECTORY + filename


ps = get_file_contents()
dom = minidom.parseString(ps)

# HERE THE LOGIC COMES

# just iter over all .xml's and register items specified there
for mod_name, actions in _iter_mods_documents():
    print('[INFO]: processing %s' % mod_name)
    for action in actions:
        attrs = dict(action.attributes.items())
        b = get_first_block_matching_params(dom, **attrs)
        remove_block_from_xml(b)

# HERE THE MAIN LOGIC ENDS

save_xml_file()
