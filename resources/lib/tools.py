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


import sys, re
from tulip.compat import unquote_plus, urljoin
from random import shuffle
from tulip import control, client, cache, directory
from resources.lib import variables
from base64 import b64decode as decoder
from youtube_registration import register_api_keys


def play_item(url):

    if url == 'netv':

        url = substitute(variables.NETV_Toronto_url[1])
        headers = {'Referer': variables.NETV_Toronto_url[0], 'Origin': variables.NETV_Toronto_url[0]}

    elif url == 'cannali':

        url = substitute(variables.Cannali_url[1])
        headers = {'Referer': variables.Cannali_url[0], 'Origin': variables.Cannali_url[0]}

    elif url == 'lifehd':

        url = substitute(variables.Life_url[1])
        headers = {'Referer': variables.Life_url[0], 'Origin': variables.Life_url[0]}

    else:

        headers = None

    directory.resolve(url, headers=headers)


def play_yt_m3u(url, title):

    NETV2_overlay = control.transPath(control.join(control.addonPath, 'media', 'netv2-overlay.png'))
    Life_overlay = control.transPath(control.join(control.addonPath, 'media', 'life-overlay.png'))

    if title == 'NETV Toronto 2':
        control.copy(
            NETV2_overlay, control.transPath(control.join(control.addon('service.banners.mod').getAddonInfo('profile'), 'mybanners', 'logo.png'))
        )
    elif title == 'Life HD':
        control.copy(
            Life_overlay, control.transPath(control.join(control.addon('service.banners.mod').getAddonInfo('profile'), 'mybanners', 'logo.png'))
        )

    control.addon('service.banners.mod').setSetting('on', 'true')
    control.addon('service.banners.mod').setSetting('bannerpos', '0')
    control.addon('service.banners.mod').setSetting('yoffset', '0')
    control.addon('service.banners.mod').setSetting('cyclepause', '0')
    control.addon('service.banners.mod').setSetting('changetime', '5')

    m3u_file = control.join(control.dataPath, url.rpartition('/')[2])

    play_list = client.request(url)
    videos = play_list.splitlines()[1:][1::2]
    shuffle(videos)
    m3u_playlist = '#EXTM3U\n#EXTINF:0,{0}\n'.format(title) + '\n#EXTINF:0,{0}\n'.format(title).join(videos)

    with open(m3u_file, 'w') as f:
        f.write(m3u_playlist)

    control.playlist().load(m3u_file)
    control.execute('Action(Play)')


def play_media(link, image):

    link = unquote_plus(link)
    li = control.item(path=link, iconImage=image, thumbnailImage=image)
    li.setArt({'thumb': image})

    control.player().play(link, li)
    # Reserving backup method, requires li.setProperty('IsPlayable', 'true'):
    # xbmcplugin.setResolvedUrl(syshandle, True, li)


def magazine_list():

    control.content(int(sys.argv[1]), 'images')

    index_txt = client.request(variables.mags_base_url)

    splitted = index_txt.splitlines()

    number = re.sub(r'Volume (\d{1,3}).+', r'\1', splitted[-1])

    if len(number) == 1:
        number = '00' + number
    elif len(number) == 2:
        number = '0' + number

    voice_img = urljoin(variables.mags_base_url, 'mag_thumb_{0}.jpg'.format(number))

    magazines = []

    for line in splitted:

        title = line.replace('Volume', control.lang(30025))

        image = line.partition(' - ')[0].replace('Volume ', 'vol')
        image = urljoin(variables.mags_base_url, image + '/thumbs' + '/thumb-01.jpg')

        url = '{0}?action=mag_index&url={1}'.format(sys.argv[0], image.partition('/thumbs')[0])

        data = {'title': title, 'image': image, 'url': url}

        magazines.append(data)

    return magazines, voice_img


def mags_addon():

    directory.run_builtin('plugin.video.Toronto-Channels', content_type='image')


def radio_player():

    lista = ['Radio Melodia Toronto', 'Canadian Ethnic Web Radio']

    selection = control.selectDialog(lista)

    if selection == 0:

        listitem = control.item(label=lista[0])
        listitem.setInfo('music', {'title': lista[0], 'genre': 'Greek Music'})
        listitem.setArt({'icon': control.addonmedia('RADIO_MELODIA_TORONTO.png'), 'thumb': control.addonmedia('RADIO_MELODIA_TORONTO.png')})

        control.player().play(item=variables.Melodia_url, listitem=listitem)

    elif selection == 1:

        listitem = control.item(label=lista[1])
        listitem.setInfo('music', {'title': lista[1], 'genre': 'Ethnic Music'})
        listitem.setArt({'icon': control.addonmedia('CANADIAN_ETHNIC_WEB_RADIO.jpg'), 'thumb': control.addonmedia('CANADIAN_ETHNIC_WEB_RADIO.jpg')})

        control.player().play(item=variables.CEWR_url, listitem=listitem)


