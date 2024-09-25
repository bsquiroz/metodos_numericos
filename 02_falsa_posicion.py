def func(x):
  return -0.4*(x**2) + 2.3*(x) + 2.2

def main(a,b, err_pro, f):

  err = err_pro
  mi_prev = 0

  while(True):
    fa = f(a)
    fb = f(b)

    mi = b - (fb * (a - b)) / (fa - fb)
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

    print(f'punto medio: {mi}\npunto medio funcion: {fmi}\nerror: { round(abs(err*100), 2) if err != err_pro else None}%\n')

    if(abs(err) < err_pro): break

main(5, 8, 0.001, func)