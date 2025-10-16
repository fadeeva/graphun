import pygame


SETTINGS = {
    'screen'  : {
        'width' : 800,
        'height': 600,
    },
    'caption' : '01',
}

COLORS = {
    'red'   : (249, 102, 56),
    'blue'  : (48, 96, 249),
    'green' : (52, 206, 147),
    'yellow': (255, 204, 95),
    
    'black' : (36, 52, 53),
    'white' : (234, 228, 214)
}


def draw_background()->None:
    game_display.fill(COLORS['white'])


def loop()->None:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pygame.display.update()



if __name__ == '__main__':
    pygame.init()
    
    game_display = pygame.display\
                         .set_mode((SETTINGS['screen']['width'],
                                    SETTINGS['screen']['height']))
    pygame.display.set_caption(SETTINGS['caption'])
    clock = pygame.time.Clock()
    
    draw_background()
    loop()
    
    pygame.quit()
    quit()