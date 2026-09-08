# Detecting Microaggressions and Subtle Hate Speech in Social Media Data Using BERT 
### Performing Sentiment Analysis on YouTube Comments under Minority-Lead Superhero Films - Presented at the Summer 2023 Undergraduate Research Symposium at East Carolina University

## Acknowledgements
This research is based upon work supported by the National Science Foundation under Grant No. 2050883 and was conducted during the NSF's 2023 Research Experience for Undergraduate (REU) program at East Carolina University, with a focus on Software Engineering and Data Science. 

## Abstract
Sentiment analysis is the process of capturing the emotional tone of a given text and assigning it a label, such as positive or negative. This method has been used to detect hate speech and bigotry on social media platforms such as Twitter and YouTube to facilitate the removal of such content. However, machine learning models used for this process are often not trained on data that contains subtle forms of hate speech or microaggressions. This research aims to fine-tune a hate speech detection model with a dataset containing subtle forms of hate speech to improve the model's labeling accuracy. We used a pre-trained BERT model, fine-tuned it using this dataset, and analyzed YouTube comments containing subtle forms of bigotry. The comments we performed analysis on were collected by extracting recent comments from YouTube trailers of superhero films and TV shows led by both minority and non-minority figures. The labels the BERT model assigned to these comments before and after the fine-tuning process were compared against the true labels which were determined by myself and my faculty mentor. The primary purpose of this research was to fine-tune a pre-trained hate speech detection model with a dataset containing subtle forms of hate speech and determine if the same model can be improved to identify text that contains subtle forms of hate speech.

## Introduction and Background
Social media has allowed for hate speech and bigotry to spread on several different platforms throughout the years. We especially recognized the amount of bigotry aimed at minority-led characters in superhero films and TV shows on social media platforms, so we wanted to analyze comments under trailers for said media. We specifically wanted to see the amount of hate speech there was under trailers for minority-led superhero films and TV shows using sentiment analysis. However, after extracting comments, we found that the comments that did contain hate speech only had subtle forms of it. Machine learning models used to detect hate speech tend to only be trained on obvious forms of it, therefore are not effective at detecting subtle forms of bigotry and microaggressions. Therefore, using the model we used to originally analyze the comments with, we attempted to fine tune a hate speech detection model to improve its accuracy in detecting microaggressions and subtle forms of hate speech. 

## Methodology
According to Aluru et al’s paper, “Deep Learning Models for Multilingual Hate Speech Detection”, the best type of model for detecting hate speech in the English language is a BERT model. For that reason, we decided to use their pre-trained BERT model to analyze our extracted comments. The BERT model analyzes the text and outputs two labels: a label for whether the comment contained hate speech (“HATE”) or did not contain any hate speech (“NON_HATE”) and a confident score for how confident the model is with the label it gave the text. We took the 200 most recent comments from six different trailers in each category and analyzed the raw data with the model. Then, we labeled the comments ourselves and compared it to the model’s labels (figure 1), not including comments that were blank, in another language, or that we were not sure what to label them as. Afterwards, we fine tuned the model with a dataset that contained subtle forms of sexism. There were 13632 total pieces of text extracted and 1809 of them were labeled as “sexist”. We then evaluated the comments with this fine-tuned model and compared the labels to our own labels (figure 2). We also calculated exactly how many comments were incorrectly labeled as hate and non-hate before (figure 3) and after (figure 4) the model was fine tuned.

## Conclusion / Future Work
According to our results, the model did not improve in labelling accuracy after fine-tuning. There were a lower number of comments correctly labeled for comments from minority-led superhero trailers and would more often incorrectly label comments as “hate” rather than “non-hate”. For these reasons, it is best to either 1) collect more data that contains microaggressions/subtle forms of hate speech to finetune the model, 2) find a model that is trained specifically for finding microaggressions or 3) create a model that does so from scratch. For future work, we can either use a pre-trained model and fine tune it or creating one from scratch to see if it will accurately detect microaggressions. We also hope to specifically create a wide-scale dataset that contains microaggressions against different identities such as one’s race, religion, sexual orientation, gender, disability, etc.

## References
- Aluru, Sai Saketh, et al. "Deep learning models for multilingual hate speech detection." arXiv preprint arXiv:2004.06465 (2020).
- J. Nair, V. G and A. Vinayak, "Comparative study of Twitter Sentiment On COVID - 19 Tweets," 2021 5th International Conference on Computing Methodologies and Communication (ICCMC), Erode, India, 2021, pp. 1773-1778, doi: 10.1109/ICCMC51019.2021.9418320.
- Samory, Mattia (2021). The 'Call me sexist but' Dataset (CMSB). GESIS - Leibniz-Institute for the Social Sciences. Data File Version 1.0.0, https://doi.org/10.7802/2251.

## Information About Data Extraction
I used [onlyphantom's YouTube API Python source code](https://github.com/srazam/youtube_api_python) to randomly extract comments from the trailers listed below: 

#### Minority-Lead Superhero Films/Tv Shows
* Ms. Marvel
* Wonder Woman
* Black Adam
* Black Panther
* Captain Marvel
* Shang Chi

#### Non-Minority Lead Films/TV Shows
 * Pennyworth
 * Captain America: Winder Soldier
 * Ant Man
 * Doctor Strange
 * Shazam
