#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
Run Flask App from here
"""

from ncaabb.app import app
import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
