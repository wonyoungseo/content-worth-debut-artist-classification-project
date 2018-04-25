# Project Timeline

* * * *

### 20180413
Meeting w/ [**_HIPHOPLE_**](www.hiphople.com) staffs Heman(CEO), Beasel, Loner and discussed needs in data analysis for the business
- (1) Hongkong, Singapore, English Using Country K-Hiphop Buzz Analysis for South East Asian market trend analysis
- (2) Quick quantitative indicator of rookie artists for content ideas
- (3) Public reputation and trend analysis on particular artist for merchandise sales forcast
- (4) Kakao Plusfriend Chatbot development for Daily Music Chart from various streaming platforms


### 20180414-15
- Project (4) initiation (—> currently on hold due to low priority)


### 20180416-17
- Planning for project (2)
  - Needs assessment
  - Goal setting
  - Capacity assessment

### 20180418
- Scrape debut album 2011~2018 (Wikipedia)
  - **_HIPHOPLE_** was established 2011

### 20180419
- Researched various sources for data

### 20180420
- Scrape rating _Pitchfork_ with BeautifulSoup

### 20180421
- Store data directly into MySQL in AWS ... or sqlite (—> postponed due to AWS MySQL connection error)
- Flask and Html (CSS) setting for chart dashboard —> Decided to use Dash instead.


### 20180422
- Scrape SNS followers with selenium (—> postponed due to element error)
- Fix the debut artist train dataset (from 2011-2018) and Initiate collecting target data ( 1: worth a content , 0: not worth a content) from hiphople.com editors (—> postponed)
- Contact Shim EB (GDB) for industrial knowledge regarding buzz


### 20180423
- Scrape rating _Metacritic_ with BeautifulSoup
- Scrape news article buzz on _Genius.com_
- Dash tutorial (1)


### 20180424
- Learn how to deploy dash app with Heroku
- Scrape news article buzz on _Genius.com_ (2nd attempt)
- Scrape news article buzz _XXL Magazine_
- Scrape news article buzz _The Source Magazine_ (on hold due to session expiration)
- Scrape debut album Wikipedia (2nd attempt with genre and release date)
- Impute missing genre manually


### 20180425
- Scrape rating _Metacritic_ with Scrapy
- Scrape news article buzz _The Source Magazine_ with threading to solve session expiration issue.
- Troubleshoot AWS ECS MySQL connection errors
- Troubleshoot csv data files upload to MySQL server via SQLAlchemy


### 20180426
- Parse debut album “genre” column and regroup genre. (Hiphop, RnB, POP, ROCK, ELECTRONIC, INDIE, ETC)
- Parse “release date” column into timestamp
- Troubleshoot SNS scraping with threading
