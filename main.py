ver = "B.0.7.0"
if ver[0] == "D":
    blockSettings.write_string("lev", "8")

sleep_counter = 5
cidk = textsprite.create("Version: " + ver)
cidk.x = 80
cidk.y = 115
pause(1)
music.play(music.create_song(assets.song("""title""")), music.PlaybackMode.LOOPING_IN_BACKGROUND)
lastu = int(blockSettings.read_string("lev"))

if not lastu and lastu != 0:
    lastu = 0
    nivel = -1
    dif = "temp"

# Times per level
times_easy   = [30, 35, 30, 125, 45]
times_normal = [24, 30, 26, 120, 40]
times_hard   = [13, 19, 19, 115, 35]

def sq(n: number) -> number:
    guess = n / 2
    for i in range(10):
        guess = (guess + n / guess) / 2
    return guess

def lenls(iterable: List[string] = None):
    c = 0
    for _ in iterable:
        c+=1
    return c

def menudo(menu_type, options: List[string], unlocked: List[number], size=None):
    while controller.A.is_pressed():
        pause(1)
    if menu_type == "archipelago":
        if not size:
            square = sq(lenls(options))
            if int(str(square)) != square:
                return "Error"
            size = [square,square]
        dummy = sprites.create(img("."), SpriteKind.projectile)
        islands = [dummy]
        islands.remove_at(0)  # quitas el dummy
        nums = [dummy]
        nums.remove_at(0)  # quitas el dummy
        op = 0
        for y in range(size[1]):
            for x in range(size[0]):
                buff = sprites.create(assets.image("island_no") if unlocked[(y*size[1])+x] else assets.image("island_no0"), SpriteKind.projectile)
                buff.x = (x*30) + 160-((lenls(options)*30)/2.5)
                buff.y = (y*30) + 120-((lenls(options)*30)/3)
                tb = textsprite.create(str(options[op]))
                tb.x = buff.x
                tb.y = buff.y
                islands.append(buff)
                nums.append(tb)
                op += 1
        sel = 0
        ant = 1
        bef = ""
        while True:
            pause(1)
            if unlocked[ant] == 1:
                islands[ant].set_image(assets.image("island_no"))
            else:
                islands[ant].set_image(assets.image("island_no0"))

            islands[sel].set_image(assets.image("island_se"))
            if unlocked[sel] == 0:
                bsel = sel
                sel = ant
                ant = bsel
                #pass
            if controller.right.is_pressed() and bef != "R":
                bef = "R"
                ant = sel if sel != lenls(options)-1 else ant
                sel += 1 if sel != lenls(options)-1 else 0
            if not controller.right.is_pressed() and bef == "R":
                bef = ""
            if controller.left.is_pressed() and bef != "L":
                bef = "L"
                ant = sel if sel != 0 else ant
                sel -= 1 if sel != 0 else 0
            if not controller.left.is_pressed() and bef == "L":
                bef = ""
            if controller.down.is_pressed() and bef != "D":
                bef = "D"
                ant = sel if sel < lenls(options)-square else ant
                sel += square if sel < lenls(options)-square else 0
            if not controller.down.is_pressed() and bef == "D":
                bef = ""
            if controller.up.is_pressed() and bef != "U":
                bef = "U"
                ant = sel if sel >= square else ant
                sel -= square if sel >= square else 0
            if not controller.up.is_pressed() and bef == "U":
                bef = ""
            if controller.A.is_pressed():
                for spr in islands:
                    sprites.destroy(spr)
                for sprd in nums:
                    sprites.destroy(sprd)
                return str(options[sel])
    if menu_type == "list":
        if not size:
            square = lenls(options)
        dummy = sprites.create(img("."), SpriteKind.projectile)
        islands = [dummy]
        islands.remove_at(0)  # quitas el dummy
        nums = [dummy]
        nums.remove_at(0)  # quitas el dummy
        op = 0
        for y in range(size[1]):
            for x in range(size[0]):
                buff = sprites.create(assets.image("rect_no"), SpriteKind.projectile)
                buff.x = (x*30) + 160-((lenls(options)*30)/1.125)
                buff.y = (y*30) + 120-((lenls(options)*30)/1)
                tb = textsprite.create(options[op])
                tb.x = buff.x
                tb.y = buff.y
                islands.append(buff)
                nums.append(tb)
                op += 1
        sel = 0
        ant = 1
        bef = ""
        while True:
            pause(1)
            islands[ant].set_image(assets.image("rect_no"))
            islands[sel].set_image(assets.image("rect_se"))
            if controller.right.is_pressed() and bef != "R":
                bef = "R"
                ant = sel if sel != lenls(options)-1 else ant
                sel += 1 if sel != lenls(options)-1 else 0
            if not controller.right.is_pressed() and bef == "R":
                bef = ""
            if controller.left.is_pressed() and bef != "L":
                bef = "L"
                ant = sel if sel != 0 else ant
                sel -= 1 if sel != 0 else 0
            if not controller.left.is_pressed() and bef == "L":
                bef = ""
            if controller.down.is_pressed() and bef != "D":
                bef = "D"
                ant = sel if sel < lenls(options)-square else ant
                sel += square if sel < lenls(options)-square else 0
            if not controller.down.is_pressed() and bef == "D":
                bef = ""
            if controller.up.is_pressed() and bef != "U":
                bef = "U"
                ant = sel if sel >= square else ant
                sel -= square if sel >= square else 0
            if not controller.up.is_pressed() and bef == "U":
                bef = ""
            if controller.A.is_pressed():
                for sprt in islands:
                    sprites.destroy(sprt)
                for sprf in nums:
                    sprites.destroy(sprf)
                return str(options[sel])
    return "Error"

