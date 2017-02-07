from setuptools import setup

install_requires = [
    'requests>=2.4.3',
]

setup(
    name = "msger",
    version = "0.0.1",
    author = "Asahi Himura",
    author_email = "himura@nitolab.com",
    description = ("nitorikawaii"),
    license = "MIT",
    url = "https://nitolab.com",
    packages = ["msger"],
    download_url = "https://nitolab.com/archives/msger-0.0.1.tar.gz",
    install_requires = install_requires,
    classifiers = [
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        "License :: OSI Approved :: MIT License"
    ],
)

