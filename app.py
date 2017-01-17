#!/usr/bin/python
"""
"""
import time

from modules.images import TextToImage
from modules.ip_commands import get_ip, whoami
from modules.twitter import tweet_image

image = TextToImage(get_ip())
image.create_image()

now = time.strftime("%Y-%m-%d %H:%M")
message = '#{whoami} {now}'.format(whoami=whoami, now=now)

try:
    tweet_image(image.filename.name, message)
finally:
    image.del_image()
