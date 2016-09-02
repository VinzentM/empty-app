from ggame import App, Color, LineStyle, Sprite
from ggame import RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

oragne = Color(0xFFD740, 1.0)
greywhite = Color(0xF5F5F5, 1.0)

thinline = LineStyle(1, greywhite)

rectangle = RectangleAsset(50, 20, thinline, oragne)


myapp = App()
myapp.run()