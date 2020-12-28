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
import json
from zlib import decompress
from tulip.control import setting
from base64 import b64decode


Melodia_url = 'http://cast.streams.ovh:9086/live'
RIK_url = 'http://l3.cloudskep.com/cybcsat/abr/playlist.m3u8'
RIK_proto = 'http://r1.cloudskep.com/cybcr/cybc1/playlist.m3u8'
RIK_trito = 'http://r1.cloudskep.com/cybcr/cybc3/playlist.m3u8'
# SIGMA_url = 'http://81.21.47.74/hls/live.m3u8'
# CEWR_url = 'http://147.135.252.4:10221/live'
YT_Channel = 'UCKXFDK9dRGcnwr7mWmzoY2w'
mags_base_url = 'https://alivegr.net/bci_mags/index.txt'

# NETV_Toronto_url = ('https://www.netvtoronto.com/', 'Ahr0Chm6lY9SAxzLlNn0CMvHBxmUB3zOl1q0ndrutMfWv1ryEtrWl1q0ndrutMfWv1ryEtrWl3bSyxLSAxn0lM0ZDtG=')
# Cannali_url = ('https://www.cannalimusic.com/', 'Ahr0Chm6lY9SAxzLlNn0CMvHBxmUB3zOl3nLuuD4sdzTngeVC2vrr3HinM00ys9JAhvUA2XPC3rFDZeZntCWmJmWmY5Tm3u4')
# Life_url = ('https://www.lifehd.magicstreams.net/', 'Ahr0Chm6lY9SAxzLlNn0CMvHBxmUB3zOlZHnBw1uwMPAsfaVoe1TBvrAALPiuc9JAhvUA2XPC3rFDZe5mJeXmJmWmdiUBtn1oa==')


scramble = (
    'eJwVzM0OgiAAAOBXcZzLpaiwblmt2cHNXHlshoSm/AREWuvdmw/wfV/QNWDtgRAhjCMYJzAMlzJY6TbRSpgWUx3A2A1INOZppUNxyx5+rZTxmZRsoC'
    '9DNZHCUmF9IjlYeKBW3bWn09xusk9dTinKmzHYVq6fduKENWHBLXsXZKyY40c+nmdlKNHUziiP9gfMLrBitHAFx6S7K8zSEvz+QP85Rw=='
)


if setting('hls') == 'true':

    NETV_Toronto_url = 'https://live.netvtoronto.com:1935/NetvToronto/NetvToronto/playlist.m3u8'
    # NETV_Toronto_2_url = 'http://162.219.176.210/live/eugo242017p1a/playlist.m3u8'
    Life_url = 'https://live.streams.ovh:1935/LIFEHD/LIFEHD/playlist.m3u8'
    # Eugo24_url = 'http://162.219.176.210:18935/live/eugo242017p1a/playlist.m3u8'
    Cannali_url = 'https://live.streams.ovh:1935/cannali/cannali/playlist.m3u8'
    NEWS_url = 'https://live.streams.ovh:443/netmedia/netmedia/playlist.m3u8'

else:

    NETV_Toronto_url = 'rtmp://live.netvtoronto.com/NetvToronto/NetvToronto'
    # NETV_Toronto_2_url = 'rtmp://162.219.176.210/live/eugo242017p1a'
    Life_url = 'rtmp://live.streams.ovh:1935/LIFEHD/LIFEHD'
    # Eugo24_url = 'rtmp://162.219.176.210:18935/live/eugo242017p1a'
    Cannali_url = 'rtmp://live.streams.ovh/cannali/cannali'
    NEWS_url = 'rtmps://live.streams.ovh:443/netmedia/netmedia'


keys = json.loads(decompress(b64decode(scramble)))
