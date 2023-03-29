# AI-Friend
Do you struggle with making friends? Do you miss having a good conversation with someone without them judging you? Then this for you. This is a python code designed to listen to your voice and then utilize OpenAI's GPT-3 language model to generate responses. The output from GPT-3 is then read out loud using a TTS (Text-to-Speech) engine called pyttsx3.

# Setup
Install the following dependencies:
```
pip install openai
pip install SpeechRecognition
pip install pyttsx3
```

It also requires you to have VTube Studio installed and install the Desktop Audio VTube Studio plugin. 
Check this video for installing and setting up the plugin: (https://www.youtube.com/watch?v=IiZ0JrGd6BQ&t=371s)

# API Keys
Edit the variable `api_key`. This is the API key for OpenAI, which can be found here:
https://platform.openai.com/account/api-keys

# Voices
You can change the voice using `voices[n].id`
Set n = 0 for male, 1 for female.

Now you're all set to start talking to your AI friend and maybe learn something new along the way

# Demo
https://youtu.be/UdGl1i9X1zo
