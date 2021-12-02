# Quora-Question-Pairs Project
This project uses the same dataset of a competition on the Kaggle. Although it is possible for you to find solutions on the website, we HIGHLY recommend you to construct your model by yourself.

## introduction
Quora is a question-and-answer platform where question are created, answered, edited by its users. Its couterpart in China is Zhihu.

Considering the huge traffic to the website every month, there are a number of simialr questions. The goal of this project is to construct a model to judge whether two questions share the same meaning or not. You are excepted to tackle this problem by using what you've learned in the class, i.e., **the pre-trained language models in NLP**, including BERT, RoBERTa, to name but a few.

The details of dataset is shown in [Dataset](#dataset). We will intorduce the basic procedure for constructing a model in [Getting Started](#start). The submission requirements will be discussed in [Submission](#submission)

<h2 id='dataset'>Dataset</h2>
Each line in the dataset responds to an example, which contains 3 parts separated by `\t`:

-   `question1, question2`. The full text of each question.
-   `label`. The grand truth, set to `1` if `question1` and `question2` have essentially the same meaning, and `0` otherwise.

A typical example in the dataset looks like:
```
I got my Facebook account hacked. How can I recover my i.d.?    My Facebook account was hacked. How can I recover my Facebook account?    1
```

NOTE: The original file also contains the `id` of each question. We dropped them because the utilization of this information is irrelevant to the main points of this project.

Due to we have no access to the official test file provided by Kaggle, we randomly split the train file into `train.txt`, `valid.txt`, and `test.txt`. The size of each dataset is shown as follows:

| Dataset |  Size   |
| :-----: | :-----: |
|  train  | 282,995 |
|  valid  | 80,855  |
|  test   | 40,429  |


<h2 id='start'>Getting Started</h2>



<h2 id='submission'>Submission Requirements</h2>