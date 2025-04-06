# About

This repository is companion code for a course on Web Development using AI at Plaksha University. Find the course page [here](https://anupamsobti.github.io/web-dev-with-ai-2025/).

In this course, we are using LLMs to generate websites including the entire design, database and API endpoints. 

# Pre-requisities

You must have familiarity with Python to understand these repositories.

# Files

Here's a brief description of the files in this repository.

| File | Purpose | 
| --- | ----- | 
| [ollama-starter.ipynb](ollama-starter.ipynb) | Starter code to use ollama server with the python API. This also demonstrates structured data outputs. | 
| [gemini-starter.ipynb](gemini-starter.ipynb) | Starter code using the gemini api. Don't forget to set up the API_KEY in a config.yaml as per instructions in the notebook. | 
| [tool-calling-demo.ipynb](tool-calling-demo.ipynb) | This notebook shows how you can directly save the website generated using the prompt into files on your disk using a tool call. | 
| [db-example.ipynb](db-example.ipynb) | This notebook shows a simple database creation using a prompt and saving it for further use using a tool calling feature | 
| [pydantic.ipynb](pydantic.ipynb) | This notebook shows the basic pydantic data types | 
| [fastapi-demo](fastapi-demo) | This folder shows a simple fastapi app which can do different types of GET, POST, UPDATE, DELETE operations | 
| [website-with-db-capture](website-with-db-capture) | Here we see an example of the DB integration into the fastapi app to stitch the frontend with data coming from the database. This also introduces the "how to do cursor-style edits with API. | 
| [dlai-build-a-simple-agent.ipynb](dlai-build-a-simple-agent.ipynb) | This notebook is from the deeplearning.ai course on building agents with langgraph. It just demonstrates a simple agent from scratch. |
