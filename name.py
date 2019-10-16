#!/usr/bin/env python3
import io
import re
from random import randint

dictionary = io.open("/usr/share/dict/words", "r").readlines()

g_part = re.compile(r"^gr[aeiouy][a-z]{1,3}$")
h_part = re.compile(r"^h[aeiouy][a-z]{2,4}$")

g_words = [word for word in dictionary if re.match(g_part, word)]
h_words = [word for word in dictionary if re.match(h_part, word)]

rand_word = lambda arr: arr[randint(0, len(arr)-1)].strip()

name = "{g}{h}".format(g=rand_word(g_words), h=rand_word(h_words)).title()

print(name)
