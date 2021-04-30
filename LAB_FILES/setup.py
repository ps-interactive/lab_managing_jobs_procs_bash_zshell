from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        setup_requires=['setuptools_scm'],
        use_scm_version=True,
    )
