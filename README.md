# IMDB Reviews Sentiment Analysis

### Objective
In this project, the main was to implement Rule-Based approach using VADER models to predict the sentiment of IMDb reviews, either as positive or negative or neutral. 

### Rule - based Approach
VADER analyses a piece of text to see if any of the words from the text are present in the VADER lexicon. It can find the polarity indices using polarity_scores() function.
The Standard values of compound are given below :
+ Positive Sentiment: compound score >= 0.05
+ Neutral Sentiment: compound score > -0.05 and < 0.05
+ Negative Sentiment: compound score <= -0.05

### Project Stages
+ STAGE 1: Importing Data
+ STAGE 2: Removing unwanted characters, Lowercase text
+ STAGE 3: Remove stop words
+ STAGE 4:  Lemmatization
+ STAGE 5: Use Vader Module for calculating polarity score
+ STAGE 6: Determine sentiment based on polarity score
+ STAGE 7:  Sentiment Analysis Representation 

### Output
Firstly review was taken from any movie, for example - "Haseen Dilruba"
![WhatsApp Image 2021-07-26 at 01 49 09](https://user-images.githubusercontent.com/65845120/126912704-eb94351a-e7d8-42a4-8bb1-586d7cacf9cd.jpeg)

Secondly, the sentiment of the input given in the text box is displayed in the form of a piechart.
![WhatsApp Image 2021-07-26 at 01 49 19](https://user-images.githubusercontent.com/65845120/126912770-0c26cee4-3c7a-4817-94a5-e8de981b40f6.jpeg)


