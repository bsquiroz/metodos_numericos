# Tener en cuenta la diagonal estrictamente dominante
# ingresar las ecuaciones despejadas para x,y,z
def def_x(y,z):
  return 

def def_y(x,z):
  return

def def_z(x,y):
  return 

def gaus_seidel(ecu_x, ecu_y, ecu_z):
  x = 0
  y = 0
  z = 0

  count = 0

  def validationDig(num1, num2, val):
    return str(num1)[:val] == str(num2)[:val]
  
  while True:
    prev_x = x
    prev_y = y
    prev_z = z

    x = ecu_x(y, z)
    y = ecu_y(x, z)
    z = ecu_z(x, y)

    print(f"iteración: {count + 1}: \nx: {x}\ny: {y}\nz: {z}\n---------\n")

    if count > 0:
      pass_x = validationDig(prev_x, x, 10)
      pass_y = validationDig(prev_y, y, 10)
      pass_z = validationDig(prev_z, z, 10)
      
      if(pass_x and pass_y and pass_z): break

    count += 1

gaus_seidel(def_x, def_y, def_z)