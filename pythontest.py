from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

darkoragne = Color(0xFB8C00, 1.0)
greywhite = Color(0xF5F5F5, 1.0)
lightblue = Color(0x03A9F4, 1.0)

thinline = LineStyle(1, greywhite)
background = RectangleAsset(1920, 1080, thinline, lightblue)
face = CircleAsset(180, thinline, darkoragne)
Sprite(background)
Sprite(face, (210, 300))

myapp = App()
myapp.run()