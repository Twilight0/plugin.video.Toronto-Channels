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
from tulip import control, directory, client
from tulip.compat import range
from . import variables
from .tools import magazine_list


class Indexer:

    def __init__(self, argv):

        self.list = []; self.menu = []
        self.argv = argv

    def main_menu(self):

        self.list = [
            {
                'title': 'NET Toronto',
                'action': 'play', 'isFolder': 'False',
                'url': variables.NETV_Toronto_url,
                'icon': 'NET_Toronto.png',
                'boolean': control.setting('netv') == 'true',
                'plot': control.lang(30006), 'genre': 'Live'
            }
            ,
            # {
            #     'title': 'Life HD',
            #     'action': 'play', 'isFolder': 'False',
            #     'url': variables.Life_url,
            #     'icon': 'LIFEHD.png',
            #     'boolean': control.setting('life') == 'true',
            #     'plot': control.lang(30008), 'genre': 'Pseudo-Live'
            # }
            # ,
            {
                'title': 'CANNALI Music',
                'action': 'play', 'isFolder': 'False',
                'url': variables.Cannali_url,
                'icon': 'CANNALI.png',
                'boolean': control.setting('cannali') == 'true',
                'plot': control.lang(30007), 'genre': 'Live'
            }
            ,
            {
                'title': 'BCI 24 News',
                'url': variables.NEWS_url,
                'icon': 'BCI_24_News.png',
                'action': 'play', 'isFolder': 'False',
                'boolean': control.setting('news') == 'true',
                'genre': 'Live'
            }
            ,
            {
                'title': 'RIK Sat',
                'url': variables.RIK_url,
                'icon': 'RIK_SAT.png',
                'action': 'play', 'isFolder': 'False',
                'boolean': control.setting('rik') == 'true',
                'genre': 'Live'
            }
            ,
            {
                'title': 'RIK Proto',
                'url': variables.RIK_proto,
                'icon': 'RIK_PROTO.png',
                'action': 'play', 'isFolder': 'False',
                'boolean': control.setting('rik') == 'true',
                'genre': 'Live'
            }
            ,
            {
                'title': 'RIK Trito',
                'url': variables.RIK_trito,
                'icon': 'RIK_TRITO.png',
                'action': 'play', 'isFolder': 'False',
                'boolean': control.setting('rik') == 'true',
                'genre': 'Live'
            }
            # ,
            # {
            #     'title': 'Energy',
            #     'action': 'play', 'isFolder': 'False',
            #     'url': 'energy',
            #     'icon': 'ENERGY.png',
            #     'boolean': control.setting('energy') == 'true',
            #     'plot': control.lang(30041), 'genre': 'Live'
            # }
            ,
            {
                'title': 'Youtube Channel',
                'action': 'youtube_channel', 'isFolder': 'False', 'isPlayable': 'False',
                'url': 'plugin://plugin.video.youtube/channel/{0}/?addon_id={1}'.format(variables.YT_Channel, control.addonInfo('id')),
                'boolean': control.setting('youtube') == 'true'
            }
            ,
            {
                'title': 'Radio Melodia Toronto',
                'url': variables.Melodia_url,
                'action': 'play', 'isFolder': 'False',
                'icon': 'RADIO_MELODIA_TORONTO.png',
                'boolean': control.setting('melodia') == 'true',
                'plot': control.lang(30009), 'genre': 'Live',
                'infotype': 'music'
            }
            # ,
            # {
            #     'title': 'Canadian Ethnic Web Radio',
            #     'url': variables.CEWR_url,
            #     'action': 'play', 'isFolder': 'False',
            #     'icon': 'CANADIAN_ETHNIC_WEB_RADIO.jpg',
            #     'boolean': control.setting('cewr') == 'true',
            #     'genre': 'Live',
            #     'infotype': 'music'
            # }
            ,
            {
                'title': 'Voice Life & Style Mag',
                'action': 'mags_addon', 'isFolder': 'False', 'isPlayable': 'False',
                'image': magazine_list()[1],
                'boolean': control.setting('voice') == 'true'
            }
            ,
            {
                'title': 'BCI Media Website',
                'url': 'https://www.bcimedia.net/',
                'action': 'open_url', 'isFolder': 'False', 'isPlayable': 'False',
                'boolean': control.setting('external') == 'true'
            }
        ]

        self.menu = [i for i in self.list if i['boolean']]

        self.menu.append(
            {
                'title': control.lang(30001), 'action': 'settings', 'icon': 'settings.png',
                'isFolder': 'False', 'isPlayable': 'False'
            }
        )

        directory.add(self.menu, argv=self.argv, content='movies')

    def mag_index(self, url):

        number = int(client.request(url + '/pages'))

        pages = []

        for page in list(range(1, number + 1)):

            string = str(page)

            title = control.lang(30026) + ' ' + string

            if len(string) == 2:
                image = url + '/thumbs' + '/thumb-' + string + '.jpg'
                link = url + '/page-' + string + '.jpg'
            else:
                image = url + '/thumbs' + '/thumb-' + '0' + string + '.jpg'
                link = url + '/page-' + '0' + string + '.jpg'

            data = {'title': title, 'image': image, 'url': link}
            pages.append(data)

        for p in pages:

            li = control.item(label=p['title'], iconImage=p['image'], thumbnailImage=p['image'])
            li.setArt({'poster': p['image'], 'thumb': p['image'], 'fanart': control.addonInfo('fanart')})
            li.setInfo('image', {'title': p['title'], 'picturepath': p['image']})
            path = p['url']

            control.addItem(int(self.argv[1]), path, li, False)

        control.directory(int(self.argv[1]))

    def mags_index(self):

        magazines = magazine_list()[0]

        for mag in magazines:

            li = control.item(label=mag['title'], iconImage=mag['image'])
            li.setArt({'poster': mag['image'], 'thumb': mag['image'], 'fanart': control.addonInfo('fanart')})
            li.setInfo('image', {'title': mag['title'], 'picturepath': mag['url']})
            url = mag['url']

            control.addItem(int(self.argv[1]), url, li, True)

        control.directory(int(self.argv[1]))
