import vpython
import physical_laws as pl
import vector_math as vm

sphere1 = vpython.sphere(pos=vpython.vector(-5, -9, -14), radius=20.5, color=vpython.color.red)
sphere2 = vpython.sphere(pos=vpython.vector(9, 17, 14), radius=3.75, color=vpython.color.blue)
sphere1.mass = 80e15
sphere1.force = 0
sphere2.mass = 60e11
sphere2.force = 0

f_curves = vpython.graph(title="Force vs. Time", xtitle="Time (s)", ytitle="Force (N)")
velocity_curves = vpython.graph(title="Abs Velocity vs. Time", xtitle="Time (s)", ytitle="Velocity (m/s)")
sphere1_fcurve = vpython.gcurve(graph=f_curves, color=vpython.color.red)
sphere2_fcurve = vpython.gcurve(graph=f_curves, color=vpython.color.blue)
sphere1_velocity_curve = vpython.gcurve(graph=velocity_curves, color=vpython.color.red, dot=True)
sphere2_velocity_curve = vpython.gcurve(graph=velocity_curves, color=vpython.color.blue, dot=True)


def main_loop(max_t: float = 5, dt: float = 0.001, compute_rate: float = 100) -> None: 
    t = 0
    while t < max_t:
        vpython.rate(compute_rate)
        distance = sphere2.pos - sphere1.pos
        if distance.mag >= (sphere1.radius + sphere2.radius):
            # update
            sphere2.force = pl.newton_universal_gravitation(sphere1.mass, sphere2.mass, vm.Vec_3D(*distance.value))
            sphere1.force = -sphere2.force
            
            sphere1_new_pos = pl.kinematic_distance(dt, distance=vm.Vec_3D(*sphere1.pos.value), acceleration=sphere1.force / sphere1.mass)
            sphere2_new_pos = pl.kinematic_distance(dt, distance=vm.Vec_3D(*sphere2.pos.value), acceleration=sphere2.force / sphere2.mass)
            sphere1.pos, sphere2.pos = vpython.vector(*sphere1_new_pos), vpython.vector(*sphere2_new_pos)
        else: 
            sphere1.force = vm.Vec_3D.ZERO
            sphere2.force = vm.Vec_3D.ZERO
            
        
        t += dt
        sphere1_fcurve.plot(t, sphere1.force.magnitude)
        sphere2_fcurve.plot(t, -sphere2.force.magnitude)
        sphere1_velocity_curve.plot(t, (t * sphere1.force / sphere1.mass).magnitude)
        sphere2_velocity_curve.plot(t, (t * sphere2.force / sphere2.mass).magnitude)
            
            
main_loop(10, compute_rate=400)