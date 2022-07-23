import os
Img_size = 128
Scr_size = 512
Num_tiles_side = 4
Num_tiles_total = 16
Margin = 4

Asset_dir = 'assets'
Asset_files = [x for x in os.listdir(Asset_dir) if x[-3:].lower() == 'png']
assert len(Asset_files) == 8
