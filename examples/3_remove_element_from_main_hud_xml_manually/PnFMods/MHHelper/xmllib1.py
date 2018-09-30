#!/usr/bin/python
# coding=utf-8

__author__ = "Aleksandr Shyshatsky"


def _next(iterable):
    for i in iterable:
        return i


def get_blocks_matching_params(dom, tagname, **attrs):
    for b in dom.getElementsByTagName(tagname):
        for name, value in attrs.items():
            if b.getAttribute(name) != value:
                break
        else:
            yield b


def get_first_block_matching_params(dom, tag, **attrs):
    block = _next(get_blocks_matching_params(dom, tag, **attrs))
    if block is None:
        print 'WARN: no such element tag=%s attrs=%s' % (tag, attrs)
    return block


def remove_block_from_xml(block):
    if block is None:
        return
    block.parentNode.removeChild(block)


def get_pretty_xml_string(dom):
    return ('\n'.join(
        line for line in
        dom.toprettyxml(indent=' ' * 4).split('\n')
        if line.strip()
    ))