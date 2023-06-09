import pickle

with open('/content/drive/MyDrive/RL_project/Pre_trained/statistics.pkl', 'rb') as f:
    results = pickle.load(f)

f = open('/content/drive/MyDrive/RL_project/Pre_trained/my_stats.txt', 'r')
last_time_step_ran = f.readlines()[-1]

stoped_in_timestep = 0
mean_episode_rewards = results['mean_episode_rewards']
best_episode_rewards = results['best_mean_episode_rewards']
#append to my_stats.txt end of the file 
with open('/content/drive/MyDrive/RL_project/Pre_trained/my_stats.txt', 'a') as f:
    #write that we have done a new run
    f.write('-----------------New run-----------------\n')
    #write the mean episode rewards
    f.write('mean_episode_rewards:\n')
    for i in range(len(mean_episode_rewards)):
        f.write(str(mean_episode_rewards[i])+',')
    f.write('\n')
    #write the best episode rewards
    f.write('best_episode_rewards:\n')
    for i in range(len(best_episode_rewards)):
        f.write(str(best_episode_rewards[i])+',')
    f.write('\n')
    #write the number of steps we stopped in
    f.write('stopped in timestep:\n')
    f.write(str(stoped_in_timestep)+'\n')
    #write the next time step we will run
    f.write('next time step to run:\n')
    f.write(str(int(last_time_step_ran) + int(stoped_in_timestep))+'\n')

