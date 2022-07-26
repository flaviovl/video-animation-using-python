from manim import *


class DisplayHelloWorld(Scene):
    def construct(self):
        first_line = Text("Hello World!")
        second_line = Text("Primeira animação usando Manim!", color=RED)
        third_line = Text("Vamos aprender juntos!!", color=GREEN)

        second_line.next_to(first_line, DOWN)

        self.wait(1)
        self.play(Write(first_line), Write(second_line))
        self.wait(3)
        self.play(ReplacementTransform(first_line, third_line), FadeOut(second_line))
        self.wait(5)

        # self.play(FadeOut(first_line), FadeOut(second_line))
