# NLP-Project-Lyric-Generation
Project to analyze the lyrics of a specified artist and generate similar stylistic lyrics to that artist.

## Using the Files
The following list outlines the processes and files in sequential order:
- Lyric_Scrape.ipynb contains the web scraper used to get lyrics from Metrolyrics.com for any artist of the user's choosing in notebook format.
- Predict_Word_Model.ipynb loads the word model and gives predictions.
- drake-songs.csv contains the data used to develop the models.  Other datasets can be used from the scraper.
- drake_character_model.h5 is the character model that has been trained on data from drake-songs.csv.
- *_scraped_lyrics.csv any file with this naming is output from our scraper.  They can be used to train the models if you desire.
- drake_word_model.h5 is the word model that has been trained on data from drake-songs.csv.
- lyric_generator.ipynb contains an early iteration of our character model that allows the user to enter their own phrase.  The model will predict the next characters.
- lyric_generator_Words.ipynb contains the training for the word model using drake-songs.csv.
- lyric_generator_character.ipynb contains the training for the character model using drake-songs.csv.
- lyric_scrape.py contains the web scraper used to get lyrics from Metrolyrics.com for any artist of the user's choosing in Python script format.
- **predict_Character_Model.ipynb** loads the character model and gives predictions.  This is the main notebook for the project.  It includes evaluation metrics for assessing model performance.

## Report
- Visit: https://docs.google.com/document/d/1ks1J05O1hB6n2E6RYSIGCKeymxNJw0IIndmfwVvSra8/edit?usp=sharing to view the report.
