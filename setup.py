import os
from setuptools import setup, find_packages

NAME = "ebay_jka_cnn"
CURRENT_DIR = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(CURRENT_DIR, NAME.replace("-", "_"), "__version__.py")) as f:
    exec (f.read(), about)

version = about["__version__"]

REQUIRED = [
        "gensim==3.8.1",
        "nltk==3.4.5",
        "numpy==1.17.4",
        "pandas==0.24.2",
        "scikit-learn==0.21.3",
        "scipy==1.3.2",
        "sklearn==0.0",
        "tensorboard==1.12.2",
        "tensorflow==2.11.1",
        "termcolor==1.1.0"
        ]

setup(
    name=NAME,
    version=version,
    description="Ebay Content Risk Convolutional Neural Network Model",
    url="https://github.com/g2webservices/jka-ebay-content-classification-cnn",
    author="G2 Data Science",
    author_email="datascience@g2llc.com",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "ebay_jka_cnn": [
            "data/*"
        ]
    },
    install_requires=REQUIRED
)
