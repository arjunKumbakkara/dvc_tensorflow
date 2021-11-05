from setuptools import setup


with open("README.md", "r",encoding="utf-8") as f:
    long_description= f.read()


setup(
    name ="src",
    version ="0.0.1",
    author ="arjunKumbakkara",
    description="A small package for dvc ml pipeline demo for beginner boilerplate",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arjunKumbakkara/dvc_tensorflow",
    author_email="arjunkumbakkara@gmail.com",
    packages=["src"],
    license="GNU",
    python_requires=">=3.7",
    install_requires=[
        "dvc",
        "tensorflow",
        "matplotlib",
        "numpy",
        "pandas",
        "tqdm",
        "pyYAML",
#Boto is for aws: s3  command line access integration
        "boto3"
    ]

)