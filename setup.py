#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# vim: ts=4:sw=4:et:ai:sts=4

from distutils.core import setup, Extension, Command

passfd = Extension('_passfd', sources = ['src/passfd/passfd.c'])

setup(
        name        = 'nemu',
        version     = '0.3.1',
        description = 'A lightweight network emulator embedded in a small '
                      'python library.',
        author      = 'Martina Ferrari, Alina Quereilhac',
        author_email = 'tina@tina.pm, aquereilhac@gmail.com',
        url         = 'https://github.com/NightTsarina/nemu',
        license     = 'GPLv2',
        platforms   = 'Linux',
        packages    = ['nemu'],
        install_requires = ['unshare', 'six'],
        package_dir = {'': 'src'},
        ext_modules = [passfd]
        )
