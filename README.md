## About
This repository includes some key project files for the Topics in Computer Science project, 'Automated diagnosis of coronary artery disease from electrocardiograms using machine learning'.


## Setup
Each of the notebooks make use of one or more datasets which can be downloaded from [PhysioNet](https://physionet.org/). Of these, the PTB database is largely optional. The following are the directory names referenced throughout the notebooks, supplemented with the dataset they correspond to.

- `ptbxl/`: [PTB-XL](https://physionet.org/content/ptb-xl/1.0.1/)
- `ptbdb/`: [PTB Diagnostic ECG Database](https://physionet.org/content/ptbdb/1.0.0/)
- `st-petersburg/`: [St Petersburg INCART 12-lead Arrhythmia Database](https://physionet.org/content/incartdb/1.0.0/)


## Dependencies
Not all of the following are necessary for each Jupyter Notebook. It is recommended to install these as required. Using an Anaconda virtual environment is also recommended.

- keras (2.9.0)
- keras-tuner (1.1.3)
- matplotlib (3.5.1)
- numpy (1.23.1)
- padasip (1.2.2)
- pandas (1.4.3)
- pywavelets (1.3.0)
- scikit-learn (1.1.1) 
- scipy (1.7.3)
- tensorflow (2.9.1)
- wfdb (4.0.0)