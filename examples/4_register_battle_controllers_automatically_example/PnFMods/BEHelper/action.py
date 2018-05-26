#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"


class Action:
    def __init__(self, _xml_document, _action):
        self.target = _action.getAttribute('target')
        self.type = _action.getAttribute('type')
        self._xml_data, = _xml_document.getElementsByTagName(self.target)

    def _get_element_by_name_and_attributes(self, tag_name, **attributes):
        items = list(self._get_elements_by_name_and_attributes(tag_name, **attributes))
        return items[0] if items else None

    def _get_elements_by_name_and_attributes(self, tag_name, **attributes):
        for element in self._xml_data.getElementsByTagName(tag_name):
            if attributes is None:
                yield element
            else:
                for key, value in attributes.items():
                    if element.getAttribute(key) != value:
                        break
                else:
                    yield element

    def run(self):
        raise NotImplementedError


class AddAction(Action):
    def __init__(self, _xml_document, _action):
        Action.__init__(self, _xml_document, _action)
        self._before = _action.getAttribute('before')

    def _insert_element_before_other(self, element, other):
        self._xml_data.insertBefore(element, other)

    def _append_element_to_the_list(self, element):
        self._xml_data.appendChild(element)


class DeleteAction(Action):
    def __init__(self, _xml_document, _action):
        Action.__init__(self, _xml_document, _action)
        self._elements = _action.getElementsByTagName('element')

    def _delete_element_from_list(self, element):
        self._xml_data.removeChild(element)