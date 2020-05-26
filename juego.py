from random import shuffle

def baraja():
  return [(n,p) for n in (['A','J','Q','K'] + [str(x) for x in range(2,11)]) for p in ['♥','♦','♣','♠']]

def mezclar(baraja):
  shuffle(baraja)
  return baraja

def sacar_carta(baraja):
  if baraja == []:
    pass
  else:
    #print (baraja[0])
    sacar_carta(baraja[1:])

def valor_carta(carta):
  if carta[0] in ['J','Q','K']:
    return 10
  elif carta[0] == 'A':
    return 1
  else:
    return int(carta[0])

def valor_mano(mano):
  if mano == []:
    return 0
  return valor_carta(mano[0]) + valor_mano(mano[1:])

def valor_juego(mano):
  if valor_mano(mano) <= 11 and 1 in [valor_carta(x) for x in mano]:
    return valor_mano(mano) + 10
  else:
    return valor_mano(mano)

def jugar(mazo, jugador, repartidor):
  print(jugador, repartidor)
  if len(mazo) > 2 and valor_juego(jugador) < 21 and valor_juego(repartidor) < 21:
    jugar(mazo[2:], jugador+[mazo[0]], repartidor+[mazo[1]])
  print(valor_juego(jugador))
  print(valor_juego(repartidor))
  ganador(valor_juego(jugador),valor_juego(repartidor))

def ganador(jugador, repartidor):
  if jugador > 21:
    print("Gana repartidor")
    return False
  elif repartidor > 21:
    print("Gana jugador")
    return False
  elif jugador > repartidor:
    print("Gana jugador")
    return False
  else:
    print("Gana repartidor")
    return False
  return True

while(input()=='p'):
  
jugar(mezclar(baraja()),[],[])
#prueba()
#print(valor_mano(mezclar(baraja())[:2]))