# Question Answering Model on SQuAD 2.0
This project originated from the default final project of Stanford CS 224N. This [repository](https://github.com/minggg/squad) contains its starter code. You can read the original [introduction](https://web.stanford.edu/class/cs224n/project/default-final-project-handout.pdf) updated on February 5, 2020.

It is worth noting that you may have to revise a few places in the code. The details are shown in [Changes](#changes). You need to pay attention to the requirements in [Evaluation](#evaluation). And the requirements for submission is introduced in [Submission Requirements](#submission).


<h2 id='changes'>Changes</h2>

The version of PyTorch in the `environment.yml` is `pytorch 1.0.0`, which is out-dated. This code works well with `pytorch 1.7.0` after examination. So you can choose a higher version than `1.0.0`.

If you run the code with a GPU, [Line 102](https://github.com/minggg/squad/blob/3b6aa9ca5653993f0d1a49e2660c7aa6117a3d9e/layers.py#L102) in `layer.py` should be revised as:
```python
x = pack_padded_sequence(x, lengths.cpu(), batch_first=True)
```

Bisides, **NOT ALL** Package in the `environment.yml` is necessary. Specifically, what you need is:
-    python >= 3.6
-    ujson
-    numpy
-    spacy == 2.0.16
     
     If you install a newly released spaCy (e.g. 3.2), you may need to modify >the corresponding lines accroding to its [official documents](https://>spacy.io/usage/models).
-    urllib3
-    tqdm
-    pytorch

     You may need to pick up the appropriate version of cudatoolkit if you have access to GPUs. You can check the version information on the [PyTorch website](https://pytorch.org/get-started/previous-versions/).

-    tensorboardX

     This one is not always needed. Actually, you can use `from torch.utils.tensorboard import SummaryWritter` instead of `from tensorboardX import SummaryWritter` in the `main.py` and `test.py`.

You're encouraged to use `conda` to manage these packages in case of inconsistency problems.


<h2 id='evaluation'>Evaluation</h2>

Because we have no access to the answers of `test` set, we will evaluate your model on the `dev` set. 

Similarly, we also use F1 score as the performance metric.

The BiDAF model in the starter code trained after 30 epochs can achieve:
| Model |  F1   |  EM   | AvNA  |  NLL  |
| :---: | :---: | :---: | :---: | :---: |
| BiDAF | 61.59 | 58.29 | 68.07 | 3.08  |


<h2 id='submission'>Submission Requirements</h2>

You need to submit:

1.    **The best-performed model you saved** after training.
2.    **All** of your python files and scripts used.
3.    **A report** describing the methods and models your team adopted, the training procedure, and their final performances.