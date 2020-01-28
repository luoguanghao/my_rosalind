'''
Given: Two positive integers k (k≤7) and N (N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. Tom has two children in the 1st generation, each of whom has two children, and so on. Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.
-------------
Sample Dataset
2 1
-------------
Sample Output
0.684
'''
import sys, os


class child:

    def __init__(self):
        self.AA = 0
        self.Aa = 0
        self.aa = 0

        self.BB = 0
        self.Bb = 0
        self.bb = 0

        self.generation = 0

#def calPr(pr1, pr2, pr3):

def cb(n,i):

	result = 1

	for j in range(1, i+1):

		result = result * (n-i+j) // j

	return result

print(cb(28,2))

def calculate(type, preChild):
    AA_AA = 0.5
    AA_Aa = 0.25
    AA_aa = 0

    Aa_AA = 0.5
    Aa_Aa = 0.5
    Aa_aa = 0.5

    aa_AA = 0
    aa_Aa = 0.25
    aa_aa = 0.5


    if type is 'AA':
        pr1 = preChild.AA
        pr2 = preChild.Aa
        pr3 = preChild.aa
        ans = None
        ans = AA_AA * pr1 + AA_Aa * pr2 + AA_aa * pr3
        return ans
        #return calPr(preChild.AA, preChild.Aa, preChild.aa)
    elif type is 'Aa':
        pr1 = preChild.AA
        pr2 = preChild.Aa
        pr3 = preChild.aa
        ans = None
        ans = Aa_AA * pr1 + Aa_Aa * pr2 + Aa_aa * pr3
        return ans
    elif type is 'aa':
        pr1 = preChild.AA
        pr2 = preChild.Aa
        pr3 = preChild.aa
        ans = None
        ans = aa_AA * pr1 + aa_Aa * pr2 + aa_aa * pr3
        return ans
    ##########    
    elif type is 'BB':
        pr1 = preChild.BB
        pr2 = preChild.Bb
        pr3 = preChild.bb
        ans = None
        ans = AA_AA * pr1 + AA_Aa * pr2 + AA_aa * pr3
        return ans
    elif type is 'Bb':
        pr1 = preChild.BB
        pr2 = preChild.Bb
        pr3 = preChild.bb
        ans = None
        ans = Aa_AA * pr1 + Aa_Aa * pr2 + Aa_aa * pr3
        return ans
    elif type is 'bb':    
        pr1 = preChild.BB
        pr2 = preChild.Bb
        pr3 = preChild.bb
        ans = None
        ans = aa_AA * pr1 + aa_Aa * pr2 + aa_aa * pr3
        return ans


def do(k,N):
    num = 1
    preChild = child()
    preChild.Aa = 1
    preChild.Bb = 1

    nextChild = child()


    for i in range(1,k+1):

        if i != 1:
            preChild = nextChild

        num = 2**k

        nextChild.AA = calculate('AA',preChild)
        nextChild.Aa = calculate('Aa',preChild)
        nextChild.aa = calculate('aa',preChild)

        nextChild.BB = calculate('BB',preChild)
        nextChild.Bb = calculate('Bb',preChild)
        nextChild.bb = calculate('bb',preChild)

    AaBb = nextChild.Aa*nextChild.Bb
    print("the probility of AaBb of one is %f"%(nextChild.Aa*nextChild.Bb))
    num = 2**k
    ans = 0
    for i in range(N):
        ans += cb(num,i)*(AaBb**i)*((1-AaBb)**(num-i))
    
    print('ans =',1-ans)


if __name__ == "__main__":

    k = int(sys.argv[1])
    N = int(sys.argv[2])

    do(k, N)



