# pymfe: Python Meta-Feature Extractor
[![Build Status](https://travis-ci.org/ealcobaca/pymfe.svg?branch=master)](https://travis-ci.org/ealcobaca/pymfe)
[![codecov](https://codecov.io/gh/ealcobaca/pymfe/branch/master/graph/badge.svg)](https://codecov.io/gh/ealcobaca/pymfe)
[![Documentation Status](https://readthedocs.org/projects/pymfe/badge/?version=latest)](https://pymfe.readthedocs.io/en/latest/?badge=latest)
[![PythonVersion](https://img.shields.io/pypi/pyversions/pymfe.svg)](https://www.python.org/downloads/release/python-370/)
[![Pypi](https://badge.fury.io/py/pymfe.svg)](https://badge.fury.io/py/pymfe)


Extracts meta-features from datasets to support the design of recommendation systems based on Meta-Learning (MtL). The meta-features are able to characterize the complexity of datasets and to provide estimates of algorithm performance. The package contains not only the standard, but also more recent characterization measures. By making available a large set of meta-feature extraction functions, this package allows a comprehensive data characterization, a deep data exploration and a large number of MtL-based data analysis.

## Measures

In MtL, meta-features are designed to extract general properties able to characterize datasets. The meta-feature values should provide relevant evidences about the performance of algorithms, allowing the design of MtL-based recommendation systems. Thus, these measures must be able to predict, with a low computational cost, the performance of the  algorithms under evaluation. In this package, the meta-feature measures are divided into six groups:

* **General**: General information related to the dataset, also known as simple measures, such as number of instances, attributes and classes.
* **Statistical**: Standard statistical measures to describe the numerical properties of a distribution of data.
* **Information-theoretic**: Particularly appropriate to describe discrete (categorical) attributes and their relationship with the classes.
* **Model-based**: Measures designed to extract characteristics like the depth, the shape and size of a Decision Tree (DT) model induced from a dataset.
* **Landmarking**: Represents the performance of simple and efficient learning algorithms. Include the subsampling and relative strategies to decrease the computation cost and enrich the relations between these meta-features (relative and subsampling landmarking are also available).
* **Clustering:** Clustering measures extract information about dataset based on external validation indexes.

## Dependencies

The main `pymfe` requirement is:
* Python (>= 3.6)

## Installation

The installation process is similar to other packages available on pip:

```python
pip install -U pymfe
```

It is possible to install the development version using:

```python
pip install -U git+https://github.com/ealcobaca/pymfe
```

or

```
git clone https://github.com/ealcobaca/pymfe.git
cd pymfe
python3 setup.py install
```

## Example of use

The simplest way to extract meta-features is instantiating the `MFE` class. The parameters are the measures, the group of measures and the summarization functions to be extracted. The default parameter is extract all the measures. The `fit` function can be called by passing the `X` and `y`. The `extract` function is used to extract the related measures. A simple example is given next:

```python
# Load a dataset
from sklearn.datasets import load_iris
from pymfe.mfe import MFE

data = load_iris()
y = data.target
X = data.data

# Extract all measures
mfe = MFE()
mfe.fit(X, y)
ft = mfe.extract()
print(ft)

# Extract general, statistical and information-theoretic measures
mfe = MFE(groups=["general", "statistical", "info-theory"])
mfe.fit(X, y)
ft = mfe.extract()
print(ft)
```

Several measures return more than one value. To aggregate the returned values, summarization function can be used. This method can compute `min`, `max`, `mean`, `median`, `kurtosis`, `standard deviation`, among others. The default methods are the `mean` and the `sd`. Next, it is possible to see an example of the use of this method:

```python
## Extract all measures using min, median and max 
mfe = MFE(summary=["min", "median", "max"])
mfe.fit(X, y)
ft = mfe.extract()
print(ft)
                          
## Extract all measures using quantile
mfe = MFE(summary=["quantiles"])
mfe.fit(X, y)
ft = mfe.extract()
print(ft)
```

It is possible to pass custom arguments to every metafeature using MFE `extract` method kwargs. The keywords must be the target metafeature name, and the value must be a dictionary in the format {`argument`: `value`}, i.e., each key in the dictionary is a target argument with its respective value. In the example below, the extraction of metafeatures `min` and `max`  happens as usual, but the metafeatures `sd,` `nr_norm` and `nr_cor_attr` will receive user custom argument values, which will interfere in each metafeature result.

```python
# Extract measures with custom user arguments
mfe = MFE(features=["sd", "nr_norm", "nr_cor_attr", "min", "max"])
mfe.fit(X, y)
ft = mfe.extract(
    sd={"ddof": 0},
    nr_norm={"method": "all", "failure": "hard", "threshold": 0.025},
    nr_cor_attr={"threshold": 0.6},
)
print(ft)
```

## Documentation
We write a great Documentation to guide you on how to use the pymfe library. You can find the Documentation in this [link](https://pymfe.readthedocs.io/en/latest/?badge=latest).
You can find in the documentation interesting pages like:
* [Getting started](https://pymfe.readthedocs.io/en/latest/install.html)
* [API documentation](https://pymfe.readthedocs.io/en/latest/api.html)
* [Examples](https://pymfe.readthedocs.io/en/latest/auto_examples/index.html)
* [News about pymfe](https://pymfe.readthedocs.io/en/latest/new.html)

## Developer notes

* We are glad to accept any contributions, please check [Contributing](https://github.com/ealcobaca/pymfe/blob/master/CONTRIBUTING.md) and the [Documentation](https://pymfe.readthedocs.io/en/latest/?badge=latest).
* To submit bugs and feature requests, report at [project issues](https://github.com/ealcobaca/pymfe/issues).
* In the current version, the meta-feature extractor supports only classification problems. The authors plan to extend the package to add clustering and regression measures and to support MtL evaluation measures. For more specific information on how to extract each group of measures, please refer to the functions documentation page and the examples contained therein. For a general overview of the `pymfe` package, please have a look at the associated documentation.

## License

This project is licensed under the MIT License - see the [License](LICENSE) file for details.

## Cite Us

If you use the `pymfe` or [`mfe`](https://github.com/rivolli/mfe) in scientific publication, we would appreciate citations to the following paper:
```
@article{}
```

## Acknowledgments
We would like to thank every [Contributor](https://github.com/ealcobaca/pymfe/graphs/contributors) directly or indirectly has helped this project to happen. Thank you all.

## References
 
1. Rivolli, A., Garcia, L. P. F., Soares, C., Vanschoren, J., and de Carvalho, A. C. P. L. F. (2018). Towards Reproducible Empirical Research in Meta-Learning. arXiv:1808.10406.
2. Pinto, F., Soares, C., & Mendes-Moreira, J. (2016, April). Towards automatic generation of metafeatures. In Pacific-Asia Conference on Knowledge Discovery and Data Mining (pp. 215-226). Springer, Cham.
3. Brazdil, P., Carrier, C. G., Soares, C., & Vilalta, R. (2008). Metalearning: Applications to data mining. Springer Science & Business Media.
