input.onGesture(Gesture.Shake, function () {
    reset()
})
function reset () {
    trigger = 5
    timer = 0
    music.stopMelody(MelodyStopOptions.All)
    isTriggered = false
}
let ring_time = 0
let isTriggered = false
let timer = 0
let trigger = 0
reset()
loops.everyInterval(1000, function () {
    timer += 1
    ring_time += 1
    if (isTriggered) {
        music.setVolume(Math.max(127 + ring_time * 10, 255))
        basic.showLeds(`
            . . # . .
            . . # . .
            . . # . .
            . . . . .
            . . # . .
            `)
    } else if (timer % 2 == 0) {
        basic.showLeds(`
            . # # # .
            . # # # .
            . . # . .
            . # # # .
            . # # # .
            `)
    } else {
        basic.showLeds(`
            . . . . .
            # # . # #
            # # # # #
            # # . # #
            . . . . .
            `)
    }
})
basic.forever(function () {
    if (trigger == timer) {
        ring_time = 0
        isTriggered = true
        music.play(music.stringPlayable("E D G F B A C5 B ", 120), music.PlaybackMode.LoopingInBackground)
    }
})
