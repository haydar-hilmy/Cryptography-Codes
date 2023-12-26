from terminal_modif import Color
from blockcipher import ECB

isLoop = True

ecb = ECB()

while isLoop:
  print('--- BLOCK CIPHER [ECB] ---')
  print('1. Encryption')
  print('2. Decryption')
  print('3. Exit')
  choose = input('choose [1/2/3]: ')

  if choose == "1":
    Color.clear_terminal()
    ecb.encryption()
  elif choose == "2":
    Color.clear_terminal()
    ecb.decryption()
  elif choose == "3":
    isLoop = False
    Color.clear_terminal()
    print(Color.CYAN + '\n=== Thank You ===' + Color.RESET)
  else:
    Color.clear_terminal()
    print('\nNo Suitable Input\n')

