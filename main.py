import pygame
import random
import time

# Initializing and Music
pygame.init()
screen = pygame.display.set_mode((600, 600))
Clock = pygame.time.Clock()
running = True
music = pygame.mixer.music.load("roblox-minecraft-fortnite-video-game-music-358426.mp3")
pygame.mixer.music.play(-1)
pygame.display.set_caption("Treasure Hunt")

# Class of Grid
class GridSquare:
    width = 60
    height = 60

    # Constructor
    def __init__(self, x, y, color="#000000"):
        self.x = x * 60
        self.y = y * 60
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, GridSquare.width, GridSquare.height)

    # Hypotenuse (Distance)
    def findDistance(self, another):
        A2 = self.y - another.y if another.y < self.y else another.y - self.y
        B2 = self.x - another.x if another.x < self.x else another.x - self.x
        C = ((int(A2) ** 2) + (int(B2) ** 2)) ** 0.5
        return int(C)

    # Color Shifting (ChatGPT)
    def shift_warm(self, t):
        r = self.color[1:3].upper()
        g = self.color[3:5].upper()
        b = self.color[5:].upper()
        r = int(r, 16); g = int(g, 16); b = int(b, 16)
        r += 0.05 * t; g -= 0.02 * t; b -= 0.03 * t
        r = max(0, min(r, 255)) # CLAMP: ChatGPT
        g = max(0, min(g, 255))
        b = max(0, min(b, 255))
        r  = hex(int(r)); g = hex(int(g)); b = hex(int(b));
        r = r.replace("0x", "").zfill(2) # ZFILL: ChatGPT
        g = g.replace("0x", "").zfill(2)
        b = b.replace("0x", "").zfill(2)
        self.color = "#" + "".join([r, g, b])

    # Color Shifting (ChatGPT)
    def shift_cold(self, t):
        r = self.color[1:3]
        g = self.color[3:5]
        b = self.color[5:]
        r = int(r, 16); g = int(g, 16); b = int(b, 16)
        r -= 0.03 * t; g += 0.02 * t; b += 0.05 * t
        r = max(0, min(r, 255)) # CLAMP: ChatGPT
        g = max(0, min(g, 255))
        b = max(0, min(b, 255))
        r  = hex(int(r)); g = hex(int(g)); b = hex(int(b));
        r = r.replace("0x", "").zfill(2) # ZFILL: ChatGPT
        g = g.replace("0x", "").zfill(2)
        b = b.replace("0x", "").zfill(2)
        self.color = "#" + "".join([r, g, b])

class LevelObject:
    def __init__(self, image, indexInRects: GridSquare):
        self.image = image
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect(center=(indexInRects.x - 30, indexInRects.y - 30))

# Grid
Rects = []
for i in range(10):
    for j in range(10):
        Rects.append(GridSquare(i, j))

# Trees
TreePoses = []
for i in range(random.randint(1, 20)):
    TreePoses.append(LevelObject(pygame.image.load("Tree.png"), Rects[random.randint(0, 99)]))

# Cats
CatPoses = []
for i in range(random.randint(1, 20)):
    CatPoses.append(LevelObject(pygame.image.load("Cat.png"), Rects[random.randint(0, 99)]))

# Flowers
FlowerPoses = []
for i in range(random.randint(1, 20)):
    FlowerPoses.append(LevelObject(pygame.image.load("Flower.png"), Rects[random.randint(0, 99)]))

# Dinos
DinoPoses = []
for i in range(random.randint(1, 20)):
    DinoPoses.append(LevelObject(pygame.image.load("Dino.png"), Rects[random.randint(0, 99)]))

# Cars
CarPoses = []
for i in range(random.randint(1, 20)):
    CarPoses.append(LevelObject(pygame.image.load("Car.png"), Rects[random.randint(0, 99)]))

# Treasure
Treasure = GridSquare(
    random.randint(0, 9),
    random.randint(0, 9)
                      )
TreasImg = pygame.transform.scale(pygame.image.load("download.png"), (100, 100))
TreasImgRect = TreasImg.get_rect(center=(540, 60))
ShowImg = False

# Player Instance
Me = GridSquare(5, 5, "#0000FF")
Level = 0

# Player Image
Player = pygame.image.load("Girl.png")
GirlImgRect = Player.get_rect(center=(Me.rect.x - 30, Me.rect.y - 30))

# Font
F1 = pygame.font.Font("KgHappy-wWZZ.ttf", 40)
RectOfTextPlacement = pygame.Rect((370, 520), (200, 60))

