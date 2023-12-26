from terminal_modif import Color
from playfair import Playfair

isLoop = True

playfair = Playfair()

while isLoop:
  print('--- PLAYFAIR ---')
  print('1. Encryption')
  print('2. Decryption')
  print('3. Exit')
  choose = input('choose [1/2/3]: ')

  if choose == "1":
    Color.clear_terminal()
    playfair.encryption()
  elif choose == "2":
    Color.clear_terminal()
    playfair.decryption()
  elif choose == "3":
    isLoop = False
    Color.clear_terminal()
    print(Color.CYAN + '\n=== Thank You ===' + Color.RESET)
  else:
    Color.clear_terminal()
    print(Color.RED + '\nNo Suitable Input\n' + Color.RESET)

