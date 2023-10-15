# Malware-Detection-using-Machine-Learning
Blog: https://kiiocity.wordpress.com/2022/05/08/anomaly-based-malware-detection-1/

With the rapid development of the Internet, malware became one of the major cyber threats nowadays. Any software performing malicious actions, including information stealing, espionage, etc. can be referred to as malware. Kaspersky Labs (2017) define malware as “a type of computer program designed to infect a legitimate user's computer and inflict harm on it in multiple ways.”.

While the diversity of malware is increasing, anti-virus scanners cannot fulfil the needs of protection, resulting in millions of hosts being attacked. According to Kaspersky Labs (2016), 6,563,145 different hosts were attacked, and 4,000,000 unique malware objects were detected in 2015. In turn, Juniper Research (2016) predicts the cost of data breaches to increase to $2.1 trillion globally by 2019.

In addition to that, there is a decrease in the skill level that is required for malware development, due to the high availability of attacking tools on the Internet nowadays. High availability of anti-detection techniques, as well as ability to buy malware on the black-market result in the opportunity to become an attacker for anyone, not depending on the skill level. Current studies show that more and more attacks are being issued by script-kiddies or are automated. (Aliyev 2010).

Malware detection through standard, signature-based methods is getting increasingly difﬁcult since all current malware applications tend to have multiple polymorphic layers to avoid detection or to use side mechanisms to automatically update themselves to a newer version at short periods of time to avoid detection by any antivirus software.

Machine learning helps antivirus software detect new threats without relying on signatures. In the past, antivirus software relied largely on fingerprinting, which works by cross-referencing files against a huge database of known malware.

The major flaw here is that signature checkers can only detect malware that has been seen before. That’s a rather large blind spot, given that hundreds of thousands of new malware variants are created every single day. Machine learning, on the other hand, can be trained to recognize the signs of good and bad files, enabling it to identify malicious patterns and detect malware –
regardless of whether it’s been seen before or not.

## Objective
As stated before, Malware detectors that are based on signatures can perform well on previously-known malware, that was already discovered by some anti-virus vendors. However, it is unable to detect polymorphic malware, that has the ability to change its signatures, as well as new malware, for which signatures have not been created yet. In turn, the accuracy of heuristics-based detectors is not always sufficient for adequate detection, resulting in a lot of false positives and false negatives. (Baskaran and Ralescu 2016). The need for the new detection methods is dictated by the high spreading rate of polymorphic viruses.

## Dataset
PE Header: https://www.kaggle.com/datasets/dscclass/malware

URL: 

