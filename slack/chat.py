# Copyright (c) 2014 Katsuya Noguchi
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

import json

import slack
import slack.http_client


def default_encoder(value): return value


FIELD_ENCODERS = {
    'attachments': json.dumps
}


def post_message(channel, text, **kwargs):
    """
    Sends a message to a channel.
    """
    data = {
        'token':        slack.api_token,
        'channel':      channel,
        'text':         text,
    }

    for key, value in kwargs.items():
        data[key] = FIELD_ENCODERS.get(key, default_encoder)(value)

    return slack.http_client.post('chat.postMessage', data)


def update(channel, timestamp, text, **kwargs):
    """
    Updates a message to a channel.
    """

    data = {
        'token':        slack.api_token,
        'channel':      channel,
        'ts':           timestamp,
        'text':         text
    }

    for key, value in kwargs.items():
        data[key] = FIELD_ENCODERS.get(key, default_encoder)(value)

    return slack.http_client.post('chat.update', data)
