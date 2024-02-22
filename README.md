# BomberMan
![game.jpg](game.jpg)
Список объектов
* Creature
  * x,y
  * speed
  * skin
  * hitbox
  * life = 3

* Player (Creature)
  * bomb_count

* TileType(Enum)
  * BORDER, GRASS, DESTRUCTIBLE = 0, 1, 2

* Tile
  * x, y
  * Type (GRASS, BORDER, DESTRUCTIBLE = 0, 1, 2)
  * hitbox
  * image

* Map 
  * map_width
  * map_height 
  * tiles_map list[Tile]
  * horizontal_offset (for now)
  * vertical_offset (for now)

* keyboardInput
  * def keyEvent()

* Menu
  * start -> main loop
  * exit -> close game

* Bomb
  * x,y
  * hitbox
  * power
  * timer
 
* NPC
  * movement

![scheme.jpg](scheme.jpg)

        # Проверка когда клавиша нажимается
        elif event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                #x -= 10
                fl_left = True
            elif event.key == py.K_RIGHT:
                #x += 10
                fl_right = True
            elif event.key == py.K_UP:
                #y -= 10
                fl_up = True
            elif event.key == py.K_DOWN:
                #y += 10
                fl_down = True
        # Проверка когда клавиша отпускается
        elif event.type == py.KEYUP:
            if event.key == py.K_LEFT:
                fl_left = False
            elif event.key == py.K_RIGHT:
                fl_right = False
            elif event.key == py.K_UP:
                fl_up = False
            elif event.key == py.K_DOWN:
                fl_down = False