"""
In this tutorial, we will using python's `multiproccessing` module to speed up
computations which can be done in parallel.

Recall from one of the PSETs, we investigated Monte-Carlo (MC) integration. 
We found that, for high-dimensional integrals, MC integration was much faster
than nested 1D quadratures. But suppose we would like to speed up the MC
integration. 
"""

# Import the multiprocessing library
import multiprocessing as mp


