import os
import sys
from PIL import Image

palettes = {}


def load_palettes(fpath="palettes.txt"):
    '''Load predefined palettes into global dictionary'''
    with open(fpath) as f:
        for line in f:
            split_line = line.strip().split()
            palettes[split_line[0]] = split_line[1:]
    f.close()


def save_single_color(hex, height, width, folder=None, fname=None):
    '''Save color to a PNG file of (height x width)'''
    if not hex.startswith('#'):
        hex = '#' + hex
    im = Image.new("RGB", (height, width), hex)
    fname = fname if fname else hex
    folder = folder if folder else '.'
    path = f"{folder}/{fname}.png"
    im.save(path)


def save_color_batch(hex_list, height=1500, width=300, folder=None):
    '''Batch save color to PNG images'''
    if folder:
        if not os.path.exists(folder):
            os.makedirs(folder)
    for hex in hex_list:
        save_single_color(hex, height, width, folder)


def save_color_by_palette(palette_name):
    '''Save color in predefine palette to PNG images in folder'''
    if palette_name in palettes.keys():
        save_color_batch(palettes[palette_name], folder=palette_name)
    else:
        print("Palette not found")


def main():
    load_palettes()
    save_color_by_palette("wheat")


if __name__ == '__main__':
    main()
