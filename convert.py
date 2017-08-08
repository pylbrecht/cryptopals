#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Conversions
"""

import base64


def hex_to_base64(hexstring):
    return base64.b64encode(bytes.fromhex(hexstring)).decode()
