from sympy.physics.mechanics import Body, PinJoint
parent = Body('P')
child = Body('C')
joint = PinJoint('PC', parent, child, None, None, None, None, None, child_axis=None, parent_point=None, child_point=None, parent_interframe=None, child_interframe=None, joint_axis=None)