dif = None
if nivel != -1:
    dif = menudo("list", ["Normal", "Facil", "Dificil"],[1,1,1],[1,3])
while not dif and nivel != -1:
    pause(1)
#pause(1000)
unlk: List[number] = []
for lev in range(0,9):
    unlk.append(1 if lev<=lastu else 0)
if nivel != -1:
    nivel = int(menudo("archipelago", ["1","2","3","4","5","6","7","8","9"], unlk))


while not dif and nivel != -1:
    dif = story.get_last_answer()

if nivel != -1:
  if dif == "Normal":
    times = times_normal
    turn = 100
  elif dif == "Facil":
    times = times_easy
    turn = 1000
  elif dif == "Dificil":
    times = times_hard
    turn = 50
  elif dif == "temp":
    times = [50]
    turn = 1000

fiches: List[Sprite] = []
def itws(sprite: Sprite, k: number) -> bool:
    global fiches
    # Get sprite position in tile coordinates
    col = sprite.x // 16
    row = sprite.y // 16

    # Check left tile
    left_tile = tiles.get_tile_location(col - 1, row)
    if (k==0 and tiles.tile_at_location_equals(left_tile, assets.tile("ce"))) or (k==1 and tiles.tile_at_location_equals(left_tile, assets.tile("st"))):    return True

    # Check right tile
    right_tile = tiles.get_tile_location(col + 1, row)
    if (k==0 and tiles.tile_at_location_equals(right_tile, assets.tile("ce"))) or (k==1 and tiles.tile_at_location_equals(right_tile, assets.tile("st"))):        return True
    lf = -1
    up_p = tiles.get_tile_location(playersprite.x // 16, (playersprite.y // 16) -1)
    if tiles.tile_at_location_equals(up_p, assets.tile("fish_a")):
        lf += 1
        print(lf)
        print(up_p)
        print("airesitus")
        tiles.set_tile_at(up_p, assets.tile("""fish_b"""))
        fiches.append(sprites.create(assets.image("""fish"""),SpriteKind.food))
        tiles.place_on_tile(fiches[lf], up_p)
        fiches[lf].y -= 16



    return False

music.stop_all_sounds()
fen = [-1]
# Load tilemap
if nivel == 1:
    tiles.set_current_tilemap(tilemap("""
        nivel1
    """))
    ls = 13  # coins/lives
    

    psm = [30]
    music.play(music.create_song(assets.song("""back1""")),music.PlaybackMode.LOOPING_IN_BACKGROUND)
elif nivel == 2:
    tiles.set_current_tilemap(tilemap("""
        nivel2
    """))
    ls = 13  # coins/lives
    rc = 25  # timer
    psm = [30]
    music.play(music.create_song(assets.song("""back2""")),music.PlaybackMode.LOOPING_IN_BACKGROUND)

elif nivel == 3:
    tiles.set_current_tilemap(tilemap("""
        nivel0
    """))
    ls = 6  # coins/lives
    rc = 24  # timer
    music.play(music.create_song(assets.song("""back3""")),music.PlaybackMode.LOOPING_IN_BACKGROUND)


elif nivel == 4:
    tiles.set_current_tilemap(tilemap("""
        nivel10
    """)) # 6
    ls = 5  # coins/lives 2
    rc = 40  # timer 15
    psm = [-50,-50,-50,-50,-50,-50,-50,-50]
    fen = [1,2]
    music.play(music.create_song(assets.song("""back4""")),music.PlaybackMode.LOOPING_IN_BACKGROUND)

elif nivel == 5:
    tiles.set_current_tilemap(tilemap("""nivel8"""))
    ls = 3
    psm = [-30, 50, 70, 90, 110, 30, 150, 170,100,300,500]
    rc = 40
    music.play(music.create_song(assets.song("""back5""")),music.PlaybackMode.LOOPING_IN_BACKGROUND)

elif nivel == 6:
    tiles.set_current_tilemap(tilemap("""nivel13"""))
    ls = 4
    rc = 9999
    music.play(music.create_song(assets.song("""back6""")),music.PlaybackMode.LOOPING_IN_BACKGROUND)

elif nivel == 9:
    tiles.set_current_tilemap(tilemap("""
        test
    """))
    ls = 3  # coins/lives
    rc = 9999  # timer
    psm = [30, 40, 50, 60]

elif nivel == -1:
    tiles.set_current_tilemap(tilemap("""tutorial"""))
    ls = 1
    rc = 50
    psm=[20]
    music.play(music.create_song(assets.song("""backTutorial""")),music.PlaybackMode.LOOPING_IN_BACKGROUND)

else:
    game.splash("Nivel no válido")
    game.reset()
rc = times[nivel-1] if nivel != -1 else 50
pause(1)

# UI
timercount = textsprite.create(str(rc))
patatacount = textsprite.create(str(ls))
timercount.set_outline(1, 6)
patatacount.set_outline(1, 6)

# Game state
rscoins_ins: List[Sprite] = []
enmyss_ins: List[Sprite] = []
enmyssg1_ins: List[Sprite] = []
fwrs: List[Sprite] = []
    



        
isj = False  # is jumping

def load1():
    ins_tile = assets.tile("""
        ins
    """)
    if nivel == -1 or nivel == 1 or nivel == 3 or nivel == 5:
        sb_tile = assets.tile("sb")
    else:
        sb_tile = assets.tile("sb0")

    floor_tile1 = assets.tile("""
        ce
    """)
    floor_tile2 = assets.tile("""
        flbasic
    """)
    enmy_tile1 = assets.tile("""e1""")
    enmy_tile2 = assets.tile("""e2""")

    # Place coins
    ins_locations = tiles.get_tiles_by_type(ins_tile)
    enmy1_locations = tiles.get_tiles_by_type(enmy_tile1)
    enmy2_locations = tiles.get_tiles_by_type(enmy_tile2)
    for loc1 in ins_locations:
        tiles.set_tile_at(loc1, sb_tile)
        coin = sprites.create(assets.image("rscoin"), SpriteKind.food)
        rscoins_ins.append(coin)
        tiles.place_on_tile(coin, loc1)
        pause(1)

    for loc2 in enmy1_locations:
        tiles.set_tile_at(loc2, sb_tile)
        enmyns = sprites.create(assets.image("se1"), SpriteKind.enemy)
        enmyns.ay = 30
        enmyss_ins.append(enmyns)
        tiles.place_on_tile(enmyns, loc2)
        fwrb = sprites.create(assets.image("fwr"), SpriteKind.projectile)
        fwrb.follow(enmyns,1000,turn)
        fwrb.set_stay_in_screen(True)
        fwrb.setFlag(SpriteFlag.Ghost, True)
        fwrs.append(fwrb)
        pause(1)

    for loc3 in enmy2_locations:
        tiles.set_tile_at(loc3, sb_tile)
        enmyns = sprites.create(assets.image("proy0"), SpriteKind.projectile)
        enmyssg1_ins.append(enmyns)
        tiles.place_on_tile(enmyns, loc3)
        pause(1)
    
    


load1()

# Create player
playersprite = sprites.create(assets.image("player_right"), SpriteKind.player)
playersprite.set_velocity(0, 0)
playersprite.ay = 300  # gravity
scene.camera_follow_sprite(playersprite)
sprites.destroy(cidk)

# Update UI with camera
def update_ui():
    while True:
        timercount.set_position(scene.camera_property(CameraProperty.X) - 68,
                                scene.camera_property(CameraProperty.Y) - 50)
        patatacount.set_position(scene.camera_property(CameraProperty.X) + 68,
                                 scene.camera_property(CameraProperty.Y) - 50)
        pause(120)
timer.background(update_ui)

# Movement and win logic
def controller_loop():
    global sleep_counter
    while True:
        playersprite.set_image(assets.image("""player_right""") if playersprite.vx > 0 else assets.image("""player_left""")) if playersprite.vx != 0 else None
        if controller.dx() or controller.A.is_pressed():
            if sleep_counter < 1:
                playersprite.x -= 1
                if playersprite.vx == 0:
                    playersprite.set_image(assets.image("""player_right"""))
            sleep_counter = 5
        playersprite.vx = controller.dx(3750 if controller.B.is_pressed() else 2200)
        pause(10)
timer.background(controller_loop)

# Countdown timer
def countdown():
    global rc, sleep_counter
    while True:
        pause(1000)
        rc -= 1
        timercount.set_text(str(rc))
        if rc < 0 and ls > 0:
            music.stop_all_sounds()
            music.play(music.create_song(assets.song("""lose""")),music.PlaybackMode.IN_BACKGROUND)
            game.splash("Has perdido")
            music.stop_all_sounds()
            game.reset()

        sleep_counter -= 1
        if sleep_counter == 0:
            playersprite.set_image(assets.image("""player_sleep"""))
            playersprite.y += 1
            playersprite.x += 1

timer.background(countdown)

def enmydel():
    ps = psm
    if ps == None:
        return
    xs = [0]
    while True:
        ce = 0
        pause(2000)
        for ei in enmyss_ins:
            ei.vx = ps[ce]
            if xs[ce] == ei.x:
                ei.vy = -30
            xs[ce] = ei.vy
            
            if itws(ei, 0):
                ps[ce] = -ps[ce]
                ei.vy = -30
            if Math.percent_chance(25) and ei.is_hitting_tile(CollisionDirection.BOTTOM):
                ei.vy = -30
                
def enmydel2():
    prs: List[Sprite] = []
    while True:
        pause(1000)
        sc = int(str(int(game.runtime())/1000))
        cgn = 0
        for gn in enmyssg1_ins:
            #print(gn.x)
            if (sc % 2 == 0) == (int(str((gn.x-5)/16)) % 2 == 0):
                sprites.destroy(prs[cgn])
                prs[cgn] = sprites.create(assets.image("""proy"""), SpriteKind.enemy)
                prs[cgn].ay = 100
                prs[cgn].x = gn.x
                prs[cgn].y = gn.y

            cgn += 1

timer.background(enmydel)
timer.background(enmydel2)

# Collect coins
def collect_coins():
    global ls
    while True:
        if ls == 0:
            if lastu < nivel or nivel == -1:
                blockSettings.write_string("lev", str(nivel) if nivel != -1 else "0")
            music.stop_all_sounds()
            music.play(music.create_song(assets.song("""win""")),music.PlaybackMode.IN_BACKGROUND)
            game.splash("Has ganao")
            music.stop_all_sounds()
            game.reset()
        for c in rscoins_ins:
            if playersprite.overlaps_with(c):
                sprites.destroy(c)
                rscoins_ins.remove_at(rscoins_ins.index_of(c))
                ls -= 1
                patatacount.set_text(str(ls))
                music.play(music.create_sound_effect(WaveShape.NOISE,
                                                     1038, 1286, 255, 0, 500,
                                                     SoundExpressionEffect.VIBRATO,
                                                     InterpolationCurve.LOGARITHMIC),
                           music.PlaybackMode.IN_BACKGROUND)
        pause(20)
timer.background(collect_coins)
def on_overlap(sprite, otherSprite):
    music.stop_all_sounds()
    music.play(music.create_song(assets.song("""lose""")),music.PlaybackMode.IN_BACKGROUND)
    game.splash("Has perdido")
    music.stop_all_sounds()
    game.reset()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_overlap)
# Check if on ground using tile collision
def check_ground():
    global isj
    while True:
        isj = playersprite.is_hitting_tile(CollisionDirection.BOTTOM) or itws(playersprite, 1)
        pause(10)
        if isj == False:
            p = playersprite.x
            while playersprite.x == p and not playersprite.is_hitting_tile(CollisionDirection.BOTTOM):
                pause(1)
                
            isj = True

timer.background(check_ground)

# Jump logic using gravity
def jump_loop():
    global isj
    while True:
        if controller.A.is_pressed() and isj:
            isj = False
            music.play(music.create_sound_effect(WaveShape.SINE,
                                                 500, 600, 255, 0, 500,
                                                 SoundExpressionEffect.NONE,
                                                 InterpolationCurve.LINEAR),
                       music.PlaybackMode.IN_BACKGROUND)
            playersprite.vy = -175 if controller.B.is_pressed() else -150
        pause(1)
timer.background(jump_loop)
