import gym

'''
需要安装 mujoco_py  
'''
env = gym.make("Hopper-v3")
env.reset()

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())

env.close()