import timeit

from ursina import *
from ursina import curve

app = Ursina()
me = Animation(
    'alma2',
    collider='box',y=5
)
Sky()
camera.orthographic = True
camera.fov = 20

Entity(
    model='quad',
    texture='BG2',
    scale=36,
    z=1
)
fly = Entity(
    model='cube',
    texture='monster',
    collider='box',
    scale=2,x=20,y=-10
)
flies=[]
def newFly():
    new = duplicate(
        fly,
        y=-5+(5124*time.dt)%15
    )
    flies.append(new)
    invoke(newFly,delay=1)
newFly()
def update():


    me.y += held_keys['w']*6*time.dt
    me.y -= held_keys['s']*6*time.dt
    a = held_keys['w']*-20
    b = held_keys['s']*20
    if a!= 0:
        me.rotation_z =a
    else:
        me.rotation_z=b
    for fly in flies:
        fly.x-=4*time.dt
        touch = fly.intersects()
        if touch.hit:
            flies.remove(fly)
            destroy(fly)
        t = me.intersects()
        if t.hit and t.entity.scale == 2:
            quit()
def input(key):
    if key == 'space':
        e = Entity(
            y=me.y,
            x=me.x+2,
            model='cube',
            texture='bullet',
            collider='cube'
        )
        e.animate_x(
            30,
            duration=2,
            curve=curve.linear
        )
        invoke(destroy,e,delay=2)
app.run()