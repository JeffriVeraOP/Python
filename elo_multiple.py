#Calculadora de variacion de elo multiple

your_elo = int(input("Ingrese aqui su elo: "))
your_k = int(input("Ingrese su k actual: "))
rival_elo = int(input("Ingrese el elo de su rival: "))
result = float(input("Ingrese el resultado 1 para victoria / 0.5 para empate / 0 para derrota: "))

diferencia = your_elo - rival_elo
pd = 0

if diferencia >= (-3) and diferencia<=3:
		pd=0.50
if diferencia>=4 and diferencia<=10:
		pd=0.51
if diferencia>=11 and diferencia<=17:
		pd=0.52
if diferencia>=18 and diferencia<=25:
		pd=0.53
if diferencia>=26 and diferencia<=32:
		pd=0.54
if diferencia>=33 and diferencia<=39:
		pd=0.55
if diferencia>=40 and diferencia<=46:
		pd=0.56
if diferencia>=47 and diferencia<=53:
		pd=0.57
if diferencia>=54 and diferencia<=61:
		pd=0.58
if diferencia>=62 and diferencia<=68:
		pd=0.59
if diferencia>=69 and diferencia<=76:
		pd=0.60
if diferencia>=77 and diferencia<=83:
		pd=0.61
if diferencia>=84 and diferencia<=91:
		pd=0.62
if diferencia>=92 and diferencia<=98:
		pd=0.63
if diferencia>=99 and diferencia<=106:
		pd=0.64
if diferencia>=107 and diferencia<=113:
		pd=0.65
if diferencia>=114 and diferencia<=121:
		pd=0.66
if diferencia>=122 and diferencia<=129:
		pd=0.67
if diferencia>=130 and diferencia<=137:
		pd=0.68
if diferencia>=138 and diferencia<=145:
		pd=0.69
if diferencia>=146 and diferencia<=153:
		pd=0.70
if diferencia>=154 and diferencia<=162:
		pd=0.71
if diferencia>=163 and diferencia<=170:
		pd=0.72
if diferencia>=171 and diferencia<=179:
		pd=0.73
if diferencia>=180 and diferencia<=188:
		pd=0.74
if diferencia>=189 and diferencia<=197:
		pd=0.75
if diferencia>=198 and diferencia<=206:
		pd=0.76
if diferencia>=207 and diferencia<=215:
		pd=0.77
if diferencia>=216 and diferencia<=225:
		pd=0.78
if diferencia>=226 and diferencia<=235:
		pd=0.79
if diferencia>=236 and diferencia<=245:
		pd=0.80
if diferencia>=246 and diferencia<=256:
		pd=0.81
if diferencia>=257 and diferencia<=267:
		pd=0.82
if diferencia>=268 and diferencia<=278:
		pd=0.83
if diferencia>=279 and diferencia<=290:
		pd=0.84
if diferencia>=291 and diferencia<=302:
		pd=0.85
if diferencia>=303 and diferencia<=315:
		pd=0.86
if diferencia>=316 and diferencia<=328:
		pd=0.87
if diferencia>=329 and diferencia<=344:
		pd=0.88
if diferencia>=345 and diferencia<=357:
		pd=0.89
if diferencia>=358 and diferencia<=374:
		pd=0.90
if diferencia>=375 and diferencia<=391:
		pd=0.91
if diferencia>=392:
		pd=0.92
if diferencia<=(-4) and diferencia>=(-10):
		pd=0.49
if diferencia<=(-11) and diferencia>=(-17):
		pd=0.48
if diferencia<=(-18) and diferencia>=(-25):
		pd=0.47
if diferencia<=(-26) and diferencia>=(-32):
		pd=0.46
if diferencia<=(-33) and diferencia>=(-39):
		pd=0.45
if diferencia<=(-40) and diferencia>=(-46):
		pd=0.44
if diferencia<=(-47) and diferencia>=(-53):
		pd=0.43
if diferencia<=(-54) and diferencia>=(-61):
		pd=0.42
if diferencia<=(-62) and diferencia>=(-68):
		pd=0.41
if diferencia<=(-69) and diferencia>=(-76):
		pd=0.40
if diferencia<=(-77) and diferencia>=(-83):
		pd=0.39
if diferencia<=(-84) and diferencia>=(-91):
		pd=0.38
if diferencia<=(-92) and diferencia>=(-98):
		pd=0.37
if diferencia<=(-99) and diferencia>=(-106):
		pd=0.36
if diferencia<=(-107) and diferencia>=(-113):
		pd=0.35
if diferencia<=(-114) and diferencia>=(-121):
		pd=0.34
