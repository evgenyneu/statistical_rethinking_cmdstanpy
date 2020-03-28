# Statistical Rethinking with Python, cmdstanpy and Stan

This repository contains code examples from Statistical Rethinking 2nd edition textbook done with Python and Stan languages. I ran the Stan from Python with cmdstanpy library. I will keep adding new examples as I march through the textbook.

## Setup

### 1. Download code

Assuming you have GIT package manager, download code of this repository:

```
git clone https://github.com/evgenyneu/statistical_rethinking_cmdstanpy.git
```

Change current directory:

```
cd statistical_rethinking_cmdstanpy
```



### 2. Install miniconda

Install miniconda from Python 3.7 from [here](https://docs.conda.io/en/latest/miniconda.html).


### 3. Create Conda environment

This will install Python 3.7 sanboxed conda environment called `dopestats`.

```
conda create -n dopestats python=3.7 -c conda-forge
```

### 4. Activate conda environment

Switch to the `dopestats`. You will need to do this every time you want to work with this repository code:

```
conda activate dopestats
```

### 5. Install Python libraries

Install all required libraries

```
pip install -r requirements.txt
```

### 6. Install Stan

Install Stan with

```
install_cmdstan
```

### 7. Deactivating Conda environment


This is optional. After you finish working, you can switch back to normal Python environment:

```
conda deactivate
```

## The unlicense

This work is in [public domain](LICENSE).
