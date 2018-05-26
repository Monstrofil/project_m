#!/usr/bin/python
# coding=utf-8
__author__ = "Aleksandr Shyshatsky"


def modapi_map(callable, items):
    return [callable(i) for i in items]