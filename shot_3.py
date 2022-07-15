import random
from manim import*

class shot3(Scene):
    def construct(self):

        
#showing relationship between hat H(x) and trunk height T(x) with min()
        txt1 = MathTex(
            r"H(x)=",
            r"\text{Min}(",
            "T(x)",
            ")"
        )
        txt1[0][0].set_color("#00EEFF")
        txt1[0][1].set_color("#00EEFF")
        txt1[0][2].set_color("#00EEFF")
        txt1[0][3].set_color("#00EEFF")

        txt1[2][0].set_color(RED)
        txt1[2][1].set_color(RED)
        txt1[2][2].set_color(RED)
        txt1[2][3].set_color(RED)
#introducing a random value with relation to trunk height T(x)
        T = str("T(x)")
        txt2 = MathTex(
                r"H(x)=",
                r"\text{Min}(",
                T,
                ",\ ",
                r"\text{Random}(0\rightarrow1+",
                fr"\frac{{{T}}}{3})+5",
                ")"
            )
        txt2[0][0].set_color("#00EEFF")
        txt2[0][1].set_color("#00EEFF")
        txt2[0][2].set_color("#00EEFF")
        txt2[0][3].set_color("#00EEFF")

        txt2[4][0].set_color(ORANGE)
        txt2[4][1].set_color(ORANGE)
        txt2[4][2].set_color(ORANGE)
        txt2[4][3].set_color(ORANGE)
        txt2[4][4].set_color(ORANGE)
        txt2[4][5].set_color(ORANGE)

        txt2[2][0].set_color(RED)
        txt2[2][1].set_color(RED)
        txt2[2][2].set_color(RED)
        txt2[2][3].set_color(RED)

        txt2[5][0].set_color(RED)
        txt2[5][1].set_color(RED)
        txt2[5][2].set_color(RED)
        txt2[5][3].set_color(RED)
#example scenario
        T = str(7)
        txt3 = MathTex(
                r"H(x)=",
                r"\text{Min}(",
                T,
                ",\ ",
                "6",
                ")=6"
            ).to_edge(DOWN,buff=2.2)
        txt3[0][0].set_color("#00EEFF")
        txt3[0][1].set_color("#00EEFF")
        txt3[0][2].set_color("#00EEFF")
        txt3[0][3].set_color("#00EEFF")
        txt3[5][2].set_color("#00EEFF")
        
        txt3[4][0].set_color(ORANGE)
        
        txt3[2][0].set_color(RED)

        txt4 = MathTex(
                r"\text{Random}(0\rightarrow1+",
                fr"\frac{{{T}}}{3})+5",
                "=",
                "6"
            )
        txt4[0][0].set_color(ORANGE)
        txt4[0][1].set_color(ORANGE)
        txt4[0][2].set_color(ORANGE)
        txt4[0][3].set_color(ORANGE)
        txt4[0][4].set_color(ORANGE)
        txt4[0][5].set_color(ORANGE)
        txt4[3][0].set_color(ORANGE)

        txt4[1][0].set_color(RED)     
        T = str("T(x)")
        txt5 = MathTex(
            T,
            "=7"
        ).to_edge(UP,buff=2.24)
        txt5[0][0].set_color(RED)
        txt5[0][1].set_color(RED)
        txt5[0][2].set_color(RED)
        txt5[0][3].set_color(RED)
        txt5[1][1].set_color(RED)
#general animations
        self.play(Write(txt1),run_time=0.9)
        self.wait(0.5)

        self.play(TransformMatchingTex(txt1,txt2))
        self.wait(1)

        self.play(TransformMatchingTex(txt2,txt4),Write(txt3), Write(txt5), run_time=1)
        self.wait(1.5)
#looping through example values by iterating trunk height 't'
        t = 7
        while(t<=20):
            self.remove(txt3,txt4,txt5)
            
            i = random.randint(0,1+t//3)+5
            h = min(t,i)
            print(str(h)+" "+str(t))
            
            txt3 = MathTex(
                    r"H(x)=\text{Min}(",
                    str(t),
                    ",\ ",
                    str(h),
                    ")=",
                    str(min(t,h))
                ).to_edge(DOWN,buff=2.2)
            txt3[0][0].set_color("#00EEFF")
            txt3[0][1].set_color("#00EEFF")
            txt3[0][2].set_color("#00EEFF")
            txt3[0][3].set_color("#00EEFF")


            txt3[5][0].set_color("#00EEFF")
            if (h >= 10):
                txt3[5][1].set_color("#00EEFF")

            txt3[3][0].set_color(ORANGE)
            if (h >= 10):
                txt3[3][1].set_color(ORANGE)

            txt3[1][0].set_color(RED)
            if (t >= 10):
                txt3[1][1].set_color(RED)

            txt4 = MathTex(
                    r"\text{Random}(0\rightarrow1+",
                    fr"\frac{{{t}}}{3})",
                     "+5=",
                    str(i)
                )
            txt4[0][0].set_color(ORANGE)
            txt4[0][1].set_color(ORANGE)
            txt4[0][2].set_color(ORANGE)
            txt4[0][3].set_color(ORANGE)
            txt4[0][4].set_color(ORANGE)
            txt4[0][5].set_color(ORANGE)
            
            txt4[3][0].set_color(ORANGE)
            if (h >= 10):
                txt4[3][1].set_color(ORANGE)

            txt4[1][0].set_color(RED)
            if (t >= 10):
                txt4[1][1].set_color(RED)              

            txt5 = MathTex(
                    "T(x)="+" "+str(t)
                ).to_edge(UP,buff=2.24)
            txt5[0][0].set_color(RED)
            txt5[0][1].set_color(RED)
            txt5[0][2].set_color(RED)
            txt5[0][3].set_color(RED)
            txt5[0][5].set_color(RED)
            if (t >= 10):
                txt5[0][6].set_color(RED)
            
            self.play(TransformMatchingTex(txt3,txt3),TransformMatchingTex(txt4,txt4),TransformMatchingTex(txt5,txt5),run_time=0.5)
            
            t+=1

        self.wait(2)
