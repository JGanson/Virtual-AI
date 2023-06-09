

import random

from icm import PPO, PPOICM
from environment import SimpleEnv, AtariEnv

"""
Environments:

CartPole-v0 (Discrete)
Pendulum-v1 (Continuous)
BreakoutDeterministic-v4 (Discrete)


"""


def main(env_name="CartPole-v0",
         total_timesteps=100_000_000
         ):

    env = SimpleEnv(env_name)
    # env = AtariEnv(env_name)
    # PPO not compatible with atari yet, but PPOICM is
    agent = PPO(env.state_size, env.action_size, env.discrete)

    # train the agent
    agent.learn(env, total_timesteps=total_timesteps)


if __name__ == "__main__":
    main()

