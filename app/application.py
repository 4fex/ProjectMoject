#coding: utf-8

import cherrypy

#--------------------------------------
class Application_cl(object):
#--------------------------------------
	#----------------------------------
	def __init__(self):
	#--------------------------------------
		# constructor
		pass

	def studiengaenge(self):
		markup_s="blablaaaaaa"
		
		return markup_s

	studiengaenge.exposed=True
	#--------------------------------------
	def default(self, *arglist, **kwargs):
	#--------------------------------------
		msg_s = "unbekannte Anforderung: " + \
			str(arglist) + \
			''+\
			str(kwargs)
		raise cherrypy.HTTPError(404, msg_s)

	default.exposed = True
# EOF
