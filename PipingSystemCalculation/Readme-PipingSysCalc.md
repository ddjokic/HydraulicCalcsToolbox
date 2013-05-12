***Piping System Calculation***</p>
Use template file, "pytemplate.py" to create your own program for problem solution, by calling functions located in "hydrobb.py".  
For input use "input.xlsx" file, "Template" worksheet - export it in "csv" file. Results will be written in "input_file-res.csv".</p>
  
<p>List of functions in "hydrobb.py":    

    curve_intersection(APump, BPump, APipe, BPipe)  
    calculates intersection between two curves - work point of piping system  
        
    decomp_parallel(FlowQ, APRes, BPRes, AP1, BP1, AP2, BP2)  
    
    calculates Flow and Headloss in individual pipes in parallel connection   
    
    decomp_serial(Flow, AS1, BS1, AS2, BS2)  
    calculates Flow and Headloss in individual pipes in serial connection  
        
    eq_pump(APump, BPump, ASuction, BSuction)  
    calculates equivalent pump headloss - difference between pump and suction line 	headloss  
        
    flow(H, A, B)  
    calculates Flow for given Headloss  
        
	par_flow(Flow, A1, B1, A2, B2)  
	calculates Flow and Headloss through each pipeline in parallel loop for given 	total Flow which entering loop. USE THIS FUNCTION.
	    
    par_lines(A1, B1, A2, B2)  
    calculates result of parallel connected pipes  
        
    res_sub_loop(Flow, ARes, BRes, AP1, BP1, AP2, BP2, AS, BS)   
    calculates Flow and Headloss in component pipes of "fork" sub-loop 
    
    reynolds(flow, ARe)  
    calculates Reynolds number in individual pipe as function of flow  
        
    ser_lines(A1, B1, A2, B2)
    calculates result of pipes connected in series
        
    sub_loop(AP1, BP1, AP2, BP2, AS1, BS1)
    calculates resultant of two parallel and one serial pipes - "fork" sub-loop
    
    velocity(flow, Avel)  
    calculates fluid velocity in individual pipe as function of flow  
        
    write_res_head_csv(filename)  
    write headers to "csv"- file  
    
    write_res_num_csv(filename, PipeTag, Flow, Headloss, Reynolds, Velocity)  
    write results rounded on 3 decimals to "csv"-file   
        
    write_table5(fn, v1, v2, v3, v4, v5)  
    write table in previously opened csv file in "a" - mode  
      
<p> Symbols:  

	H=A*Q**2+B, headloss 
	Re=ARe*Q, Reynolds number
	Velo=AVel*Q, Velocity  
	S - serial
	P - parallel
	Res - Result
	
<p>Output of "pyHeadloss.py" can be used as input to piping system calculation.  

<u>Note:</u>
All functions are, so far, of "Beta" quality - no warranties whatsoever.   
See example file(s).
