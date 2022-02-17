(* ::Package:: *)

p := Random[];
r = RotateLeft;
Graphics3D[Table[{RGBColor[.2, p, .2],
Cuboid[l =r[{z, p, p}, a], l +r[p/8 {Sign[z - .5], p, p}, a]]}, {z, {0, 1}}, {a, 0, 2}, {6!}]]
