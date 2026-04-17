import pygame

pygame.init()
pygame.mixer.init()

done = False
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()
my_font = pygame.font.SysFont(None, 36)

current_track = 0
musics = ["music/music1.mp3", "music/music2.mp3"]
names = ["QMIRR - Tiki Tiki","Lil Peep - Nuts"]

track_lengths = []
for music in musics:
    sound = pygame.mixer.Sound(music)
    track_lengths.append(sound.get_length())


def play_track(index):
    pygame.mixer.music.load(musics[index])
    pygame.mixer.music.play()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_track(current_track)
                print("Playing!")

            elif event.key == pygame.K_s:
                pygame.mixer.music.pause()
                print("Paused!")

            elif event.key == pygame.K_n:
                current_track = (current_track + 1) % len(musics)
                play_track(current_track)
                print("Next!")

            elif event.key == pygame.K_b:
                current_track = (current_track - 1) % len(musics)
                play_track(current_track)
                print("Previous!")

            elif event.key == pygame.K_q:
                done = True

    pos_ms = pygame.mixer.music.get_pos()
    pos_sec = pos_ms / 1000 if pos_ms != -1 else 0
    total_sec = track_lengths[current_track]

    cur = my_font.render(f"Current Track: {names[current_track]}", True, (0, 0, 0))
    time_text = my_font.render(
        f"Time: {int(pos_sec)}s / {int(total_sec)}s", True, (0, 0, 0)
    )

    screen.fill((255, 255, 255))
    screen.blit(cur, (10, 30))
    screen.blit(time_text, (10, 70))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()