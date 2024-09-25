
def fdx(x):
  return x**3 - 2*(x) - 2

def fdx_prima(x):
  return 3*(x**2) - 2

def main(x_i, err_pro, fx, fdp):

  while True:
    x_current = x_i - (fx(x_i) / fdp(x_i))
    err = (x_current - x_i) / x_current

    print(f'x_anterior: {x_i}\nx_actual: {x_current}\nfdx: {fx(x_current)}\nerror: {round(abs(err*100), 3)}%\n')

    x_i = x_current
    if abs(err) < err_pro : break

main(1.9, 0.001, fdx, fdx_prima)