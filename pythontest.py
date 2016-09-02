from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

darkoragne = Color(0xFF9800, 1.0)
greywhite = Color(0xF5F5F5, 1.0)
lightblue = Color(0x03A9F4, 1.0)
oceanblue = Color(0x283593, 1.0)
beachyellow = Color(0xFFD54F, 1.0)

thinline = LineStyle(1, greywhite)
background = RectangleAsset(1920, 1080, thinline, lightblue)
face = CircleAsset(180, thinline, darkoragne)
ocean = RectangleAsset(1920, 1000, thinline, oceanblue)
beach = RectangeAsset(1920, 1000, thinline, beachyellow)

Sprite(background)
Sprite(face, (210, 350))
Sprite(ocean, (0, 400))

myapp = App()
myapp.run()