comment on findings from perf_plot.png:

Without the use of numpy, 'perf_plot.png':



As the number of iteration steps increases, the time to produce the tree 
increases exponentially. This will cause significant problems as the size of
 Flamel's trees increase.


Using numpy, 'perf_plot_np.png':
As the number of iteration steps increases, the time to produce the tree also increases exponentially, but at a higher number of iterations, the performance plot appears linear until approximately 16 iterations. This reduces the problems seen in tree.py, making tree_np.py a more appropriate approach when a large number of iterations are needed.

The original version and numpy version plots cross at around 11 iteratons. It could therefore be concluded that when the number of iterations < 11, we should use 'tree.py', and when iterations > 11, we should use 'tree_np.py'
  