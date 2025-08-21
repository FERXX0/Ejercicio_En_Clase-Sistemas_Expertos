def diagnosticar():
    print("Sistema Experto: Diagnóstico de Fallas en Automóvil\n")
    print("Responde con 'si' o 'no' según corresponda.\n")

    arranca = input("¿El auto arranca? (si/no): ").strip().lower()

    if arranca == "no":
        luces = input("¿Las luces del tablero encienden? (si/no): ").strip().lower()
        if luces == "no":
            print("\nPosible causa: Batería descargada.")
        else:
            print("\nPosible causa: Fallo en el motor de arranque.")

    else:
        se_apaga = input("¿El auto se apaga al acelerar? (si/no): ").strip().lower()
        if se_apaga == "si":
            print("\nPosible causa: Problema en el suministro de combustible.")
        else:
            humo_negro = input("¿El auto tiene humo negro por el escape? (si/no): ").strip().lower()
            if humo_negro == "si":
                print("\nPosible causa: Mezcla rica de combustible.")
            else:
                humo_blanco = input("¿El auto tiene humo blanco constante? (si/no): ").strip().lower()
                if humo_blanco == "si":
                    print("\nPosible causa: Falla en la junta de culata.")
                else:
                    print("\nNo se pudo determinar la causa con la información dada.")

diagnosticar()