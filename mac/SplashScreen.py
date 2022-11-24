﻿## SplashScreen File
## This file contains information about your project

from datetime import date

CurrentYear = date.today().year
SoftwareName = "SimpleCalculator"
Version = "1.0"
CopyrightName = "Heitor"

print("Name:", SoftwareName)
print("Version:", Version)
print("Created By:", CopyrightName)

if CurrentYear == 2022:
   print("Copyright ©", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")
else:
   print("Copyright © 2022 -", CurrentYear, "|", CopyrightName + ".", "All rights reserved.")

print("="*80)
print(f'[{SoftwareName} for Mac] - Running...')
print("="*80)
print()
