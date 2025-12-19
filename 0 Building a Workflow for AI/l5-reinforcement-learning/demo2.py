
import sys
import os

# Manually set the path relative to the py file's location that you want to import 
func_lib_path = os.path.abspath(os.path.join(os.getcwd(), '../'))
# Add the path to sys.path
sys.path.append(func_lib_path)

# Now you can import func_lib
import func_lib
import random
import numpy as np
import gymnasium as gym
from collections import defaultdict

class SimpleGridEnv(gym.Env):
  metadata = {'render.modes': ['human']}

  def __init__(self, grid_size=5):
      super(SimpleGridEnv, self).__init__()
      self.grid_size = grid_size
      self.action_space = gym.spaces.Discrete(4)  # 4 actions: up, down, left, right
      self.observation_space = gym.spaces.MultiDiscrete([grid_size, grid_size])
      self.state = None
      self.goal = (grid_size - 1, grid_size - 1)

  def reset(self):
      self.state = (0, 0)
      return np.array(self.state, dtype=np.int32), {}  # gymnasium 需要返回 info 字典

  def step(self, action):
      x, y = self.state

      if action == 0:  # up
          x = max(0, x - 1)
      elif action == 1:  # down
          x = min(self.grid_size - 1, x + 1)
      elif action == 2:  # left
          y = max(0, y - 1)
      elif action == 3:  # right
          y = min(self.grid_size - 1, y + 1)

      self.state = (x, y)

      done = self.state == self.goal
      reward = 1 if done else -0.1

      return np.array(self.state, dtype=np.int32), reward, done, []
  def render(self, mode='human'):
    grid = np.zeros((self.env.grid_size, self.env.grid_size), dtype=str)
    grid[:] = '.'
    grid[self.env.goal] = 'G'
    x, y = self.env.state
    grid[x, y] = 'A'
    print("\n".join("".join(row) for row in grid))
    print()
        

class QLearningAgent:
    def __init__(self, env, learning_rate=0.1, discount_factor=0.99, epsilon=0.1):
        self.env = env
        self.q_table = defaultdict(lambda: np.zeros(env.action_space.n))
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return self.env.action_space.sample()
        else:
            return np.argmax(self.q_table[state])

    def learn(self, state, action, reward, next_state):
        best_next_action = np.argmax(self.q_table[next_state])
        td_target = reward + self.discount_factor * self.q_table[next_state][best_next_action]
        td_error = td_target - self.q_table[state][action]
        self.q_table[state][action] += self.learning_rate * td_error


def train_agent(env, agent, episodes=1000):
    for episode in range(episodes):
        state = tuple(env.reset())
        done = False
        while not done:
            action = agent.choose_action(state)
            next_state, reward, done, _ = env.step(action)
            next_state = tuple(next_state)
            agent.learn(state, action, reward, next_state)
            state = next_state
        if (episode + 1) % 100 == 0:
            print(f"Episode (episode + 1) completed")

if __name__ == "__main__":
    # 1. 创建环境和智能体
    env = SimpleGridEnv()
    agent = QLearningAgent(env)
    
    # 2. 训练阶段
    print("开始训练...")
    train_agent(env, agent, episodes=1000)
    print("训练完成！")
    
    # 3. 测试/演示阶段
    print("开始演示...")
    state = tuple(env.reset())
    done = False
    total_reward = 0
    
    while not done:
        # 渲染当前状态
        env.render()
        
        # 智能体选择动作（训练完成后应该使用贪婪策略）
        action = agent.choose_action(state, epsilon=0)  # 无探索
        
        # 执行动作
        next_state, reward, done, _ = env.step(action)
        next_state = tuple(next_state)
        
        # 更新
        state = next_state
        total_reward += reward
    
    print(f"测试结束，总奖励: {total_reward}")
    env.close()