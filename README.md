# Statistical Rethinking with Python, cmdstanpy and Stan

This repository contains code examples from Statistical Rethinking 2nd edition textbook done with Python and Stan languages. I ran the Stan from Python with cmdstanpy library. I will keep adding new examples as I march through the textbook.

## Setup

### 1. Download code

Download code of this repository:

```
https://github.com/evgenyneu/statistical_rethinking_cmdstanpy.git
```

Change current directory:

```
cd statistical_rethinking_cmdstanpy
```



### 2. Install miniconda

Install miniconda from Python 3.7 from [here](https://docs.conda.io/en/latest/miniconda.html).


### 3. Create Conda environment

This will install Python 3.7 and all required packages inside a sanboxed conda environment called `dopestats`.

```
conda create -n dopestats python=3.7 -c conda-forge --file requirements.txt
```

### 4. Activate conda environment

Switch to the `dopestats`.

```
conda activate dopestats
```

After you finish working, you can switch back to normal Python environment:

```
conda deactivate
```

## The unlicense

This work is in [public domain](LICENSE).
