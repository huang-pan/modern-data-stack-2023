# Generative AI

Generative AI Learning Path

- Google Generative AI learning path [https://www.cloudskillsboost.google/journeys/118](https://www.cloudskillsboost.google/journeys/118) 
    - Completed entire learning path, just a background knowledge type of thing \- they got rid of the Gen AI lab =\(
- Learning path completion badges:
    - Introduction to Generative AI 
        - [https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3737950](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3737950) 
    - Introduction to Large Language Models
        - [https://www.cloudskillsboost.google/public\_profiles/28006b56\-95bc\-45dc\-ad6c\-348b907d9afe/badges/3738003](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3738003) 
    - Introduction to Responsible AI
        - [https://www.cloudskillsboost.google/public\_profiles/28006b56\-95bc\-45dc\-ad6c\-348b907d9afe/badges/3815915](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3815915) 
    - Generative AI Fundamentals
        - [https://www.cloudskillsboost.google/public\_profiles/28006b56\-95bc\-45dc\-ad6c\-348b907d9afe/badges/3861709](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3861709) 
    - Introduction to Image Generation: diffusion models
        - [https://www.cloudskillsboost.google/public\_profiles/28006b56\-95bc\-45dc\-ad6c\-348b907d9afe/badges/3787142](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3787142) 
    - Encoder\-Decoder Architecture: translation, text summarization, Q&A
        - [https://www.cloudskillsboost.google/public\_profiles/28006b56\-95bc\-45dc\-ad6c\-348b907d9afe/badges/3787392](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3787392) 
    - Attention Mechanism
        - [https://www.cloudskillsboost.google/public\_profiles/28006b56\-95bc\-45dc\-ad6c\-348b907d9afe/badges/3766502](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3766502) 
    - Transformer Models and BERT Model
        - [https://www.cloudskillsboost.google/public\_profiles/28006b56\-95bc\-45dc\-ad6c\-348b907d9afe/badges/3787108](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3787108) 
    - Create Image Captioning Models
        - [https://www.cloudskillsboost.google/public\_profiles/28006b56\-95bc\-45dc\-ad6c\-348b907d9afe/badges/3787318](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/3787318) 
    - Introduction to Generative AI Studio
        - [https://www.cloudskillsboost.google/public\_profiles/28006b56\-95bc\-45dc\-ad6c\-348b907d9afe/badges/4150368](https://www.cloudskillsboost.google/public_profiles/28006b56-95bc-45dc-ad6c-348b907d9afe/badges/4150368) 
        - unfortunately they got rid of the lab, but played around with Gen AI studio in Vertex AI lab.
- Summary
    - The short lectures in each course gives some nice knowledge / background on LLMs. There are quizzes in each course. There is some overlap with the GCP Machine Learning learning path: [https://www.cloudskillsboost.google/journeys/17](https://www.cloudskillsboost.google/journeys/17) 
    - The important and practical thing is to get really good at prompting the LLMs to produce the code that you want.
    - https://www.elastic.co/what-is/vector-database
- Demo
    - [https://youtu.be/Jl1S4ZcSY8k](https://youtu.be/Jl1S4ZcSY8k)
        - can combine langchain prompts \+ SQL queries using GCP

Generative AI Short Courses

- [https://www.deeplearning.ai/short\-courses/](https://www.deeplearning.ai/short-courses/)
    - [https://learn.deeplearning.ai/](https://learn.deeplearning.ai/) 
    - ChatGPT Prompt Engineering for Developers
    - Langchain for LLM Application Development
    - Langchain Chat with Your Data
    - Evaluating and Debugging Generative AI using Weights and Biases
    - Large Language Models for Semantic Search
      - dense retrieval with embeddings, enhanced keyword search, find relevant documents
    - Functions, Tools, and Agents with LangChain
    - Fine Tuning LLMs
    - Pair Programming with a Large Language Model
    - Understanding and Applying Text Embeddings with Vertex AI
    - How Business Thinkers Can Start Building AI Plugins with Semantic Kernel
    - Building Generative AI apps with Gradio
        - similar to the Streamlit tutorial, Hugging Face integration
        - examples: text summarization, named entity recognition, image captioning, image generation using a diffusion model, LLM chatbot
    - How Diffusion Models work
        - not relevant to data, more for image generation
    - Building Systems with the ChatGPT AI
        - not super relevant to data, more for web apps
- Summary
    - The courses above are by Stanford Professor Andrew Ng, a leading authority in the field of AI.
    - Also went through the above courses for background knowledge. They are a combination of lectures and corresponding Jupyter notebooks that show you how to prompt
    - **class is good background knowledge to know; in reality I would just use Github Copilot X \+ ChatGPT / Code Interpreter and focus on good prompting**
        - The important and practical thing is to get really good at prompting the LLMs to produce the code that you want.
- ChatGPT Prompt Engineering for Developers
    - [https://learn.deeplearning.ai/chatgpt\-prompt\-eng/lesson/1/introduction](https://learn.deeplearning.ai/chatgpt-prompt-eng/lesson/1/introduction) 
    - Starter course on ChatGPT
        - how to prompt
    - **Guidelines for Prompting**
        - zero shot prompt: ask LLM a question
        - one shot prompt: give LLM one example
        - **few shot prompting**: provide demonstrations in the prompt to steer the LLM to better performance
        - beware of model hallucinations
    - Iterative Prompt Development
        - ChatGPT has context memory, so you can refine the outputs through successive prompting
    - Summarizing
        - summarize document
        - **extract** info from document
    - Inferring
        - infer sentiment or topics from document
        - identify emotions
        - do multiple tasks at once
    - transforming
        - language translation
        - tone transformation
        - format conversion
        - spellcheck / grammar check
    - expanding
        - generate tailored documents
    - chatbot
- Langchain for LLM Application Development
    - [https://learn.deeplearning.ai/langchain/lesson/1/introduction](https://learn.deeplearning.ai/langchain/lesson/1/introduction) 
        - Good course if you want to write an application that uses Langchain
    - Langchain is a library that strings together prompts. It is a **framework for managing all the prompts** in your application.
    - Models, Prompts and parsers
        - Models: GPT 3.5, GPT 4, etc.
            - connect through OpenAI API
        - langchain has 
            - prompt templates
            - output parsers \(specify how LLM outputs will look\)
                - e.g. parse the LLM output string into a python dictionary
    - Memory
        - look into the internals \(context\) of the LLM
        - ConversationBufferMemory
        - ConversationBufferWindowMemory
        - ConversationTokenBufferMemory
        - ConversationSummaryMemory
    - Chains
        - different types of prompt chains
        - LLMChain
            - single prompt
        - Sequential Chains
            - SimpleSequentialChain
            - SequentialChain
                - more configurable version of SimpleSequentialChain
        - Router Chain
            - give the LLM many different types of configurable prompts at once
            - e.g. physics, math, history templates, etc.
    - Questions and Answer
        - example Q&A chain
    - Evaluation
        - chain testing
            - manual evaluation
            - LLM assisted evaluation
    - Agents
        - connect LLM with APIs / external services
            - e.g. Wikipedia, search
- Langchain Chat with Your Data
    - [https://learn.deeplearning.ai/langchain\-chat\-with\-your\-data/lesson/1/introduction](https://learn.deeplearning.ai/langchain-chat-with-your-data/lesson/1/introduction)
        - Good course if you want to write an application that uses Langchain to ask questions of your data. Gives some ideas on how something like Github Copilot X is created.
        - **class is good background knowledge to know; in reality I would just use Github Copilot X \+ ChatGPT / Code Interpreter and focus on good prompting**
            - **ChatGPT code interpreter plugin to ask questions of your data**
                - **langchain chat with your data is still not private if you use a chatGPT model**
                    - **it is private if you use a H20GPT model**
    - Langchain Components
        - Prompts
            - prompt templates, output parsers, example selectors
        - Models
            - 20\+ LLM integrations, chat models, 10\+ text embedding models
        - Indexes
            - 50\+ document loaders, 10\+ text splitters, 10\+ vector stores, 5\+ retrievers
        - Chains
            - chains as building blocks for other chains, 20\+ application specific chains
        - Agents
            - 5\+ agent types \(algos for getting LLMs to use tools\), 10\+ agent toolkits \(specific tools for specific applications\)
    - RAG retrieval augmented generation
        - an LLM retrieves contextual documents from an external dataset as part of its execution
        - document loading \-\-\> splitting \-\-\> storage \-\-\> retrieval \-\-\> output
        - example: **create chatbot to talk to your notion database**
    - Document Loading
        - Load data from URLs, PDFs, youtube audio, figma / notion, databases, twitter, airbyte, stripe, airtable
        - PDF, HTML, JSON, word, powerpoint; structured or unstructured data, databases, data warehouses
        - loads variety of data into standard document type \(content, metadata\)
    - Document Splitting
        - chunk size, chunk overlap
        - type of splitters: character text, markdown header, token text, sentence transformer, recursive character text splitter, language \(c\+\+, python, ruby, markdown\), NLTK text splitter \(sentence text splitter\), spacy text splitter \(sentence text splitter\)
    - Vectorstores and Embedding
        - https://www.elastic.co/what-is/vector-database  
        - split text / document \-\-\> embedding \-\-\> vector store
        - embedding similarity search
            - question to LLM: returns all similar embeddings
                - e.g. question: has 'email'; embedding returned has 'email': semantic similarity search
        - chroma vector store: lightweight, in memory
        - Milvus: A Purpose-Built Vector Data Management System https://www.youtube.com/watch?v=kIj-KKnC-PA
    - Retrieval
        - semantic similarity search
        - maximal marginal relevance
            - fetch\_k most similar responses \-\> within set of fetch\_k, fetch k most diverse responses
            - diversity
            - specificity
        - LLM aided retrieval \(self query\)
            - user question \-\-\> query parser \-\-\> query \(filter \+ semantic search term\)
        - compression
            - pull out most relevant bits of retrieved passages
            - pass 1: retrieve most similar documents \-\-\> LLM \-\> pass 2: retrieve most similar parts of documents
        - SVM, TF\-IDF retrieval
    - Question Answering
        - pass question, documents retrieved to LLM
            - use prompt chain with LLM
        - techniques to combat short context windows \(too many documents for context window\)
            - map reduce
                - pass each document chunk to separate LLM \(map\) \-\-\> combine results in 1 LLM \(reduce\)
            - refine
                - pass each document chunk to separate LLM \(map\) \-\-\> combine results in cascading steps of LLMS \(refine\)
            - map rerank
                - pass each document chunk to separate LLM \(map\) \-\-\> select LLM output with highest score \(rerank\)
        - **LangSmith Langchain UI**
            - list of chains \(map reduce / refine / map rerank arch\); for each chain:
                - chain input
                - chain output
                - run metadata
                - run stats
                - child runs
    - Chat
        - **chatbot over your data**: ask follow up questions to original question
        - ConversationalRetrievalChain \(llm, retriever, memory inputs\)
            - conversation buffer memory: chat history: memory between chains
            - modular components
            - add additional retriever and compression features as needed
        - UI
            - input to chain: question, chat history
            - chat history managed outside the chain
            - code creates nice chatbot UI
    - Conclusion
- Evaluating and Debugging Generative AI
    - https://www.deeplearning.ai/short-courses/evaluating-debugging-generative-ai/
        - W&B Standard MLOps platform, has support for LLMOps
            - ![w b](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/553fe852-b26a-435a-be7d-54dc97fe479f)
        - Train diffusion models
        - Evaluate diffusion models
        - Evaluate LLMs
            - Track LLM chain spans
            - track langchain agents
                - ![tracklangchainagent](https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/0c149085-f5a9-4b25-b0c0-6fb81d3d811a)
        - Fine Tune LLMs

- Langgraph is built on top of Langchain and allows for DAGs https://www.youtube.com/live/c7osr__qlos
- The emerging LLMOps stack: https://www.youtube.com/watch?v=OiyP8uUI1OU
- Astronomer and LLMOps https://www.youtube.com/watch?v=oOUKB9Z4FTQ
    - Gen AI use cases
<img width="1792" alt="Screenshot 2024-06-02 at 5 50 16 PM" src="https://github.com/huang-pan/modern-data-stack-2023/assets/10567714/2b832e40-545f-4136-9179-01bb432ff5a0">

- Risc-V open source CPU instruction set (like ARM which is closed source), has adaptable vector processing of data of variable lengths https://www.youtube.com/watch?v=Ozj_xU0rSyY

- Advanced Q&A Chatbot Using Ragstack With vector-enabled Astra DB Serverless database And Huggingface https://www.youtube.com/watch?v=8Vq4K1EGq2g

### Graph RAG
- https://www.youtube.com/watch?v=vX3A96_F3FU
![Screenshot_20240705-071315_YouTube](https://github.com/user-attachments/assets/155fb21b-8d2b-4f39-bdc6-22194acb462e)
![Screenshot_20240705-071113_YouTube](https://github.com/user-attachments/assets/8d570154-1db2-4d48-9e51-f1f81e494ddc)
![Screenshot_20240705-071136_YouTube](https://github.com/user-attachments/assets/bf8883eb-432b-4757-96ba-a5cb9e359178)
![Screenshot_20240705-071227_YouTube](https://github.com/user-attachments/assets/03b5970f-bb84-4fad-a24f-ca235716b3e0)

## VectorDB

### Weviate 
- Powering Vector Search with Real-Time Data: Weviate + Quix https://www.youtube.com/live/9pG1pspgELU
![Screenshot_20240629-185511_YouTube](https://github.com/user-attachments/assets/2917b6aa-e2c6-4581-ba8a-c67d1d74986d)
![Screenshot_20240629-185628_YouTube](https://github.com/user-attachments/assets/022737be-6276-45ce-998a-4968e0125901)
![Screenshot_20240629-185744_YouTube](https://github.com/user-attachments/assets/bccdc09c-6fd5-4fe1-9cb3-e1c211b07562)
![Screenshot_20240629-185750_YouTube](https://github.com/user-attachments/assets/b23a1faf-b822-4ff4-8f2e-86ea344ca38d)
![Screenshot_20240629-185828_YouTube](https://github.com/user-attachments/assets/adce2998-4806-46b5-b30d-0f74d9ff8c8a)
![Screenshot_20240629-185924_YouTube](https://github.com/user-attachments/assets/c6eea530-5585-4ed5-8b7b-f1d05dcec440)
![Screenshot_20240629-190143_YouTube](https://github.com/user-attachments/assets/6748de26-0fae-4021-8c5c-6b04c4b3f9f5)
![Screenshot_20240629-190112_YouTube](https://github.com/user-attachments/assets/16ccd691-be2e-40a2-a899-3c7ca02c5363)
![Screenshot_20240629-190153_YouTube](https://github.com/user-attachments/assets/f81cab9f-f8c7-460a-90b5-bb76d3d6f711)
![Screenshot_20240629-190402_YouTube](https://github.com/user-attachments/assets/750846e9-931f-45e8-80b0-e64e777189c8)
![Screenshot_20240629-190516_YouTube](https://github.com/user-attachments/assets/698e6c04-aff4-4ff0-8e6c-2618539bf434)

### AI Agents
- 5 types of AI agents https://www.youtube.com/watch?v=fXizBc03D7E
