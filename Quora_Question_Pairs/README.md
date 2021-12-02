# Quora-Question-Pairs Project
This project uses the same dataset of a competition on the Kaggle. Although it is possible for you to find solutions on the website, we HIGHLY recommend you to construct your model by yourself.

## introduction
Quora is a question-and-answer platform where question are created, answered, edited by its users. Its couterpart in China is Zhihu.

Considering the huge traffic to the website every month, there are a number of simialr questions. The goal of this project is to construct a model to judge whether two questions share the same meaning or not.

The details of dataset is shown in [Dataset](#dataset). We will intorduce the basic procedure for constructing a model in [Getting Started](#start). The submission requirements will be discussed in [Submission](#submission)

<h2 id='dataset'>Dataset</h2>
The data is provided in the .csv format. There are several fields in the dataset:

-   `question1, question2`. The full text of each question.
-   `is_duplicate`. The grand truth, set to `1` if `question1` and `question2` have essentially the same meaning, and `0` otherwise.

An typical example in the dataset looks like:
```
question1: "I got my Facebook account hacked. How can I recover my i.d.?"
question2: "My Facebook account was hacked. How can I recover my Facebook account?"
is_duplicate: "1"
```
NOTE: The original file also contains the `id` of each question. We dropped them because the utilization of this information is irrelevant to the main points of this project.

Due to we have no access to the official test file provided by Kaggle, we randomly split the train file into `train`, `valid`, and `test`. The size of each dataset is shown as follows:

| Dataset |  Size   |
| :-----: | :-----: |
|  train  | 283,010 |
|  valid  | 80,659  |
|  test   | 40,430  |


<h2 id='start'>Getting Started</h2>



<h2 id='submission'>Submission Requirements</h2>