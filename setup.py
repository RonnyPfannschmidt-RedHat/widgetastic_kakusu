from setuptools import setup

INSTALL_REQUIRES = ["attrs>=17.4.0", "more-itertools>=4.0.0"]


def main():
    setup(
        use_scm_version=True,
        setup_requires=["setuptools-scm", "setuptools>=30.3"],
        package_dir={"": "src"},
    )


if __name__ == "__main__":
    main()
