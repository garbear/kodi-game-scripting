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
    'mame':                      ('mame',                       'Makefile.libretro', '.',                 'jni', {'cmake_options': 'PTR64=1'}),  # Huge and longrunning
    'mame2000':                  ('mame2000-libretro',          'Makefile',          '.',                 'jni', {}),
    'mame2003':                  ('mame2003-libretro',          'Makefile',          '.',                 'jni', {}),
    'mame2003_midway':           ('mame2003_midway',            'Makefile',          '.',                 'jni', {}),
    'mame2003_plus':             ('mame2003-plus-libretro',     'Makefile',          '.',                 'jni', {}),
    'mame2010':                  ('mame2010-libretro',          'Makefile',          '.',                 'jni', {'cmake_options': 'VRENDER=soft PTR64=1'}),  # Huge and longrunning
    'mame2015':                  ('mame2015-libretro',          'Makefile',          '.',                 'jni', {'cmake_options': 'PTR64=1 TARGET=mame'}),  # Huge and longrunning
    'mame2016':                  ('mame2016-libretro',          'Makefile.libretro', '.',                 '3rdparty/SDL2/android-project/jni', {'cmake_options': 'PTR64=1'}),  # Huge and longrunnin
}
