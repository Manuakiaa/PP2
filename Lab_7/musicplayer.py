import pygame
import os

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption("My Music Player")

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)

font = pygame.font.Font(None, 36)

music_folder = "music"
music_files = []

if os.path.exists(music_folder):
    for file in os.listdir(music_folder):
        if file.endswith('.mp3'):
            music_files.append(os.path.join(music_folder, file))
else:
    for file in os.listdir('.'):
        if file.endswith('.mp3'):
            music_files.append(file)

if not music_files:
    music_files = ["no music found"]

current_song = 0
is_playing = False

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                if music_files and music_files[0] != "no music found":
                    try:
                        pygame.mixer.music.load(music_files[current_song])
                        pygame.mixer.music.play()
                        is_playing = True
                    except:
                        print("Cannot play music")
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                is_playing = False
            elif event.key == pygame.K_n:
                if music_files and music_files[0] != "no music found":
                    current_song = (current_song + 1) % len(music_files)
                    if is_playing:
                        pygame.mixer.music.load(music_files[current_song])
                        pygame.mixer.music.play()
            elif event.key == pygame.K_b:
                if music_files and music_files[0] != "no music found":
                    current_song = (current_song - 1) % len(music_files)
                    if is_playing:
                        pygame.mixer.music.load(music_files[current_song])
                        pygame.mixer.music.play()
    
    screen.fill(white)
    
    song_name = music_files[current_song]
    if music_files[0] != "no music found":
        song_name = os.path.basename(song_name)
    
    song_text = font.render(f"Song: {song_name}", True, black)
    screen.blit(song_text, (50, 50))
    
    status = "PLAYING" if is_playing else "STOPPED"
    status_text = font.render(f"Status: {status}", True, blue)
    screen.blit(status_text, (50, 100))
    
    controls_text = font.render("P=Play  S=Stop  N=Next  B=Back", True, black)
    screen.blit(controls_text, (50, 150))
    
    pygame.display.update()
    clock.tick(30)

pygame.quit()