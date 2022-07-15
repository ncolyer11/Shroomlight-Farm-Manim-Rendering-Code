from manim import*

class shot6(Scene):
    def construct(self):
        txt1 = Text("External: 0.05%",color="#DD4400")
        txt1.shift(1.3 * DOWN)
        txt2 = Text("Internal: 10%", fill_opacity=0.4)
        txt2.shift(2.5 * UP + 3 * RIGHT)
        txt3 = Text("Corners: 1%",color="#00DD44")
        txt3.shift(2.5 * UP + 3 * LEFT)
        box = Rectangle(WHITE,1.2,5)
        box.shift(1.3 * DOWN)
        txt4 = Text("Selection:").shift(1.3 * DOWN + 4.1 * LEFT)

        self.wait(0.3)
        self.play(DrawBorderThenFill(box), Write(txt1), Write(txt2), Write(txt3), Write(txt4), run_time=2)
        self.wait(0.5)

        self.play(CyclicReplace(txt1, txt2, txt3), rate_functions=smooth)
        self.wait(1)