# We can consider x and y positions independently. With (positive) initial
# velocity v the total distance moved is v * (v + 1) / 2 before the moving
# stops. If x position can be stopped within the target area, we can find the
# best y velocity without regard to x position.
#
# With any initial y velocity upwards the probe will return to the level 0.
# If the next step downwards is the biggest possible, then the initial
# velocity upwards has been the highest possible.
#
# According to the input, the x position of the target area is 56..76. So, the
# x position can be stopped within the area with the initial x velocity of 11.
#
# According to the input, the lowest point of the target area is -162. So,
# after returning to the level 0, the biggest possible next step is 162
# downwards. Thus, the initial velocity upwards was 161. The highest point the
# probe reached was 161 * 162 / 2 = 13041.
