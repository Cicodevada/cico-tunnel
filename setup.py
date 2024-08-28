from setuptools import setup, find_packages

setup(
    name="cico-tunnel",
    version="1.1.5",
    packages=find_packages(),
    install_requires=[
        "colorama",
    ],
    entry_points={
        "console_scripts": [
            "cicotunnel=cicotunnel.main:main",
        ],
    },
    author="Hugo Santos Lisboa",
    author_email="hugosantoslisboa@gmail.com",
    description="Expose your localhost to the web. Like a Ngrok",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/hugosantoslisboa/cico-tunnel",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
