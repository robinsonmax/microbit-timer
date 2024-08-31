def on_gesture_shake():
    reset()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def reset():
    global trigger, timer, isTriggered
    trigger = 5
    timer = 0
    music.stop_melody(MelodyStopOptions.ALL)
    isTriggered = False
ring_time = 0
isTriggered = False
timer = 0
trigger = 0
reset()

def on_every_interval():
    global timer, ring_time
    timer += 1
    ring_time += 1
    if isTriggered:
        music.set_volume(max(127 + ring_time * 10, 255))
        basic.show_leds("""
            . . # . .
            . . # . .
            . . # . .
            . . . . .
            . . # . .
            """)
    else:
        if timer % 2 == 0:
            basic.show_leds("""
                . . . . .
                . . # . .
                . # . # .
                . . # . .
                . . . . .
                """)
        else:
            basic.show_leds("""
                . . . . .
                . . . . .
                . . # . .
                . . . . .
                . . . . .
                """)
loops.every_interval(1000, on_every_interval)

def on_forever():
    global ring_time, isTriggered
    if trigger == timer:
        ring_time = 0
        isTriggered = True
        music.play(music.string_playable("E D G F B A C5 B ", 120),
            music.PlaybackMode.LOOPING_IN_BACKGROUND)
basic.forever(on_forever)
