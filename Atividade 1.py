import random

sala = 1

interacoes = 0

escolha = 1

while(interacoes < 7 and sala != 9):
    
    
    print('Você está na sala:', sala)
    
    print('Escolha seu caminho:')
    
    print('[1] - Camimho vermelho')
    
    print('[2] - Camimho preto')
    
    escolha = int(input())
   
    if sala == 8 and escolha == 2:
        
        sala = random.randint(1,5)
        print('Você entrou no portal e acabou sendo jogado na sala: %i ' % sala)
        escolha = 0    
        
    elif sala == 6 and escolha == 1:
        print('Você tenta ir para o caminho vermelho,mas percebe que nesta sala só existe um caminho preto, então você segue por ele')
        sala = sala + 2
       
      
    else:
        
        sala = sala + escolha
    
    interacoes = interacoes + 1

if interacoes >= 7:
    print(' Você realizou mais de 7 interações e ficou preso pra sempre na dungeon, Game Over!')
    
elif sala == 9:
    print(' Você chegou a sala 9 e venceu a dungeon!!!')
    
