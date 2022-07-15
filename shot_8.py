from manim import *

class shot8(Scene):
    def construct(self):

        colors = [BLUE, GREEN]
       
        values = [40, 64, 78.4, 87.04, 92.224]
        yr = [0, 100, 25]
        barct = BarChart(values, y_range = yr, bar_colors = colors)

        bar = barct.get_bar_labels(font_size = 22)
        txt = Text("Growth Chance\n per cycle (%)", font_size=24).shift(LEFT * 4.5)

        txt1 = Text("Dispensers", font_size=24).shift(DOWN * 2.75)

        txt2 = Text("1", font_size = 26).shift(DOWN * 2.3 + LEFT * 2)
        txt3 = Text("5", font_size = 22).shift(DOWN * 2.3 + RIGHT * 2)
        txt4 = Text("2", font_size = 26).shift(DOWN * 2.3 + LEFT * 1)
        txt5 = Text("3", font_size = 22).shift(DOWN * 2.3)
        txt6 = Text("4", font_size = 22).shift(DOWN * 2.3 + RIGHT * 1)
        
        

        all = VGroup(bar, barct, txt, txt1, txt2, txt3, txt4, txt5, txt6)

        self.wait(1)
        self.play(DrawBorderThenFill(all), rate_func = smooth, run_time = 2.5, )
        self.wait(2)