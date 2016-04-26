from core.service import CoreService

class SandnetService(CoreService):
	''' Base class for all Sandnet services
	'''
	_name = "SandnetProcess"
	_group = "Sandnet"
	_configs = ()
	_startindex = 50
	_startup = ()

	@classmethod
	def generateconfig(cls, node, filename, services):
		return ""
