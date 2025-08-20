import pygame
import sys
import random
from pygame.locals import *
import csv

# init
pygame.init()
WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Drive Dash")
name = 'Your name:'
def main(name):
    enemy_sprite_list = ['sprite_folder\\bluetruck.png',
    'sprite_folder\\ambulance.png',
    'sprite_folder\\police.png',
    'sprite_folder\\taxi.png',
    'sprite_folder\\yellowtruck.png']
    enemy_sprites=[]
    score = 0
    score_font = pygame.font.Font("game-font.ttf", 44)
    score_surf =  score_font.render(f'Score: {score}', True, (255,255,255))
    # car variables
    car_height, car_width = 70, 50
    x, y = 400 - car_width // 2, 480  # starting point
    car_rect = pygame.Rect((x, y, car_width, car_height))
    speed = 6

    # road variables
    road_origin_x, road_origin_y = 150, 0
    road_height, road_width = HEIGHT, WIDTH - road_origin_x * 2
    road_rect = pygame.Rect(road_origin_x, road_origin_y, road_width, road_height)
    road_image_rect = pygame.Rect((0,0,road_width,road_height))

    # function to randomize enemy spawn
    def randy():
        return random.randint(-enemy_height * 6, -enemy_height)
    # function to draw the car and road
    def draw_cars():
        SCREEN.blit(road_image, road_image_rect)
        n=0
        for enemy_rect in enemy_rects:
            SCREEN.blit(enemy_sprites[n%len(enemy_sprites)],enemy_rect)
            n+=1
        SCREEN.blit(car_image, car_rect)
    # Input variables
    dynamic_width = 200
    input_box = pygame.Rect(dynamic_width, 350, 200, 50)
    dynamic_width = WIDTH//2 - input_box.w
    active =True
    # load images
    car_image = pygame.image.load('sprite_folder\\PLAYER.png').convert_alpha()
    road_image = pygame.image.load('sprite_folder\\road.png').convert()
    bg_image = pygame.image.load('sprite_folder\\cartoonbg.jpeg').convert()
    enemy_sprite1=pygame.image.load(f'{enemy_sprite_list[0]}').convert_alpha()
    enemy_sprite2=pygame.image.load(f'{enemy_sprite_list[1]}').convert_alpha()
    enemy_sprite3=pygame.image.load(f'{enemy_sprite_list[2]}').convert_alpha()
    enemy_sprite4=pygame.image.load(f'{enemy_sprite_list[3]}').convert_alpha()
    enemy_sprite5=pygame.image.load(f'{enemy_sprite_list[4]}').convert_alpha()
    enemy_sprites = [enemy_sprite1,enemy_sprite2,enemy_sprite3,enemy_sprite4,enemy_sprite5]
    # highscore sorting
    with open("Racing.csv","r") as f:
        r = csv.reader(f)
        d = dict(r)
        dict_keys = [int(x) for x in d.keys()]
        sorted_keys = list(sorted(dict_keys))[::-1][0:5]
        highscore = [(sorted_keys[0],d[str(sorted_keys[0])]),
                     (sorted_keys[1],d[str(sorted_keys[1])]),
                     (sorted_keys[2],d[str(sorted_keys[2])]),
                     (sorted_keys[3],d[str(sorted_keys[3])]),
                     (sorted_keys[4],d[str(sorted_keys[4])])]
    #STARTING SCREEN MAIN MENU
    name_menu_running = True
    if name == "Your name:":
        name_blank = True
    else:
        name_blank = False
    while name_menu_running:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if name_blank:
                    name = ''
                    name_blank = False
                if active:
                    if event.key == pygame.K_RETURN:
                        username = name
                        name_menu_running = False
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        name += event.unicode
        color = pygame.Color('black')
        # car background
        bg_rect = pygame.Rect(0,0,WIDTH,HEIGHT)
        SCREEN.blit(bg_image,bg_rect)
        font = pygame.font.Font("game-font.ttf", 30)
        no1 = font.render(f"#1. {str(highscore[0][1])+':'+str(highscore[0][0])}",True, (10,10,10))
        no2 = font.render(f"#2. {str(highscore[1][1])+':'+str(highscore[1][0])}",True, (10,10,10))
        no3 = font.render(f"#3. {str(highscore[2][1])+':'+str(highscore[2][0])}",True, (10,10,10))
        no4 = font.render(f"#4. {str(highscore[3][1])+':'+str(highscore[3][0])}",True, (10,10,10))
        no5 = font.render(f"#5. {str(highscore[4][1])+':'+str(highscore[4][0])}",True, (10,10,10))
        SCREEN.blit(no1,(WIDTH-300,300))
        SCREEN.blit(no2,(WIDTH-300,350))
        SCREEN.blit(no3,(WIDTH-300,400))
        SCREEN.blit(no4,(WIDTH-300,450))
        SCREEN.blit(no5,(WIDTH-300,500))
        big_font = pygame.font.Font("game-font.ttf", 80)
        title_text = big_font.render('Drive Dash', True, (70,70,255))
        menu_text = font.render('Input your name and press Enter to play', True, (10,10,10))
        instruction_text = font.render('Use arrow keys to move, and try not to hit', True, (10,10,10))
        dynamic_width = WIDTH//3 - input_box.w//2
        txt_surface = font.render(name, True, "white")
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        input_box = pygame.Rect(dynamic_width, 300, width, 50)
        # display everything
        SCREEN.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 5 - title_text.get_height()))
        SCREEN.blit(menu_text, (WIDTH // 2 - menu_text.get_width() // 2, HEIGHT // 3 - menu_text.get_height()))
        SCREEN.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 2.5 - instruction_text.get_height()))
        pygame.draw.rect(SCREEN, color, input_box, 0)
        pygame.draw.rect(SCREEN, "white", input_box, 2)
        SCREEN.blit(txt_surface, (input_box.x+5, input_box.y+5))
        pygame.display.flip()
    # Create enemy cars
    enemy_height, enemy_width = 90, 60
    enemy_rects = []
    enemy_speeds = []
    # randomize enemy speed
    for i in range(4):
        enemy_rect = pygame.Rect(road_origin_x + road_width * (i / 4) + 40 + random.randint(-10, 10), randy(), enemy_width, enemy_height)
        enemy_speed = random.randint(8, 15)  # Random speed for each enemy
        enemy_rects.append(enemy_rect)
        enemy_speeds.append(enemy_speed)
    # Initialize time variables
    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()  # Starting time
    running = True
    # game loop
    while running:
        new_score = (pygame.time.get_ticks() - start_ticks) // 100
        if new_score != score:  # Only update if the score has changed
            score = new_score
            score_surf =  score_font.render(f'Score: {score}', True, (255,255,255))
        SCREEN.fill("#004585")
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        # Update enemy positions
        for i in range(len(enemy_rects)):
            enemy_rects[i].y += enemy_speeds[i]
            if enemy_rects[i].y > HEIGHT + enemy_height:
                enemy_rects[i].y, enemy_rects[i].x = randy(), road_origin_x + road_width * (i / 4) + 40 + random.randint(-10, 10)
                enemy_speeds[i] = random.randint(8 , 12)  # Assign a new random speed
        # road_movement
        road_image_rect.y += 6
        if road_image_rect.y > 0:
            road_image_rect.y = -400
        # controls
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            car_rect.x -= speed * 1.25
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            car_rect.x += speed * 1.25
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            car_rect.y -= speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            car_rect.y += speed * 0.75

        # clamp the car
        car_rect.clamp_ip(road_rect)

        # check for collision
        if any(car_rect.colliderect(enemy_rect) for enemy_rect in enemy_rects):
            running = False

        # display
        draw_cars()
        SCREEN.blit(score_surf, (0, 0))
        pygame.display.flip()
        clock.tick(60)
        # Death screen
        score_added = False
        while not running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r] or keys[pygame.K_RETURN]:
                main(name)
            draw_cars()
            #adding score
            if not score_added:
                with open("Racing.csv","a+",newline ="")as f:
                    w=csv.writer(f)
                    w.writerow([score,username])
                    score_added = True
            font = pygame.font.Font("game-font.ttf", 74)
            font2 = pygame.font.Font("game-font.ttf", 44)  
            
            score_surf =  score_font.render(f'Score: {score}', True, (255,255,255))
            text = font.render('GAME OVER', True, (255,255,255))
            text2 = font2.render('Press R to restart', True, (255,255,255))
            pygame.draw.rect(SCREEN,"black",pygame.Rect(150,150,500,300),0)
            pygame.draw.rect(SCREEN,"white",pygame.Rect(150,150,500,300),5)
            SCREEN.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height()))
            SCREEN.blit(text2, (WIDTH // 2 - text2.get_width() // 2, HEIGHT // 2))
            SCREEN.blit(score_surf, (WIDTH // 2 - score_surf.get_width() // 2, HEIGHT // 2 + score_surf.get_height() * 2))
            
            pygame.display.flip()
            pygame.time.Clock().tick(60)
main(name)