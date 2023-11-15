#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:et:ai:sts=4

from distutils.core import setup, Extension, Command

setup(
        name        = 'nemu',
        version     = '0.4',
        description = 'A lightweight network emulator embedded in a small '
                      'python library.',
        author      = 'Martina Ferrari, Alina Quereilhac, Tom Niget',
        author_email = 'tina@tina.pm, aquereilhac@gmail.com, tom.niget@nexedi.com',
        url         = 'https://github.com/zdimensin/nemu3',
        license     = 'GPLv2',
        platforms   = 'Linux',
        packages    = ['nemu'],
        install_requires = ['unshare', 'six'],
        package_dir = {'': 'src'}
        )
