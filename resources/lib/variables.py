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
from tulip.control import setting

sysaddon = ''

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
mags_base_url = 'http://alivegr.net/bci_mags/index.txt'
subscribe_url = 'https://bcimedia.net/order/cart.php?gid=1'
status_url = 'https://bcimedia.net/order/handler.php?action=login&status={0}&licensekey={1}'
account_status = 'https://bcimedia.net/order/clientarea.php?action=productdetails&id=1'

# NETV_Toronto_url = ('https://www.netvtoronto.com/', 'Ahr0Chm6lY9SAxzLlNn0CMvHBxmUB3zOl1q0ndrutMfWv1ryEtrWl1q0ndrutMfWv1ryEtrWl3bSyxLSAxn0lM0ZDtG=')
# Cannali_url = ('https://www.cannalimusic.com/', 'Ahr0Chm6lY9SAxzLlNn0CMvHBxmUB3zOl3nLuuD4sdzTngeVC2vrr3HinM00ys9JAhvUA2XPC3rFDZeZntCWmJmWmY5Tm3u4')
# Life_url = ('https://www.lifehd.magicstreams.net/', 'Ahr0Chm6lY9SAxzLlNn0CMvHBxmUB3zOlZHnBw1uwMPAsfaVoe1TBvrAALPiuc9JAhvUA2XPC3rFDZe5mJeXmJmWmdiUBtn1oa==')


yt_keys = {
    'id': '498788153161-pe356urhr0uu2m98od6f72k0vvcdsij0.apps.googleusercontent.com',
    'api_key': 'AIzaSyA8k1OyLGf03HBNl0byD511jr9cFWo2GR4',
    'secret': 'e6RBIFCVh1Fm-IX87PVJjgUu'
}


if setting('hls') == 'true':

    NETV_Toronto_url = 'http://live.netvtoronto.com:1935/NetvToronto/NetvToronto/playlist.m3u8'
    # NETV_Toronto_2_url = 'http://162.219.176.210/live/eugo242017p1a/playlist.m3u8'
    Life_url = 'http://live.streams.ovh:1935/LIFEHD/LIFEHD/playlist.m3u8'
    # Eugo24_url = 'http://162.219.176.210:18935/live/eugo242017p1a/playlist.m3u8'
    Cannali_url = 'http://live.streams.ovh:1935/cannali/cannali/playlist.m3u8'

else:

    NETVToronto_url = 'rtmp://live.netvtoronto.com/NetvToronto/NetvToronto'
    # NETV_Toronto_2_url = 'rtmp://162.219.176.210/live/eugo242017p1a'
    Life_url = 'rtmp://live.streams.ovh:1935/LIFEHD/LIFEHD'
    # Eugo24_url = 'rtmp://162.219.176.210:18935/live/eugo242017p1a'
    Cannali_url = 'rtmp://live.streams.ovh/cannali/cannali'
