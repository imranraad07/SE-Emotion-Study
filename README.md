# Paper: Data Augmentation for Improving Emotion Recognition in Software Engineering Communication
In the following, we briefly describe the different components that are included in this project and the software required to run the experiments.

Of the three tools we used, two of them are open-source and available here:
* EMTk: https://github.com/collab-uniba/Emotion_and_Polarity_SO
* SEntiMoji: https://github.com/SEntiMoji/SEntiMoji

You need to follow their instructions to run the models. Now we describe our code base and datasets:

## Project Structure
The project includes the following files and folders:

  - __/dataset__: A folder that contains inputs that are used for the experiments.
    - __/experiment_dataset__: A folder that contains annotated dataset, train set, and test set.
	    - annotation-set.csv: CSV file that contains 2000 annotated GitHub instances.
	    - ann-train.csv: Train subset of annotation data.
	    - ann-test.csv: Test subset of annotation data.
    - __/Augmented__: A folder that contains augmented dataset.
	    - bart-unconstrained.csv: contains Unconstrained augmented dataset.
	    - bart-lexicon.csv: contains Lexicon based augmented dataset.
	    - bart-polarity.csv: contains Polarity based augmented dataset.
  - __/crawlers__: A folder that contains the scripts we have used for data crawling.
     - githubcrawler.py: script for GitHub crawling.
 - __/data_preprocessing__: A folder that contains data preprocessing steps described in the paper section 3.2
     - data_cleaner.py: contains implementation of the various filtering such as code filtering, url fildering, stacktrace removing, etc.
     - github_modifier.py: contains implementation of dataset modifying based on functions implementing in data_cleaner.py.
 - __/data_augmentation__: A folder that contains data augmentation related scripts.
     - data_augmenter-unconstrained.py: contains implementation of Unconstrained strategy.
     - data_augmenter-lexicon.py: contains implementation of Lexicon strategy.
     - data_augmenter-polarity.py: contains implementation of Polarity strategy.
 - __/esem-e__: A folder that contains esem-e related code, data preprocessing, preprocessed datasets, and predictions.
     - svm.py: codes for the SVM model described in the esem-e model.
  - __/results__: A folder that contains the results of all tools for all experiments.
 - Annotation Instructions.docx: contains the annotation instructions that the annotators used.
 - requriments.txt: contains the The python libraries used in this experiment.

## Setup
1. setup virtual environment and activate it
2. `pip install -r requirements.txt'
