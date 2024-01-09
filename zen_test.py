from pycounts_merete.pycounts_merete import count_words
count_words("zen.txt")

from pycounts_merete.pycounts_merete import count_words
from pycounts_merete.plotting import plot_words
counts = count_words("zen.txt")
fig = plot_words(counts, 10)

import matplotlib.pyplot as plt
plt.show()