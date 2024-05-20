# CREW AI Basic Agent Example

## Setup:

* Get a [serper API key](https://serper.dev)
* Get an [openAI API key](https://platform.openai.com/api-keys)
* Save the `env-sample` file as `.env` and paste in your API keys

## Installation:

In terminal, in root folder, type:

* `pip install crewai`
* `pip install 'crewai[tools]'`
* `pip install dotenv`

## Configuration

In `app.py`:
* Set desired model name (`OPENAI_MODEL_NAME='gpt-4o'`)
* Modify agents to do whatever task you'd like to see performed.

## Run Workflow

* In terminal, type: `python app.py`

