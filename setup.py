from setuptools import setup

with open("README.md", 'r', encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="Sales_Forecast",
    version= "0.0.1",
    author= "AAZZIOUI",
    description= "A package for Sales prediction using ML and dvc for retraining",
    long_description= long_description,
    long_description_content_type = "text/markdown",
    url= "https://github.com/AAZZIOUI/Sales_Forecast",
    author_email="anas.azzioui@gmail.com",
    packages=["src"],
    license= "GNU",
    python_requires= ">=3.6",
    install_requires= [
        'dvc',
        'pandas',
        'scikit-learn',
        'Flask',
        'Flask-Cors',
        'Flask-MonitoringDashboard',
        'tqdm',
        'PyYAML',
        'matplotlib'
    ]
)