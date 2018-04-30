#!/usr/bin/python
# coding=utf-8
from xml.dom import minidom

# syntax sugar
try:
    from API_v_1_0 import *
    from typing import Generator
except:
    pass

__author__ = "Aleksandr Shyshatsky"


class UssExpressionsManager:
    USS_XML_NAME = 'USSExpressionsLoader.xml'
    USS_FILE_PATH = '../../gui/flash/' + USS_XML_NAME
    USS_XML_BASE = """
    <data>
      <expressions_files>
        <file path="USSExpressions.swf" />
      </expressions_files>
    </data>"""
    USS_EXPRESSIONS_TAG = 'expressions_files'

    def __init__(self):
        self._xml_file = self._load_xml_file()
        self._expressions_list = self._get_expressions_list()
        self._registered_uss_files = set(self._iter_registered_files())

    def _create_empty_xml(self):
        # type: () -> minidom.Document
        return minidom.parseString(self.USS_XML_BASE)

    def _load_xml_file(self):
        # type: () -> minidom.Document
        # utils.isFile works only in home directory
        try:
            with open(self.USS_FILE_PATH, 'r') as f:
                return minidom.parseString(f.read())
        except:
            return self._create_empty_xml()

    def _get_pretty_xml_string(self):
        # type: () -> str
        return ('\n'.join(
            line for line in
            self._xml_file.toprettyxml(indent=' ' * 4).split('\n')
            if line.strip()
        ))

    def _save_xml_file(self):
        # type: () -> None
        # TODO: errors hangling
        with open(self.USS_FILE_PATH, 'w') as f:
            f.write(self._get_pretty_xml_string())

    def _iter_registered_files(self):
        # type: () -> Generator[str]
        for item in self._expressions_list.childNodes:
            if item.attributes is None:
                continue
            yield item.attributes['path'].value

    def _get_expressions_list(self):
        # type: () -> minidom.Element
        expressions, = self._xml_file.getElementsByTagName(self.USS_EXPRESSIONS_TAG)
        return expressions

    def _create_file_node(self, path):
        # type: (str) -> minidom.Element
        node = self._xml_file.createElement('file')
        node.setAttribute('path', path)
        return node

    def register_uss_expression_swf(self, uss_path):
        # type: () -> None
        if uss_path in self._registered_uss_files:
            print('[INFO]: %s is already registered in %s' % (uss_path, self.USS_XML_NAME))
            return
        expressions = self._get_expressions_list()
        expressions.appendChild(self._create_file_node(uss_path))
        self._save_xml_file()
        print('[INFO]: %s successfully registered in %s' % (uss_path, self.USS_XML_NAME))


_ussExpressionsManager = UssExpressionsManager()
register_uss_expression_swf = _ussExpressionsManager.register_uss_expression_swf
