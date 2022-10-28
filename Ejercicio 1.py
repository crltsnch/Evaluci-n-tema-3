def Hanoi(discos, AgujaInicio=1, AgujaAuxiliar=2, AgujaFinal=3):
    if discos==1:
        print(AgujaInicio, "a", AgujaFinal)
    else:
        Hanoi(discos-1, AgujaInicio, AgujaFinal, AgujaAuxiliar)