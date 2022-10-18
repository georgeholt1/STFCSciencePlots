import os
import matplotlib.pyplot as plt
import numpy as np

from stfcscienceplots import legend as stfclegend

# Output directory
outdir = os.path.join('.', 'img')
if not os.path.isdir(outdir):
    os.makedirs(outdir)

# Data to plot and range
def sigmoid(x, w):
    return 1 / (1 + np.e ** (-w * x))

x = np.linspace(-5, 5, 1000)
vals = (0.3, 0.5, 0.9, 1.5, 3, 50)

# Plotting
def plot_fn(x, vals):
    fig, ax = plt.subplots()
    for val in vals:
        ax.plot(x, sigmoid(x, val), label=f'${{{val}}}$')
    ax.set_xlim(x.min(), x.max())
    ax.set_xlabel('$x$')
    ax.set_ylabel(r'$\frac{1}{1 + \mathrm{e}^{-wx}}$')
    stfclegend(ax, legend_kwargs={'title': '$w$'})
    return fig

with plt.style.context(['stfc']):
    fig = plot_fn(x, vals)
    fig.savefig(os.path.join(outdir, 'plot.png'))
    fig.suptitle('Style: $\mathtt{stfc}$')
    fig.savefig(os.path.join(outdir, 'stfc.png'))

with plt.style.context(['stfc', 'stfc-deep']):
    fig = plot_fn(x, vals)
    fig.suptitle(r'Style: $\mathtt{stfc\text{-}deep}$')
    fig.savefig(os.path.join(outdir, 'stfc-deep.png'))