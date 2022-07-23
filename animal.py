import os
import random
import game_config as gc

from pygame import image, transform

animals_count = dict((a,0) for a in gc.Asset_files)
def available_animals():
    return [a for a,c in animals_count.items() if c<2]

class Animals:
    def __init__(self,index):
        self.index = index
        self.row = index // gc.Num_tiles_side
        self.col = index % gc.Num_tiles_side
        self.name = random.choice(available_animals())
        animals_count[self.name] += 1

        self.image_path = os.path.join(gc.Asset_dir, self.name)
        self.image = image.load(self.image_path)
        self.image = transform.scale(self.image, (gc.Images_size -2*gc.Margin, gc.Images_size -2*gc.Margin ))
        self.box = self.image.copy()
        self.box.fill((200,200,200))
        self.skip = False
