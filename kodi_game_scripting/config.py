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
    'melonds':                   ('melonDS',                    'Makefile',          '.',                 'jni', {}),
    'meowpc98':                  ('libretro-meowPC98',          'Makefile.libretro', 'libretro',          'libretro/jni', {'soname': 'nekop2'}),
    'mesen':                     ('Mesen',                      'Makefile',          'Libretro',          'Libretro/jni', {}),
    'mesen-s':                   ('Mesen-S',                    'Makefile',          'Libretro',          'Libretro/jni', {}),
    'meteor':                    ('meteor-libretro',            'Makefile',          'libretro',          'libretro/jni', {}),
    'mgba':                      ('mgba',                       'Makefile',          '.',                 'libretro-build/jni', {}),
    'mrboom':                    ('kodi-game/mrboom-libretro',  'Makefile',          '.',                 'libretro/jni', {}),
    'mu':                        ('Mu',                         'Makefile.libretro', 'libretroBuildSystem', 'libretroBuildSystem/jni', {}),
    'mupen64plus-nx':            ('mupen64plus-libretro-nx',    'Makefile',          '.',                 'jni', {'soname': 'mupen64plus_next'}),
    'nestopia':                  ('nestopia',                   'Makefile',          'libretro',          'libretro/jni', {}),
    'neocd':                     ('neocd_libretro',             'Makefile',          '.',                 'jni', {}),
    'nx':                        ('nxengine-libretro',          'Makefile',          '.',                 'jni', {'soname': 'nxengine'}),
    'o2em':                      ('libretro-o2em',              'Makefile',          '.',                 'jni', {}),
    'oberon':                    ('oberon-risc-emu',            'Makefile.libretro', '.',                 'Libretro/jni', {}),
    'openlara':                  ('OpenLara',                   'Makefile',          'src/platform/libretro', 'src/platform/libretro/jni', {}),
    'opera':                     ('opera-libretro',             'Makefile',          '.',                 'jni', {}),
    'parallel_n64':              ('parallel-n64',               'Makefile',          '.',                 'jni', {}),
    'parallext':                 ('parallext',                  'Makefile',          '.',                 'libretro/jni', {'soname': 'parallel_n64'}),
    'pcem':                      ('libretro-pcem',              'Makefile.libretro', 'src',               'jni', {}),
    'pcsx-rearmed':              ('pcsx_rearmed',               'Makefile.libretro', '.',                 'jni', {'soname': 'pcsx_rearmed'}),
    'picodrive':                 ('kodi-game/picodrive',        'Makefile.libretro', '.',                 'jni', {}),
    'pocketcdg':                 ('libretro-pocketcdg',         'Makefile',          '.',                 'jni', {}),
    'pokemini':                  ('PokeMini',                   'Makefile.libretro', '.',                 'jni', {}),
    'potator':                   ('potator',                    'Makefile' ,         ' platform/libretro', 'platform/libretro/jni', {}),
    'ppsspp':                    ('ppsspp',                     'Makefile',          'libretro',          'libretro/jni', {}),
    'prboom':                    ('libretro-prboom',            'Makefile',          '.',                 'jni', {}),
    'prosystem':                 ('prosystem-libretro',         'Makefile',          '.',                 'jni', {}),
    'px68k':                     ('px68k-libretro',             'Makefile.libretro', '.',                 'libretro/jni', {}),
    'quasi88':                   ('quasi88-libretro',           'Makefile',          '.',                 'src/LIBRETRO/jni', {}),
    'quicknes':                  ('QuickNES_Core',              'Makefile',          '.',                 'jni', {}),
    'race':                      ('RACE',                       'Makefile',          '.',                 'jni', {}),
    'redbook':                   ('redbook',                    'Makefile',          '.',                 'jni', {}),
    'reminiscence':              ('REminiscence',               'Makefile',          '.',                 'jni', {}),
    'remotejoy':                 ('libretro-remotejoy',         'Makefile',          '.',                 'jni', {}),
    'retro8':                    ('retro8',                     'Makefile',          '.',                 'jni', {}),
    #'rustation':                 ('rustation-libretro',         'Makefile',          '.',                 'jni', {}),  # Checkout fails
    'same_cdi':                  ('same_cdi',                   'Makefile.libretro', '.',                 'jni', {}),
    'sameboy':                   ('SameBoy',                    'Makefile',          'libretro',          'libretro/jni', {'branch': 'buildbot'}),
    'scummvm':                   ('kodi-game/scummvm',          'Makefile',          '.',                 'jni', {'branch': 'main'}),
    'smsplus-gx':                ('smsplus-gx',                 'Makefile.libretro', '.',                 'jni', {'soname': 'smsplus'}),
    'snes9x':                    ('snes9x',                     'Makefile',          'libretro',          'libretro/jni', {}),
    'snes9x2002':                ('snes9x2002',                 'Makefile',          '.',                 'jni', {}),
    'snes9x2010':                ('snes9x2010',                 'Makefile',          '.',                 'jni', {}),
    'stella':                    ('stella2014-libretro',        'Makefile',          '.',                 'jni', {'soname': 'stella2014'}),
    'supafaust':                 ('supafaust',                  'Makefile',          '.',                 'jni', {'soname': 'mednafen_supafaust'}),
    'swanstation':               ('swanstation',                '',                  '.',                 '', {'branch': 'main', 'cmake': True}),
    'tgbdual':                   ('tgbdual-libretro',           'Makefile',          '.',                 'jni', {}),
    'theodore':                  ('Zlika/theodore',             'Makefile',          '.',                  'jni', {}),
    'thepowdertoy':              ('kodi-game/ThePowderToy',     '',                  '',                  '', {'cmake': True, 'binary_dir': 'src', 'jnisoname': 'thepowdertoy_libretro_android'}),
    'tyrquake':                  ('tyrquake',                   'Makefile',          '.',                 'jni', {}),
    'uae':                       ('libretro-uae',               'Makefile',          '.',                 'jni', {'soname': 'puae'}),
    #'uae4arm':                   ('uae4arm-libretro',           'Makefile',          '.',                 'jni', {}),  # Fails to build on non arm system
    'uzem':                      ('libretro-uzem',              'Makefile.libretro', '.',                 'jni', {}),
    'vba-next':                  ('vba-next',                   'Makefile',          '.',                 'libretro/jni', {'soname': 'vba_next'}),
    'vbam':                      ('vbam-libretro',              'Makefile',          'src/libretro',      'src/libretro/jni', {}),
    'vecx':                      ('libretro-vecx',              'Makefile',          '.',                 'jni', {}),
    'vemulator':                 ('vemulator-libretro',         'Makefile',          '.',                 'jni', {}),
    'vice':                      ('kodi-game/vice-libretro',    'Makefile',          '.',                 'jni', {'soname': 'vice_x64'}),
    'virtualjaguar':             ('virtualjaguar-libretro',     'Makefile',          '.',                 'jni', {}),
    'wolfenstein3d':             ('kodi-game/libretro-wolfenstein3d', 'Makefile.libretro', '.',           'jni', {}),
    'xmil':                      ('xmil-libretro',              'Makefile.libretro', 'libretro',          'libretro/jni', {'soname': 'x1'}),
    'xrick':                     ('xrick-libretro',             'Makefile.libretro', '.',                 'jni', {}),
    'yabause':                   ('yabause',                    'Makefile',          'yabause/src/libretro', 'yabause/src/libretro/jni', {}),
}
