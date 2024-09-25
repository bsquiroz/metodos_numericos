from math import e, sqrt,log

def fdx(x):
  return ((5/2)*e**x**2) - ((7/2)*x) - 3

def gdx(x):
  return sqrt(log((7*(x) + 6) / 5))

def main(x_i, err_pro, fdx, gdx):

  while True:
    x_current = gdx(x_i)
    err = (x_current - x_i) / x_current

    print(f'x_anterior: {x_i}\nx_actual: {x_current}\nfdx: {fdx(x_current)}\nerror: {round(abs(err*100), 2)}%\n')

    x_i = x_current
    if abs(err) < err_pro : break

main(0.8, 0.0001, fdx, gdx)