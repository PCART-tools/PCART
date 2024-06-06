from sympy.physics.mechanics import Body, PinJoint
parent = Body('P')
child = Body('C')
joint = PinJoint('PC', parent=parent, child=child, coordinates=None, speeds=None, parent_joint_pos=None, parent_point=None, child_point=None, parent_interframe=None, child_interframe=None, joint_axis=None)
