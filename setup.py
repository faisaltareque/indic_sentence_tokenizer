from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="indic_sentence_tokenizer",
    description="Sentence Tokenizer for Indic Language",
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License"
    ],
    install_requires=[
        "pandas",
        "numpy",
    ],
    extras_require ={
        "dev":[
            "pytest >=3.7",
        ]
    },
    python_requires='>=3.6',
)
