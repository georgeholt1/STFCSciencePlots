STFC Science Plots
==================

*Matplotlib styles for scientific figures using STFC style*

<p align="center">
<img src="https://github.com/georgeholt1/STFCSciencePlots/blob/master/examples/img/plot.png" width="500">
</p>

This repo has Matplotlib styles to format your figures for scientific papers, presentations and theses following the Science and Technology Facilities Council (STFC) style. It is a fork of garrettj403's [SciencePlots](https://github.com/garrettj403/SciencePlots).

Getting Started
---------------

The easiest way to install STFCSciencePlots is by using `pip`:

```bash
# to install the latest commit (from GitHub)
pip install git+https://github.com/georgeholt1/STFCSciencePlots

# to clone and install from a local copy
git clone https://github.com/georgeholt1/STFCSciencePlots
cd SciencePlots
pip install -e .
```

The pip installation will automatically move all of the Matplotlib style files `*.mplstyle` into the appropriate directory on your computer.

**Notes:** 
- STFCSciencePlots requires Latex ([see Latex installation instructions](https://github.com/garrettj403/SciencePlots/wiki/FAQ#installing-latex)). 
- If running on Linux, you may need to explicitly install the Arial font. See the [mscorefonts](https://anaconda.org/conda-forge/mscorefonts) package.

The [SciencePlots FAQ](https://github.com/garrettj403/SciencePlots/wiki/FAQ) may be useful for more information and troubleshooting.

Using the Styles
----------------

``"stfc"`` is the primary style in this repo. Whenever you want to use it, simply add the following to the top of your python script:

```python
import matplotlib.pyplot as plt

plt.style.use('stfc')
```

To use any of the styles temporarily, you can use:

```python
with plt.style.context('stfc'):
    plt.figure()
    plt.plot(x, y)
    plt.show()
```

Using the Function Replacements
-------------------------------

Some functions designed to replace Matplotlib methods are also contained in this library. Their usage is documented in their docstrings. Typically, a matplotlib object must be passed as an argument, and keyword arguments to be forwarded to the matplotlib function call are supplied in a keyword argument dictionary. For example, to use the `legend` replacement function:

```python
# Import as usual
from stfcscienceplots import legend as stfclegend
plt.style.use('stfc')

# Load/generate/whatever some data
x = # data
y = # data

# Plot using the OOP API
fig, ax = plt.subplots()
ax.plot(x, y, label='data')

# Instead of calling ax.legend():
stfclegend(ax, legend_kwargs={'title': 'Legend'})
```

Examples
--------

See `examples/plot_examples.py`.

<p align="center">
<img src="https://github.com/georgeholt1/STFCSciencePlots/blob/master/examples/img/stfc.png" width="500">
</p>

<p align="center">
<img src="https://github.com/georgeholt1/STFCSciencePlots/blob/master/examples/img/stfc-deep.png" width="500">
</p>