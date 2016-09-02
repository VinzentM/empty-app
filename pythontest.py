from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

oragne = Color(0xFFD740, 1.0)
greywhite = Color(0xF5F5F5, 1.0)
lightblue = Color(0x03A9F4, 1.0)

thinline = LineStyle(1, greywhite)

rectangle = RectangleAsset(50, 50, thinline, lightblue)

Sprite(rectangle)

myapp = App()
myapp.run()