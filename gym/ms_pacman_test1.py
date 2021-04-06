import gym

'''
需要安装atari_py 安装方式
pip install --no-index -f https://github.com/Kojoley/atari-py/releases atari_py
'''
env = gym.make("MsPacman-v0")
env.reset()

for _ in range(100000):
    env.render()
    env.step(env.action_space.sample())

env.close()