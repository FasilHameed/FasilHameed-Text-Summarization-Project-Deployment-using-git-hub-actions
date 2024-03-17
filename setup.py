import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

SRC_REPO = "textSummarizer"
REPO_NAME = "Text-Summarization-Project-Deployment-using-git-hub-actions"
AUTHOR_USER_NAME = "FasilHameed"
AUTHOR_EMAIL = "faisalhameed763@gmail.com"
__version__ = "0.0.0"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A text Summarizer app",
    long_description=long_description,
    long_description_content_type="text/markdown",  # corrected parameter name
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)
