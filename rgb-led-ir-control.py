# Voraussetzung: LIRC installiert und FB-Config erstellt
# Wenn eine andere FB-Config verwendet wird muss die Code-Liste und der FB-Name angepasst werden.

import os

baseCommand = "irsend SEND_ONCE rgbled "
codeList = ["ON","OFF","WHITE","RED","GREEN","BLUE","ORANGE","YELLOW_DARK","YELLOW_LIME","YELLOW_GREENISH","TURQUOISE","TURQUOISE_LIGHT","BLUE_LIGHT","BLUE_PASTEL","BLUE_PURPLE","PURPLE_DARK","PURPLE_PINKISH","PINK"]
codeCount = len(codeList)

os.system("sudo systemctl start lircd")

# Ausgabe der bekannten Codes
print("+++ IR-Sender +++ \n")
print("Bekannte Codes:")
for i in range(codeCount):
    print(str(i+1) + ": " + codeList[i])
print("\n")

# Per Benutzereingabe senden
print("Bitte die Nummer des Codes eingeben, der gesendet werden soll.")
print("\"0\" zum Beenden eingeben \n")

while True:
    codeNummer = int(input("Nummer des Codes, der gesendet werden soll: "))

    if (codeNummer == 0):
        break

    command = baseCommand + codeList[codeNummer-1]
    os.system(command)
    print()
