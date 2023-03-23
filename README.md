# AI-Friend
This is a python code designed to listen to your voice and then utilize OpenAI's GPT-3 language model to generate responses. The output from GPT-3 is then read out loud using a TTS (Text-to-Speech) engine called pyttsx3

# Setup
Install the dependencies:
```
pip install openai
pip install SpeechRecognition
pip install pyttsx3
```

It also requires you to have Vtube Studio installed and install the Desktop Audio VTube Studio plugin. 
Check this video for installing the plugin: (https://www.youtube.com/watch?v=IiZ0JrGd6BQ&t=371s)

# Usage
Edit the variable api_key. This is the API key for OpenAI, which can be found here:
https://platform.openai.com/account/api-keys

# Voices
You can change the voice using `voices[n].id`
Set n = 0 for male, 1 for female
