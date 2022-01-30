class sorte:
	def lissor(self):
		'''will revers the lis without revers'''
		emplis=[]
		ma=max(lis.deep)
		mi=min(lis.deep)-1
		for i in range(ma,mi,-1):
			if i in lis.deep:
				emplis.append(i)
		print(emplis)

if __name__=='__main__':
	lis=sorte()
	lis.deep=[3,79,56,9,12,69,677]
	lis.lissor()
	
	