def keymap_edit():

    location = control.transPath(control.join('special://profile', 'keymaps', 'tc.xml'))

    def seq():

        string_start = '<keymap><slideshow><mouse>'
        string_end = '</mouse></slideshow></keymap>'
        string_for_left = '<leftclick>NextPicture</leftclick>'
        string_for_right = '<rightclick>PreviousPicture</rightclick>'
        string_for_middle = '<middleclick>Rotate</middleclick>'
        string_for_up = '<wheelup>ZoomIn</wheelup>'
        string_for_down = '<wheeldown>ZoomOut</wheeldown>'

        strings = [string_for_left, string_for_right, string_for_middle, string_for_up, string_for_down]

        map_left = control.lang(30031)
        map_right = control.lang(30032)
        map_middle = control.lang(30033)
        map_up = control.lang(30034)
        map_down = control.lang(30035)

        keys = [map_left, map_right, map_middle, map_up, map_down]

        control.okDialog(control.name(), control.lang(30030))

        indices = control.dialog.multiselect(control.name(), keys)

        if not indices:

            control.infoDialog(control.lang(30036))

        else:

            finalized = []

            for i in indices:
                finalized.append(strings[i])

            joined = ''.join(finalized)

            to_write = string_start + joined + string_end

            with open(location, 'w') as f:
                f.write(to_write)

            control.execute('Action(reloadkeymaps)')

            control.infoDialog(control.lang(30015))

    yes = control.yesnoDialog(control.lang(30028), control.lang(30014))

    if yes:

        if control.exists(location):

            choices = [control.lang(30038), control.lang(30039)]

            choice = control.selectDialog(choices)

            if choice == 0:

                seq()

            elif choice == 1:

                control.deleteFile(location)
                control.execute('Action(reloadkeymaps)')

            else:

                control.infoDialog(control.lang(30016))

        else:

            seq()

    else:

        control.infoDialog(control.lang(30016))


def youtube_channel(url):

    register_api_keys(
        control.addonInfo('id'), variables.yt_keys['api_key'], variables.yt_keys['id'], variables.yt_keys['secret']
    )

    control.execute('Container.Update({0},return)'.format(url))


def substitute(regex):

    substitution = decoder(regex.swapcase())

    return substitution


def check_key(key=control.addon(variables.sysaddon).getSetting('licence_key')):

    status = client.request(
        variables.status_url.format('active', key)
    ) == 'Active' or client.request(
        variables.status_url.format('reissued', key)
    ) == 'Active'

    if status is False:

        control.addon(variables.sysaddon).setSetting('status', 'false')
        return False

    else:

        control.addon(variables.sysaddon).setSetting('status', 'true')
        return True


def checkpoint():

    if not control.setting('licence_key'):

        choices = [control.lang(30064), control.lang(30065), control.lang(30066)]

        choice = control.selectDialog(choices, control.lang(30058))

        if choice == 0 or choice == 1:

            if choice == 0:

                control.open_web_browser(variables.subscribe_url)

            key = control.inputDialog(heading=control.lang(30060))

            if not key:

                control.infoDialog(control.lang(30061))

                return

            else:

                control.setSetting('licence_key', key)

                status = cache.get(check_key, 2, key)

                if not status:

                    return

                else:

                    return status

        elif choice == 2:

            control.open_web_browser(variables.subscribe_url)

        else:

            control.okDialog(heading=control.name(), line1=control.lang(30062))

    elif control.setting('licence_key') and control.setting('status') == 'false':

        choices = [control.lang(30067), control.lang(30065), control.lang(30066)]

        # choice = control.selectDialog(choices, control.lang(30063))
        choice = control.dialog.select(heading=control.lang(30063), list=choices)

        if choice == 0 or choice == 1:

            if choice == 0:

                control.open_web_browser(variables.subscribe_url)

            key = control.inputDialog(heading=control.lang(30060))

            if not key:

                control.infoDialog(control.lang(30061))

                return False

            else:

                control.setSetting('licence_key', key)

                status = cache.get(check_key, 2, key)

                if not status:

                    return

                else:

                    return status

        elif choice == 2:

            control.open_web_browser(variables.subscribe_url)

        else:

            control.okDialog(heading=control.name(), line1=control.lang(30062))

    else:

        return cache.get(check_key, 2)
