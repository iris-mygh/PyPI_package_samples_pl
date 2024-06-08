# from draw_circle import draw_circle_with_symbol # test.py same folder: Simple_drawing
from Simple_drawing import draw_circle_with_symbol # __init__.py vs "from .draw_circle import draw_circle_with_symbol"
# from Simple_drawing.draw_circle import draw_circle_with_symbol # __init__.py without "from .draw_circle import draw_circle_with_symbol"

draw_circle_with_symbol(5, "*", filename="circle.png")