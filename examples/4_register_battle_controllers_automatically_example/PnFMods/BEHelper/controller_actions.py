#!/usr/bin/python
# coding=utf-8
from action import DeleteAction, AddAction, Action
from battlelib import Controller
from helper import modapi_map

__author__ = "Aleksandr Shyshatsky"


class DeleteControllerAction(DeleteAction):
    def __init__(self, _xml_document, _action):
        DeleteAction.__init__(self, _xml_document, _action)
        self._elements = _action.getElementsByTagName('controller')

    def _look_for_controllers_partly_matching_clips(self, controllers, clips):
        for controller in controllers:
            items = controller.getAttribute('clips').split(',')
            if set(items) & set(clips):
                yield controller

    def run(self):
        for element in modapi_map(Controller, self._elements):
            items = list(self._get_elements_by_name_and_attributes(
                'controller', **{'class': element.get_class()}))
            if len(items) == 0:
                print('[INFO]: controller %s already deleted' % element.get_class())
                continue
            elif len(items) == 1:
                self._delete_element_from_list(items[0])
            else:
                print('[INFO]: multiple controllers %s found, trying to guess by clips tag' % element.get_class())
                items = list(self._look_for_controllers_partly_matching_clips(items, element.get_clips()))
                if items is None or len(items) > 1:
                    print('[ERROR]: unable to guess controller %s %s' % (element.get_class(), element.get_clips()))
                    return False
                elif items is not None and len(items) == 0:
                    print('[WARNING]: either we are unable to guess controller, '
                          'or it is already removed %s %s' % (element.get_class(), element.get_clips()))
                    return True
                item = items[0]
                self._delete_element_from_list(item)
            print("[INFO]: controller removed successfully {}".format(element.get_class()))
        return True


class AddControllerAction(AddAction):
    def __init__(self, _xml_document, _action):
        AddAction.__init__(self, _xml_document, _action)
        self._elements = _action.getElementsByTagName('controller')

    def _look_for_controllers_partly_matching_clips(self, controllers, clips):
        for controller in controllers:
            items = controller.getAttribute('clips').split(',')
            if set(items) & set(clips):
                yield controller

    def run(self):
        for controller in modapi_map(Controller, self._elements):
            items = self._get_elements_by_name_and_attributes(
                'controller', **{'class': controller.get_class()})
            tmp = list(self._look_for_controllers_partly_matching_clips(items, controller.get_clips()))
            if len(tmp) == 1:
                print('[INFO]: controller %s:%s already added' % (controller.get_class(),
                                                                  controller.get_clips()))
                return True
            elif len(tmp) > 1:
                print('[INFO]: unable to detect controller %s:%s, multiple results found' % (controller.get_class(),
                                                                                             controller.get_clips()))
                return True

            if self._before:
                other = self._get_element_by_name_and_attributes(
                    'element', **{'class': self._before})
                if other is None:
                    print("[ERROR]: unable to find a controller named %s to register new one before it" % other)
                    return False
                self._insert_element_before_other(controller.get_xml_item(), other)
            else:
                self._append_element_to_the_list(controller.get_xml_item())
            print("[INFO]: controller added successfully {}".format(controller.get_xml_item().toxml()))
        return True


class UpdateControllerAction(Action):
    def __init__(self, _xml_document, _action):
        Action.__init__(self, _xml_document, _action)
        self._elements = _action.getElementsByTagName('controller')

    def run(self):
        for controller in modapi_map(Controller, self._elements):
            item = self._get_element_by_name_and_attributes(
                'controller', **{'class': controller.get_class()})
            if item is None:
                print('[ERROR]: controller %s not found' % controller.get_class())
                return False
            print('[INFO]: found controller for update %s' % controller.get_class())
            original = Controller(item)

            for clip in controller.get_clips():
                if clip.startswith('-'):
                    original.del_clip(clip[1:])
                    print('[INFO]: adding clip %s' % clip[1:])
                elif clip.startswith('+'):
                    original.add_clip(clip[1:])
                    print('[INFO]: removing clip %s' % clip[1:])
                else:
                    pass
            original.get_xml_item()
        return True