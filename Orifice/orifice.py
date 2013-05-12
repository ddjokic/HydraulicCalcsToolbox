#!/usr/bin/env python
import inout
import math
print ("Sharp edge orifice calculation - orifice coeficient (C)=0.62 is default")
C=inout.get_float("Enter orifice coeficient or 0 for default of 0.62: ", 0.61)
g=9.81  #m/s^2
print("1-Solving for Flow Through Orifice")
print("2-Solving for Orifice Diameter")
print("3-Solving for Headloss through Orifice")
problem = int(raw_input("Input 1, 2 or 3: "))
if problem ==1:
	print ("Solving for Flow")
	d=inout.get_float("Enter orifice hole diameter [mm] or 0 fo 10mm: ", 10)
	H=inout.get_float("Enter head loss in orifice [m] or 0 for 1.5m: ", 1.5)
	dm=float(d/1000)
	A=dm*dm*math.pi/4
	Qs=float(C*A*(2*g*H)**0.5)
	Q=round(float(Qs*3600),3)
	print ("Q=%r cum/h") %Q
	print ("End of execution")
elif problem==2:
	print ("Solving for diameter")
	Qh=inout.get_float("Enter Flow [cum/h] or 0 for 120 cum/h: ", 120)
	Qs=float(Qh/3600)  #in cum/s
	H=inout.get_float("Enter head loss in orifice [m] or 0 for 1.5m: ", 1.5)
	Am=float(Qs/(C*(2*g*H)**0.5))
	Amm=round(Am*(1000**2),3)
	d=round((4*Amm/math.pi)**0.5,3)
	print ("Oriffice hole area = %r mm**2") %Amm
	print ("Oriffice hole dia =%r mm") %d
	print ("End of execution")
elif problem==3:
	print ("Solving for Headloss")
	Qh=inout.get_float("Enter Flow [cum/h] or 0 for 120 cum/h: ", 120)
	d=inout.get_float("Enter orifice hole diameter [mm] or 0 fo 10mm: ", 10)
	dm=float(d/1000)
	A=dm*dm*math.pi/4
	Qs=float(Qh/3600)  #in cum/s
	H=round((Qs/(C*A))**2/(2*g),3)
	print ("Headloss = %r m") %H
	print ("End of execution")
else:
	print ("Something went wrong! Try again. Exit now!")
	print ("END")
