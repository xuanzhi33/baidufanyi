from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="baidufanyi",
    version="0.2.5",
    author="xuanzhi33",
    author_email="xuanzhi33@qq.com",
    url="https://github.com/xuanzhi33/baidufanyi",
    description="A simple SDK for the Baidu Translation API (unofficial)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    license="GPL-3.0",
    install_requires=["requests"],
    packages=find_packages(),
    python_requires=">=3.6"
)
