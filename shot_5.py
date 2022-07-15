from manim import*

class shot5(Scene):
    def construct(self):  
        
        txt1 = MathTex(
                r"A &=",
                r"\text{Amount of cycles/h}\\",
                r"P &=",
                r"\text{Chance of bonemeal attempt failing}\\",
                r"n &=",
                r"\text{Number of Dispensers}")
        
        txt1.shift(UP * 2)
        txt1[0][0].set_color(YELLOW_E)
        txt1[1].set_color(YELLOW_E)
        txt1[2][0].set_color(ORANGE)
        txt1[3].set_color(ORANGE)
        txt1[4][0].set_color(BLUE_D)
        txt1[5].set_color(BLUE_D)

        txt5 = MathTex(
                r"A &=",
                r"18,000\\",
                r"P &=",
                r"0.6\\",
                r"n &=",
                r"3")
        
        txt5.shift(UP * 2 + LEFT * 1.82)   
        txt5[0][0].set_color(YELLOW_E)
        txt5[1].set_color(YELLOW_E)
        txt5[2][0].set_color(ORANGE)
        txt5[3].set_color(ORANGE)
        txt5[4][0].set_color(BLUE_D)
        txt5[5].set_color(BLUE_D)

        txt6 = MathTex(
                r"A &=",
                r"18,000\\",
                r"P &=",
                r"0.6\\",
                r"n &=",
                r"4")
        txt6.shift(UP * 2 + LEFT * 1.82)
        txt6[0][0].set_color(YELLOW_E)
        txt6[1].set_color(YELLOW_E)
        txt6[2][0].set_color(ORANGE)
        txt6[3].set_color(ORANGE)
        txt6[4][0].set_color(BLUE_D)
        txt6[5].set_color(BLUE_D)

        txt2 = MathTex(
                r"A",
                r"(1-",
                r"P^n",
                r")\ =\ ",
                r"\text{Tree's Grown/h}"
            )
        txt2[0].set_color(YELLOW_E)
        txt2[2][0].set_color(ORANGE)
        txt2[2][1].set_color(BLUE_D)
        txt2[4].set_color(GREEN)

        txt3 = MathTex(
                r"18,000",
                r"(1-",
                r"0.6^3",
                r")\ =\ ",
                r"14,112"
            )
        txt3[0].set_color(YELLOW_E)
        txt3[2][0].set_color(ORANGE)
        txt3[2][1].set_color(ORANGE)
        txt3[2][2].set_color(ORANGE)
        txt3[2][3].set_color(BLUE_D)
        txt3[4].set_color(GREEN)

        txt4 = MathTex(
                r"18,000",
                r"(1-",
                r"0.6^4",
                r")\ =\ ",
                r"15,667"
            )
        txt4[0].set_color(YELLOW_E)
        txt4[2][0].set_color(ORANGE)
        txt4[2][1].set_color(ORANGE)
        txt4[2][2].set_color(ORANGE)
        txt4[2][3].set_color(BLUE_D)
        txt4[4].set_color(GREEN)

        self.wait(0.5)

        self.play(Write(txt1), Write(txt2), run_time = 1.5)
        self.wait(2)

        self.play(TransformMatchingTex(txt2, txt3), TransformMatchingTex(txt1, txt5), run_time = 1)
        self.wait(2)

        self.play(TransformMatchingTex(txt3, txt4), TransformMatchingTex(txt5, txt6), run_time = 0.6)
        self.wait(2)