def Blit(level):
    global TreePoses, CarPoses, CatPoses, DinoPoses, FlowerPoses, screen
    rem = level % 5
    if rem ==  0:
        for Tree in TreePoses:
            screen.blit(Tree.image, Tree.rect)
    elif rem ==  1:
        for Cat in CatPoses:
            screen.blit(Cat.image, Cat.rect)
    elif rem ==  2:
        for Flower in FlowerPoses:
            screen.blit(Flower.image, Flower.rect)
    elif rem ==  3:
        for Dino in DinoPoses:
            screen.blit(Dino.image, Dino.rect)
    elif rem ==  4:
        for Car in CarPoses:
            screen.blit(Car.image, Car.rect)

prevdist = Me.findDistance(Treasure)
while running:
    print(Me.color)
    GirlImgRect = Player.get_rect(center=(Me.rect.x, Me.rect.y))

    # Level Text
    T1 = F1.render(f"Level: {Level}", True, "#341539")

    # Draw Player and Grid
    screen.fill("white")
    for i in Rects:
        pygame.draw.rect(screen, i.color, i.rect, width=1)
    pygame.draw.rect(screen, Me.color, Me.rect)

    # Text Blitting
    rectOfTextBG = pygame.Rect((360, 520), (215, 60)) # Main RECT
    rectOfTextPrettyBorder = pygame.Rect((354, 514.75), (227, 73)) # Border RECT
    pygame.draw.rect(screen, "Black", rectOfTextPrettyBorder, width=7,
                     border_radius=0) # Border
    pygame.draw.rect(screen, "White", rectOfTextBG,
                     border_radius=0) # Background
    screen.blit(T1, RectOfTextPlacement)
    GirlImgRect2 = GirlImgRect.copy()
    GirlImgRect2.width += 5
    GirlImgRect2.height += 5
    GirlImgRect2.x -= 2.35
    GirlImgRect2.y -= 2.35
    pygame.draw.rect(screen, "black", GirlImgRect2,
                width=4)
    screen.blit(Player, GirlImgRect)

    Blit(Level)

    # Event Detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # QUIT
            running = False
        if event.type == pygame.KEYDOWN: # KEYDOWN: ChatGPT
            if pygame.key.get_pressed()[pygame.K_w] and Me.rect.top > screen.get_rect().top:
                Me = GridSquare(int(Me.x) // 60, (int(Me.y) // 60) - 1, "#3d426b")
            if pygame.key.get_pressed()[pygame.K_a] and Me.rect.left > screen.get_rect().left:
                Me = GridSquare((int(Me.x) // 60) - 1, int(Me.y) // 60, "#3d426b")
            if pygame.key.get_pressed()[pygame.K_d] and Me.rect.right < screen.get_rect().right:
                Me = GridSquare((int(Me.x) // 60) + 1, int(Me.y) // 60, "#3d426b")
            if pygame.key.get_pressed()[pygame.K_s] and Me.rect.bottom < screen.get_rect().bottom:
                Me = GridSquare(int(Me.x) // 60, (int(Me.y) // 60) + 1, "#3d426b")


    new_dist = Me.findDistance(Treasure)
    # Treasure Detection
    if Me.rect.x == Treasure.rect.x and Me.rect.y == Treasure.rect.y:
        pygame.mixer.Sound("success-221935.mp3").play()
        screen.blit(TreasImg, TreasImgRect)
        pygame.display.update()

        pygame.time.wait(3000)
        Treasure = GridSquare(
            random.randint(0, 9),
            random.randint(0, 9)
        )
        Level += 1
        # Trees
        TreePoses = []
        for i in range(random.randint(1, 20)):
            TreePoses.append(LevelObject(pygame.image.load("Tree.png"), Rects[random.randint(0, 99)]))

        # Cats
        CatPoses = []
        for i in range(random.randint(1, 20)):
            CatPoses.append(LevelObject(pygame.image.load("Cat.png"), Rects[random.randint(0, 99)]))

        # Flowers
        FlowerPoses = []
        for i in range(random.randint(1, 20)):
            FlowerPoses.append(LevelObject(pygame.image.load("Flower.png"), Rects[random.randint(0, 99)]))

        # Dinos
        DinoPoses = []
        for i in range(random.randint(1, 20)):
            DinoPoses.append(LevelObject(pygame.image.load("Dino.png"), Rects[random.randint(0, 99)]))

        # Cars
        CarPoses = []
        for i in range(random.randint(1, 20)):
            CarPoses.append(LevelObject(pygame.image.load("Car.png"), Rects[random.randint(0, 99)]))


    # Color Shifting
    else:
        if prevdist > new_dist:
            Me.shift_warm(prevdist - new_dist)
        elif prevdist < new_dist:
            Me.shift_cold(new_dist - prevdist)


    Clock.tick(100)
    pygame.display.update()

