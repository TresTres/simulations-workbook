import vpython
import physical_laws as pl

sphere1 = vpython.sphere(pos=vpython.vector(-25, 0, 0), radius=20.5, color=vpython.color.red)
sphere2 = vpython.sphere(pos=vpython.vector(25, 0, 0), radius=16.75, color=vpython.color.blue)
sphere1.mass = 80e15
sphere1.force = 0
sphere2.mass = 60e15
sphere2.force = 0

f_curves = vpython.graph(title="Force vs. Time", xtitle="Time (s)", ytitle="Force (N)")
velocity_curves = vpython.graph(title="Velocity vs. Time", xtitle="Time (s)", ytitle="Velocity (m/s)")
sphere1_fcurve = vpython.gcurve(graph=f_curves, color=vpython.color.red)
sphere2_fcurve = vpython.gcurve(graph=f_curves, color=vpython.color.blue)
sphere1_velocity_curve = vpython.gcurve(graph=velocity_curves, color=vpython.color.red, dot=True)
sphere2_velocity_curve = vpython.gcurve(graph=velocity_curves, color=vpython.color.blue, dot=True)


def main_loop(max_t: float = 5, dt: float = 0.001, compute_rate: float = 100) -> None: 
    t = 0
    while t < max_t:
        vpython.rate(compute_rate)
        distance = abs(sphere2.pos.x - sphere1.pos.x)
        if distance >= (sphere1.radius + sphere2.radius):
            # update
            sphere1.force = pl.newton_universal_gravitation(sphere1.mass, sphere2.mass, distance)
            sphere2.force = -sphere1.force
            
            sphere1_new_pos = pl.kinematic_distance(dt, sphere1.pos.x, 0, sphere1.force / sphere1.mass)
            sphere2_new_pos = pl.kinematic_distance(dt, sphere2.pos.x, 0, sphere2.force / sphere2.mass)
            sphere1.pos.x, sphere2.pos.x = sphere1_new_pos, sphere2_new_pos
        else: 
            sphere1.force = 0
            sphere2.force = 0
            
        
        t += dt
        sphere1_fcurve.plot(t, sphere1.force)
        sphere2_fcurve.plot(t, sphere2.force)
        sphere1_velocity_curve.plot(t, t * sphere1.force / sphere1.mass)
        sphere2_velocity_curve.plot(t, t * sphere2.force / sphere2.mass)
            
            
main_loop(10, compute_rate=400)