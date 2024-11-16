from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mlchain-client",
    version="0.1.12",
    author="Mlchain",
    author_email="hello@mlchain.khulnasoft.com",
    description="A package for interacting with the Mlchain Service-API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mlchain/mlchain",
    license="MIT",
    packages=["mlchain_client"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["requests"],
    keywords="mlchain nlp ai language-processing",
    include_package_data=True,
)
