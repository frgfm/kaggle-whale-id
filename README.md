# Kaggle whale identification challenge
This repository is a short team project about the Kaggle Whale identification [challenge](https://www.kaggle.com/c/humpback-whale-identification). 

## Requirements

The torch, torchvision, numpy, pandas and matplotlib packages are required to properly use the repo.
Tested on the following version:

```python
import sys
import torch, torchvision, numpy, pandas, matplotlib
print(f"Python {'.'.join(map(str, sys.version_info[:3]))}")
print(f"PyTorch {torch.__version__}, Torchvision {torchvision.__version__}, Numpy {numpy.__version__}, Pandas {pandas.__version__}, Matplotlib {matplotlib.__version__}")
```

```console
Python 3.6.5
PyTorch 1.0.0, Torchvision 0.2.1, Numpy 1.15.4, Pandas 0.23.4, Matplotlib 2.2.3
```

## 

## How to use it

Download the dataset, and run the training script

### Downloading the dataset

- Create a data folder within the root 
- Join the Kaggle competition (accept the terms)
- Download the dataset directly with browser download or set your [Kaggle API](https://github.com/Kaggle/kaggle-api) and run the following commands

```bash
cd data
kaggle competitions download -c humpback-whale-identification
```

- Unzip the train and test folders



## TODO

- [ ] Explanatory Data Analysis
- [ ] State-of-the-art review
- [ ] Submission implementation
- [ ] Optimization & improvements