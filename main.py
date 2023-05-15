from aiohttp import web


router = web.RouteTableDef()

async def setup_app():
    app = web.Application()
    app.add_routes(router)
    return app

web.run_app(setup_app())
