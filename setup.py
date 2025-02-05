from setuptools import setup

setup(
    name="odd_labeler",
    version="1.0",
    py_modules=["app"],  # Name of your Python file (app.py)
    install_requires=[
        "streamlit",  # Add other dependencies as needed
        "numpy",
        "minio"
    ],
    entry_points={
        "console_scripts": [
            "oddGui = app:main",  # This lets users run `run-my-app`
        ],
    },
)
