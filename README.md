# About

This is a 1-1 inspired ASCII recreation in Python. The inspiration came as part of a video game ([RoboCo](https://www.roboco.co/)) building contest. 

In the game RoboCo, along with building various robots to solve puzzles you can also include a microcontroller that can run a python script. 

Using RoboCo's [API](https://docs.roboco.co/latest/api.html) I was inspired to create a design of a robot playing a game within a game. 

This project is the "game within a game"

# Constraints
Given this must run inside of another game using it's rules I have to follow a couple constraints:
* I can only have one python file per controller. For performance reasons I want to use as few controllers as possible
* Given there is a deadline for the build contest, I have a limited time to develop this. So expect hackathon level code quality. 
* I can only use vanilla python with no imports besides what is provided by RoboCo. I used TX to render a version on my desktop for debugging purposes but remove TX when uploading to RoboCo

# Special Thanks:
Thank you to the following people who unknowingly assisted me in developing this:
* RoboCo for making their excellent game
* [Xem](https://codegolf.stackexchange.com/users/10732/xem) for their code golf post that [gave an example of a grid for 1-1](https://codegolf.stackexchange.com/questions/40008/pixel-art-episode-2-display-the-map-1-1-of-super-mario-bros)