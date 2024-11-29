class py_solution:
    def intoroman(self,num):
        val=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        syb=["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        romannum=" "
        i=0
        while num>0:
            for j in range(num//val[i]):
                romannum+=syb[i]
                num-=val[i]
            i+=1
        return romannum
print(py_solution().intoroman(1))
print(py_solution().intoroman(35))