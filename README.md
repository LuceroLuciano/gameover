# Basic Game

This is a basic game when I use the library Pygame of Python. 

Game consist in touch with a bar an ball and this rebot. just use colors, events to move the keyboard keys and use coordinates for the screen. 

### How does the game work?
1. Install library pygame
```python
    pip install pygame
```
2. Create an file game1.py and import library pygame, then initial the library
```python
    import pygame
    pygame.init()
```
3. The fundamentas for create a game are, screen, clock and principal loop

4. Define the size of screen and show
```python
    screen_size = (800, 600) 
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
```

5. Create the principal loop with two conditonals for let the move of playgames
```python
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
```


5. Check the move of ball 
    ```python
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
    ```


7. Modify the coordinates to give movement to the players
    ````python
        player1_y_coor += player1_y_speed
        player2_y_coor += player2_y_speed

        # movimiento pelota
        pelota_x += pelota_speed_x
        pelota_y += pelota_speed_y
    ```

8. Paint the screen and the players and ball

```python
    screen.fill(black) # pintar la pantalla

    # Zona de dibujo pinta la pelota y los jugadores
    jugador1 = pygame.draw.rect(screen, white, (player1_x_coor, player1_y_coor, player_width, player_height))
    jugador2 = pygame.draw.rect(screen, white, (player2_x_coor, player2_y_coor, player_width, player_height))
    
    pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)
```

9. When the ball touch whit the players then the ball bounces

```python
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x *= -1
    pygame.display.flip()    # actualizar la pantalla
    clock.tick(60) # velocidad del reloj/moviemito de la pelota 
```

10. And finally if we can stop to play only clos the screen or window where we are playing, this screen close with  this code
    ```python
        pygame.quit()
    ```


This game ist very basic and it is only for a little about the fundamentals of the pygame library. 


