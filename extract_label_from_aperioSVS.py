#!/usr/bin/env python3

from openslide import open_slide
import sys

image_param = sys.argv[1]

slide_in = open_slide(image_param)

slide_label = slide_in.associated_images["label"]
slide_label.save("output.png" ,"PNG")
