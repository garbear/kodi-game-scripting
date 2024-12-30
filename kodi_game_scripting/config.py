# Copyright (C) 2016-2018 Christian Fetzer
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

""" Libretro core configuration

    Override settings for specific libretro cores. """

# pylint: disable=bad-option-value, bad-whitespace, line-too-long
# flake8: noqa

GITHUB_ORGANIZATION = 'kodi-game'
GITHUB_ADDON_PREFIX = 'game.libretro.'

# core: {(Libretro repo, Makefile, Directory)}
ADDONS = {
    'reminiscence':              ('REminiscence',               'Makefile',          '.',                 'jni', {}),
    'remotejoy':                 ('libretro-remotejoy',         'Makefile',          '.',                 'jni', {}),
    'retro8':                    ('retro8',                     'Makefile',          '.',                 'jni', {}),
    #'rustation':                 ('rustation-libretro',         'Makefile',          '.',                 'jni', {}),  # Checkout fails
    'same_cdi':                  ('same_cdi',                   'Makefile.libretro', '.',                 'jni', {}),
    'sameboy':                   ('SameBoy',                    'Makefile',          'libretro',          'libretro/jni', {'branch': 'buildbot'}),
    'scummvm':                   ('scummvm',                    'Makefile',          'backends/platform/libretro', 'backends/platform/libretro/jni', {}),
    'smsplus-gx':                ('smsplus-gx',                 'Makefile.libretro', '.',                 'jni', {'soname': 'smsplus'}),
    'snes9x':                    ('snes9x',                     'Makefile',          'libretro',          'libretro/jni', {}),
    'snes9x2002':                ('snes9x2002',                 'Makefile',          '.',                 'jni', {}),
    'snes9x2010':                ('snes9x2010',                 'Makefile',          '.',                 'jni', {}),
    'stella':                    ('stella-emu/stella',          'Makefile',          'src/os/libretro',   'src/os/libretro/jni', {}),
    'supafaust':                 ('supafaust',                  'Makefile',          '.',                 'jni', {'soname': 'mednafen_supafaust', 'exclude_platforms': ['osx-x86_64', 'osx-arm64']}),
    'swanstation':               ('swanstation',                '',                  '.',                 '', {'branch': 'main', 'cmake': True}),
    'tgbdual':                   ('tgbdual-libretro',           'Makefile',          '.',                 'jni', {}),
    'theodore':                  ('Zlika/theodore',             'Makefile',          '.',                 'jni', {}),
    'thepowdertoy':              ('kodi-game/ThePowderToy',     '',                  '',                  '', {'cmake': True, 'binary_dir': 'src'}),
    'tyrquake':                  ('tyrquake',                   'Makefile',          '.',                 'jni', {}),
    'uae':                       ('libretro-uae',               'Makefile',          '.',                 'jni', {'soname': 'puae'}),
    #'uae4arm':                   ('Chips-fr/uae4arm-rpi',       'Makefile.libretro', '.',                 'jni', {}),  # Fails to build on non arm system
    'uzem':                      ('libretro-uzem',              'Makefile.libretro', '.',                 'jni', {}),
    'vba-next':                  ('vba-next',                   'Makefile',          '.',                 'libretro/jni', {'soname': 'vba_next'}),
    'vbam':                      ('visualboyadvance-m/visualboyadvance-m', 'Makefile', 'src/libretro',    'src/libretro/jni', {}),
    'vecx':                      ('libretro-vecx',              'Makefile',          '.',                 'jni', {}),
    'vemulator':                 ('vemulator-libretro',         'Makefile',          '.',                 'jni', {}),
    'vice_x128':                 ('vice-libretro',              'Makefile',          '.',                 'jni', {'soname': 'vice_x128', 'cmake_options': 'EMUTYPE=x128'}),
    'vice_x64':                  ('vice-libretro',              'Makefile',          '.',                 'jni', {'soname': 'vice_x64', 'cmake_options': 'EMUTYPE=x64'}),
    'vice_x64dtv':               ('vice-libretro',              'Makefile',          '.',                 'jni', {'soname': 'vice_x64dtv', 'cmake_options': 'EMUTYPE=x64dtv'}),
    'vice_x64sc':                ('vice-libretro',              'Makefile',          '.',                 'jni', {'soname': 'vice_x64sc', 'cmake_options': 'EMUTYPE=x64sc'}),
    'vice_xcbm2':                ('vice-libretro',              'Makefile',          '.',                 'jni', {'soname': 'vice_xcbm2', 'cmake_options': 'EMUTYPE=xcbm2'}),
    'vice_xcbm5x0':              ('vice-libretro',              'Makefile',          '.',                 'jni', {'soname': 'vice_xcbm5x0', 'cmake_options': 'EMUTYPE=xcbm5x0'}),
    'vice_xpet':                 ('vice-libretro',              'Makefile',          '.',                 'jni', {'soname': 'vice_xpet', 'cmake_options': 'EMUTYPE=xpet'}),
    'vice_xplus4':               ('vice-libretro',              'Makefile',          '.',                 'jni', {'soname': 'vice_xplus4', 'cmake_options': 'EMUTYPE=xplus4'}),
    'vice_xscpu64':              ('vice-libretro',              'Makefile',          '.',                 'jni', {'soname': 'vice_xscpu64', 'cmake_options': 'EMUTYPE=xscpu64'}),
    'vice_xvic':                 ('vice-libretro',              'Makefile',          '.',                 'jni', {'soname': 'vice_xvic', 'cmake_options': 'EMUTYPE=xvic'}),
    'virtualjaguar':             ('virtualjaguar-libretro',     'Makefile',          '.',                 'jni', {}),
    #'wolfenstein3d':             ('kodi-game/libretro-wolfenstein3d', 'Makefile.libretro', '.',           'jni', {}),  # Requires SDL 1
    'xmil':                      ('xmil-libretro',              'Makefile.libretro', 'libretro',          'libretro/jni', {'soname': 'x1'}),
    'xrick':                     ('xrick-libretro',             'Makefile.libretro', '.',                 'jni', {}),
    'yabasanshiro':              ('yabause',                    'Makefile',          'yabause/src/libretro', 'yabause/src/libretro/jni', {'branch': 'yabasanshiro'}),
    'yabause':                   ('yabause',                    'Makefile',          'yabause/src/libretro', 'yabause/src/libretro/jni', {}),
}
