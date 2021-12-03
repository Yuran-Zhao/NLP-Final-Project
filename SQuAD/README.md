# Question Answering Model on SQuAD 2.0 dataset
This project originated from the default final project of Stanford CS 224N. This [repository](https://github.com/minggg/squad) contains its starter code. You can read the original [introduction](https://web.stanford.edu/class/cs224n/project/default-final-project-handout.pdf) updated on February 5, 2020.

## Modification
It is worth noting that the `environment.yml` in the original repository used `pytorch 1.0.0`, which is out-dated. This code works well with `pytorch 1.7.0` after examination.

NOTE: [Line 102](https://github.com/minggg/squad/blob/3b6aa9ca5653993f0d1a49e2660c7aa6117a3d9e/layers.py#L102) in `layer.py` should be revised as:
```python
x = pack_padded_sequence(x, lengths.cpu(), batch_first=True)
```

Bisides, **NOT ALL Package** in the `environment.yml` is necessary. Specifically, what you need is:
-    python >= 3.6
-    ujson
-    numpy
-    spacy == 2.0.16. If you install a newly released spaCy (e.g. 3.2), you may need to modify the corresponding lines accroding to its [official documents](https://spacy.io/usage/models).
-    urllib3
-    tqdm
-    pytorch
-    tensorboardX. You can use `from torch.utils.tensorboard import SummaryWritter` instead in the `main.py`.


<h2 id='submission'>Submission Requirements</h2>
You need to submit:

1.    **The best-performed model you saved** after training.
2.    **All** of your python files and scripts used.
3.    **A report** describing the methods and models your team adopted, the training procedure, and their final performances.