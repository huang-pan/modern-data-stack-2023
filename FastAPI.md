# FastAPI

## Udemy FastAPI course
[https://www.udemy.com/course/completefastapi/](https://www.udemy.com/course/completefastapi/)
- Course completion certificate: [https://www.udemy.com/certificate/UC\-f91bde24\-2803\-4e24\-beba\-7e2f3963c9d6/](https://www.udemy.com/certificate/UC-f91bde24-2803-4e24-beba-7e2f3963c9d6/) 
- Summary:
    - FastAPI is one of the fastest python API frameworks available, on par with NodeJS and Go.
    - This course in just an introductory course, mainly taken just for my background knowledge. It went through how to install FastAPI, all CRUD methods in FastAPI, how to order routes, how to connect to databases / files, how to authenticate with FastAPI, etc. 
        - Once you know how to do the basic stuff like routing, parameters, parameter documentation, tagging categories, ORM / schemas / models / db connection, async / await, background tasks, etc. \- the rest is just putting together a combination of everything.
        - Unless you know how everything is structured, FastAPIs APIs code files can be very messy.
    - It went through simple APIs built with FastAPI: an OCR application, a Blog site, an instagram clone, and a warehouse app that uses 2 microservices and Redis.
    - This course was good background knowledge to have in case I need to build out any data service APIs in the future. You can build out a scalable data service API by using the FastAPI framework and a cloud API Gateway / load balancer and scalable VMs / Docker containers or serverless compute.
    - For online serving of machine learning models, GCP / AWS / Azure all have services that automatically create APIs for the ML model \(probably using Flask\). They also have services that deploy the ML model for batch serving as well.
    - The gist of this course \(and any API framework course\) is to know where to put what in the framework. If I had to implement an API in another language / framework, I'd take a Udemy course on that framework as well.
    - I mostly skipped the React front end / android parts of this course as I'm not a front end developer. There is now a python library that lets you develop React front ends using python: [https://reactpy.dev/docs/index.html](https://reactpy.dev/docs/index.html) 
    - Again, this is just an introductory course. For the knowledge to really sink in, I need to actually implement a FastAPI API for a project. After going through this course, I can comfortably dig into an existing FastAPI project and know how to modify / extend the code. I'd also be comfortable creating an initial FastAPI project scaffold using something like [https://github.com/AntonOsika/gpt\-engineer](https://github.com/AntonOsika/gpt-engineer) and then start creating the API.
- Github repos for course:
    - [https://github.com/CatalinStefan/fastapi\-blog\-api](https://github.com/CatalinStefan/fastapi-blog-api)
    - [https://github.com/CatalinStefan/fastapi\-blog\-web](https://github.com/CatalinStefan/fastapi-blog-web)
    - [https://github.com/CatalinStefan/instagram\-clone\-api](https://github.com/CatalinStefan/instagram-clone-api)
    - [https://github.com/CatalinStefan/instagram\-clone](https://github.com/CatalinStefan/instagram-clone)
    - [https://github.com/CatalinStefan/instagram\-clone\-android](https://github.com/CatalinStefan/instagram-clone-android)
    - [https://github.com/CatalinStefan/fastapi\-microservices](https://github.com/CatalinStefan/fastapi-microservices) 
    - [https://github.com/CatalinStefan/fastapi\-ocr](https://github.com/CatalinStefan/fastapi-ocr)
    - FastAPI cheat sheet: [https://lyz\-code.github.io/blue\-book/fastapi/](https://lyz-code.github.io/blue-book/fastapi/)
    - FastAPI boilerplate setup: https://www.linkedin.com/posts/kamran-abdi-1582b514a_github-kamranabdicsefastapi-postgres-boilerplate-activity-7111052328517939200-m7od/
-  FastAPI features
    - installation
        - [https://docs.python.org/3/tutorial/venv.html](https://docs.python.org/3/tutorial/venv.html)
            - python venv on macos
            - fastapi\-env folder automatically created in project when you install fastapi and all other requirements in requirements.txt in the virtual environment
    - automatically creates Swagger doc
        - localhost:8000/docs\#/
    - authentication
    - dependency injection
    - testing
- app
    - hello world example
        - uvicorn main:app \-\-reload
            - uvicorn app server
            - starts fastAPI API instance on localhost:8000
- **docs on localhost:8000/docs\#**
    - GET, POST, PUT, DELETE methods by tag / router
        - **can test out all methods here, no need for postman**
            - input parameters \-\-\> execute method
            - curl version of command
            - request URL
                - request body
            - server response
                - response body
                - response headers
    - has list of valid HTTP response codes
    	- Informational (100-199)
     	- Success (200-299)
      	- Redirection (300-399)
      	- Client Error (400-499)
      	- Server Error (500-599)
   ![httpstatuscodes](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/42db4807-0fe9-407c-bafc-18fe8d37493a)

    - schemas of custom types like BlogType
- CRUD Create Read Update Delete
    - order of CRUD methods is important
        - GET, POST, PUT, DELETE
    - GET method
        - path parameters 
            - localhost:8000/blog/type/foo
            - pass a path parameter to the GET method
                - @app.get\('/blog/type/{type}'\)
                - def get\_blogs\(type: BlogType\):
                    - return {'message': f'Blog type {type}'}
            - pydantic type validation of any parameters
            - can have predefined values with Enum
                - class BlogType\(str, Enum\):
                    - short = 'short'
                    - story = 'story'
                - type: BlogType parameter
            - list of valid enum parameters in documentation
        - query parameters 
            - localhost:8000/blog/all?page=2&page\_size=10
            - @app.get\('/blog/all\)
            - def get\_blogs\(page=1, page\_size: Optional\[int\] = None, status\_code=status.HTTP\_404\_NOT\_FOUND\):
                - return {'message': f'All {page\_size} blogs on page {page}'}
            - can test out integer parameters in box in documentation
            - **list of status codes**
                - [https://developer.mozilla.org/en\-US/docs/Web/HTTP/Status](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)
- tags / summary / description
    - categorize operations for Swagger doc
        - blog category, comment category, user category
            - all GET / POST / PUT / DELETE methods
    - @app.get\('/blog/comments', tags=\['blog', 'comment'\], title='blog\_comments', summary = 'get all comments', description = 'this api call gets all comments', response\_description='comment response'\)
        - description also taken from **function** **docstring**
- routers
    - main app can have multiple routers, order matters
    - separate operations into multiple files
        - simple [main.py](http://main.py) file with main app
            - from fastapi import FastAPI
            - from router import blog\_get
            - app = FastAPI\(\)
            - app.include\_router\(blog\_get.router\)
            - app.include\_router\(blog\_post.router\)
            - @app.get\('/hello'\)
            - def index\(\):
                -  return {'message': 'Hello world\!'}from fastapi import FastAPI
        - router folder
            - separate file for each router
                - blog\_[get.py](http://get.py): blogs category / section of API
                    - from fastapi import APIRouter, Response, status
                    - router = APIRouter\(
                    -     prefix='/blog',
                    -     tags=\['blog'\]
                    - \)
                    - @router.get\(
                    -   '/all',
                    -   summary='Retrieve all blogs',
                    -   description='This api call simulates fetching all blogs',
                    -   response\_description="The list of available blogs"
                    -   \)
                    - def get\_blogs\(page = 1, page\_size: Optional\[int\] = None\):
                        - return {'message': f'All {page\_size} blogs on page {page}'}share a prefix between multiple operations
                - blog\_post.y
        - share tags
- parameters
    - request body / path and query parameters 
        - **request body is a type of query parameter, but it is distinct from a regular / simple query parameter**
            - you put data into the request body
            - below example shows JSON input to PUT method
            - does not appear in path parameter
        - blog\_post.y
            - from pydantic import **BaseModel**
                - **converts from JSON in request body to pydantic model**
                    - **automatically does data validation in request body JSON subfield**
                - for example, can access blog.title as a python variable below
                - **pydantic: library for data parsing and validation**
            - class BlogModel\(BaseModel\):
            -   title: str
            -   content: str
            -   nb\_comments: int
            -   published: Optional\[bool\]
            - @router.post\('/new/{id}'\)
            - def create\_blog\(blog: BaseModel, id: int, version: int = 1\):
            -   return {
            -     'id': id,
            -     'data': blog,
            -     'version': version
            -     }
    - parameter metadata: info displayed in docs for query / path / body parameters
        - attached parameter metadata using **Query, Path, Body imports**
        - **validators validate data passed to parameters**
        - **alias: query parameter alias**
        - from fastapi import APIRouter, Query, Body, Path
        - @router.post\('/new/{id}/comment'\)
        - def create\_comment\(blog: BlogModel, id: int, 
        -         comment\_id: int = Query\(None,
        -             title='Id of the comment',
        -             description='Some description for comment\_id',
        -             alias='commentId',
        -             deprecated=True
        -         \),
        -         content: str = Body\(...,
        -             min\_length=10,
        -             max\_length=50,
        -             regex='^\[a\-z\\s\]\*$'
        -         \),
        -         v: Optional\[List\[str\]\] = Query\(\['1.0', '1.1', '1.2'\]\),    \):
        -     return {
        -         'blog': blog,
        -         'id': id,
        -         'comment\_id': comment\_id,
        -         'content': content
        -     }
        - **content: additional part of request body, distinct from blog**
            - can make optional by using default value
                - content: str = Body\('default value'\)
            - can make it mandatory by using: ...
    - multiple values
        - only for query parameters
        -         v: Optional\[List\[str\]\] = Query\(\['1.0', '1.1', '1.2'\]\),    \):
    - number validators
        - @[router.post](http://router.post)\('/new/{id}/comment/{comment\_id}'\)
        - comment\_id: int = Path\(None, le=5\)
            - path parameter, has to be \<= 5
    - complex subtypes: list, set, dict, tuple
        - metadata: Dict\[str, str\] = {'key1': 'val1'}
- databases
    - dependency injection
        - def required\_functionality\(\):
        -   return {'message': 'Learning FastAPI is important'}
        - @router.get\( \)
        - def get\_blogs\(page = 1, page\_size: Optional\[int\] = None, req\_parameter: dict = Depends\(**required\_functionality**\)\):
        -   return {'message': f'All {page\_size} blogs on page {page}', 'req': req\_parameter}relational database accessed through Object Relational Mapper ORM library \(SQLAlchemy\)
    - create ORM table schema \(model\) in FastAPI
        - user \-\-\> schema \-\> model \-\> DB
    - accessing database not too different than previous code written in Airflow accessing data warehouse / database
    - files
    - **Structure of simple MVC FastAPI: database Model / ORM, View schema, router Controller**
        - [database.py](http://database.py): database definition, connection
            - uses **sqlalchemy**
        - [models.py](http://models.py): model definition: **model** for database table
            - can also use https://github.com/tiangolo/sqlmodel 
        - [main.py](http://main.py): create instance of database to connect to, uses [database.py](http://database.py)
            - from db.database import engine
            - models.Base.metadata.create\_all\(engine\)
        - [schemas.py](http://schemas.py): **schema** definition: data type exposed to API, can have restricted model views
            - **custom schema classes extend pydantic BaseModel class**
            - **extending pydantic BaseModel**
                - **can be used in schemas**
                - **can also be used in parameter data validation**
        - db\_[user.py](http://user.py): **ORM** functionality
            - functions that interact with the database
            - e.g.: create\_user function that imports model from [models.py](http://models.py), schema from [schemas.py](http://schemas.py), converts schema to model and inserts data into database
            - e.g. query database for get\_all\_users function
        - [user.py](http://user.py): **API** functionality: GET / POST, etc. methods, separate **router**
            - from schemas import UserBase, UserDisplay
            - @router.post\('/', response\_model=UserDisplay\)
            - def create\_user\(request: UserBase, db: Session = Depends\(get\_db\)\):
                - return db\_user.create\_user\(db, request\)
        - [hash.py](http://hash.py): for password hashing
        - [services.py](http://services.py): can put functions here that GET / POST, etc. methods call
    - relationships
        - **generally only one type of model per table in database, but can have many different types of similar schemas depending on API usage**
        - retrieve elements from multiple tables in a single request
        - define relationships in models
        - add the elements we want to retrieve in schemas
- misc
    - error handling: raise exception to client
        - from fastapi import HTTPException, status
        - in db\_user.py:
            - def get\_user\(db: Session, id: int\):
            -   user = db.query\(DbUser\).filter\(DbUser.id == id\).first\(\)
            -   if not user:
            - **    raise HTTPException\(status\_code=status.HTTP\_404\_NOT\_FOUND,**
            -       detail=f'User with id {id} not found'\)
            -   return user
        - can have custom exceptions in exceptions.py
    - custom responses
        - standard response: model, list, database model, dict, etc.
        - custom
            - add parameters: headers, cookies
            - plain text, xml, html, files, streaming
    - headers
        - request headers
    - cookies
        - store info in browser: str, list, dict, models
    - HTML form data
    - Cross Origin Resource Sharing CORS
        - allow access to API from multiple ports
            - swagger doc: localhost:8080
            - React frontend client: localhost:3000
        - origins = \[
        -   'http://localhost:3000'
        - \]
        - app.add\_middleware\(
        -   CORSMiddleware,
        -   allow\_origins = origins,
        -   allow\_credentials = True,
        -   allow\_methods = \["\*"\],
        -   allow\_headers = \['\*'\]
        - \)
- authentication
    - good background knowledge, but not so important for data services APIs
    - securing an endpoint
    - generating access token
    - user authentication: oath2 with username / password
    - oath2.py
        - from fastapi.security import OAuth2PasswordBearer
        - oauth2\_scheme = OAuth2PasswordBearer\(tokenUrl="token"\)
        - create\_access\_token function
        - get\_current\_user function now requires authentication
    - authentication.py
    - ![oath2](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/3e9fd3f5-4c5c-4e92-bfba-b40202b81ca9)

- files
    - stored in memory or on disk \(S3\)
        - can change below to read / write from S3 instead of local disk, etc.
    - upload
        - @router.post\('/uploadfile'\)
        - def get\_uploadfile\(upload\_file: UploadFile = File\(...\)\):
        -   path = f"files/{upload\_file.filename}"
        -   with open\(path, 'w\+b'\) as buffer:
        -     shutil.copyfileobj\(upload\_file.file, buffer\)
        -   return {
        -     'filename': path,
        -     'type': upload\_file.content\_type
    -   }
    - download
        - @router.get\('/download/{name}', response\_class=FileResponse\)
        - def get\_file\(name: str\):
        -   path = f'files/{name}'
        -   return path
- deployment
    - any simple app deployment service out there, e.g. AWS elastic beanstalk, digital ocean
    - minimal app
        - [main.py](http://main.py)
        - requirements.txt
- debugging
    - VS code: command pallet: debug restart \-\> fast api
        - add breakpoints in code
- testing
    - use python libraries: requests, **pytest**
    - test\_[main.py](http://main.py)
        - from fastapi.testclient import TestClient
        - from main import app
        - client = TestClient\(app\)
        - def test\_get\_all\_blogs\(\):
        -   response = client.get\("/blog/all"\)
        -   assert response.status\_code == 200
- logging
    - custom\_log.py
- **concurrency**
    - **non\-blocking** execution
    - await
        - process can be paused
        - wait for process to finish, can do something else in the meantime
    - async
        - defines a function with suspendable points
        - skip waiting for this method to finish; process other methods
    - async def time\_consuming\_functionality\(\):
        - time.sleep\(5\)
        - return 'ok'
    - @router.get\('/all'\)
    - async def get\_all\_products\(\):
    -   \# return products
          await time\_consuming\_functionality\(\)
    -   data = " ".join\(products\)
    -   response = Response\(content=data, media\_type="text/plain"\)
    -   response.set\_cookie\(key="test\_cookie", value="test\_cookie\_value"\)
    -   return response
- templates
    - not so important for data services APIs
    - jinja2 templating engine: provide ready made HTML and CSS content
- middleware
    - function that intercepts the request and response
        - for example: allow CORS
        - process before and after a request
    - @app.middleware\("http"\)
    - async def add\_middleware\(request: Request, call\_next\):
    -   start\_time = time.time\(\)
    -   response = await call\_next\(request\)
    -   duration = time.time\(\) \- start\_time
    -   response.headers\['duration'\] = str\(duration\)
    -   return response
- **background tasks**
    - **functionality to be run after the call has been completed**
    - from starlette.background import BackgroundTasks
    - @router.post\("/products/{id}", response\_class=HTMLResponse\)
    - def get\_product\(id: str, 
    -       product: ProductBase, 
    -       request: Request, 
    -       bt: BackgroundTasks\):
    -   bt.add\_task\(log\_template\_call, f"Template read for product with id {id}"\)
    - ...
    - def log\_template\_call\(message: str\):
    -   log\("MyAPI", message\)
- websockets
    - not so important for data services APIs
    - two way communication, always open
- dependencies
    - class
        - any callable can be a dependency
        - depends on custom class
    - multi\-level
        - dependencies can have dependencies
    - global
        - apply to all endpoints: router, app
- case studies: putting knowledge above to practice
    - NOTE: skipped all front end / mobile client sections of the course since it is not relevant to a data services API
    - OCR application
    - blog site
    - instagram clone
        - categories: post, blog, user, comment
    - microservices
        - warehouse microservice example
            - warehouse category
        - store microservice example
            - store category
        - uses redis
            - redis streams: use to communicate between two microservices as a background task
                - save info to redis, accessible by both microservices

## Another FastAPI course
- https://www.youtube.com/watch?v=rkPIftzu1pQ
![Screenshot_20240703-183925_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b94cd3cc-2018-4f05-a56f-f78a6bca2eb9)

## FastAPI ecosystem libraries
- https://www.youtube.com/watch?v=07QqFYILP4w
![Screenshot_20240701-173101_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/662df27d-a2c0-4442-946c-2c1fdbf24380)
![Screenshot_20240701-173206_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5127598b-c6fc-4ee7-98ac-4d7860b03182)
![Screenshot_20240701-173343_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/17ffd4f9-455d-45a2-9668-00ed18f1c2fe)
![Screenshot_20240701-173442_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/bbd5058f-14ca-46d8-b048-ac1ba0e818fb)
![Screenshot_20240701-173508_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/b11bb197-7ae6-40fe-b386-0f504adee598)
![Screenshot_20240701-173516_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/6de641c3-8c7b-4e1f-bb16-71e7f8ca1143)
![Screenshot_20240701-173543_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/326c9707-f1f7-4c30-b9cf-4819ad1e1fb1)
![Screenshot_20240701-173555_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/5f81f517-f250-47bf-8bd3-d3dca8baec07)
![Screenshot_20240701-173634_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/43943605-0444-43b5-acb3-1e20d9710652)
![Screenshot_20240701-173721_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2111d55c-b911-45bf-803f-c75d106f4ab9)
![Screenshot_20240701-173729_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/a0885845-b493-4f4c-b084-4db19c68e13f)
![Screenshot_20240701-173748_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/9ae14c18-d964-4b12-b1fe-ab8ddf840613)
![Screenshot_20240701-173833_YouTube](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/54dbf9e4-5f91-4a93-8a21-8f71c435b670)

## 6 API styles
- https://www.linkedin.com/posts/nelsonamigoscode_systemdesign-coding-interviewtips-activity-7211707276565323778-4hnm/
	- GRPC: High-performance RPC framework for distributed systems.
	- SOAP: Protocol for structured web services with strict XML standards.
	- GraphQL: Query language for APIs to fetch only needed data.
	- Webhook: Real-time communication via HTTP POST to trigger actions.
	- REST: Architectural style using HTTP methods to manipulate resources.
	- WebSocket: Bidirectional, real-time communication for low-latency applications.
![1719400197980](https://github.com/user-attachments/assets/a11b8ccc-7739-42af-964e-eb355aa520a9)

## API Testing
![apitesting](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/33cbb4f9-64ab-4fea-b154-f0baa84b012a)
- Smoke Testing: This is done after API development is complete. Simply validate if the APIs are working and nothing breaks.
- Functional Testing: This creates a test plan based on the functional requirements and compares the results with the expected results.
- Integration Testing: This test combines several API calls to perform end-to-end tests. The intra-service communications and data transmissions are tested.
- Regression Testing: This test ensures that bug fixes or new features shouldn’t break the existing behaviors of APIs.
- Load Testing: This tests applications’ performance by simulating different loads. Then we can calculate the capacity of the application.
- Stress Testing: We deliberately create high loads to the APIs and test if the APIs are able to function normally.
- Security Testing: This tests the APIs against all possible external threats.
- UI Testing: This tests the UI interactions with the APIs to make sure the data can be displayed properly.
- Fuzz Testing: This injects invalid or unexpected input data into the API and tries to crash the API. In this way, it identifies the API vulnerabilities.

## Top 7 Ways to 10x Your API Performance
- Rest API - Performance - Best Practices https://www.youtube.com/watch?v=CI0ZxSQ8sWQ
<img width="1920" alt="Screenshot 2024-10-09 at 9 39 09 AM (3)" src="https://github.com/user-attachments/assets/43c48933-4863-4e96-a7a0-a98a42cfb080">

- https://www.linkedin.com/posts/alexxubyte_systemdesign-coding-interviewtips-activity-7144366633526988800-4cGQ/
	- Result Pagination: This method is used to optimize large result sets by streaming them back to the client, enhancing service responsiveness and user experience.
 	- Asynchronous Logging: This approach involves sending logs to a lock-free buffer and returning immediately, rather than dealing with the disk on every call. Logs are periodically flushed to the disk, significantly reducing I/O overhead.
  	- Data Caching: Frequently accessed data can be stored in a cache to speed up retrieval. Clients check the cache before querying the database, with data storage solutions like Redis offering faster access due to in-memory storage.
  	- Payload Compression: To reduce data transmission time, requests and responses can be compressed (e.g., using gzip), making the upload and download processes quicker.
  	- Connection Pooling: This technique involves using a pool of open connections to manage database interaction, which reduces the overhead associated with opening and closing connections each time data needs to be loaded. The pool manages the lifecycle of connections for efficient resource use.
- https://youtube.com/watch?v=zvWKqUiovAM&feature=share 
	- 1. 1:00 Caching 
	- 2. 1:45 Connection Pool 
	- 3. 2:45 Avoid N+1 Query pattern 
	- 4. 3:35 Pagination 
	- 5. 3:58 JSON Serialization 
	- 6. 4:20 Compression 
	- 7. 4:50 Asynchronous logging
- Other techniques:
	- 1. Tuning the database connection pool size based on the application behaviour. (Large number doesn't always mean more performance)
	- 2. Optimizing the SQL query. (Ensuring your most frequent queries end up using index scan instead of full table scan)
	- 3. Not hopping between multiple microservices for a single user request. (While a single user request can hit multiple services but those services should not in turn hit another set of services and so on).
	- 4. Authorization data should be always cached.
	- 5. As much as possible, do the most computation on the database layer. There's a huge difference between doing the computation at application layer vs doing it at database layer.
![ATS](https://github.com/user-attachments/assets/c865e487-6a9c-4278-82c1-d957e69247ce)

## Scalable AWS API
- System Design: 0 Scaling From Zero to Billions of Requests https://www.youtube.com/watch?v=69UjMatrOa4
![Screenshot_20240701-102521_YouTube](https://github.com/user-attachments/assets/3906118f-5a40-45d9-b6df-81067ce6e33f)

- https://www.linkedin.com/posts/semaan_great-visualization-of-resilient-3-tier-architecture-activity-7211712558402060289-VNOi/
	- 𝗡𝗲𝘁𝘄𝗼𝗿𝗸: VPC, Subnets, Route tables
	- 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆: Security groups, NACLs
	- 𝗔𝗽𝗽𝗹𝗶𝗰𝗮𝘁𝗶𝗼𝗻 𝘀𝗲𝗿𝘃𝗶𝗰𝗲𝘀: EC2/Fargate, Auto Scaling
	- 𝗦𝘁𝗼𝗿𝗮𝗴𝗲 & 𝗗𝗮𝘁𝗮𝗯𝗮𝘀𝗲: S3, Amazon Aurora
  ![1719373639077](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/86bdcd32-7f95-4985-8501-7463ecb7bb3a)
![86fdda13-d57b-4d9c-b868-ac35d3c52569_1600x1582](https://github.com/user-attachments/assets/7a2d5505-02a0-405f-8080-45211999ebb5)
- API gateway
![apigateway](https://github.com/user-attachments/assets/be90c2e0-ecdb-4806-83bf-a55cef5396a9)
![lb](https://github.com/user-attachments/assets/92126f0b-cb59-4e00-a916-3a261b629914)

![acid](https://github.com/user-attachments/assets/b5699a2d-dafe-40c8-9224-55f9d4b60698)
![dep](https://github.com/user-attachments/assets/3f0ca813-d82e-4271-a1bb-bb93b38b13f6)
