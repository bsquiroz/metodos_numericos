def func(x):
  return (x**4) - 7*(x**2) + 14*(x) - 6

def main(a,b, err_pro, f):

  err = err_pro
  mi_prev = 0

  while(True):
    fa = f(a)
    fb = f(b)

    mi = (a + b) / 2
    fmi = f(mi)

    if mi_prev:
      err = (mi - mi_prev) / mi
      mi_prev = mi
    else:
      mi_prev = mi
      

    if fa * fmi < 0:
      b = mi
    else:
      a = mi

    print(f'punto medio: {mi}\npunto medio funcion: {fmi}\nerror: {round(abs(err*100), 2)}%\n')

    if(abs(err) < err_pro): break

main(0.4, 0.9, 0.001, func)