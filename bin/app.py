import web
import json

urls = (
'/', 'Index',
'/Step', 'Step'
)
app = web.application(urls, globals())
render = web.template.render('templates/')

# little hack so that debug mode works with sessions
if web.config.get('_session') is None:
	store = web.session.DiskStore('sessions')
	session = web.session.Session(app, store,initializer={'room': None})
	web.config._session = session
else:
	session = web.config._session

class Index(object):
	def GET(self):
		greeting = "Hello World"
		return render.index()

class Step(object):
	def GET(self):
		# i = web.input();
		# print i.x," ",i.y;
		# print web.cookies().get("webpy_session_id");
		pyDict = {'x':1,'y':2}
		web.header('Content-Type', 'application/json')
		return json.dumps(pyDict)
		
if __name__ == "__main__":
	app.run()
