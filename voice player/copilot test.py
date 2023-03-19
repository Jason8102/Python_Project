#create an audio player using pygame in gui
#this is a simple audio player that can play mp3, wav, ogg, and midi files

import pygame
import sys
import os
import time
import random
import pygame.midi
import pygame.mixer
import pygame.time
import pygame.event
import pygame.display
import pygame.draw
import pygame.font
import pygame.image
import pygame.transform

#initialize pygame
pygame.init()
pygame.midi.init()
pygame.mixer.init()

#set up the window
window = pygame.display.set_mode((800 , 400))
pygame.display.set_caption("Audio Player")

#set up the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
PURPLE = (128, 0, 128)
CYAN = (0, 255, 255)
PINK = (255, 192, 203)  

#set up the fonts
basicFont = pygame.font.SysFont(None, 48)

#set up the text
text = basicFont.render('Audio Player', True, WHITE, BLACK)
textRect = text.get_rect()
textRect.centerx = window.get_rect().centerx
textRect.centery = window.get_rect().centery

#set up the buttons
playButton = pygame.Rect(100, 100, 100, 50)
pauseButton = pygame.Rect(250, 100, 100, 50)
stopButton = pygame.Rect(400, 100, 100, 50)
nextButton = pygame.Rect(550, 100, 100, 50)
previousButton = pygame.Rect(700, 100, 100, 50)

#set up the button text
playButtonText = basicFont.render('Play', True, WHITE, BLACK)
playButtonTextRect = playButtonText.get_rect()
playButtonTextRect.centerx = playButton.centerx
playButtonTextRect.centery = playButton.centery

pauseButtonText = basicFont.render('Pause', True, WHITE, BLACK)
pauseButtonTextRect = pauseButtonText.get_rect()
pauseButtonTextRect.centerx = pauseButton.centerx
pauseButtonTextRect.centery = pauseButton.centery

stopButtonText = basicFont.render('Stop', True, WHITE, BLACK)
stopButtonTextRect = stopButtonText.get_rect()
stopButtonTextRect.centerx = stopButton.centerx
stopButtonTextRect.centery = stopButton.centery

nextButtonText = basicFont.render('Next', True, WHITE, BLACK)
nextButtonTextRect = nextButtonText.get_rect()
nextButtonTextRect.centerx = nextButton.centerx
nextButtonTextRect.centery = nextButton.centery

previousButtonText = basicFont.render('Previous', True, WHITE, BLACK)
previousButtonTextRect = previousButtonText.get_rect()
previousButtonTextRect.centerx = previousButton.centerx
previousButtonTextRect.centery = previousButton.centery

#set up the music
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1, 0.0)

#set up the clock
clock = pygame.time.Clock()

#set up the main loop
while True:
    #check for the QUIT event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #check for mouse clicks
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #check if the play button was clicked
            if playButton.collidepoint(event.pos):
                pygame.mixer.music.unpause()
            #check if the pause button was clicked
            elif pauseButton.collidepoint(event.pos):
                pygame.mixer.music.pause()
            #check if the stop button was clicked
            elif stopButton.collidepoint(event.pos):
                pygame.mixer.music.stop()
            #check if the next button was clicked
            elif nextButton.collidepoint(event.pos):
                pygame.mixer.music.load('music2.mp3')
                pygame.mixer.music.play(-1, 0.0)
            #check if the previous button was clicked
            elif previousButton.collidepoint(event.pos):
                pygame.mixer.music.load('music.mp3')
                pygame.mixer.music.play(-1, 0.0)
    #draw the white background onto the surface
    window.fill(WHITE)
    #draw the text onto the surface
    window.blit(text, textRect)
    #draw the buttons onto the surface
    pygame.draw.rect(window, BLACK, playButton)
    pygame.draw.rect(window, BLACK, pauseButton)
    pygame.draw.rect(window, BLACK, stopButton)
    pygame.draw.rect(window, BLACK, nextButton)
    pygame.draw.rect(window, BLACK, previousButton)
    #draw the button text onto the surface
    window.blit(playButtonText, playButtonTextRect)
    window.blit(pauseButtonText, pauseButtonTextRect)
    window.blit(stopButtonText, stopButtonTextRect)
    window.blit(nextButtonText, nextButtonTextRect)
    window.blit(previousButtonText, previousButtonTextRect)
    #draw the window onto the screen
    pygame.display.update()
    #set the framerate
    clock.tick(60)






















