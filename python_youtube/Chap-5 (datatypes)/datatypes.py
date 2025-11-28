# data types in python
a = 1
b = 1
print(a+b)
print(type(a)) # checking data type: integer

c = "1"
d = "1"
print(c+d)
print(type(c)) # checking data type: string

# basic data types in python:
# 1. Numeric
a1 = 1                    #1a1. integer        
a2 = 1.5                  #1a2. float
print(type(a2))
a3 = complex(3, 5)        #1a3. complex
print(type(a3))

# 2. Sequence
b1 = "Madhavi"                          #2b1. string
b11 = "28" 
print(type(b1))
print(type(b11))
b2 = [1, 4, 7, 26, 108, 'Madhavi']      #2b2. list
print(type(b2))
b3 = (1, 4, 7, 26, 108, 'Madhavi')      #2b3. tuple   
print(type(b3))

# 3. Dictionary
my_dictionary = {'name' : 'pradnya', 'age' : 28, 'city' : 'mumbai'}
print(type(my_dictionary))

# 4. Sets
my_sets = {1, 4, 7, 26, 108, 'Madhavi'}
print(type(my_sets))

# 5. Boolean
bool1 = True
bool2 = False
print(type(bool1))
print(type(bool2))

# 6. Binary
# bytes, bytearray, memoryview
byte1 = b"Madhavi"
print(type(byte1))