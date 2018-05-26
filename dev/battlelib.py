#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"

from ResMgr import PkgMgr
from xml.dom import minidom


# just a syntax sugar
class staticmethod:
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls):
        return self.func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


class Element:
    NAME = 'name'
    CLASS = 'class'
    URL = 'url'
    ENABLED = 'enabled'

    def __init__(self, xml_element):
        self._xml = xml_element
        self._name = xml_element.getAttribute(self.NAME)
        self._class = xml_element.getAttribute(self.CLASS)
        self._url = xml_element.getAttribute(self.URL)
        self._enabled = xml_element.getAttribute(self.ENABLED) != 'false'

    def get_name(self):
        return self._name

    def get_xml_item(self):
        # type: () -> minidom.Element
        self._xml = minidom.Element('element')
        self._xml.setAttribute(self.NAME, self._name)
        self._xml.setAttribute(self.CLASS, self._class)
        self._xml.setAttribute(self.URL, self._url)
        self._xml.setAttribute(self.ENABLED, 'true' if self._enabled else 'false')
        return self._xml

    @staticmethod
    def create():
        return Element(minidom.Element('element'))


class Controller:
    CLIPS = 'clips'
    CLASS = 'class'

    def __init__(self, xml_element):
        # type: (minidom.Element) -> None
        self._xml = xml_element
        self._clips = xml_element.getAttribute('clips').split(',')
        self._class = xml_element.getAttribute('class')

    def get_clips(self):
        return self._clips

    def get_class(self):
        return self._class

    def del_clip(self, clip):
        if clip in self._clips:
            self._clips.remove(clip)

    def add_clip(self, clip):
        if clip not in self._clips:
            self._clips.append(clip)


    def get_xml_item(self):
        # type: (minidom.Element) -> minidom.Element
        self._xml.setAttribute(self.CLIPS, ','.join(self._clips))
        self._xml.setAttribute(self.CLASS, self._class)
        return self._xml

    @staticmethod
    def create():
        return Controller(minidom.Element('controller'))

    def update(self, controller):
        self._class = controller.get_class()
        self._clips = controller.get_clips()


class BattleElementsHelper:
    BATTLE_ELEMENTS = 'gui/battle_elements.xml'
    ROOT_DIR = '../../'
    PACKAGE = 'gui'

    def __init__(self):
        self._pkg = PkgMgr(self.PACKAGE)
        self._battle_elements = self._load_battle_elements_config()

    def _load_battle_elements_config(self):
        try:
            with open(self.ROOT_DIR + self.BATTLE_ELEMENTS, 'r') as f:
                return minidom.parse(f)
        except:
            return minidom.parseString(
                self._pkg.get_file_contents(self.BATTLE_ELEMENTS))

    def _save_battle_elements_config(self):
        with open(self.ROOT_DIR + self.BATTLE_ELEMENTS, 'w') as f:
            return f.write(self._get_pretty_xml_string())

    def _get_pretty_xml_string(self):
        # type: () -> str
        return ('\n'.join(
            line for line in
            self._battle_elements.toprettyxml(indent=' ' * 4).split('\n')
            if line.strip()
        ))

    def get_xml_document(self):
        return self._battle_elements

    def save(self):
        self._save_battle_elements_config()


