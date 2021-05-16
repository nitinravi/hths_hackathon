from threading import Thread
import pygame

from app import q, get_current_note

pygame.init()

screenWidth, screenHeight = 288, 512
screen = pygame.display.set_mode((screenWidth, screenHeight))
clock = pygame.time.Clock()

running = True

titleFont = pygame.font.Font("assets/Roboto-Medium.ttf", 34)
titleText = titleFont.render("Sing a", True, (0, 128, 0))
titleCurr = titleFont.render("Low Note", True, (0, 128, 0))

noteFont = pygame.font.Font("assets/Roboto-Medium.ttf", 55)

t = Thread(target=get_current_note)
t.daemon = True
t.start()


low_note = ""
high_note = ""
have_low = False
have_high = True

noteHoldLength = 20  # how many samples in a row user needs to hold a note
noteHeldCurrently = 0  # keep track of how long current note is held
noteHeld = ""  # string of the current note

centTolerance = 20  # how much deviance from proper note to tolerate

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            running = False

    screen.fill((0, 0, 0))

    # our user should be singing if there's a note on the queue
    if not q.empty():
        b = q.get()
        if b['Cents'] < 15:
            pygame.draw.circle(screen, (0, 128, 0), 
                               (screenWidth // 2 + (int(b['Cents']) * 2),300),
                               5)
        else:
            pygame.draw.circle(screen, (128, 0, 0),
                               (screenWidth // 2 + (int(b['Cents']) * 2), 300),
                               5)

        noteText = noteFont.render(b['Note'], True, (0, 128, 0))
    screen.blit(titleText, (10,  80))
    screen.blit(titleCurr, (10, 120))
    pygame.display.flip()
    clock.tick(30)
