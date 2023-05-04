# importamos libreria pygame
import pygame
# iniciamos libreria pygame
pygame.init()

# colores
black = (0, 0, 0)
white = (255, 255, 255)

player_width = 15
player_height = 90

# tamaño de la ventana
screen_size = (800, 600) 

# mostrar ventana
screen = pygame.display.set_mode(screen_size)

# reloj
clock = pygame.time.Clock()

#coordenadas y velocidad del jugador 1
player1_x_coor = 50
player1_y_coor = 300 - 45
player1_y_speed = 0

# coordenadas y velocidad del jugador 2
player2_x_coor = 750 - player_width
player2_y_coor = 300 - 45
player2_y_speed = 0

# coordenadas de la pelota
pelota_x = 400
pelota_y = 300
pelota_speed_x = 3
pelota_speed_y = 3

# juego inicia en false
game_over = False

# bucle principal
while not game_over: # mientras no sea falso, es decir, siempre que sea verdadero
    for event in pygame.event.get():    # recorre todos los eventos
        if event.type == pygame.QUIT:   # scierra la ventana
            game_over = True
        if event.type == pygame.KEYDOWN:    # moviemiento hacia arriba
            # Jugador 1
            if event.key == pygame.K_w:     # movimiento arriba con tecla w 
                player1_y_speed = -3
            if event.key == pygame.K_s:     # movimiento abajo con tecla s
                player1_y_speed = 3
            #jugador 2
            if event.key == pygame.K_UP:    # movimiento arriba con flecha
                player2_y_speed = -3    
            if event.key == pygame.K_DOWN:  # movimiento abajo con flecha
                player2_y_speed = 3
        
        if event.type == pygame.KEYUP:      # moviemiento hacia abajo
            # Jugador 1
            if event.key == pygame.K_w:
                player1_y_speed = 0
            if event.key == pygame.K_s:
                player1_y_speed = 0
            #jugador 2
            if event.key == pygame.K_UP:
                player2_y_speed = 0
            if event.key == pygame.K_DOWN:
                player2_y_speed = 0

    # checamos los rebotes de la pelota
    if pelota_y > 590 or pelota_y < 10:
        pelota_speed_y *= -1

    # revisa si la pelota sale del lado derecho
    if pelota_x > 800:
        pelota_x = 400
        pelota_y = 300
        # si sale de la pantalla, convierte direccion
        pelota_speed_x *= -1
        pelota_speed_y *= -1
    
    # revisa si la pelota sale del lado izquierdo
    if pelota_x < 0:
        pelota_x = 400
        pelota_y = 300
        # si sale de la pantalla, onvierte direccion
        pelota_speed_x *= -1
        pelota_speed_y *= -1


    # modifica las coordenadas para dar movimineto a los jugadores/pelot
    player1_y_coor += player1_y_speed
    player2_y_coor += player2_y_speed

    # movimiento pelota
    pelota_x += pelota_speed_x
    pelota_y += pelota_speed_y
    

    screen.fill(black) # pintar la pantalla

    # Zona de dibujo pinta la pelota y los jugadores
    jugador1 = pygame.draw.rect(screen, white, (player1_x_coor, player1_y_coor, player_width, player_height))
    jugador2 = pygame.draw.rect(screen, white, (player2_x_coor, player2_y_coor, player_width, player_height))
    
    pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)


    # colisiones cunado los jugadores tocan la pelota
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x *= -1

    pygame.display.flip()    # actualizar la pantalla
    clock.tick(60) # velocidad del reloj/moviemito de la pelota 

pygame.quit() # cierra ventana