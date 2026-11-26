"""Render the six-close-comparison example with a rotating 3D camera."""

import argparse
from itertools import combinations, product
from math import cos, sin, tau
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


BG = "#101c30"
TEXT = "#f5f7fb"
MUTED = "#cbd7ec"
TEAL = "#8be8df"
AMBER = "#ffd38f"
VERTICES = list(product((-1, 1), repeat=3))
EDGES = [(a, b) for a, b in combinations(VERTICES, 2)
         if sum(x != y for x, y in zip(a, b)) == 1]
NORMALS = [tuple(sign if index == axis else 0 for index in range(3))
           for axis in range(3) for sign in (-1, 1)]


def project(point, yaw):
    x, y, z = point
    turned_x = x*cos(yaw) + z*sin(yaw)
    turned_z = z*cos(yaw) - x*sin(yaw)
    pitch = .43 + .12*sin(yaw)
    turned_y = y*cos(pitch) - turned_z*sin(pitch)
    depth = y*sin(pitch) + turned_z*cos(pitch)
    scale = 447/(5.2-depth)
    return 228+turned_x*scale, 263-turned_y*scale, depth


def frame(angle, fonts):
    title, label, result, body = fonts
    image = Image.new("RGB", (880, 580), BG)
    draw = ImageDraw.Draw(image)
    draw.text((26, 23), "Nearby comparisons localize the mean", font=title, fill=TEXT)
    draw.line((28, 81, 852, 81), fill="#3b5274", width=2)

    segments = []
    for a, b in EDGES:
        p, q = project(a, angle), project(b, angle)
        depth = (p[2]+q[2])/2
        segments.append((depth, p, q, False))
    for axis in NORMALS:
        p = project(axis, angle)
        q = project(tuple(1.34*x for x in axis), angle)
        segments.append(((p[2]+q[2])/2, p, q, True))
    for depth, p, q, normal in sorted(segments):
        color = "#77a2bc" if normal else TEAL
        if depth < 0:
            color = "#3a5b76" if normal else "#476f7e"
        draw.line((*p[:2], *q[:2]), fill=color, width=3 if depth>=0 else 2)
        if normal:
            x, y = q[:2]
            draw.ellipse((x-4,y-4,x+4,y+4), fill=color)
    draw.ellipse((218,253,238,273), fill=AMBER, outline=BG, width=3)

    draw.rounded_rectangle((454, 108, 854, 443), radius=16, fill="#1b2d48")
    draw.text((475, 127), "Six nearby cuts", font=label, fill=TEXT)
    draw.text((475, 180), "Each axis: ±1/16", font=body, fill=MUTED)
    draw.line((475, 240, 831, 240), fill="#3b5274", width=2)
    draw.text((475, 264), "Farthest feasible", font=body, fill=MUTED)
    draw.text((475, 319), "√3/16", font=result, fill=TEAL)
    draw.text((658, 332), "< 1/2", font=label, fill=TEXT)
    draw.ellipse((30,487,46,503), fill=AMBER)
    draw.text((62,474), "True mean at the center", font=body, fill=MUTED)
    draw.ellipse((30,536,46,552), fill=TEAL)
    draw.text((62,523), "Six comparisons bound the feasible cube", font=body, fill=MUTED)
    return image


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--regular-font", default="DejaVuSans.ttf")
    parser.add_argument("--bold-font", default="DejaVuSans-Bold.ttf")
    parser.add_argument("--output", type=Path, default=Path("visualization/nearby-comparisons.gif"))
    args = parser.parse_args()
    fonts = tuple(ImageFont.truetype(font,size) for font,size in (
        (args.bold_font,42),(args.bold_font,34),(args.bold_font,56),(args.regular_font,31)
    ))
    frames = [frame(.58+tau*i/64, fonts).quantize(colors=120,method=2) for i in range(64)]
    frames[0].save(args.output,save_all=True,append_images=frames[1:],
                   duration=92,loop=0,disposal=2,optimize=True)


if __name__ == "__main__":
    main()