if diferencia<=(-122) and diferencia>=(-129):
		pd=0.33
if diferencia<=(-130) and diferencia>=(-137):
		pd=0.32
if diferencia<=(-138) and diferencia>=(-145):
		pd=0.31
if diferencia<=(-146) and diferencia>=(-153):
		pd=0.30
if diferencia<=(-154) and diferencia>=(-162):
		pd=0.29
if diferencia<=(-163) and diferencia>=(-170):
		pd=0.28
if diferencia<=(-171) and diferencia>=(-179):
		pd=0.27
if diferencia<=(-180) and diferencia>=(-188):
		pd=0.26
if diferencia<=(-189) and diferencia>=(-197):
		pd=0.25
if diferencia<=(-198) and diferencia>=(-206):
		pd=0.24
if diferencia<=(-207) and diferencia>=(-215):
		pd=0.23
if diferencia<=(-216) and diferencia>=(-225):
		pd=0.22
if diferencia<=(-226) and diferencia>=(-235):
		pd=0.21
if diferencia<=(-236) and diferencia>=(-245):
		pd=0.20
if diferencia<=(-246) and diferencia>=(-256):
		pd=0.19
if diferencia<=(-257) and diferencia>=(-267):
		pd=0.18
if diferencia<=(-268) and diferencia>=(-278):
		pd=0.17
if diferencia<=(-279) and diferencia>=(-290):
		pd=0.16
if diferencia<=(-291) and diferencia>=(-302):
		pd=0.15
if diferencia<=(-303) and diferencia>=(-315):
		pd=0.14
if diferencia<=(-316) and diferencia>=(-328):
		pd=0.13
if diferencia<=(-329) and diferencia>=(-344):
		pd=0.12
if diferencia<=(-345) and diferencia>=(-357):
		pd=0.11
if diferencia<=(-358) and diferencia>=(-374):
		pd=0.10
if diferencia<=(-375) and diferencia>=(-391):
		pd=0.09
if diferencia<=(-392):
		pd=0.08

var_elo = (result - pd) * your_k
print("Su variación en esta partida será de: ", round(var_elo, 2))
new_elo = your_elo + round(var_elo, 2)

rival_elo = int(input("Ingrese el elo de su siguiente rival o coloque 0 si es que no tiene mas rivales para calcular: "))

