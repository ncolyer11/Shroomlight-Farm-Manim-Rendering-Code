from manim import*

class shot7(Scene):
    def construct(self):
        
        txt1 = MathTex("Basalt").shift(UP * 1)
        box1 = SurroundingRectangle(
            txt1, color=GRAY, fill_opacity=0.7, buff=0.25
        )
        txt1_1 = MathTex(r"\text{Blast\ res:\ }", "4.2").next_to(box1, DOWN, buff=0.25)
        
        txt2 = MathTex("Slime").shift(DOWN * 0.705)
        box2 = SurroundingRectangle(
            txt2, color=GREEN, fill_opacity=0.6, buff=0.25
        )
        txt2_1 = MathTex(r"\text{Blast\ res:\ }", "0.0").next_to(box2, UP, buff=0.25)

        self.play(Create(VGroup(box1, txt1, txt1_1)), run_time=1)
        self.wait(1)

        self.play(TransformMatchingShapes(VGroup(box1, txt1, txt1_1), VGroup(box2, txt2, txt2_1)), run_time=1)
        self.wait(1)
