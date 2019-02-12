# -*- coding: utf-8 -*-

"""
    Toronto-Channels Add-on
    Author: Twilight0

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

import os, sys, re
import xbmcaddon, xbmcgui, xbmcplugin, xbmc, xbmcvfs
from urllib import quote_plus, unquote_plus
from urlparse import parse_qsl, urljoin
from resources.lib.url_opener import read_url, open_web_browser

# Addon variables:
join = os.path.join
addon = xbmcaddon.Addon
language = addon().getLocalizedString
addonname = addon().getAddonInfo("name")
addonid = addon().getAddonInfo("id")
addonpath = addon().getAddonInfo("path")
addonfanart = addon().getAddonInfo("fanart")
addItem = xbmcplugin.addDirectoryItem
endDir = xbmcplugin.endOfDirectory
transpath = xbmc.translatePath
datapath = transpath(addon().getAddonInfo("profile")).decode("utf-8")

if not xbmcvfs.exists(datapath):
    xbmcvfs.mkdirs(datapath)

dialog = xbmcgui.Dialog()
infoLabel = xbmc.getInfoLabel
fp = infoLabel('Container.FolderPath')
player = xbmc.Player().play
playlist = xbmc.PlayList(xbmc.PLAYLIST_VIDEO)
monitor = xbmc.Monitor()
copy = xbmcvfs.copy
delete = xbmcvfs.delete

# Misc variables:
addonicon = join(addonpath, 'icon.png')
addonart = join(addonpath, 'resources/media')
NETVToronto_img = join(addonart, 'NETV_Toronto.png')
NETVToronto_2_img = join(addonart, 'NETV_Toronto_2.png')
NETV2_overlay = join(addonart, 'netv2-overlay.png')
NETVToronto_3_img = join(addonart, 'NETV_Toronto_3.png')
Cannali_img = join(addonart, 'CANNALI_WEB_MUSIC.png')
Melodia_img = join(addonart, 'RADIO_MELODIA_TORONTO.png')
CEWR_img = join(addonart, 'CANADIAN_ETHNIC_WEB_RADIO.jpg')
Life_img = join(addonart, 'LIFEHD.png')
Life_overlay = join(addonart, 'life-overlay.png')
Energy_img = join(addonart, 'ENERGY.png')
Energy_overlay = join(addonart, 'energy-overlay.png')
Eugo24_img = join(addonart, 'EUGO24.png')
RIK_img = join(addonart, 'RIK.png')
SIGMA_img = join(addonart, 'SIGMA.png')
OMEGA_CY_img = join(addonart, 'OMEGA.png')
ALPHA_CY_img = join(addonart, 'ALPHA.png')
PLUS_img = join(addonart, 'PLUS.png')
CAPITAL_img = join(addonart, 'CAPITAL.png')
Settings_img = join(addonart, 'settings.png')
# Voice_img = join(addonart, 'mag_thumb.jpg')

# Links:
if addon().getSetting('hls') == 'false':

    NETVToronto_url = 'rtmp://live.netvtoronto.com/NetvToronto/NetvToronto'
    # NETV_Toronto_2_url = 'rtmp://162.219.176.210/live/eugo242017p1a'
    NETV_Toronto_3_url = Energy_url = 'rtmp://live.streams.ovh:1935/LIFEHD/LIFEHD'
    # Eugo24_url = 'rtmp://162.219.176.210:18935/live/eugo242017p1a'
    Cannali_url = 'rtmp://live.streams.ovh/cannali/cannali'

else:

    NETVToronto_url = 'http://live.netvtoronto.com:1935/NetvToronto/NetvToronto/playlist.m3u8'
    # NETV_Toronto_2_url = 'http://162.219.176.210/live/eugo242017p1a/playlist.m3u8'
    NETV_Toronto_3_url = Energy_url = 'http://live.streams.ovh:1935/LIFEHD/LIFEHD/playlist.m3u8'
    # Eugo24_url = 'http://162.219.176.210:18935/live/eugo242017p1a/playlist.m3u8'
    Cannali_url = 'http://live.streams.ovh:1935/cannali/cannali/playlist.m3u8'

########################################################################################################################

Melodia_url = 'http://149.202.208.214:9086/live'
ALPHA_CY_url = 'plugin://plugin.video.alphatv.gr/?action=live&url=cy'
RIK_url = 'http://l3.cloudskep.com/cybcsat/abr/playlist.m3u8'
SIGMA_url = 'http://81.21.47.74/hls/live.m3u8'
CEWR_url = 'http://147.135.252.4:10221/live'
OMEGA_CY_url = 'http://freeview.ashttp9.visionip.tv/live/tvnetwork-hellenictv-mega-hsslive-25f-4x3-SDh/chunklist.m3u8'
PLUS_url = 'http://freeview.ashttp9.visionip.tv/live/tvnetwork-hellenictv-plus_tv-hsslive-25f-4x3-SDh/chunklist.m3u8'
CAPITAL_url = 'http://freeview.ashttp9.visionip.tv/live/tvnetwork-hellenictv-htvcapital-hsslive-25f-4x3-SDh/chunklist.m3u8'
YT_Channel = 'UCKXFDK9dRGcnwr7mWmzoY2w'
YT_Doc_playlist = 'http://alivegr.net/raw/docs.m3u'
YT_Kids_playlist = 'http://alivegr.net/raw/kids.m3u'
mags_base_url = 'http://alivegr.net/bci_mags/'
index_url = urljoin(mags_base_url, 'index.txt')


# Handlers:
sysaddon = sys.argv[0]
syshandle = int(sys.argv[1])
params = dict(parse_qsl(sys.argv[2][1:]))
action = params.get('action', None)
url = params.get('url')
name = params.get('name')
image = params.get('image')


def play_item(path):

    li = xbmcgui.ListItem(path=path)
    xbmcplugin.setResolvedUrl(syshandle, True, listitem=li)


def play_yt_m3u(link, title):

    if title == 'NETV Toronto 2':
        copy(NETV2_overlay, transpath(join(addon('service.banners.mod').getAddonInfo('profile').decode('utf-8'), 'mybanners', 'logo.png')))
    elif title == 'Life HD':
        copy(Life_overlay, transpath(join(addon('service.banners.mod').getAddonInfo('profile').decode('utf-8'), 'mybanners', 'logo.png')))

    addon('service.banners.mod').setSetting('on', 'true')
    addon('service.banners.mod').setSetting('bannerpos', '0')
    addon('service.banners.mod').setSetting('yoffset', '0')
    addon('service.banners.mod').setSetting('cyclepause', '0')
    addon('service.banners.mod').setSetting('changetime', '5')

    import random

    if not xbmcvfs.exists(datapath):
        xbmcvfs.mkdirs(datapath)

    m3u_file = join(datapath, link.rpartition('/')[2])

    play_list = read_url(link)
    videos = play_list.splitlines()[1:][1::2]
    random.shuffle(videos)
    m3u_playlist = '#EXTM3U\n#EXTINF:0,{0}\n'.format(title) + '\n#EXTINF:0,{0}\n'.format(title).join(videos)

    with open(m3u_file, 'w') as f:
        f.write(m3u_playlist)

    playlist.load(m3u_file)
    xbmc.executebuiltin('Action(Play)')


def play_media(link, image):

    link = unquote_plus(link)
    li = xbmcgui.ListItem(path=link, iconImage=image, thumbnailImage=image)
    li.setArt({'thumb': image})

    xbmc.Player().play(link, li)
    # Reserving backup method, requires li.setProperty('IsPlayable', 'true'):
    # xbmcplugin.setResolvedUrl(syshandle, True, li)


def magazine_list():

    xbmcplugin.setContent(syshandle, 'images')

    index_txt = read_url(index_url)

    splitted = index_txt.splitlines()

    number = re.sub(r'Volume (\d{1,3}).+', r'\1', splitted[-1])

    if len(number) == 1:
        number = '00' + number
    elif len(number) == 2:
        number = '0' + number

    voice_img = urljoin(mags_base_url, 'mag_thumb_{0}.jpg'.format(number))

    magazines = []

    for line in splitted:

        title = line.replace('Volume', language(30025))

        image = line.partition(' - ')[0].replace('Volume ', 'vol')
        image = urljoin(mags_base_url, image + '/thumbs' + '/thumb-01.jpg')

        url = '{0}?action=mag_index&url={1}'.format(sysaddon, image.partition('/thumbs')[0])

        data = {'title': title, 'image': image, 'url': url}

        magazines.append(data)

    return magazines, voice_img


def mags_index():

    magazines = magazine_list()[0]

    for mag in magazines:

        li = xbmcgui.ListItem(label=mag['title'], iconImage=mag['image'])
        li.setArt({'poster': mag['image'], 'thumb': mag['image'], 'fanart': addonfanart})
        li.setInfo('image', {'title': mag['title'], 'picturepath': mag['url']})
        url = mag['url']
        isFolder = True

        xbmcplugin.addDirectoryItem(syshandle, url, li, isFolder)

    xbmcplugin.endOfDirectory(syshandle)


def mag_index(url):

    number = int(read_url(url + '/pages'))

    pages = []

    for page in range(1, number + 1):

        string = str(page)

        title = language(30026) + ' ' + string

        if len(string) == 2:
            image = url + '/thumbs' + '/thumb-' + string + '.jpg'
            link = url + '/page-' + string + '.jpg'
        else:
            image = url + '/thumbs' + '/thumb-' + '0' + string + '.jpg'
            link = url + '/page-' + '0' + string + '.jpg'

        data = {'title': title, 'image': image, 'url': link}
        pages.append(data)

    for p in pages:

        li = xbmcgui.ListItem(label=p['title'], iconImage=p['image'], thumbnailImage=p['image'])
        li.setArt({'poster': p['image'], 'thumb': p['image'], 'fanart': addonfanart})
        li.setInfo('image', {'title': p['title'], 'picturepath': p['image']})
        path = p['url']

        xbmcplugin.addDirectoryItem(syshandle, path, li, False)

    xbmcplugin.endOfDirectory(syshandle)


def main_menu():

    xbmcplugin.setContent(syshandle, 'movies')

    # NETV Toronto
    if addon().getSetting('netv') == 'true':

        url0 = '{0}?action=play&url={1}'.format(sysaddon, NETVToronto_url)
        li0 = xbmcgui.ListItem(label='NETV Toronto', iconImage=NETVToronto_img)
        li0.setArt({'poster': NETVToronto_img, 'thumb': NETVToronto_img, 'fanart': addonfanart})
        li0.setInfo('video', {'title': 'NETV Toronto', 'plot': language(30006), 'genre': 'Live'})
        li0.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url0, listitem=li0, isFolder=False)

    # NETV Toronto 2
    if addon().getSetting('netv2') == 'true':

        url1 = '{0}?action=play_yt_m3u&url={1}&name={2}'.format(sysaddon, YT_Doc_playlist, 'NETV Toronto 2')
        li1 = xbmcgui.ListItem(label='NETV Toronto 2', iconImage=NETVToronto_2_img)
        li1.setArt({'poster': NETVToronto_2_img, 'thumb': NETVToronto_2_img, 'fanart': addonfanart})
        li1.setInfo('video', {'title': 'NETV Toronto 2', 'plot': language(30019), 'genre': 'Live'})
        li1.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url1, listitem=li1, isFolder=False)

    # NETV Toronto 3
    if addon().getSetting('netv3') == 'true':

        url2 = '{0}?action=play&url={1}'.format(sysaddon, NETV_Toronto_3_url)
        li2 = xbmcgui.ListItem(label='NETV Toronto 3', iconImage=NETVToronto_3_img)
        li2.setArt({'poster': NETVToronto_3_img, 'thumb': NETVToronto_3_img, 'fanart': addonfanart})
        li2.setInfo('video', {'title': 'NETV Toronto 3', 'plot': '', 'genre': 'Live'})
        li2.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url2, listitem=li2, isFolder=False)

    # Life HD
    if addon().getSetting('life') == 'true':

        url3 = '{0}?action=play_yt_m3u&url={1}&name={2}'.format(sysaddon, YT_Kids_playlist, 'Life HD')
        li3 = xbmcgui.ListItem(label='Life HD', iconImage=Life_img)
        li3.setArt({'poster': Life_img, 'thumb': Life_img, 'fanart': addonfanart})
        li3.setInfo('video', {'title': 'Life HD', 'plot': language(30008), 'genre': 'Live'})
        li3.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url3, listitem=li3, isFolder=False)

    # Cannali Music
    if addon().getSetting('cannali') == 'true':

        url5 = '{0}?action=play&url={1}'.format(sysaddon, Cannali_url)
        li5 = xbmcgui.ListItem(label='CANNALI Music', iconImage=Cannali_img)
        li5.setArt({'poster': Cannali_img, 'thumb': Cannali_img, 'fanart': addonfanart})
        li5.setInfo('video', {'title': 'CANNALI Music', 'plot': language(30007), 'genre': 'Live'})
        li5.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url5, listitem=li5, isFolder=False)

    # Energy
    if addon().getSetting('energy') == 'true':

        url5 = '{0}?action=play&url={1}'.format(sysaddon, Energy_url)
        li5 = xbmcgui.ListItem(label='Energy', iconImage=Energy_img)
        li5.setArt({'poster': Energy_img, 'thumb': Energy_img, 'fanart': addonfanart})
        li5.setInfo('video', {'title': 'Energy', 'plot': language(30041), 'genre': 'Live'})
        li5.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url5, listitem=li5, isFolder=False)

    # Youtube Channel
    if addon().getSetting('youtube') == 'true':

        from youtube_registration import register_api_keys

        yt_keys = {
            'id': '498788153161-pe356urhr0uu2m98od6f72k0vvcdsij0.apps.googleusercontent.com',
            'api_key': 'AIzaSyA8k1OyLGf03HBNl0byD511jr9cFWo2GR4',
            'secret': 'e6RBIFCVh1Fm-IX87PVJjgUu'
        }

        register_api_keys('plugin.video.Toronto-Channels', yt_keys['api_key'], yt_keys['id'], yt_keys['secret'])

        url6 = 'plugin://plugin.video.youtube/channel/{0}/'.format(YT_Channel) + '?addon_id=plugin.video.Toronto-Channels'
        li6 = xbmcgui.ListItem(label='Youtube Channel', iconImage=addonicon)
        li6.setArt({'poster': addonicon, 'thumb': addonicon, 'fanart': addonfanart})
        addItem(handle=syshandle, url=url6, listitem=li6, isFolder=True)

    # Radio Melodia Toronto
    if addon().getSetting('melodia') == 'true':

        url7 = '{0}?action=play&url={1}'.format(sysaddon, Melodia_url)
        li7 = xbmcgui.ListItem(label='Radio Melodia Toronto', iconImage=Melodia_img)
        li7.setArt({'poster': Melodia_img, 'thumb': Melodia_img, 'fanart': addonfanart})
        li7.setInfo('music', {'title': 'Radio Melodia Toronto', 'comment': language(30009), 'genre': 'Live'})
        li7.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url7, listitem=li7, isFolder=False)

    # Canadian Ethnic Web Radio
    if addon().getSetting('cewr') == 'true':

        url8 = '{0}?action=play&url={1}'.format(sysaddon, CEWR_url)
        li8 = xbmcgui.ListItem(label='Canadian Ethnic Web Radio', iconImage=CEWR_img)
        li8.setArt({'poster': CEWR_img, 'thumb': CEWR_img, 'fanart': addonfanart})
        li8.setInfo('music', {'title': 'Canadian Ethnic Web Radio', 'comment': 'Canadian Ethnic Web Radio', 'genre': 'Live'})
        li8.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url8, listitem=li8, isFolder=False)

    # Voice Life & Style
    if addon().getSetting('voice') == 'true':

        url9 = '{0}?action={1}'.format(sysaddon, 'mags_addon')
        li9 = xbmcgui.ListItem(label='Voice Life & Style Mag', iconImage=magazine_list()[1])
        li9.setArt({'poster': magazine_list()[1], 'thumb': magazine_list()[1], 'fanart': addonfanart})
        li9.setInfo('image', {'title': 'Voice Life & Style', 'picturepath': magazine_list()[1]})
        addItem(handle=syshandle, url=url9, listitem=li9, isFolder=False)

    # External link
    if addon().getSetting('external') == 'true':
        url22 = '{0}?action={1}&url={2}'.format(sysaddon, 'open_url', quote_plus('http://www.bcimedia.net/'))
        li22 = xbmcgui.ListItem(label='BCI Media Website', iconImage=addonicon)
        li22.setArt({'poster': addonicon, 'thumb': addonicon, 'fanart': addonfanart})
        addItem(handle=syshandle, url=url22, listitem=li22, isFolder=False)

    # RIK
    if addon().getSetting('rik') == 'true':

        url16 = '{0}?action=play&url={1}'.format(sysaddon, RIK_url)
        li16 = xbmcgui.ListItem(label='RIK', iconImage=RIK_img)
        li16.setArt({'poster': RIK_img, 'thumb': RIK_img, 'fanart': addonfanart})
        li16.setInfo('video', {'title': 'RIK', 'genre': 'Live'})
        li16.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url16, listitem=li16, isFolder=False)

    # SIGMA
    if addon().getSetting('sigma') == 'true':

        url17 = '{0}?action=play&url={1}'.format(sysaddon, SIGMA_url)
        li17 = xbmcgui.ListItem(label='SIGMA', iconImage=SIGMA_img)
        li17.setArt({'poster': SIGMA_img, 'thumb': SIGMA_img, 'fanart': addonfanart})
        li17.setInfo('video', {'title': 'SIGMA', 'genre': 'Live'})
        li17.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url17, listitem=li17, isFolder=False)

    # OMEGA CY
    if addon().getSetting('omega') == 'true':
        url18 = '{0}?action=play&url={1}'.format(sysaddon, OMEGA_CY_url)
        li18 = xbmcgui.ListItem(label='OMEGA CY', iconImage=OMEGA_CY_img)
        li18.setArt({'poster': OMEGA_CY_img, 'thumb': OMEGA_CY_img, 'fanart': addonfanart})
        li18.setInfo('video', {'title': 'OMEGA CY', 'genre': 'Live'})
        li18.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url18, listitem=li18, isFolder=False)

    # ALPHA CY
    if addon().getSetting('alpha') == 'true':
        url19 = '{0}?action=play_media&url={1}&image={2}'.format(sysaddon, quote_plus(ALPHA_CY_url), quote_plus(ALPHA_CY_img))
        li19 = xbmcgui.ListItem(label='ALPHA CY', iconImage=ALPHA_CY_img)
        li19.setArt({'poster': ALPHA_CY_img, 'thumb': ALPHA_CY_img, 'fanart': addonfanart})
        li19.setInfo('video', {'title': 'ALPHA CY', 'genre': 'Live'})
        addItem(handle=syshandle, url=url19, listitem=li19, isFolder=False)

    # CAPITAL
    if addon().getSetting('capital') == 'true':
        url20 = '{0}?action=play&url={1}'.format(sysaddon, CAPITAL_url)
        li20 = xbmcgui.ListItem(label='CAPITAL', iconImage=CAPITAL_img)
        li20.setArt({'poster': CAPITAL_img, 'thumb': CAPITAL_img, 'fanart': addonfanart})
        li20.setInfo('video', {'title': 'CAPITAL', 'genre': 'Live'})
        li20.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url20, listitem=li20, isFolder=False)

    # PLUS
    if addon().getSetting('plus') == 'true':
        url21 = '{0}?action=play&url={1}'.format(sysaddon, PLUS_url)
        li21 = xbmcgui.ListItem(label='PLUS', iconImage=PLUS_img)
        li21.setArt({'poster': PLUS_img, 'thumb': PLUS_img, 'fanart': addonfanart})
        li21.setInfo('video', {'title': 'PLUS', 'genre': 'Live'})
        li21.setProperty('IsPlayable', 'true')
        addItem(handle=syshandle, url=url21, listitem=li21, isFolder=False)

    # Settings
    settings_url = '{0}?action=settings'.format(sysaddon)
    settings_li = xbmcgui.ListItem(label=language(30001), iconImage=Settings_img)
    settings_li.setArt({'thumb': Settings_img, 'fanart': addonfanart})
    addItem(handle=syshandle, url=settings_url, listitem=settings_li, isFolder=True)

    endDir(syshandle)


def setup_iptv():

    if not xbmcvfs.exists(datapath):

        xbmcvfs.mkdirs(datapath)

    iptv_folder = transpath('special://profile/addon_data/pvr.iptvsimple')

    def seq():

        xbmcvfs.copy(join(addonpath, 'resources', 'iptv', 'iptv_settings.xml'), join(iptv_folder, 'settings.xml'))
        # xbmcvfs.copy(join(addonpath, 'resources', 'iptv', 'simple-client.m3u'), join(datapath, 'simple-client.m3u'))
        iscon = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
        liveon = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
        xbmc.executeJSONRPC(iscon)
        xbmc.executeJSONRPC(liveon)
        dialog.notification(addonname, language(30015), sound=False)

    if not xbmcvfs.exists(join(iptv_folder, 'settings.xml')):

        xbmcvfs.mkdirs(iptv_folder)

        if dialog.yesno(addonname, language(30013), language(30014)):
            seq()
        else:
            dialog.notification(addonname, language(30016), sound=False)

    elif xbmcvfs.exists(join(iptv_folder, 'settings.xml')):

        if dialog.yesno(addonname, language(30013), language(30017)):
            seq()
        else:
            dialog.notification(addonname, language(30016), sound=False)


def radio_player():

    lista = ['Radio Melodia Toronto', 'Canadian Ethnic Web Radio']

    selection = dialog.select(addonname, lista)

    if selection == 0:
        listitem = xbmcgui.ListItem(thumbnailImage=Melodia_img)
        listitem.setInfo('music', {'title': lista[0], 'genre': 'Greek Music'})
        player(item=Melodia_url, listitem=listitem)
    elif selection == 1:
        listitem = xbmcgui.ListItem(thumbnailImage=CEWR_img)
        listitem.setInfo('music', {'title': lista[1], 'genre': 'Ethnic Music'})
        player(item=CEWR_url, listitem=listitem)
    else:
        xbmc.executebuiltin('ActivateWindow(videos,"plugin://plugin.video.Toronto-Channels/",return)')


def mags_addon():

    xbmc.executebuiltin('ActivateWindow(pictures,"plugin://plugin.video.Toronto-Channels/?content_type=image",return)')


def keymap_edit():

    location = transpath(join('special://profile', 'keymaps', 'tc.xml'))

    def seq():

        string_start = '<keymap><slideshow><mouse>'
        string_end = '</mouse></slideshow></keymap>'
        string_for_left = '<leftclick>NextPicture</leftclick>'
        string_for_right = '<rightclick>PreviousPicture</rightclick>'
        string_for_middle = '<middleclick>Rotate</middleclick>'
        string_for_up = '<wheelup>ZoomIn</wheelup>'
        string_for_down = '<wheeldown>ZoomOut</wheeldown>'

        strings = [string_for_left, string_for_right, string_for_middle, string_for_up, string_for_down]

        map_left = language(30031)
        map_right = language(30032)
        map_middle = language(30033)
        map_up = language(30034)
        map_down = language(30035)

        keys = [map_left, map_right, map_middle, map_up, map_down]

        dialog.ok(addonname, language(30030))

        indices = dialog.multiselect(addonname, keys)

        if not indices:

            dialog.notification(addonname, language(30036), time=3, sound=False)

        else:

            finalized = []

            for i in indices:
                finalized.append(strings[i])

            joined = ''.join(finalized)

            to_write = string_start + joined + string_end

            with open(location, 'w') as f:
                f.write(to_write)

            xbmc.executebuiltin('Action(reloadkeymaps)')

            dialog.notification(addonname, language(30015), sound=False)

    yes = dialog.yesno(addonname, language(30028), language(30014))

    if yes:

        if xbmcvfs.exists(location):

            choices = [language(30038), language(30039)]

            choice = dialog.select(language(30037), choices)

            if choice == 0:

                seq()

            elif choice == 1:

                xbmcvfs.delete(location)
                xbmc.executebuiltin('Action(reloadkeymaps)')

            else:

                dialog.notification(addonname, language(30016))

        else:

            seq()

    else:

        dialog.notification(addonname, language(30016))


if action is None:

    if 'audio' in fp:
        radio_player()
    elif 'image' in fp:
        mags_index()
    else:
        main_menu()

elif action == 'play':

    play_item(url)

elif action == 'play_yt_m3u':

    play_yt_m3u(url, name)

elif action == 'play_media':

    play_media(url, image)

elif action == 'mags_index':

    mags_index()

elif action == 'mags_addon':

    mags_addon()

elif action == 'mag_index':

    mag_index(url)

elif action == 'settings':

    addon().openSettings()

elif action == 'setup_iptv':

    setup_iptv()

elif action == 'keymap_edit':

    keymap_edit()

elif action == 'open_url':

    open_web_browser(url)
