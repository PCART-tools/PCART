from sympy.physics.mechanics import Body, PinJoint
parent = Body('P')
child = Body('C')
joint = PinJoint('PC', parent, child=child, parent_point=None, child_point=None, parent_interframe=None, child_interframe=None, joint_axis=None)
