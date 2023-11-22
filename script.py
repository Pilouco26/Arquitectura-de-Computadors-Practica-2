#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

# Define the simulation commands and paths in a more structured way using dictionaries.
simulators = {
    "applu": "../../exe/applu.exe < applu.in > applu.out 2> applu.err",
    "crafty": "../../exe/crafty.exe < crafty.in > crafty.out 2> crafty.err",
    "twolf": "../../exe/twolf.exe ref > ref.stdout 2> ref.err",
    "vortex": "../../exe/vortex.exe lendian1.raw > vortex1.out2 2> vortex1.err",
    "vpr": "/home/milax/Escriptori/Fase2/Benchmarks/vpr/exe/vpr.exe /home/milax/Escriptori/Fase2/Benchmarks/vpr/data/ref/net.in /home/milax/Escriptori/Fase2/Benchmarks/vpr/data/ref/arch.in /home/milax/Escriptori/Fase2/Benchmarks/vpr/data/ref/route.out -nodisp -route_only -route_chan_width 15 -pres_fac_mult 2 -acc_fac 1 -first_iter_pres_fac 4 -initial_pres_fac 8 > route_log.out 2> route_log.err"
}

paths = {
    "applu": "/home/milax/Escriptori/Fase2/Benchmarks/applu/data/ref",
    "crafty": "/home/milax/Escriptori/Fase2/Benchmarks/crafty/data/ref",
    "vpr": "/home/milax/Escriptori/Fase2/Benchmarks/vpr/data/ref",
    "twolf": "/home/milax/Escriptori/Fase2/Benchmarks/twolf/data/ref",
    "vortex": "/home/milax/Escriptori/Fase2/Benchmarks/vortex/data/ref"
}

mida = {
	"1 8 3 0", 
	"1 64 6 0",
	"1 128 7 0",
	"1 512 9 0",
	"1 2048 11 0"
}

branchpredictors = {
                    "gag":":2lev",
                    }
proc = "/home/milax/Escriptori/Fase2/simplescalar.txt"
configMida= "/home/milax/Escriptori/Fase2/configMida.txt"
resultado = open("resultado.txt", "w")
i=1
j=1
print(proc)
for bp in branchpredictors:
    print(bp)
    for sim in simulators:
        for mid in mida:
            print("Executing " + sim + "....")
            os.chdir(paths[sim])
            os.system("/home/milax/Escriptori/Fase2/simplesim-3.0_acx2/sim-outorder -bpred 2lev -bpred"+branchpredictors[bp]+" "+mid+" -redir:sim /home/milax/Escriptori/Fase2/output/"+bp+str(j)+"_"+str(i)+"-"+sim+".txt -config "+proc+" -fastfwd 100000000 -max:inst 100000000 "+ simulators[sim])
            i=i+1
            i = i % 6
        j=j+1
        

