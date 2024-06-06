from sympy.physics.mechanics import Body, PrismaticJoint
parent = Body('P')
child = Body('C')
joint = PrismaticJoint('PC', parent, child, None, None, parent_joint_pos=None, child_joint_pos=None, parent_axis=None, parent_point=None, child_point=None, parent_interframe=None, child_interframe=None, joint_axis=None)
