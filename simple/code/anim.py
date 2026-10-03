from raylib import *

current_frame = 0
frame_counter = 0
frame_speed = 12

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 720

InitWindow(SCREEN_WIDTH, SCREEN_HEIGHT, b'animation')

SetTargetFPS(60)

anim = LoadTexture(b'move.png')
frame_num = 6
frame_rec = [0, 0, anim.width/frame_num, anim.height]

position = [350, 280]
velocity = 10

while not WindowShouldClose():
    frame_counter += 1
    
    if frame_counter >= 60/frame_speed:
        frame_counter = 0
        current_frame += 1
        if current_frame > 5:
            current_frame = 0
        
        frame_rec[0] = float(current_frame)*float(anim.width/frame_num)
    if (IsKeyDown(KEY_RIGHT)):
        position[0] += velocity
    if (IsKeyDown(KEY_LEFT)):
        position[0] -= velocity

    BeginDrawing()
    ClearBackground((70,70,70))

    DrawTextureRec(anim, frame_rec, position, WHITE)

    EndDrawing()