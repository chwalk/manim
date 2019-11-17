from big_ol_pile_of_manim_imports import *

class Shapes(Scene):
#A few simple shapes
    def construct(self):
        circle = Circle()
        square = Square()
        line=Line(np.array([3,0,0]),np.array([5,0,0]))
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))

        self.add(line)
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square,triangle))


class MoreShapes(Scene):
    def construct(self):
        circle = Circle(color=PURPLE_A)
        square = Square(fill_color=GOLD_B, fill_opacity=1, color=GOLD_A)
        square.move_to(UP+LEFT)
        circle.surround(square)
        rectangle = Rectangle(height=2, width=3)
        ellipse = Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(2*RIGHT,5*RIGHT,color=MAROON_C)
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow,DOWN+LEFT)
        ring=Annulus(inner_radius=.5, outer_radius=1, color=BLUE)
        ring.next_to(ellipse, RIGHT)

        self.add(pointer)
        self.play(FadeIn(square))
        self.play(Rotating(square),FadeIn(circle))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))

# You can compile this with python3 -m manim manim_tutorial_P37.py PhysicsExample -p
# You borrowed it from F:\Cus\3b1b\manim\old_projects\eola\chapter0.py
# See if you can get the file referenced above to compile by figuring out all the dependencies and folders.
class PhysicsExample(Scene):
    def construct(self):
        title = TextMobject("Physics")
        title.to_corner(UP+LEFT)
        parabola = FunctionGraph(
            lambda x : (3-x)*(3+x)/4,
            x_min = -4, 
            x_max = 4
        )

        self.play(Write(title))
        self.projectile(parabola)
        self.velocity_vector(parabola)
        self.approximate_sine()

    def projectile(self, parabola):
        # dot = Dot(radius = 0.15)
        dot = Rectangle(height=2, width=3)
        kwargs = {
            "run_time" : 3,
            "rate_func" : None
        }
        self.play(
            MoveAlongPath(dot, parabola.copy(), **kwargs),
            ShowCreation(parabola, **kwargs)
        )
        self.wait()


    def velocity_vector(self, parabola):
        alpha = 0.7
        d_alpha = 0.01
        vector_length = 3

        p1 = parabola.point_from_proportion(alpha)
        p2 = parabola.point_from_proportion(alpha + d_alpha)
        vector = vector_length*(p2-p1)/get_norm(p2-p1)
        v_mob = Vector(vector, color = YELLOW)
        vx = Vector(vector[0]*RIGHT, color = GREEN_B)
        vy = Vector(vector[1]*UP, color = RED)
        v_mob.shift(p1)
        vx.shift(p1)
        vy.shift(vx.get_end())

        arc = Arc(
            angle_of_vector(vector), 
            radius = vector_length / 4.
        )
        arc.shift(p1)
        theta = TexMobject("\\theta").scale(0.75)
        theta.next_to(arc, RIGHT, buff = 0.1)

        v_label = TexMobject("\\vec{v}")
        v_label.shift(p1 + RIGHT*vector[0]/4 + UP*vector[1]/2)
        v_label.set_color(v_mob.get_color())
        vx_label = TexMobject("||\\vec{v}|| \\cos(\\theta)")
        vx_label.next_to(vx, UP)
        vx_label.set_color(vx.get_color())
        vy_label = TexMobject("||\\vec{v}|| \\sin(\\theta)")
        vy_label.next_to(vy, RIGHT)
        vy_label.set_color(vy.get_color())

        kwargs = {"submobject_mode" : "one_at_a_time"}
        for v in v_mob, vx, vy:
            self.play(
                ShowCreation(v, submobject_mode = "one_at_a_time")
            )
        self.play(
            ShowCreation(arc),
            Write(theta, run_time = 1)
        )
        for label in v_label, vx_label, vy_label:
            self.play(Write(label, run_time = 1))
        self.wait()

    def approximate_sine(self):
        approx = TexMobject("\\sin(\\theta) \\approx 0.7\\text{-ish}")
        morty = Mortimer(mode = "speaking")
        morty.flip()
        morty.to_corner()
        bubble = SpeechBubble(width = 4, height = 3)
        bubble.set_fill(BLACK, opacity = 1)
        bubble.pin_to(morty)
        bubble.position_mobject_inside(approx)

        self.play(
            FadeIn(morty),
            ShowCreation(bubble),
            Write(approx),
            run_time = 2
        )
        self.wait()
