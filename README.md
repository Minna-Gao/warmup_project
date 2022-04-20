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
#### code explanation
#### gif
#### challenges
#### future work
#### takeaways 
