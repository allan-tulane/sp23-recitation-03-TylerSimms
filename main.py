"""
CMPS 2200  Recitation 3.
See recitation-03.pdf for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.

def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x,y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    if len(x) < len(y):
        x = ['0'] * (len(y)-len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x)-len(y)) + y
    # pad with leading 0 if not even number of bits
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x,y

def _quadratic_multiply(x, y):
  xvec = x.binary_vec
  yvec = y.binary_vec
  xvec, yvec = pad(xvec, yvec)

  n = max(len(xvec), len(yvec))

  if x.decimal_val <= 1 and y.decimal_val <= 1:
    number = BinaryNumber(x.decimal_val * y.decimal_val)
    return number
  else:
    x_left, x_right = split_number(xvec)
    y_left, y_right = split_number(yvec)

  mult1 = _quadratic_multiply(x_left, y_left)
  mult2 = _quadratic_multiply(x_left, y_right)
  mult3 = _quadratic_multiply(x_right, y_left)
  mult4 = _quadratic_multiply(x_right, y_right)

  shift1 = bit_shift(mult1, n)
  add = mult2.decimal_val + mult3.decimal_val
  sum = BinaryNumber(add)
  shift2 = bit_shift(sum, n//2)

  answer = shift1.decimal_val + shift2.decimal_val + mult4.decimal_val
  product = BinaryNumber(answer)
  
  return product
  
  

def quadratic_multiply(x, y):
  return _quadratic_multiply(x, y).decimal_val



## Feel free to add your own tests here.
def test_multiply():
  assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2*2
  assert quadratic_multiply(BinaryNumber(4), BinaryNumber(4)) == 4*4
  assert quadratic_multiply(BinaryNumber(8), BinaryNumber(8)) == 8*8
  assert quadratic_multiply(BinaryNumber(3), BinaryNumber(7)) == 3*7
  assert quadratic_multiply(BinaryNumber(5), BinaryNumber(7)) == 5*7
  assert quadratic_multiply(BinaryNumber(4), BinaryNumber(9)) == 4*9
  assert quadratic_multiply(BinaryNumber(6), BinaryNumber(4)) == 6*4
  assert quadratic_multiply(BinaryNumber(24), BinaryNumber(82)) == 24*82
  
    
    
def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start)*1000
  
