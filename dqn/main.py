import gym
import torch.optim as optim

from dqn_model import DQN
from dqn_learn import OptimizerSpec, dqn_learing
from utils.gym import get_env, get_wrapper_by_name
from utils.schedule import LinearSchedule

import pickle
import os

BATCH_SIZE = 32
GAMMA = 0.99
REPLAY_BUFFER_SIZE = 1000000
LEARNING_STARTS = 50000
LEARNING_FREQ = 4
FRAME_HISTORY_LEN = 4
TARGER_UPDATE_FREQ = 10000
#LEARNING_RATE = 0.00025
LEARNING_RATE = 0.0001
ALPHA = 0.95
EPS = 0.01

def main(env, num_timesteps, pre_trained_model=None, start_from=0):

    def stopping_criterion(env):
        # notice that here t is the number of steps of the wrapped env,
        # which is different from the number of steps in the underlying env
        if get_wrapper_by_name(env, "Monitor").get_total_steps() % 10000 == 0:
            print("The number of steps left:" , max(0, num_timesteps - get_wrapper_by_name(env, "Monitor").get_total_steps()))
        return get_wrapper_by_name(env, "Monitor").get_total_steps() >= num_timesteps

    optimizer_spec = OptimizerSpec(
        constructor=optim.RMSprop,
        kwargs=dict(lr=LEARNING_RATE, alpha=ALPHA, eps=EPS),
    )

    #exploration_schedule = LinearSchedule(1000000, 0.1)
    exploration_schedule = LinearSchedule(600000, 0.1)
    dqn_learing(
        env=env,
        q_func=DQN,
        optimizer_spec=optimizer_spec,
        exploration=exploration_schedule,
        stopping_criterion=stopping_criterion,
        replay_buffer_size=REPLAY_BUFFER_SIZE,
        batch_size=BATCH_SIZE,
        gamma=GAMMA,
        learning_starts=LEARNING_STARTS,
        learning_freq=LEARNING_FREQ,
        frame_history_len=FRAME_HISTORY_LEN,
        target_update_freq=TARGER_UPDATE_FREQ,
    )

if __name__ == '__main__':
    # Get Atari games.
    benchmark = gym.benchmark_spec('Atari40M')

    # Change the index to select a different game.
    task = benchmark.tasks[3]

    # Run training
    seed = 0 # Use a seed of zero (you may want to randomize the seed!)
    env = get_env(task, seed)

    #open pre_trained_model if exists
    pre_trained_model = None
    Q_pckl = None
    target_pckl = None
    my_stats = None
    start_from = 0
    '''
    from google.colab import drive

    drive.mount('/content/drive')
    '''
    
    main(env, 1e6 * 16, pre_trained_model)
