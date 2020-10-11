from random import randint  
import time
start = input("Wanna generate a CPF? Type yes[y]:  ")
c = int(input("How many CPFS do you want to generate?"))
count = 0
storage = []
while count < c + 1:
    if start.lower() == "Yes" or start.lower() == "y":
        reverse = 10
        total = 0
        cpf = ''.join([str(randint(0, 9)) for x in range(9)])
        new_cpf = cpf
        for i in range(19):
            if i > 8:
                i -= 9

            total += int(new_cpf[i]) * reverse

            reverse -= 1
            if reverse < 2:
                reverse = 11
                d = 11 - (total % 11)

                if d > 9:
                    d = 0
                total = 0
                new_cpf += str(d)
    storage.append(new_cpf)
    count += 1
             
        
def random(n):
    for cpfs in n:
        yield cpfs
        time.sleep(0.1)
        
        
s = random(storage)
for c in s:
    print(c)

"""
Copyright (c) 2020 Mateus Burlamaqui

 Permission is hereby granted, free of charge, to any person obtaining a copy
 of this software and associated documentation files (the "Software"), to deal
 in the Software without restriction, including without limitation the rights
 to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in
 all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 THE SOFTWARE.
"""
