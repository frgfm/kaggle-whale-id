# Review of publicly available implementations
Summary of existing github repo, articles, Kaggle kernels that achieve interesting performances (excluding ensembling approached for now)



## No Deep Learning

Implementations that do not involve deep learning techniques (classic computer vision approaches such as descriptors, etc.)

- Name of the resource ([link](https://www.google.com/)): *short explanation of core implementation ideas*



## Deep Learning without convolution

Implementations that only involve non-convolutional layers

- Improving fully-connected layer [link](https://openreview.net/pdf?id=1WvovwjA7UMnPB1oinBL): two approaches focused on improving fully-connected layers:linear bottleneck layers and unsupervised pre-training using autoencoders without hidden unit biases



## CNN without pretrained models

Implementations that involve CNN but no pretrained models

- Name of the resource ([link](https://www.google.com/)): *short explanation of core implementation ideas*



## Customization of pretrained models

Implementations that involve common Imagenet pretrained models

- ResNeXt ([link](https://www.kaggle.com/stalkermustang/pytorch-pretraiedmodels-se-resnext101-baseline/notebook)): *resnext101 is a simple, highly modularized network architecture for image classification. Our network is constructed by repeating a building block that aggregates a set of transformations with the same topology. Our simple design results in a homogeneous, multi-branch architecture that has only a few hyper-parameters to set. This strategy exposes a new dimension, which we call “cardinality” (the size of the set of transformations), as an essential factor in addition to the dimensions of depth and width.*
- VGG16 [link](https://www.kaggle.com/gimunu/training-augmentation-and-pretrained-vgg16-model): kernel from the last challenge which used pretrained VGG16.. no comments or discussion provided though.
- Resnet34 [link](https://github.com/kheyer/ML-DL-Projects/blob/master/Kaggle%20Humpback/Kaggle_Humpback_Whale_Identification_Challenge_Writeup.ipynb): complete solution (from setup to submission) using pretrained resnet34 from a past humpback whale competition
- Implementation in github for whale identification: [link](https://github.com/rumaak/humpback_whale_fastai/blob/master/Image%20classifier.ipynb)

## Other
<<<<<<< Updated upstream
EDA and other transformations: ([link](https://spark-in.me/post/playing-with-dwt-and-ds-bowl-2018))
Kaggle kernels collection [link](https://www.kaggle.com/shivamb/data-science-glossary-on-kaggle): covers algorithms, pytorch, DL, pretrained models
=======
EDA and other transformations: ([link](https://spark-in.me/post/playing-with-dwt-and-ds-bowl-2018)
- Siamese Networks Part1: [link](https://hackernoon.com/one-shot-learning-with-siamese-networks-in-pytorch-8ddaab10340e) : Siamese networks: special type of neural network architecure focused on differentiating between two inputs.
- Siamese Networks Part2: [link](https://hackernoon.com/facial-similarity-with-siamese-networks-in-pytorch-9642aa9db2f7) 
>>>>>>> Stashed changes
