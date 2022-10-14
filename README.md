Science Plots
=============

*Matplotlib styles for scientific figures using STFC style*

This repo has Matplotlib styles to format your figures for scientific papers, presentations and theses following the Science and Technology Facilities Council (STFC) style. It is a fork of garrettj403's [SciencePlots](https://github.com/garrettj403/SciencePlots).

Getting Started
---------------

The easiest way to install SciencePlots is by using `pip`:

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
- SciencePlots requires Latex ([see Latex installation instructions](https://github.com/garrettj403/SciencePlots/wiki/FAQ#installing-latex)). 
- If running on Linux, you may need to explicitly install the Arial font. See the [mscorefonts](https://anaconda.org/conda-forge/mscorefonts) package.

The [SciencePlots FAQ](https://github.com/garrettj403/SciencePlots/wiki/FAQ) may be useful for more information and troubleshooting.

Using the Styles
----------------

``"science"`` is the primary style in this repo. Whenever you want to use it, simply add the following to the top of your python script:

```python
import matplotlib.pyplot as plt

plt.style.use('science')
```

You can also combine multiple styles together by:

```python
plt.style.use(['science','ieee'])
```

In this case, the ``ieee`` style will override some of the parameters from the ``science`` style in order to configure the plot for IEEE papers (column width, fontsizes, etc.).

To use any of the styles temporarily, you can use:

```python
with plt.style.context('science'):
    plt.figure()
    plt.plot(x, y)
    plt.show()
```

Examples
--------



