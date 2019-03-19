# -*- coding: utf-8 -*-

"""
    Toronto Channels Add-on
    Author: BCI Media Inc.

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import absolute_import

########################################################################################################################

import sys
from tulip.compat import parse_qsl
from resources.lib import navigator, tools

########################################################################################################################

argv = sys.argv
syshandle = int(argv[1])
sysaddon = argv[0]
params = dict(parse_qsl(argv[2].replace('?','')))

########################################################################################################################

content = params.get('content_type')
action = params.get('action')
url = params.get('url')
image = params.get('image')
title = params.get('title')
name = params.get('name')
query = params.get('query')


proceed = tools.checkpoint()


if content == 'video' and proceed:

    navigator.Indexer(argv=argv).main_menu()

elif content == 'audio' and proceed:

    tools.radio_player()

elif content == 'image' and proceed:

    navigator.Indexer(argv=argv).mags_index()

elif action is None and proceed:

    navigator.Indexer(argv=argv).main_menu()

elif action == 'play' and proceed:

    tools.play_item(url)

elif action == 'play_yt_m3u':

    tools.play_yt_m3u(url, title)

elif action == 'play_media':

    tools.play_media(url, image)

elif action == 'mags_index' and proceed:

    navigator.Indexer(argv=argv).mags_index()

elif action == 'mags_addon' and proceed:

    tools.mags_addon()

elif action == 'youtube_channel':

    tools.youtube_channel(url)

elif action == 'mag_index' and proceed:

    navigator.Indexer(argv=argv).mag_index(url)

elif action == 'settings':

    from tulip.control import Settings
    Settings()

elif action == 'keymap_edit':

    tools.keymap_edit()

elif action == 'open_url':

    from tulip.control import open_web_browser
    open_web_browser(url)

elif action == 'account_info':

    from tulip.control import open_web_browser
    from resources.lib.variables import account_status
    open_web_browser(account_status)
