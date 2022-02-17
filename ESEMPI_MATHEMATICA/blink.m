(* ::Package:: *)

Do[ (*avvio del loop*)
DeviceWrite["GPIO", 8->1] (*attiva la porta GPIO 8*)
Print ["LED Acceso"]
Pause [1] (*pausa di un secondo*)
DeviceWrite["GPIO", 8->0] (*disattiva la porta GPIO 8*)
Print ["LED Spento"]
Pause [1], (*pausa di un secondo *)
{50}] (*fine del loop di 50 cicli*)



