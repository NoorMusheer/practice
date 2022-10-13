# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# Given a roman numeral, convert it to an integer .

def romanToInt(s):
    sum = 0
    new_list = []
    conversion = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    for c in s:
        new_list.append(conversion[c])
    print (new_list)
    print("length : ", len(new_list))
    d=0
    while d<len(new_list):
        if d == (len(new_list)-1):
            print ("d = :", d, ";   adding :", new_list[d])
            sum += new_list[d]
            print ("done")
            return sum
        elif new_list[d+1]> new_list[d]:
            print ("d = :", d, ";   adding :", (new_list[d+1] - new_list[d]))
            sum += (new_list[d+1] - new_list[d])
            d+=2
        else:
            print ("d = :", d, ";   adding :", new_list[d])
            sum+=new_list[d]
            d+=1
    return sum
                
print(romanToInt('MDXLVI')) 
