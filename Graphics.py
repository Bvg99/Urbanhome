import simple_draw

simple_draw.resolution = (1200, 600)
point = simple_draw.get_point(300, 400)
# simple_draw.circle(point)
radius = 50
wid = 9
for _ in range(3):
    radius += 5
    simple_draw.circle(point, radius, width=wid)


simple_draw.pause()

