# aaa

from nes_py.wrappers import JoypadSpace
import gym_super_mario_bros
from gym_super_mario_bros.actions import  SIMPLE_MOVEMENT
import matplotlib.pyplot as plt
import cv2
import numpy as np
import subprocess as sp

env = gym_super_mario_bros.make("SuperMarioBros-v0")
obj = env.reset()
print(obj.shape)
plt.imshow(obj)

env = JoypadSpace(env, SIMPLE_MOVEMENT)
print("env.action_space: ", env.action_space)
# from gym import wrappers
# env = wrappers.Monitor(env,"./gym-results", force=True)

done = True #游戏结束标志

for step in range(2000):
    if done:
        state = env.reset()
    state, reward, done, info = env.step(3)
    env.render()

env.close()

