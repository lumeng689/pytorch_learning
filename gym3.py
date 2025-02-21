import gym

test_envs = {'algorithm': 'Copy-v0',
             'toy_text': 'FrozenLake-v0',
             'control': 'CartPole-v0',
             'atari': 'SpaceInvaders-v0',
             'mujoco': 'Humanoid-v1',
             'box2d': 'LunarLander-v2'}

game_name = test_envs['algorithm']
env = gym.make(game_name)
for i_episode in range(20):
    observation = env.reset()
    for t in range(100):
        env.render()
        print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        if done:
            print("Episode finished after {} timesteps".format(t + 1))
            break
