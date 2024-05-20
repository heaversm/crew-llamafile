#!/bin/zsh

# variables
model_name="llama2"
custom_model_name="crewai-llama2"

#get the base model
ollama pull $model_name

#create the model file
ollama create $custom_model_name -f ./Llama2ModelFile