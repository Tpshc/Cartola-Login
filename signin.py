import cherrypy
import login 

@cherrypy.expose
class SignIn(object):
    
    @cherrypy.tools.json_in()
    @cherrypy.tools.json_out()
    @cherrypy.tools.accept(media='application/json')
    def POST(self):
        json = cherrypy.request.json
        username =  json['username']
        password =  json['password']
        if username and password :
            if login.signin(username, password):
                return 'success'
            else:
                raise cherrypy.HTTPError(401, 'Invalid Username or Password.')
        else:
            raise cherrypy.HTTPError(401, 'Missing data.')  