while rival_elo != 0:
	result = float(input("Ingrese el resultado 1 para victoria / 0.5 para empate / 0 para derrota: "))
 
	diferencia = your_elo - rival_elo
	pd = 0

	if diferencia >= (-3) and diferencia<=3:
		pd=0.50
	if diferencia>=4 and diferencia<=10:
		pd=0.51
	if diferencia>=11 and diferencia<=17:
		pd=0.52
	if diferencia>=18 and diferencia<=25:
		pd=0.53
	if diferencia>=26 and diferencia<=32:
		pd=0.54
	if diferencia>=33 and diferencia<=39:
		pd=0.55
	if diferencia>=40 and diferencia<=46:
		pd=0.56
	if diferencia>=47 and diferencia<=53:
		pd=0.57
	if diferencia>=54 and diferencia<=61:
		pd=0.58
	if diferencia>=62 and diferencia<=68:
		pd=0.59
	if diferencia>=69 and diferencia<=76:
		pd=0.60
	if diferencia>=77 and diferencia<=83:
		pd=0.61
	if diferencia>=84 and diferencia<=91:
		pd=0.62
	if diferencia>=92 and diferencia<=98:
		pd=0.63
	if diferencia>=99 and diferencia<=106:
		pd=0.64
	if diferencia>=107 and diferencia<=113:
		pd=0.65
	if diferencia>=114 and diferencia<=121:
		pd=0.66
	if diferencia>=122 and diferencia<=129:
		pd=0.67
	if diferencia>=130 and diferencia<=137:
		pd=0.68
	if diferencia>=138 and diferencia<=145:
		pd=0.69
	if diferencia>=146 and diferencia<=153:
		pd=0.70
	if diferencia>=154 and diferencia<=162:
		pd=0.71
	if diferencia>=163 and diferencia<=170:
		pd=0.72
	if diferencia>=171 and diferencia<=179:
		pd=0.73
	if diferencia>=180 and diferencia<=188:
		pd=0.74
	if diferencia>=189 and diferencia<=197:
		pd=0.75
	if diferencia>=198 and diferencia<=206:
		pd=0.76
	if diferencia>=207 and diferencia<=215:
		pd=0.77
	if diferencia>=216 and diferencia<=225:
		pd=0.78
	if diferencia>=226 and diferencia<=235:
		pd=0.79
	if diferencia>=236 and diferencia<=245:
		pd=0.80
	if diferencia>=246 and diferencia<=256:
		pd=0.81
	if diferencia>=257 and diferencia<=267:
		pd=0.82
	if diferencia>=268 and diferencia<=278:
		pd=0.83
	if diferencia>=279 and diferencia<=290:
		pd=0.84
	if diferencia>=291 and diferencia<=302:
		pd=0.85
	if diferencia>=303 and diferencia<=315:
		pd=0.86
	if diferencia>=316 and diferencia<=328:
		pd=0.87
	if diferencia>=329 and diferencia<=344:
		pd=0.88
	if diferencia>=345 and diferencia<=357:
		pd=0.89
	if diferencia>=358 and diferencia<=374:
		pd=0.90
	if diferencia>=375 and diferencia<=391:
		pd=0.91
	if diferencia>=392:
		pd=0.92
	if diferencia<=(-4) and diferencia>=(-10):
		pd=0.49
	if diferencia<=(-11) and diferencia>=(-17):
		pd=0.48
	if diferencia<=(-18) and diferencia>=(-25):
		pd=0.47
	if diferencia<=(-26) and diferencia>=(-32):
		pd=0.46
	if diferencia<=(-33) and diferencia>=(-39):
		pd=0.45
	if diferencia<=(-40) and diferencia>=(-46):
		pd=0.44
	if diferencia<=(-47) and diferencia>=(-53):
		pd=0.43
	if diferencia<=(-54) and diferencia>=(-61):
		pd=0.42
	if diferencia<=(-62) and diferencia>=(-68):
		pd=0.41
	if diferencia<=(-69) and diferencia>=(-76):
		pd=0.40
	if diferencia<=(-77) and diferencia>=(-83):
		pd=0.39
	if diferencia<=(-84) and diferencia>=(-91):
		pd=0.38
	if diferencia<=(-92) and diferencia>=(-98):
		pd=0.37
	if diferencia<=(-99) and diferencia>=(-106):
		pd=0.36
	if diferencia<=(-107) and diferencia>=(-113):
		pd=0.35
	if diferencia<=(-114) and diferencia>=(-121):
		pd=0.34
	if diferencia<=(-122) and diferencia>=(-129):
		pd=0.33
	if diferencia<=(-130) and diferencia>=(-137):
		pd=0.32
	if diferencia<=(-138) and diferencia>=(-145):
		pd=0.31
	if diferencia<=(-146) and diferencia>=(-153):
		pd=0.30
	if diferencia<=(-154) and diferencia>=(-162):
		pd=0.29
	if diferencia<=(-163) and diferencia>=(-170):
		pd=0.28
	if diferencia<=(-171) and diferencia>=(-179):
		pd=0.27
	if diferencia<=(-180) and diferencia>=(-188):
		pd=0.26
	if diferencia<=(-189) and diferencia>=(-197):
		pd=0.25
	if diferencia<=(-198) and diferencia>=(-206):
		pd=0.24
	if diferencia<=(-207) and diferencia>=(-215):
		pd=0.23
	if diferencia<=(-216) and diferencia>=(-225):
		pd=0.22
	if diferencia<=(-226) and diferencia>=(-235):
		pd=0.21
	if diferencia<=(-236) and diferencia>=(-245):
		pd=0.20
	if diferencia<=(-246) and diferencia>=(-256):
		pd=0.19
	if diferencia<=(-257) and diferencia>=(-267):
		pd=0.18
	if diferencia<=(-268) and diferencia>=(-278):
		pd=0.17
	if diferencia<=(-279) and diferencia>=(-290):
		pd=0.16
	if diferencia<=(-291) and diferencia>=(-302):
		pd=0.15
	if diferencia<=(-303) and diferencia>=(-315):
		pd=0.14
	if diferencia<=(-316) and diferencia>=(-328):
		pd=0.13
	if diferencia<=(-329) and diferencia>=(-344):
		pd=0.12
	if diferencia<=(-345) and diferencia>=(-357):
		pd=0.11
	if diferencia<=(-358) and diferencia>=(-374):
		pd=0.10
	if diferencia<=(-375) and diferencia>=(-391):
		pd=0.09
	if diferencia<=(-392):
		pd=0.08

	var_elo = (result - pd) * your_k
	print("Su variación en esta partida será de: ", round(var_elo, 2))
	new_elo = new_elo + round(var_elo, 2)
	
	rival_elo = int(input("Ingrese el elo de su siguiente rival o coloque 0 si ya no tiene mas rivales para calcular: "))

else:
	print("Su nuevo elo será de: ", round(new_elo))