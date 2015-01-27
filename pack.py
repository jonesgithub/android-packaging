__author__ = 'jie'

import zipfile
import shutil
import sys
import os

apk_path = sys.argv[1]
out_path = sys.argv[2]

if not os.path.exists(out_path):
    os.makedirs(out_path)

name = os.path.basename(apk_path)

channels_file = open('channels.txt')

origin_apk_name = os.path.splitext(name)[0]

for channel in channels_file:
    channel_apk_name = "{}_{}.apk".format(origin_apk_name, channel.strip())
    channel_apk_path = os.path.join(out_path, channel_apk_name)
    shutil.copy2(apk_path, channel_apk_path)
    zipped = zipfile.ZipFile(channel_apk_path, 'a', zipfile.ZIP_DEFLATED)
    empty_channel_file = "META-INF/gmchannel_{}".format(channel)
    zipped.writestr(empty_channel_file, '')
    zipped.close()



