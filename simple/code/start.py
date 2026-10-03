import raylib as rl 

rl.InitWindow(1080, 720, b'sonic')
rl.SetTargetFPS(60)

CENTER_X = 1080//2
CENTER_Y = 720//2
PLAYER_POSITION_X = CENTER_X
PLAYER_POSITION_Y = CENTER_Y
PLAYER_VELOCITY = 50

PLAYER_TEXTURE = rl.LoadTexture(b'1.png')
Player = rl.LoadTexture(b'move.png')

frame_nums = 6
current_frame = 0
frame_time_counter = 0

frame_start = 0
frame_end = 

source_rect = (0.0, 0.0, float(Player.width)/frame_nums, float(Player.height))
dest_rect = (300, 400, float(Player.width/frame_nums)*3, float(Player.height)*3)

origin = (0,0)

while not rl.WindowShouldClose():

    rl.BeginDrawing()
    rl.ClearBackground((50, 50, 50))
    
    #draw begins
    rl.DrawLine(1080//2, 720//2, PLAYER_POSITION_X, PLAYER_POSITION_Y, rl.RED)
    rl.DrawTextureEx(PLAYER_TEXTURE, ( PLAYER_POSITION_X-54//2, PLAYER_POSITION_Y-60//2), 0, 1, (255,255,255,255) )
    rl.DrawTexturePro(Player, source_rect, dest_rect, origin, 0, (255,255,255,255))
    
    #control statement
    if rl.IsKeyDown(rl.KEY_RIGHT):
        PLAYER_POSITION_X += PLAYER_VELOCITY
    if rl.IsKeyDown(rl.KEY_LEFT):
        PLAYER_POSITION_X -= PLAYER_VELOCITY
    if rl.IsKeyDown(rl.KEY_UP):
        PLAYER_POSITION_Y -= PLAYER_VELOCITY
    if rl.IsKeyDown(rl.KEY_DOWN):
        PLAYER_POSITION_Y += PLAYER_VELOCITY
                
    if rl.IsKeyPressed(rl.KEY_ESCAPE):
        rl.UnloadTexture(Player)
        rl.CloseWindow()       
    
    #draw end
    rl.EndDrawing()
rl.CloseWindow()
