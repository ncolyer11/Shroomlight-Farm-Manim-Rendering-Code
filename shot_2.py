from manim import*

class shot2(Scene):
    def construct(self):
        
        txt1 = MathTex(
                r"T(x)",
                r"=",
                r"\text{Random}",
                r"(4\rightarrow13)"
            ) 
        txt1[0].set_color(RED)
        txt1[2].set_color(ORANGE)

        txt2 = MathTex(
                r"\text{if }",
                r"\text{Random}",
                r"(0\rightarrow1)<\frac{1}{12}"
            )      
        txt2[1].set_color(ORANGE)

        txt3 = MathTex(
                r"T(x)",
                r" = 2 \times",
                r"T(x)"
            )
        txt3[0].set_color(RED)
        txt3[2].set_color(RED)
        txt3.shift(DOWN * 0.1)
        
        

        ln1 = Line(UP * 0, UP * 1) 
        ln2 = Line(UP * 0.375, UP * 1.5)      
        self.wait(0.4)
        self.play(Write(txt1), run_time = 0.75)
        self.wait(1)

        self.play(MoveAlongPath(txt1, ln1), Write(txt2), run_time = 1)
        all = VGroup(txt1,txt2)
        self.wait(1)

        self.play(MoveAlongPath(all, ln2), Write(txt3))