## Organisation
![image](https://user-images.githubusercontent.com/34811605/148759818-65e2c0ee-c91e-4ef8-b8d1-b8d037a213c3.png)

## Existing Methods

Although not widely implemented, the concept of machine learning methods for malware detection is not new. Several types of studies were carried out in this field, aiming to figure the accuracy of different methods.

In his paper “Malware Detection Using Machine Learning” Dragos Gavrilut aimed for developing a detection system based on several modified perceptron algorithms. For different algorithms, he achieved the accuracy of 69.90%- 96.18%. It should be stated that the algorithms that resulted in best accuracy also produced the highest number of false-positives: the most accurate one resulted in 48 false positives. The most balanced algorithm with appropriate accuracy and the low false-positive rate had the accuracy of 93.01%. (Gavrilut,et al. 2009)

“A Static Malware Detection System Using Data Mining Methods” proposed extraction methods based on PE headers, DLLs and API functions and methods based on Naive Bayes, J48 Decision Trees, and Support Vector Machines. Highest overall accuracy was achieved with the J48 algorithm (99% with PE header feature type and hybrid PE header & API function feature type, 99.1% with API function feature type). (Baldangombo, Jambaljav and Horng 2013)

## Specific Project requirements

###	Data Requirement
The two data set that we have used in this project can be found in Kaggle.com
While installing/running this project, the used does not need to install the module from Kaggle, it is already provided in the project file.

###	Functional Requirement
Modules used (while installation):
- sklearn 0.24.1
-	pyfiglet 0.8.post1
-	pefile
-	joblib 1.1.0

###	Look and Feel Requirement

As the whole project’s interface is terminal based and the only visuals we used is in the main screen, so only for printing the ASCII art on the home screen the user needs to install pyfiglet which is a python library which converts the strings to ASCII art.

## Architecture Design
![image](https://user-images.githubusercontent.com/34811605/148760268-2f1a81da-ac45-402b-8135-21d2ac7fe2f1.png)

## User Interface Design
![image](https://user-images.githubusercontent.com/34811605/148760302-775ef62e-f0dd-4586-9c1a-64bed1234f7d.png)

![image](https://user-images.githubusercontent.com/34811605/148760317-b7afa5e7-01b5-4656-8520-a95f37f544bd.png)

![image](https://user-images.githubusercontent.com/34811605/148760334-257e2fd8-541b-4916-8e4e-9047e65c2f99.png)

## Technical Coding and code solutions

###	PE-header-based malware detection

The main part of this project is the machine learning model in which we used Random Forest classifier tree to classify the malware/benign files. The dataset that we are using contains 70.1% malwares and 29.9% benign files.

As per the splitting part goes, we divided the data into 70% training data and 30% testing data and then we selected the important features that are required for the classification using the extratrees.feature_importances_ function and then we compared the score of Decision Tree Classifier and Random Forest classifier and found that Random Forest Classifier’s score (99.45%) is better than Decision Tree Classifier (99.04%), hence we selected it for training and then after training we saved it as Classifier.pkl and also saved the features that we found important as features.pkl to keep track of the required function while extracting it from any real file.
 
After the Machine Learning part comes the file extraction part in which we extract the features that are required for the classification. The major challenge that we faced while coding this project was to extract the features of the PE Header file and then storing it for the saved machine learning model. For extracting the content of the PE Header we used pefile library (https://pypi.org/project/pefile/). The selection of those features is done using the feature.pkl model that stores all the important features for the Random Forest Classifier. The extraction of the PE Header files is done using pefile library in python and then the selected features are then given to the classifier.pkl machine and it predicts the output.

###	Malicious URL detection

This part of the program also consists of two phases, Cleaning the data for the Logistic Regression and then training the machine to identify if it is malicious or not. The Model is sketched out in such a way that it can meaningfully understand the data from which it has to be trained upon and tried to develop a defined behaviour from the data-sets. Data-sets are the backbone of any model and hence it should be adequate and precise data for good as well as bad URLs present in the data for the model to be trained upon. The Machine Learning for the malicious website detection will first involve in cleaning of our data within the data-sets. We used pandas and defined our own vectorizer to clear the data-sets and then used Logistic Regression to train our model.

Since the URLs are different from our normal text documents, a sanitization method is used to get the relevant data from raw URLs.
 
We will implement our sanitization function in python to filter the URLs. This will give us the desired URL data-set values to train the model and test it. The data-set will have two column structure one for URLs and other for labels (malicious or not).

Then we used Tf-idf machine learning text feature extraction approach from the sklearn python module. Before that we need to read the data-sets into data frames and matrix which can be understood by the vectorizer we prepared and later pass onto the term-frequency and inverse document frequency text extraction approach. We used pandas module in python for that task. As stated above we used logistic regression method to train our model but before that we passed the data to our custom vectorizer function using Tf-idf approach and after that we can train and test our ML model.

Still the model was not able to predict all the good URLs and hence club good URLs with bad URLs so we used the classical method of URL filtering with conjunction to the machine learning model i.e., Whitelist Filter. It is the list of websites that we know are good and at-least non-malicious and won’t harm our users. So, we allow these particular websites through our internet traffic, the opposite is called as blacklisting. It’s a very simple but efficient approach to segregate our network traffic, similarly we implemented that in our machine learning model.


## Test and Validation
### ROC Curve for URL Detector
![image](https://user-images.githubusercontent.com/34811605/148760513-829d8f48-2b8d-4e3b-9b67-cd2570e23099.png)
### Confusion Matrix for URL Detector
![image](https://user-images.githubusercontent.com/34811605/148760584-f8fad164-bba6-48ef-a454-c5ece44b311c.png)

### Correlation Matrix for Malicious PE Header Detector
![image](https://user-images.githubusercontent.com/34811605/148760609-defdc32e-60e6-4f72-87c7-ac7be3ba2d15.png)

### Confusion Matrix for Malicious PE Header Detector
![image](https://user-images.githubusercontent.com/34811605/148760666-058d1c92-b3c1-45c8-8533-7168442bacbe.png)

## Performance Analysis

- The Accuracy percentage of Random Forest Classifier: 99.37% 
- The Accuracy of Logistic Regression: 98.46%
- The Precision of Logistic Regression: 99.18% 
- The Recall of Logistic Regression: 96.25%

## Future Enhancements
- Use a wider, well-labelled dataset.
- Instead of only hosting it in our local system, we can upload it in the web and provide the feature of uploading files to be checked and also create a section for URL detector.
- GUI based program can be made for windows, as of now it is only made for terminal.
- Real time scanning of every file while downloading/transferring can be done to be used in daily life scenario to detect malicious files.

## Installation

https://user-images.githubusercontent.com/34811605/148761184-cb6040d8-a8a1-4654-b592-f19b91c98c74.mp4

## Contributing
First you need to clone this repo, you can do this using

``` git clone https://github.com/Kiinitix/Malware-Detection-using-Machine-learning.git ```

After clone this repo, open the terminal in that location and install all the dependencies of the project using,

``` pip install -r requirement.text ```

Now you can use the project in your local machine, if you wish to make any changes in the repo then you first need to make a new branch and switch to that new branch using

```
git branch new-branch
git checkout new-branch
```
After changing your current branch, make change locally and then add all those changes in your branch and then fianlly commit

```
git add .
git commit -m "<comment>"
```

After successfully commiting the changes you need to push the code using,

```
git push --set-upstream origin new-branch
```
After pushing the changes you are now good to send the pull request and after evaluation we can commit it in the main-branch.

### Run it using Docker

```
git clone https://github.com/Kiinitix/Malware-Detection-using-Machine-learning.git
cd Malware-Detection-using-Machine-learning
docker build -t py-md .
docker run -ti py-md
```

Thanks for reading!


## Some interesting facts about malwares

Trojan is a malware which masks as another software. Trojan is from the infamous Greek Trojan Horse used to infiltrate and defeat Troy. Like virus and worms, Trojan is equally destructive which displaying annoying pop ups, and opens backdoor for other malware to access to. Yet, worms and (some) virus replicates but not Trojan. When Trojan infects other devices, it becomes a virus.
