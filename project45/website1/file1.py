class MyClass(object):
	def __init__(self,get_response):
		self.get_response=get_response

	def __call__(self,request):
		print('this line added at pre-processing of request')
		response=self.get_response(request)
		print('this line added post proccessing of request ')
		return response
