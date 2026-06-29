from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("ai_ses_requirements.txt", "r", encoding="utf-8") as f:
    requirements = [
        line.strip() for line in f
        if line.strip() and not line.startswith("#")
    ]

setup(
    name="ai-sesli-asistan",
    version="1.0.0",
    author="yasar-afk",
    description="AI destekli sesli asistan sistemi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yasar-afk/ai-sesli-asistan",
    py_modules=["main"],
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=requirements,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "ai-sesli-asistan=main:main",
        ],
    },
)
