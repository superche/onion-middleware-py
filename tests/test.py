import unittest
from ..onion_middleware_py import OnionMiddleware

class BasicTestsSuite(unittest.TestCase):
    def test_setContext(self):
        OnionMiddleware.setContext({'a':1})
        self.assertEquals( OnionMiddleware.getContext(), {'a':1} )

    def test_register(self):
        fnc = lambda: 1
        OnionMiddleware.register(fnc)
        self.assertEquals( OnionMiddleware.getMiddlewares(), [fnc] )

    def test_delete(self):
        fnc = lambda: 2
        OnionMiddleware.register(fnc)
        OnionMiddleware.delete(fnc)
        self.assertFalse( fnc in OnionMiddleware.getMiddlewares() )

    def test_deleteAll(self):
        OnionMiddleware.deleteAll()
        self.assertEquals( OnionMiddleware.getMiddlewares(), [] )

    def test_run(self):
        def tempMw(ctx, nextFnc):
            return 1
        OnionMiddleware.deleteAll()
        OnionMiddleware.register(tempMw)
        self.assertEquals( OnionMiddleware.run(), 1 )

if __name__ == '__main__':
    unittest.main()