import matplotlib.pyplot as plt
from read_write_array import *

def plot_graphs(arr, metric):
  plt.cla()
  plt.plot(arr)
  plt.xlabel("Epochs")
  plt.ylabel(metric)
  plt.legend([metric])
  plt.savefig('train_history')

if __name__ == '__main__':
  plot_graphs(read_arr('./history/loss_history.csv'), 'loss')
