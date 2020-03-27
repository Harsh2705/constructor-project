class employee:
	def __init__(self,name,basicpay,hra):#make a constructor
		self.name=name#self is a keyword
		self.basicpay=basicpay
		self.hra=hra

obj=employee("harsh","1000","2000")#make a object obj
print("employee name:", obj.name)
print( " basic pay:",obj.basicpay)
print("hra is :",obj.hra)