import pygame
import random


SETTINGS = {
    'screen'  : {
        'width' : 800,
        'height': 600,
    },
    'caption' : '01',
}

COLORS = {
    'black' : (36, 52, 53),
    'white' : (234, 228, 214)
}

SQUARE_COLORS = {
    'red'   : (249, 102, 56),
    'blue'  : (48, 96, 249),
    'green' : (52, 206, 147),
    'yellow': (255, 204, 95),
}

PROPS = {
    'border_radius': 8,
}


def draw_background()->None:
    surface.fill(COLORS['white'])

    
def get_random_color():
    return SQUARE_COLORS[random.choice(list(SQUARE_COLORS.keys()))]
    
    
def draw_square()->None:
    X = random.randint(0, 750)
    Y = random.randint(0, 550)
    size = random.randint(10, 200)
    color = get_random_color()
    pygame.draw.rect(surface, color, (X, Y, size, size), 0, PROPS['border_radius'])


def draw_circle()->None:
    X = random.randint(25, 775)
    Y = random.randint(25, 575)
    radius = random.randint(10, 200)
    color = get_random_color()
    pygame.draw.circle(surface, color, (X, Y), radius)


POS = { 'end_pos': () }
def draw_segment()->None:
    if POS['end_pos']:
        start_pos = POS['end_pos']
    else:
        start_pos = (random.randint(0, 800), random.randint(0, 600))
    
    end_pos = (random.randint(0, 800), random.randint(0, 600))
    POS['end_pos'] = end_pos
    
    width = random.randint(1, 10)
    pygame.draw.line(surface, get_random_color(), start_pos, end_pos, width)
    


def draw_figure()->None:
    figures = {
        'circle': draw_circle,
        'square': draw_square,
    }
    figures[random.choice(list(figures.keys()))]()
    
    
def loop()->None:
    i = 0
    while True:
        i+=1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        if i<100:
#            draw_square()
#            draw_circle()
#            draw_figure()
            draw_segment()
            pygame.time.wait(100)
        
        pygame.display.update()



if __name__ == '__main__':
    pygame.init()
    
    surface = pygame.display.set_mode((SETTINGS['screen']['width'],
                                       SETTINGS['screen']['height']))
    pygame.display.set_caption(SETTINGS['caption'])
    clock = pygame.time.Clock()
    
    draw_background()
    loop()
    
    pygame.quit()
    quit()