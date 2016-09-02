from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

darkoragne = Color(0xFF9800, 1.0)
greywhite = Color(0xF5F5F5, 1.0)
lightblue = Color(0x03A9F4, 1.0)
oceanblue = Color(0x283593, 1.0)
beachyellow = Color(0xFFD54F, 1.0)


no-line = LineStyle(0, greywhite)
thinline = LineStyle(1, greywhite)

background = RectangleAsset(1920, 1080, thinline, lightblue)
sun = CircleAsset(180, thinline, darkoragne)
ocean = RectangleAsset(1920, 1000, thinline, oceanblue)
beach = RectangleAsset(1920, 1000, thinline, beachyellow)
reflection = RectangleAsset(30, 30, no-line, reflectionyellow)

Sprite(background)
Sprite(sun, (1310, 350))
Sprite(ocean, (0, 400))
Sprite(beach, (0, 700))

myapp = App()
myapp.run()