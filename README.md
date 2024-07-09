# MNISTConverter-Python

When you are browsing various Machine Learning code examples, it is likely that you will come across a piece of code like this:

```python
from keras.datasets import mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
```

The Python code above is a common way to load data using the Keras library in Python.

The `datasets` module in Keras provides access to several well-known datasets pre-loaded and formatted in a way that makes them easy to use directly in machine learning models. This module is part of the high-level Keras API.

The `mnist.load_data()` function specifically deals with the MNIST dataset, which is a large database of handwritten digits commonly used for training various image processing systems. It downloads the MNIST dataset from a remote repository if it's not already present on the local machine, and then loads it into memory.

The MNIST data is typically hosted on Yann LeCun’s website. Keras's `mnist.load_data()` function has the URL hardcoded and downloads the data from this URL if it's not found in the local cache. Once downloaded, the data is stored locally in a cache directory.

This function is extremely useful for quickly setting up benchmarks or teaching examples because it abstracts away all the details of data handling, preprocessing, and storage. For someone learning machine learning or testing different image processing models, it provides a straightforward and hassle-free way to get started with real data.

That is why it is more than likely that you will come across this line of code.

It's all good and dandy if you are working with Python, but what if you are working with ML.NET?

ML.NET does not support this format, so you need the data in CSV format. To accomplish this task, you need to download the MNIST dataset, preprocess the data and then load the data into ML.NET.

You can download the data from Yann LeCun's website: [http://yann.lecun.com/exdb/mnist/](http://yann.lecun.com/exdb/mnist/)

If that link does not work or the files are not available, try this one: [https://github.com/cvdfoundation/mnist](https://github.com/cvdfoundation/mnist)

Since the raw MNIST data comes in a binary format that is not immediately usable in ML.NET, our goal here is to convert this data into a more accessible format like CSV or a set of image files.

This is the Python version of the converter. There is also a .NET version available.

Here is the blog article: [https://tjgokcen.com/converting-minst-data-to-csv-or-individual-files-using-python](https://tjgokcen.com/converting-minst-data-to-csv-or-individual-files-using-python)
