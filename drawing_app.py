import pygame
import sys


pygame.init()

pygame.display.set_caption("Drawing Application")  # Set the window title

screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()


drawing = False
color = (255, 0, 0)
radius = 5
brush_sizes = [5, 10, 15, 20]
colors = [
    (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
    (255, 255, 255), (0, 0, 0), (255, 165, 0), (128, 0, 128),
    (0, 255, 255), (255, 20, 147), (128, 128, 128), (0, 128, 128)
]
palette_width = 6
palette_size = 80
palette_height = 2

button_font = pygame.font.SysFont(None, 24)

def draw_demo(demo_type):

 screen.fill((0, 0, 0), (0, palette_size * (palette_height + 1), 800, 600))
 if demo_type == 'cat':
        # Cat body
        pygame.draw.circle(screen, (255, 223, 186), (400, 400), 100)
        # Cat ears
        pygame.draw.polygon(screen, (255, 223, 186), [(340, 300), (380, 200), (420, 300)])
        pygame.draw.polygon(screen, (255, 223, 186), [(460, 300), (500, 200), (540, 300)])
        pygame.draw.polygon(screen, (255, 192, 203), [(350, 290), (380, 220), (410, 290)])
        pygame.draw.polygon(screen, (255, 192, 203), [(470, 290), (500, 220), (530, 290)])
        # Cat eyes
        pygame.draw.ellipse(screen, (0, 0, 0), (375, 375, 20, 30))
        pygame.draw.ellipse(screen, (0, 0, 0), (415, 375, 20, 30))
        pygame.draw.ellipse(screen, (255, 255, 255), (380, 380, 5, 10))
        pygame.draw.ellipse(screen, (255, 255, 255), (420, 380, 5, 10))
        # Cat nose
        pygame.draw.polygon(screen, (255, 105, 180), [(395, 420), (405, 420), (400, 430)])
        # Cat whiskers
        for i in range(-1, 2):
            pygame.draw.line(screen, (0, 0, 0), (300, 400 + i * 10), (375, 400 + i * 10), 2)
            pygame.draw.line(screen, (0, 0, 0), (425, 400 + i * 10), (500, 400 + i * 10), 2)
        # Cat mouth
        pygame.draw.arc(screen, (0, 0, 0), (380, 430, 40, 20), 3.14, 0, 2)
 elif demo_type == 'bear':
        # Bear body
        pygame.draw.circle(screen, (139, 69, 19), (400, 400), 100)
        pygame.draw.circle(screen, (205, 133, 63), (400, 420), 80)
        # Bear ears
        pygame.draw.circle(screen, (139, 69, 19), (340, 320), 30)
        pygame.draw.circle(screen, (139, 69, 19), (460, 320), 30)
        pygame.draw.circle(screen, (205, 133, 63), (340, 320), 15)
        pygame.draw.circle(screen, (205, 133, 63), (460, 320), 15)
        # Bear eyes
        pygame.draw.circle(screen, (0, 0, 0), (375, 375), 10)
        pygame.draw.circle(screen, (0, 0, 0), (425, 375), 10)
        pygame.draw.circle(screen, (255, 255, 255), (375, 375), 5)
        pygame.draw.circle(screen, (255, 255, 255), (425, 375), 5)
        # Bear nose
        pygame.draw.circle(screen, (0, 0, 0), (400, 400), 12)
        # Bear mouth
        pygame.draw.arc(screen, (0, 0, 0), (385, 410, 30, 20), 3.14, 0, 2)
 elif demo_type == 'car':
        # Car body
        pygame.draw.rect(screen, (0, 0, 255), (300, 350, 200, 100))
        pygame.draw.rect(screen, (0, 0, 128), (300, 350, 200, 40))
        # Car windows
        pygame.draw.rect(screen, (255, 255, 255), (320, 370, 60, 40))
        pygame.draw.rect(screen, (255, 255, 255), (420, 370, 60, 40))
        # Car wheels
        pygame.draw.circle(screen, (128, 128, 128), (340, 450), 30)
        pygame.draw.circle(screen, (0, 0, 0), (340, 450), 20)
        pygame.draw.circle(screen, (128, 128, 128), (460, 450), 30)
        pygame.draw.circle(screen, (0, 0, 0), (460, 450), 20)
 elif demo_type == 'excavator':
        # Excavator body
        pygame.draw.rect(screen, (255, 140, 0), (200, 350, 400, 100))

        # Excavator control room
        pygame.draw.rect(screen, (200, 200, 200), (500, 300, 100, 50))
        pygame.draw.rect(screen, (0, 0, 0), (500, 300, 100, 50), 2)
        pygame.draw.rect(screen, (135, 206, 235), (510, 310, 80, 30))

        # Excavator arm
        pygame.draw.line(screen, (255, 140, 0), (400, 350), (600, 250), 20)
        pygame.draw.line(screen, (255, 140, 0), (600, 250), (680, 350), 20)

        # Excavator bucket
        pygame.draw.rect(screen, (0, 0, 0), (640, 310, 80, 40))

        # Excavator wheels
        pygame.draw.circle(screen, (128, 128, 128), (240, 450), 40)
        pygame.draw.circle(screen, (128, 128, 128), (560, 450), 40)

 elif demo_type == 'truck':
        # Truck body
        pygame.draw.rect(screen, (0, 255, 0), (200, 350, 400, 100))
        pygame.draw.rect(screen, (0, 128, 0), (200, 350, 400, 40))
        pygame.draw.rect(screen, (255, 0, 0), (500, 300, 100, 150))
        # Truck windows
        pygame.draw.rect(screen, (255, 255, 255), (520, 320, 60, 50))
        pygame.draw.rect(screen, (255, 25.5, 255), (520, 380, 60, 50))
        # Truck wheels
        pygame.draw.circle(screen, (128, 128, 128), (240, 450), 40)
        pygame.draw.circle(screen, (0, 0, 0), (240, 450), 30)
        pygame.draw.circle(screen, (128, 128, 128), (560, 450), 40)
        pygame.draw.circle(screen, (0, 0, 0), (560, 450), 30)



def draw_palette():
    for i, col in enumerate(colors):
        row = i // palette_width
        col_index = i % palette_width
        pygame.draw.rect(screen, col, (col_index * palette_size, row * palette_size, palette_size, palette_size))
    for i, size in enumerate(brush_sizes):
        pygame.draw.circle(screen, (255, 255, 255),
                           (palette_size // 2 + i * palette_size, palette_size * palette_height + 20), size)


def draw_buttons(samples_menu_open=None):
    new_button = pygame.draw.rect(screen, (100, 100, 100), (400, 10, 80, 40))
    samples_button = pygame.draw.rect(screen, (100, 100, 100), (500, 10, 80, 40))
    cross_button = None

    screen.blit(button_font.render("New", True, (255, 255, 255)), (415, 20))
    screen.blit(button_font.render("Samples", True, (255, 255, 255)), (505, 20))

    if samples_menu_open:
        cross_button = pygame.draw.rect(screen, (255, 0, 0), (600, 10, 40, 40))
        screen.blit(button_font.render("X", True, (255, 255, 255)), (615, 20))

    return new_button, samples_button, cross_button
def draw_samples_menu():
    samples = ["cat", "bear", "car", "excavator", "truck"]
    for i, sample in enumerate(samples):
        pygame.draw.rect(screen, (200, 200, 200), (i * 160, palette_size * palette_height + 40, 160, 40))
        screen.blit(button_font.render(sample.capitalize(), True, (0, 0, 0)),
                    (i * 160 + 50, palette_size * palette_height + 50))
def draw_game(samples_menu_open):
    draw_palette()
    new_button, samples_button, cross_button = draw_buttons(samples_menu_open)
    if samples_menu_open:
        draw_samples_menu()
    pygame.display.flip()
    return new_button, samples_button, cross_button

def new_drawing():
    screen.fill((0, 0, 0), (0, palette_size * (palette_height + 1), 1200, 10000))

    samples_menu_open = False
    selected_demo = None

def main():
    samples_menu_open = False
    selected_demo = None
    drawing = False
    color = (255, 0, 0)
    radius = 5

    while True:
        new_button, samples_button, cross_button = draw_game(samples_menu_open)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if new_button.collidepoint(pos):
                    new_drawing()
                elif samples_button.collidepoint(pos):
                    samples_menu_open = not samples_menu_open
                elif samples_menu_open and cross_button and cross_button.collidepoint(pos):
                    selected_demo = None
                    samples_menu_open = False
                    new_drawing()
                elif samples_menu_open:
                    sample_pos = pos[1] - (palette_size * palette_height + 40)
                    if sample_pos > 0 and sample_pos < 40:
                        sample_index = pos[0] // 160
                        samples = ["cat", "bear", "car", "excavator", "truck"]
                        if sample_index < len(samples):
                            selected_demo = samples[sample_index]
                            draw_demo(selected_demo)
                else:
                    drawing = True
                    if pos[1] < palette_size * palette_height:
                        col_index = pos[0] // palette_size
                        row_index = pos[1] // palette_size
                        color_index = row_index * palette_width + col_index
                        if color_index < len(colors):
                            color = colors[color_index]
                    elif pos[1] < palette_size * (palette_height + 1):
                        radius = brush_sizes[(pos[0] // palette_size)]
            elif event.type == pygame.MOUSEBUTTONUP:
                drawing = False
            elif event.type == pygame.MOUSEMOTION:
                if drawing:
                    pos = pygame.mouse.get_pos()
                    if pos[1] >= palette_size * (palette_height + 1):
                        pygame.draw.circle(screen, color, pos, radius)

        pygame.display.flip()
        clock.tick(60)



if __name__ == '__main__':
    main()
