# CREW AI Examples

## Basic Example

### Setup:

* Get a [serper API key](https://serper.dev)
* Get an [openAI API key](https://platform.openai.com/api-keys)
* Save the `env-sample` file as `.env` and paste in your API keys

### Installation:

In terminal, in root folder, type:

* `pip install crewai`
* `pip install 'crewai[tools]'`
* `pip install dotenv`

### Configuration

In `app.py`:
* Set desired model name (`OPENAI_MODEL_NAME='gpt-4o'`)
* Modify agents to do whatever task you'd like to see performed.

### Run Workflow

* In terminal, type: `python app.py`

## Ollama Example

In addition to the installation steps above, do the following:

* [Download ollama](https://github.com/ollama/ollama)
* In terminal, run `pip install langchain_openai`
* Get the llama2 model: `ollama pull llama2`
* In the terminal from project root, run `bash crewai-create-llamafile.sh`
* Once this is done, from terminal, run `python ollama-app.py` and view the output in your terminal