from setuptools import setup, find_packages

setup(
    name="infosips",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests", "argparse", "logging", "urllib3", "json" # Add other dependencies if needed
    ],
    entry_points={
        "console_scripts": [
            "infosips=infosips.infosips:main",  # Allows running via `infosips` in CLI
        ],
    },
    author="DeadmanXXXII",
    author_email="themadhattersplayground@gmail.com",
    description="An ethical hacking tool for testing vulnerable SIP endpoints.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DeadmanXXXII/infosips",  # Update with your repo URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
