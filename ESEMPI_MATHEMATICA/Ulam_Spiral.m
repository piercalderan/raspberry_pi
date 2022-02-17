(* ::Package:: *)

s = {Re@#, Im@#} & /@ Fold[Join[#1, Last@#1 + I^#2 Range@#2/2] &, {0},
Range@140]; ListPlot[s, Joined -> True,
Epilog -> {Point /@ s[[Prime@Range@PrimePi@Length@s]]}]
