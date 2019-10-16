#!/usr/bin/env python3
import io
import re
from random import randint

dictionary = io.open("/usr/share/dict/words", "r").readlines()

g_part = re.compile(r"^gr[aeiouy][a-z]{1,3}$")
h_part = re.compile(r"^h[aeiouy][a-z]{2,4}$")

g_words = [word for word in dictionary if re.match(g_part, word)]
h_words = [word for word in dictionary if re.match(h_part, word)]

rand = lambda arr: arr[randint(0, len(arr)-1)].strip()

print("{g}{h}".format(g=rand(g_words), h=rand(h_words)))
