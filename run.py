#! /usr/bin/env python
import asyncio

import tornado
from tornado.platform.asyncio import AsyncIOMainLoop

from tetris.routes import handlers
from tetris.settings import settings


if __name__ == '__main__':
    AsyncIOMainLoop().install()
    tornado.web.Application(handlers, debug=True, **settings).listen(8080)
    print('Ready!')
    asyncio.get_event_loop().run_forever()
