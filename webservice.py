import cherrypy
from signup import SignUp
from signin import SignIn

class Root(object):
    pass

root = Root()
root.signup = SignUp()
root.signin = SignIn()

conf = {    
    'global': {
        'server.socket_port': 3000,
    },
    '/': {
        'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
    },
}
cherrypy.quickstart(root, '/', conf)

# signup request example:
# curl -H "Content-Type: application/json" -X POST -d '{"username":"xyz","password":"xyz"}' http://localhost:3001/signup
# {returns 'success'}
#
# signin request example:
# curl -H "Content-Type: application/json" -X POST -d '{"username":"xyz","password":"xyz"}' http://localhost:3001/signin
# {returns 'success'}

