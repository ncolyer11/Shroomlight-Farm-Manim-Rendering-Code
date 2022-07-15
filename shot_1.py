from manim import *

class BarCharExam(Scene):
    def construct(self):

        colors = [BLUE, ORANGE, BLUE, ORANGE, BLUE, ORANGE, BLUE, ORANGE]
       
        values = [18, 10, 97.951, 0.05, 69.3, 1, 27.1125, 0]
        yr = [0, 100, 25]
        barct = BarChart(values, y_range = yr, bar_colors = colors)

        bar = barct.get_bar_labels(font_size = 20)
        txt = Text("(%)", font_size=24).shift(LEFT * 5)

        txt1 = Text("Internal", font_size=24).shift(LEFT * 3 + DOWN * 2.4)
        txt2 = Text("External", font_size=24).shift(LEFT * 1 + DOWN * 2.4)
        txt3 = Text("Corners", font_size=24).shift(RIGHT * 1 + DOWN * 2.4)
        txt4 = Text("Vines", font_size=24).shift(RIGHT * 3 + DOWN * 2.4)
      
        
        lbl1 = Text("Wart Blocks", color = WHITE, font_size = 18).shift(RIGHT * 2.6 + UP * 1.7)
        box1 = SurroundingRectangle(
            lbl1, color = BLUE, fill_opacity = 0.7, buff = 0.18
        )

        lbl2 = Text("Shroomlights",color = WHITE, font_size = 17,disable_ligatures=True).shift(RIGHT * 2.6 + UP * 0.9)
        box2 = SurroundingRectangle(
            lbl2, color = ORANGE, fill_opacity = 0.7, buff = 0.14
        )


        all = VGroup(bar, barct, box1, box2, lbl1, lbl2, txt, txt1, txt2, txt3, txt4)

        self.wait(1)
        self.play(DrawBorderThenFill(all), rate_func = smooth, run_time = 2.5, )
        self.wait(2)