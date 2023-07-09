from numpy import exp, pi, linspace
import matplotlib.pyplot as plt

θ = linspace(0, 2*pi, 200)

def circle(radius, center):
    return center + radius*exp(1j*θ)

def plot_curves(curves):
    for c in curves:
        plt.plot(c.real, c.imag)
    plt.axes().set_aspect(1)
    plt.show()
    plt.close()

def mobius(z, a, b, c, d):
    return (a*z + b)/(c*z + d)

def m(curve):
    return mobius(curve, 1, 2, 3, 4)

circles = [circle(1, 0), circle(2, 0), circle(2, 2)]
plot_curves(circles)
plot_curves([m(c) for c in circles])

line = linspace(-100, 100, 600)
curves = [line, 1j*line - 4/3]
plot_curves(curves)
plot_curves([m(c) for c in curves])

lines = [1j*line - 4, 1j*line + 4, line - 4j, line + 4j]
plot_curves(lines)
plot_curves([m(c) for c in lines])