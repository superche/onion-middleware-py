"""OnionMiddleware"""

__all__ = ['setContext', 'getContext', 'register', 'delete', 'deleteAll', 'getMiddlewares', 'run']

middlewares = []
ctx = {}

def setContext(p_ctx):
    global ctx
    ctx = p_ctx

def getContext():
    return ctx

def register(mw):
    if (mw in middlewares):
        return
    middlewares.append(mw)

def delete(mw):
    if (mw in middlewares):
        middlewares.remove(mw)

def getMiddlewares():
    return middlewares

def deleteAll():
    global middlewares
    middlewares = []

def run():
    def dispatch(index):
        if (index >= len(middlewares)):
            return
        fnc = middlewares[index]
        return fnc(ctx, lambda: dispatch(index + 1))
    
    return dispatch(0)
