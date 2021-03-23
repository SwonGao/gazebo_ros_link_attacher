#!/usr/bin/env python

import rospy
from gazebo_ros_link_attacher.srv import Attach, AttachRequest, AttachResponse


if __name__ == '__main__':
    rospy.init_node('cooperative_assembly_attacher')
    rospy.loginfo("Creating ServiceProxy to /link_attacher_node/attach")
    attach_srv = rospy.ServiceProxy('/link_attacher_node/attach',
                                    Attach)
    attach_srv.wait_for_service()
    rospy.loginfo("Created ServiceProxy to /link_attacher_node/attach")
    rospy.sleep(5)
    rospy.loginfo("Attaching links, please wait a bit longer")
    
    # Link them
    rospy.loginfo("Attaching iris_0 and payload")
    req = AttachRequest()
    req.model_name_1 = "iris_0"
    req.link_name_1 = "Rope::ball0_link"
    req.model_name_2 = "payload"
    req.link_name_2 = "link"

    attach_srv.call(req)

    # Link them
    rospy.loginfo("Attaching iris_1 and payload")
    req = AttachRequest()
    req.model_name_1 = "iris_1"
    req.link_name_1 = "Rope::ball0_link"
    req.model_name_2 = "payload"
    req.link_name_2 = "link"

    attach_srv.call(req)
    # From the shell:
    # Link them
    rospy.loginfo("Attaching iris_2 and payload")
    req = AttachRequest()
    req.model_name_1 = "iris_2"
    req.link_name_1 = "Rope::ball0_link"
    req.model_name_2 = "payload"
    req.link_name_2 = "link"

    attach_srv.call(req)

    rospy.loginfo("attachment is complete")
