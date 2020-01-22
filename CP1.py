'''
CP1 - Polynomial
'''

class Polynomial(object):
    def __init__(self, n):
       self.list = n
    
    def PolyToList(self, input_list):
        #print("polytolist input" + str(input_list))
        # function to process polynomials into list form
        input_list = (str(input_list)).split(" ")
        for i in range(0, len(input_list)-1):
            if input_list[i] == '-':
                input_list[i+1] = '-' + input_list[i+1]
                input_list.pop(i)
        input_list = [s for s in input_list if any(char.isdigit() for char in s)]
        for i in range(0, len(input_list)-1):
            if "x" not in input_list[i]:
                input_list[i] = input_list[i] + "x^0"
        for i in range(0, len(input_list)-1):
            if "x^" not in input_list[i]:
                input_list[i] = input_list[i] + "^1"
        
        # pass through until contains 0-terms for all coefficient structures
        check_pass = False
        while check_pass != True:
            check_pass = False
            
            for i in range(0, int((input_list[-1])[-1])+1):
                #print(i)
                #print((input_list[i])[-1])
                if (input_list[i])[-1] != str(i):
                    input_list.insert(i, ("0x^"+str(i)))
                    check_pass = True
            if check_pass == False:
                break
        
        for i in range(0, len(input_list)):
            if (input_list[i])[:-3] == "-":
                input_list[i] = float("-1")
            else:
                input_list[i] = float((input_list[i])[:-3])
        return input_list
     
    def AddPoly(self, a, b):
        # method to convert 2 polys into list form, accounting for different lengths
        # and then add them before using printPoly method to output it
        list_a = self.PolyToList(a)
        list_b = self.PolyToList(b)
        if len(list_a) > len(list_b):
            while len(list_b) != len(list_a):
                list_b.append(0.0)
        else:
            while len(list_a) != len(list_b):
                list_a.append(0.0)
        #print([x + y for x, y in zip(list_a, list_b)])
        p = Polynomial([x + y for x, y in zip(list_a, list_b)])
        return p.printPoly()
        
    def DerivePoly(self, a):
        # method to calculate the derivative of a polynomial and return the result as a new
        # polynomial
        #print(a)
        list_a = self.PolyToList(a)
        #print(list_a)
        list_a.pop(0)
        for i in range(0, len(list_a)):
            list_a[i] = (i+1) * list_a[i]
        p = Polynomial(list_a)
        print("poly")
        return p.printPoly()
        
    def IntegratePoly(self, a):
        # method to calculate the indefinite integral of a polynomial and return the result as a
        # new polynomial
        c = 2 # integration constant
        list_a = self.PolyToList(str(a))
        for i in range(0, len(list_a)):
            list_a[i] = list_a[i] / (i+1)
        list_a.insert(0, c)
        p = Polynomial(list_a)
        return p.printPoly()
        
    def printPoly(self):
        # print the list by concatenating in the proper format
        s = "P(x) = "
        for i in range(0, len(self.list)):
            if self.list[i] != 0:
                if i == 0:
                    s += str(self.list[i]) + " + "
                elif i == 1:
                    s += str(self.list[i]) + "x + "
                elif i == (len(self.list) - 1):
                    s += str(self.list[i]) + "x^" + str(i)
                elif str(self.list[i])[0] == "-":
                    s = s[:-3] + " - " + (str(self.list[i]))[1:] + "x^" + str(i) + " + "
                else:
                    s += str(self.list[i]) + "x^" + str(i) + " + "
        # remove weird irregularities
        # "1x", "+ -",
        s = ((s.replace("1.0x", "x")).replace("1x", "x")).replace("+ -", "- ")
        return s
        
'''
Code to test Polynomial class
'''

def main():
    g = Polynomial([-1,-3,0,4.5])
    #g.printPoly()
    g.AddPoly("P(x) = 2 + 4x^2 - x^3 + 6x^5", "P(x) = -1 - 3x + 4.5x^3")
    #g.DerivePoly("P(x) = -1 - 3x + 4.5x^3")
    #g.IntegratePoly("P(x) = -1 - 3x + 4.5x^3") 
    # P(x) = -1 - 3x + 4.5x^3 , [-1,-3,0,4.5]
    # P(x) = 2 + 4x^2 - x^3 + 6x^5 , [2,0,4,-1,0,6]

#main()