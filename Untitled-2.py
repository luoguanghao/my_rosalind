
class child:

	def __init__(self):
		self.AA = 0
		self.Aa = 0
		self.aa = 0

		self.BB = 0
		self.Bb = 0
		self.bb = 0

tmp = child             

#print(tmp.AA)


import itertools
def f(k,n):
    p = []
    child_num = 2**k
    for i in range(n):
        p.append(len(list(itertools.combinations([x for x in range(child_num)],i)))*(0.25**i)*(0.75**(child_num-i)))
        # combinations('ABCD', 2)       AB AC AD BC BD CD
    return 1-sum(p)

print(f(2,1))
print(f(6,17))