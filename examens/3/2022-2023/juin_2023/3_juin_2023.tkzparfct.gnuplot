set table "3_juin_2023.tkzparfct.table"; set format "%.5f"
set samples 200.0; set parametric; plot [t=0:6.283185307179586476] [] [] (16*(sin(t))**3)/1,(13*cos(t)-5*cos(2*t)-2*cos(3*t)-cos(4*t))/1
