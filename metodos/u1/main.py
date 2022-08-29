from bin import b10_to_b2

err =  [
        0.046875,
        0.04998779296875,
        0.0499999523162841796875,
        0.049999999813735485076904296875,
        0.0499999999883584678173065185546875

    ]

i = 1
vm = 2641
for e in err:
    E= 500 * 60 * 60 * 20 * 24*(0.05 -e) * vm
    if  E > 200:
        print(i* 8, "bits no sirven")
    else:
        print(i* 8, "bits sirven")

    print("Error en metros: ", E)
    i+=1

