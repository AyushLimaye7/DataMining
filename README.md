# DataMining


Answer the following:
What are the risks involved in building such a pipeline?
* Dependency on 3rd API like twitter, if it fails we cannot access data
* Data Cleaning 
* Streaming services can have data coming extensively and parsely, depending on the event. Example, Justin Beiber music tweets be low when no songs are out, but high when his songs are about to release.
* Since it is third party data, its json structure can change easily
and so from above point Mainting it in relational database will be costly to that non relational database.
* Making batches of the streaming data is one method and there can be several pros and cons on the several batching. Few are as follows:
 * Pros :  Smaller batching easy to load
 * Cons : Large number of small batches and hard to maintian consistency 
 

How would you roll out the pipeline going from proof-of-concept to a production-ready solution?

* First of all, to think of production-ready solution , we start with creating of the independent tasks, which can run on their own to build scalable and reliable data pipeline by using some of the test data.  
	1. Data Collections : Collecting of the tweets
	2. Data Cleaning : Making sure the data is accepted in chosen database
	3. Database Creation
	4. Filter out the tweets. (will not be curtainling it to music, as focusing towards scaling it to filter on the basis of any tag)
	5. Database ready operations
		1. Read and Write operations

What would a production-ready solution entail that a POC wouldn't?
* Scalability
	1. Tweets collection will not only curtail to Justin Beiber
	2. Seaching of tags in the database will not be curtailed to one tag
	3. Using NoSQL, for schema independecy as we are using third party 4. Building database with all read and write operations

* Reliability
	1. If third party api is not streaming data, have a backup plan to collect post data, instead of stream service use api.
	2. Having reliable database for no loss of data

* Fault Tolerance 
	1. Database to be build in a manner that, even if any one of the server fails we are still able to collect the data. Example, Cassandra Server

* Consistency across the fetching of the data from our data pipeline.

What is the level of effort required to deliver each phase of the solution?

So while estimating effort spent, I personally consider not only from the perspective of writing code, but information accumulation and risk involved. 
As discussed above, once parallelised , and breaking it effort
1.  Collecting of tweet - Major effort is posed in what we want to or use this pipeline for. Once requirements are clear, creating a dynamic tweet scrawler is not huge effort. And requirements changing will also not be an issue as there will be just parameter change to fetch the data. 
2. Data Cleaning : Understaning of data with regress testing, if we know all the meta character and have better understaning of data we are receiving then this should be straight forward to achieve. But risk involved here is high, as only one unreadable character can block the further pipeline 
3. Database creation and operation : Effort are not huge, but there is risk involment at this stage is high. We have to clearly define our goals. Efforts to make it robust and scalable will be time consuming.
Also palnign of fallback options if service is down.
4. Tweet filter 
	: Read operations on consistent data base, not huge effort.


What is your estimated timeline for delivery for a production-ready solution?

1. Tweet Scrawler : 2 weeks 
2. Data Cleaning : 2 weeks 
3. DataBase Creator : 5 weeks 
4. Database operation : 2 weeks


And from this, by end on three month we can have a pipeline which can crawl through the tweets, and add it into the the database and finally we can perform any read opertion on it.
