#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Defines the recommend view
"""

from NCAABB import app
import os

if __name__ == '__main__':
    #app.secret_key = 'whiskeystuff'
    app.debug = True
    #app.run(host='localhost', port=5000, debug=True)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
