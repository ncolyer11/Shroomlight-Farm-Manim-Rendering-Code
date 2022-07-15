from manim import*

class title(Scene):
    def construct(self):
        
        txt = MathTex(
            r"\text{Shroomlight}^{\text{Farm}}"
        )

        txt.set_color_by_gradient(RED, YELLOW_E)
        txt.font_size = 100

        self.play(DrawBorderThenFill(txt), run_time = 2.2)
