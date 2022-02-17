(* ::Package:: *)

pins = {7,8,25,23,24,18,15,4}
DeviceWrite["GPIO", First[pins] -> 1 ]
Do[
Do[
DeviceWrite["GPIO", pins[[i]]->1 ];
Pause[.5];
DeviceWrite["GPIO", pins[[i]]->0 ];
,{i,8}]
,{10}]
