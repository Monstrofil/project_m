#!/usr/bin/python
# coding=utf-8
from action import AddAction, DeleteAction
from battlelib import Element
from helper import modapi_map

__author__ = "Aleksandr Shyshatsky"


class AddElementAction(AddAction):
    def __init__(self, _xml_document, _action):
        AddAction.__init__(self, _xml_document, _action)
        self._elements = _action.getElementsByTagName('element')

    def run(self):
        for element in modapi_map(Element, self._elements):
            item = self._get_element_by_name_and_attributes(
                'element', name=element.get_name())
            if item is not None:
                print('[INFO]: element %s already exists' % element.get_name())
                return True
            elif self._before:
                other = self._get_element_by_name_and_attributes(
                    'element', name=self._before)
                if other is None:
                    print("[ERROR]: unable to find a clip named %s to register new one before it" % self._before)
                    return False
                self._insert_element_before_other(element.get_xml_item(), other)
            else:
                self._append_element_to_the_list(element.get_xml_item())
            print("[INFO]: element added successfully {}".format(element.get_xml_item().toxml()))
            return True


class DeleteElementAction(DeleteAction):
    def __init__(self, _xml_document, _action):
        DeleteAction.__init__(self, _xml_document, _action)
        self._elements = _action.getElementsByTagName('element')

    def run(self):
        for element in modapi_map(Element, self._elements):
            item = self._get_element_by_name_and_attributes(
                'element', name=element.get_name())
            if item is None:
                print('[INFO]: element %s already deleted' % element.get_name())
                return True
            else:
                self._delete_element_from_list(item)
            print("[INFO]: element removed successfully {}".format(item.toxml()))
            return True