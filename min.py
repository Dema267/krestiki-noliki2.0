from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Define the sides of the right triangle
        a = 3
        b = 4
        c = 5

        # Create the right triangle
        triangle = Polygon(
            ORIGIN,
            a * RIGHT,
            a * RIGHT + b * UP,
            color=WHITE
        ).set_fill(BLUE, opacity=0.5)

        # Create squares on each side of the triangle
        square_a = Square(side_length=a, color=GREEN).set_fill(GREEN, opacity=0.5)
        square_b = Square(side_length=b, color=RED).set_fill(RED, opacity=0.5)
        square_c = Square(side_length=c, color=YELLOW).set_fill(YELLOW, opacity=0.5)

        # Position the squares on the triangle
        square_a.move_to(triangle.get_vertices()[0] + a/2 * RIGHT + a/2 * DOWN)
        square_b.move_to(triangle.get_vertices()[1] + b/2 * UP + b/2 * RIGHT)
        square_c.move_to(triangle.get_vertices()[2] + c/2 * UP + c/2 * LEFT)

        # Add text labels for the sides
        label_a = MathTex('a').next_to(square_a, DOWN)
        label_b = MathTex('b').next_to(square_b, RIGHT)
        label_c = MathTex('c').next_to(square_c, UP)

        # Add the triangle and squares to the scene
        self.play(Create(triangle))
        self.play(Create(square_a), Write(label_a))
        self.play(Create(square_b), Write(label_b))
        self.play(Create(square_c), Write(label_c))

        # Add the Pythagorean theorem equation
        equation = MathTex('a^2 + b^2 = c^2').to_edge(UP)
        self.play(Write(equation))

        # Highlight the areas of the squares to emphasize the theorem
        self.play(square_a.animate.set_fill(opacity=0.8), square_b.animate.set_fill(opacity=0.8))
        self.play(square_c.animate.set_fill(opacity=0.8))

        # Wait before ending the scene
        self.wait(2)

# To render the scene, you would typically use the following command in the terminal:
# manim -pql <filename>.py PythagoreanTheorem