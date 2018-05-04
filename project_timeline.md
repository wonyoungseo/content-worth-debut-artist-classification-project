# Project Timeline

* * * *

### 20180413
Meeting with [**_HIPHOPLE_**](www.hiphople.com) staffs Heman(CEO), Beasel, Loner and discussed needs in data analysis for the business
- (1) Hongkong, Singapore, English Using Country K-Hiphop Buzz Analysis for South East Asian market trend analysis
- (2) Quick quantitative indicator of rookie artists for content ideas
- (3) Public reputation and trend analysis on particular artist for merchandise sales forcast
- (4) Kakao Plusfriend Chatbot development for Daily Music Chart from various streaming platforms

<br>

### 20180414-15
**Kakao Chatbot**

- Project (4) initiation (—> currently on hold due to low priority)

<br>

### 20180416-17

**Planning**

- Needs assessment
- Goal setting
- Capacity assessment

<br>

### 20180418

**Scraping**

- Scrape debut album 2011~2018 (Wikipedia)
  - **_HIPHOPLE_** was established 2011

<br>

### 20180419

**Domain Knowledge**

- Researched various sources for data

<br>

### 20180420

**Scraping**

- Scrape rating _Pitchfork_ with BeautifulSoup

<br>

### 20180421

**Database**

- Store data directly into MySQL in AWS ... or sqlite (—> postponed due to AWS MySQL connection error)

**Visualization**

- Flask and Html (CSS) setting for chart dashboard —> Decided to use Dash instead.

<br>

### 20180422

**Scraping**

- Scrape SNS followers with selenium (—> postponed due to element error)

**Domain Knowledge**

- Fix the debut artist train dataset (from 2011-2018) and Initiate collecting target data ( 1: worth a content , 0: not worth a content) from hiphople.com editors (—> postponed)
- Contact Shim EB (GDB) for industrial knowledge regarding buzz

<br>

### 20180423

**Scraping**

- Scrape rating _Metacritic_ with BeautifulSoup
- Scrape news article buzz on _Genius.com_
- Dash tutorial (1)

<br>

### 20180424

**Scraping**

- Scrape news article buzz on _Genius.com_ (2nd attempt)
- Scrape news article buzz _XXL Magazine_
- Scrape news article buzz _The Source Magazine_ (on hold due to session expiration)
- Scrape debut album Wikipedia (2nd attempt with genre and release date)

**Visualization**

- Learn how to deploy dash app with Heroku

**Data Cleaning**

- Impute missing genre manually

<br>

### 20180425

**Scraping**

- Scrape rating _Metacritic_ with Scrapy
- Scrape news article buzz _The Source Magazine_ with threading to solve session expiration issue.

**Database**

- Troubleshoot AWS ECS MySQL connection errors
- Troubleshoot csv data files upload to MySQL server via SQLAlchemy

<br>

### 20180426

**Scraping**

- Troubleshoot SNS scraping with selenium

<br>

### 20180428

**Domain Knowledge**

- Fix the debut artist train dataset (from 2011-2018) and initiate collecting target data ( 1: worth a content , 0: not worth a content) from hiphople.com editors by google spreadsheet

**Data Cleaning**

- re-input MySQL in utf-8 with decoded accent characters

**Scraping**

- Scrape rating AOTY.org

<br>

### 20180427

**Database**

- Troubleshoot getting data from MySQL server via SQLAlchemy

**Data Cleaning**

- Parse debut album “genre” column and regroup genre. (Hiphop, RnB, Soul, Funk, POP)

<br>

### 20180429

**Scraping**

- Scrape SNS follower of each artist

<br>

### 20180430

**Scraping**
 
- SNS follower scraping (2)  
- Scrape Buzz Billboard

**Visualization**  

- Dash layout basic  
	- tab function not officialy published (only exists in previous version.

**Domain Knowledge**

- Collect target variable labeling from GDB and Melo

<br>

### 20180501

**Data Preprocessing**

- Merge data files (debut album list, online news article buzz, ratings, SNS followers) into one dataset.

**Modeling**

- KNN
	- Basic baseline dataset : rating columns have NaN values, therefore not included in this trial.
		- Parameter : `n_neighbors = 10'
		- Test Accuracy : 82%
		- Test Recall : 84%
		- AUC : 74%

- Decision Tree
	- Basic baseline dataset : rating columns have NaN values, therefore not included in this trial.
		- Parameter : `criterion='entropy', max_depth=5, min_samples_leaf=7`
		- Test Precision : 62%
		- Test Recall : 65%
		- AUC : 86.5%


**Visualization**

- Drop Down instead of Tab function.

<br>		
		
### 20180502

**Modeling**

- RandomForest
	- Basic baseline dataset : rating columns have NaN values, therefore not included in this trial.
		- Parameter : `criterion='entropy', n_estimators=10, max_depth=10,                               min_samples_split=5 , min_samples_leaf=5`
		- Test Precision : 74%
		- Test Recall : 67% 
		- AUC : 91.3%

- Extreme Three	
	- Basic baseline dataset : rating columns have NaN values, therefore not included in this trial.
		- Parameter : `criterion='entropy', n_estimators=10, max_depth=10,                      min_samples_split=5 , min_samples_leaf=5`
		- Test Precision : 76%
		- Test Recall : 43%
		- AUC : 85.9%

- GridSearch (Cross Validation)
	- Best Parameter
		- {'bootstrap': True,
 'class_weight': None,
 'criterion': 'entropy',
 'max_depth': 10,
 'max_features': 'auto',
 'max_leaf_nodes': None,
 'min_impurity_decrease': 0.0,
 'min_impurity_split': None,
 'min_samples_leaf': 8,
 'min_samples_split': 2,
 'min_weight_fraction_leaf': 0.0,
 'n_estimators': 10,
 'oob_score': False,
 'random_state': None,
 'verbose': 0,
 'warm_start': False}
 

- GridSearch Applied Random Forest
	- Test Precision : 84%
	- Test Recall : 71%
	- AUC : 93.1%

<br>

### 20180503









<br>
<br>

## Reference


Industrial Knowledge

- [HIPHOPLE](hiphople.com)
- [Pitchfork](pitchfork.com)
- [Chartmetric](chartmetric.io)
- [Buzz Angle Music](buzzanglemusic.com)

<br>

Data Visualization Dashboard

- [Bokeh vs Dash](https://blog.sicara.com/bokeh-dash-best-dashboard-framework-python-shiny-alternative-c5b576375f7f)
- [Introducing Dash](https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503)
- [Dash User Guide](https://dash.plot.ly)
- [Dash Webinar Tutorial for ARGO Labs collaborators](https://www.youtube.com/watch?v=yfWJXkySfe0)
- [Plotly Forum](https://community.plot.ly)

<br>

Data Sources

- [wikipedia.com](wikipedia.com)
- [metacritic.com](metacritic.com)
- [pitchfork.com](pitchfork.com)
- [albumoftheyear.com](albumoftheyear.com)
- [chartmetric.io](chartmetric.io)
- [billboard.com](billboard.com)
- [genius.com](genius.com)
- [thesource.com](thesource.com)
- [xxlmag.com](xxlmag.com)
