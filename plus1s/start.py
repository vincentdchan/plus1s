from PIL import Image
from xtermcolor import colorize
from os import listdir
from os.path import isfile, join, dirname
import random

IMAGE_PATH = join(dirname(__file__), 'resources/images')
SENTENCES_PATH = join(dirname(__file__), 'resources/sentences.txt')


def tuple_to_color_hex(tup):
    return (tup[0] << 16) + (tup[1] << 8) + tup[2]


def inverse(rgb):
    return (255 - rgb[0], 255 - rgb[1], 255 - rgb[2])


def pick_filename(path):
    return random.choice([join(path, f) for f in listdir(path) if isfile(join(path, f))])


def pick_sentence():
    sentences = []
    with open(SENTENCES_PATH, 'r') as f:
        lines = f.readlines()
        sentences = [line.strip() for line in lines if len(line) != 0]
    return random.choice(sentences) + '...'


def start():
    im = Image.open(pick_filename(IMAGE_PATH))
    im = im.convert('RGB')
    px = im.load()
    width, height = im.size
    for h in range(height):
        for w in range(width):
            print(colorize('  ', rgb=tuple_to_color_hex(inverse(px[w, h])), 
                bg=tuple_to_color_hex(px[w, h])), end='')
        print()

    print(pick_sentence())
