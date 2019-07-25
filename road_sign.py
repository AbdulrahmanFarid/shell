import argparse
from core import core

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--image', help = 'specify the path for the image')
parser.add_argument('-p', '--plot', help = 'specify if you want to see kernel move over image, support "rect", "stop", "None" [default None]')
parser.add_argument('-c', '--color', help = 'specify which color you want to seethe kernel or output image in, support "red", "green", "blue", [default red]')
parser.add_argument('-s', '--seconds', help = 'specify the time to display windows, [defualt .5 second]', type = float)

args = parser.parse_args()
core(args.image, args.plot, args.color, args.seconds)
