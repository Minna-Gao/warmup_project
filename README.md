# warmup_project

## drive_in_a_square
#### description
For this part of the project, I have to make the robot drive(roughly) in a square. I chose to program the Turtlebot so that it moves forward for a set number of seconds, then turns 90 degrees for a set number of seconds. While the Turtlebot isn't shutdown, it will continue to execute the for loop that contains the aforementioned move & turn combination four times, which completes a square. Then, it will start the for loop all over again, drawing a new square.
#### code explanation
The code is divided into two parts: the initialization function and the run function. The initialization function sets up the node and the publisher. The publisher will be sending data to the Turtlebot. The run function contains a while loop and within it a for loop that iterates four times. First, the for loop initializes the Twist() variable and stores it. Then, the linear x is set to 0.5 and the angular z is set to 0; this is so that the robot moves directly forward. Then, the function publishes this data to the robot so it executes the new Twist() settings. Then, the rospy.sleep(3) line ensures that  the robot stays moving forward for three seconds. Then, the function updates the linear x to 0 so it stops moving forward, and the angular z to 1.5708 (90 degrees in radians) so that the robot turns a corner. Then, the function publishes this change to the robot. Then, the function tells the robot to wait in this state for 1.12 seconds so that it can finish its turn. And then, the for loop repeats, so the robot (having completed its turn) now moves forward again.  
#### gif
#### challenges
The two biggest challenges were determining the overall solution to the problem. At first, I thought I would use ROS odometry and program it such that the robot moves forward for a set distance, then once it reaches that set distance, the robot turns a set number of degrees (90 degrees). However, this is hard to carry out as this requires me to keep track of the distance travelled and degrees turned. Then, David suggested that I keep the overall idea, but instead of using odometry to trigger a change in the robot's movement, use a timer so that the robot moves for a set number of seconds, and then turns for a set number of seconds.
The second challenge was determining the exact forward velocity and the sleep time for the turn. I had to budget more sleep time for the turn than initially expected to take the friction of the floor into account. I also initially had the forward velocity set to 1, which was too fast.
#### future work
Move trial and error can be done so that the robot moves in a perfect square on the floor of CSIL 5. Trying out different sleep times for the turn will make sure the robot gets exactly the amount of time it needs to complete a 90 degree turn on the CSIL 5 carpet. 
#### takeaways
This is part of the challenge of programming ROS, but I suspect it's particular to this project. My biggest takeaway is taking the time to set up all the environment variables correctly. In particular, 
	- remembering to check VM IP with hostname -I, and setting the environment variable accordingly. 
	- remembering to actually turn on the Turtlebot before running bringup
	- remembering to run roscore, pi terminal, and the code in three separate terminals
	- remembering to run roscore BEFORE running bringup in pi terminal
	- remembering that there are two actions needed to stop bot: control Z and setting all linear and angular velocities to 0.
	- remembering to taking external variables into account. In particular, friction when calculating floor navigating is critical.



##person_follower
#### description
the robot is programmed to follow the nearest object (person). I chose to use the scan topic to analyze objects close to the robot and the cmd_vel topic to publish Twist information to the robot so that it can reposition itself
to face the object and move towards the object.
#### code explanation
my code is divided into three parts: initialization, scanning environment and updating Twist() function, and a run function. The initialization function sets up the the ROS node, scan receiver, and cmd_vel publisher. The process_data function takes in the scan data, loops through data.ranges to find whether there is an object around the robot that it can follow, picks the object that is closest to the robot, and checks the angle that object lies on. This way, if a person is moving around, the robot will continuously try to minimize the distance between itself and the person by repositioning itself to face the person and move towards the person. Then, once we have the angle information, we update the Twist settings and publish that information to the robot. If we are too close to the object we're following the robot will only reposition itself to face the object. 
#### gif
![Alt Text](https://videoapi-muybridge.vimeocdn.com/animated-thumbnails/image/30398fcb-1dac-4c1e-adf2-d7e4af0ff62d.gif?ClientID=vimeo-core-prod&Date=1650475429&Signature=d3d71000194d8bf8159bb0c9b7fb64c6a90338cacd)
#### challenges
The biggest challenge is figuring out how to reposition the robot so that it faces the object it's following at all times.
A big hint from David was to not think of the angles as 360, but instead think of it as left 180 and right 180. This way, the robot can follow a person more accurately. Executing this was also difficult as initially the robot was only turning to one-side; I fixed this by completing my if-else statement in setting the index. 
The second biggest challenge is, again, trying to connect to turtlebot and running it correctly. 
#### future work
If I had more time, I would test my code on a turtlebot more thoroughly. So far it seems the turtlebot cannot keep up if I move too fast. The robot also seems to sometimes get confused about which object to follow.
#### takeaways 
	- the indexes of the range array are the angles, and the values are the distances from the object the 
	robot detects. Knowing how to understand the data.ranges array will help me work on future projects that
	require analyzing environment
	- I can have print statements inside conditional statements to test that I'm entering the correct conditionals. 

