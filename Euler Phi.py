
def prime_factors(num):
  cur_num = int(num)
  cur_div = 2
  prime_factors = []

  while cur_num > 1:
    remainder = cur_num % cur_div
    if remainder == 0:
      prime_factors.append(cur_div)
      cur_num = cur_num // cur_div
    else:
      cur_div += 1

  return prime_factors

def euler(num):
  euler_num = int(num)
  euler_factors = prime_factors(euler_num)
  euler_result = 0

  for i in range(euler_num - 1):
    list_a = prime_factors(i)
    rel_prime = True
    for j in list_a:
      if j in euler_factors:
        rel_prime = False
        break
    if rel_prime == True:
      euler_result += 1

  return euler_result
      

def main():

  a = euler(1000)
  print(a)
  b = euler(15)
  print(b)
  c = euler(27343)
  print(c)

main()
      
    
