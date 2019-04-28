import numpy as np
import matplotlib.pyplot as plt
from argparse import ArgumentParser


def z_value(scale, max_axis, axis):
    z = scale * (2*(axis/max_axis) - 1)
    return z


if __name__ == "__main__":
    parser = ArgumentParser(description="Generate a Julia set")
    parser.add_argument('--height', default=600, type=int)
    parser.add_argument('--width', default=800, type=int)
    parser.add_argument('--x_scale', default=1.5, type=float)
    parser.add_argument('--y_scale', default=1, type=float)
    parser.add_argument('--start_i', default=255, type=int)
    parser.add_argument('--x_coefficient', default=0.7, type=float)
    parser.add_argument('--y_coefficient', default=0.27015, type=float)
    args = parser.parse_args()

    height = args.height
    width = args.width
    x_scale = args.x_scale
    y_scale = args.y_scale
    start_i = args.start_i
    c_x = args.x_coefficient
    c_y = args.y_coefficient


    A = np.zeros([height, width])
    for x in range(width):
        for y in range(height):
            zx = z_value(x_scale, width, x)
            zy = z_value(y_scale, height, y)
            i = start_i
            t = True
            while t:
                if (zx**2)+(zy**2) >= 4 or i <= 1:
                    t = False
                zx_new = (zx**2)-(zy**2) + c_x
                zy = (2*zx*zy) + c_y
                zx = zx_new
                i -= 1
            A[y][x] = i


    plt.imshow(A)
    plt.savefig('Julia_image.png')
