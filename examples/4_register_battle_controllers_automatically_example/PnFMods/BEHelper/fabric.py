#!/usr/bin/python
# coding=utf-8
from controller_actions import AddControllerAction, DeleteControllerAction, UpdateControllerAction
from element_actions import AddElementAction, DeleteElementAction

__author__ = "Aleksandr Shyshatsky"


ELEMENT_LIST = 'elementList'
CONTROLLERS = 'controllers'


class ActionsFabric:
    ACTIONS = {
        'add': {
            ELEMENT_LIST: AddElementAction,
            CONTROLLERS: AddControllerAction
        },
        'remove': {
            ELEMENT_LIST: DeleteElementAction,
            CONTROLLERS: DeleteControllerAction
        },
        'update': {
            CONTROLLERS: UpdateControllerAction
        }
    }

    def get_action(self, action_xml):
        _target = action_xml.getAttribute('target')
        _type = action_xml.getAttribute('type')

        return self.ACTIONS[_type][_target]