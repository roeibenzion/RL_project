import numpy as np
import matplotlib.pyplot as plt

x_mean = []
x_best = []
y_mean = []
y_best = []
# Read in the data from the file
with open('/content/drive/MyDrive/RL_project/Pre_trained/my_stats.txt', 'r') as f:
    lines = f.readlines()
    for i in len(lines):
        if lines[i] == '-----------------New run-----------------\n':
            #extract the data from the file
            mean_episode_rewards = lines[i+1].split(',')
            best_episode_rewards = lines[i+2].split(',')   
            stopped_in_timestep = lines[i+3]
            #append the data to the lists
            x_mean.append(np.arange(0, len(mean_episode_rewards)))
            y_mean.append(mean_episode_rewards)
            x_best.append(np.arange(0, len(best_episode_rewards)))
            y_best.append(best_episode_rewards)

#plot the data (don't forget to label the y axis and to use scientific notation for x))
#where is the scientific notation?
plt.xlabel('time step')
plt.ylabel('mean reward')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.plot(x_mean, y_mean, label='mean_episode_rewards') 
plt.ylabel('best reward') 
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))      
plt.plot(x_best, y_best, label='best_episode_rewards')