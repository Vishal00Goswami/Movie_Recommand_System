I am very excited to share I new achievement. I have create movie recommandation system using IMDB dataset.

## Problem statement:
  -> We should Need to find out the solution so user can watch or see those movies which can me similar of their best collection's movies

## Dataset:
  ->  I was used the dataset of IMDB which is easily avaiable on kaggle.com

## Summarize Dataset: 
  -> I was removed unwanted columns and add those which really necessary for system and after preprocessing I was add those columns into a single columns 
  -> And make the only 3 Columns [ Id, Movie_name, content]

## Vectorication:
  -> after pre-processing and concatenation I was used vectorization methods which convert text into number form

## Algorithm:
  -> I was use the cosine_similarity. Because I need similar content. According their reviews, write_name, cast_name, and description

## Training:
 -> after all the steps I was train the model amd make movie_dict model

## Prediction:
 -> for prediction I am using function call Recommand() 

## Using:
 -> Simply put the movie name and click Recommand button
 -> It will process and provide 5 similar movie with poster 
