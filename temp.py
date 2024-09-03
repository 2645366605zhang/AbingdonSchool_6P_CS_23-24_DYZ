#import random
#import gymnasium as gym
#from gridworld import CliffWalkingWapper
"""
env = gym.make("CartPole-v1", render_mode = "human")
observation = env.reset()

for _ in range(1000):
    env.render()

    #currentAction = env.action_space.sample()
    currentAction = random.randint(0, 1)

    env.step(currentAction)

env.close()
"""

"""
env = gym.make("Humanoid-v4", render_mode = "human")
observation = env.reset()

for _ in range(1000):
    env.render()

    currentAction = env.action_space.sample()
    #currentAction = random.randint(0, 1)

    env.step(currentAction)

env.close()
"""

"""from pettingzoo.mpe import simple_world_comm_v3

env = simple_world_comm_v3.env(render_mode="human")
env.reset(seed=42)

for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()

    if termination or truncation:
        action = None
    else:
        # this is where you would insert your policy
        action = env.action_space(agent).sample()

    env.step(action)
env.close()"""

"""
from pettingzoo.classic import go_v5

env = go_v5.env(render_mode="human")
env.reset(seed=42)

for agent in env.agent_iter():
    observation, reward, termination, truncation, info = env.last()

    if termination or truncation:
        action = None
    else:
        mask = observation["action_mask"]
        # this is where you would insert your policy
        action = env.action_space(agent).sample(mask)

    env.step(action)
env.close()
"""


from dataStructure import ArrayQueue as Queue

if __name__ == "__main__":
    myQueue = Queue(8)
    print(myQueue.isEmpty())
    myQueue.add("hello")
    print(myQueue.isEmpty())
