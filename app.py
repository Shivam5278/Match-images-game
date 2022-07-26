import pygame
import game_config as gc
from animal import Animals 
from pygame import display, event, image
from time import sleep

def find_index(x,y):
    row = y // gc.Img_size
    col = x // gc.Img_size
    index = row*gc.Num_tiles_side + col
    return index

pygame.init()
display.set_caption('My Game')

screen=display.set_mode((512 ,512))

matched = image.load('other_assets/matched.png')


running = True
tiles = [Animals(i) for i in range(0, gc.Num_tiles_total)]
current_images = []
while running:
    current_events=event.get()

    for e in current_events:
        if e.type==pygame.QUIT:
            running= False
        
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = find_index(mouse_x, mouse_y)
            #print(index)
            if index not in current_images:
                current_images.append(index)
            if len(current_images) > 2:
                current_images = current_images[1:]


    screen.fill((255,255,255))

    total_skipped = 0

    for i, tile in enumerate(tiles):
        image_i = tile.image if i in current_images else tile.box
        if not tile.skip:
            screen.blit(image_i, (tile.col*gc.Img_size + gc.Margin, tile.row*gc.Img_size + gc.Margin))
        else:
            total_skipped += 1
    if len(current_images) == 2 :
        idx1, idx2 = current_images
        if tiles[idx1].name == tiles[idx2].name:
            tiles[idx1].skip = True
            tiles[idx2].skip = True
            sleep(0.4)
            screen.blit(matched, (0,0))
            display.flip()
            sleep(0.4)
            current_images = []
    if total_skipped == len(tiles):
        running = False

print('Goodbye')