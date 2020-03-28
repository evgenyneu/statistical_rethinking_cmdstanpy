# Statistical Rethinking with Python, cmdstanpy and Stan

This repository contains code examples from [Statistical Rethinking](https://xcelab.net/rm/statistical-rethinking/) 2nd edition textbook done with Python and Stan languages. I ran the Stan from Python with cmdstanpy library. I will keep adding new examples to [code/chapters](code/chapters) directory as I march through the textbook.

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

This will install Python 3.7 conda environment called `dopestats`.

```
conda create -n dopestats python=3.7 -c conda-forge
```

### 4. Activate conda environment

Switch to the `dopestats`. You will need to do this every time you want to work with this repository code:

```
conda activate dopestats
```

### 5. Install Python libraries

Install all required libraries. The libraries will be installed inside your active `dopestats` conda environment. This way, it will not pollute your normal Python environment, which may have different versions of the same libraries:

```
pip install -r requirements.txt
```

### 6. Install Stan

Finally, download and install Stan with this command:

```
install_cmdstan
```

### 7. Deactivating Conda environment

This is optional. After you finish working, you can switch back to your normal Python environment:

```
conda deactivate
```


## Running the code

The textbook example are located in separate Python files inside [code/chapters](code/chapters) directory. To run an example, `cd` to the relevant chapter sub-directory and run the script.

For example, change to the second chapter sub-directory:

```
cd code/chapters/ch02
```

And run the script for 2.1 example:

```
python ex02.01.py
```

## The unlicense

This work is in [public domain](LICENSE).
