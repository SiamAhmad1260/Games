import raylib as rl 

rl.InitWindow(1080, 720, b'sonic')
CENTER_X = 1080//2
CENTER_Y = 720//2
PLAYER_POSITION_X = CENTER_X
PLAYER_POSITION_Y = CENTER_Y
PLAYER_VELOCITY_PER_SECOND = 50
PLAYER_TEXTURE = rl.LoadTexture(b'assets/ball/1.png')

while True:
    rl.SetTargetFPS(60)
    rl.BeginDrawing()
    rl.ClearBackground((50, 50, 50))
    
    #draw begins
    rl.DrawLine(1080//2, 720//2, PLAYER_POSITION_X, PLAYER_POSITION_Y, rl.RED)
    rl.DrawTextureEx(PLAYER_TEXTURE, ( PLAYER_POSITION_X-54//2, PLAYER_POSITION_Y-60//2), 0, 1, (255,255,255,255), )

    #control statement
    if rl.IsKeyDown(rl.KEY_RIGHT):
        PLAYER_POSITION_X += PLAYER_VELOCITY_PER_SECOND
    if rl.IsKeyDown(rl.KEY_LEFT):
        PLAYER_POSITION_X -= PLAYER_VELOCITY_PER_SECOND
    if rl.IsKeyDown(rl.KEY_UP):
        PLAYER_POSITION_Y -= PLAYER_VELOCITY_PER_SECOND
    if rl.IsKeyDown(rl.KEY_DOWN):
        PLAYER_POSITION_Y += PLAYER_VELOCITY_PER_SECOND
                
    if rl.IsKeyPressed(rl.KEY_ESCAPE):
        rl.CloseWindow()       
    
    #draw end
    rl.EndDrawing()
