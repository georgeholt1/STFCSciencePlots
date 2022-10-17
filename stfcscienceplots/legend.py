"""
Part of STFCSciencePlots.

Function for adding a stylised legend to axis.

Author : George Holt
Email  : george.holt@stfc.ac.uk
"""
def legend(ax, legend_kwargs=None):
    """Add a stylised legend to an axes.
    
    Parameters
    ----------
    ax : `matplotlib.axes.Axes` instance
    legend_kwargs : dict
        Dictionary of keyword arguments to be passed to `ax.legend()`.

    Returns
    -------
    legend : `matplotlib.legend.Legend`
    """
    legend = ax.legend(**legend_kwargs)
    legend.get_frame().set_alpha(None)
    legend.get_frame().set_linewidth(0.5)
    legend.get_frame().set_facecolor((1, 1, 1, 0.2))