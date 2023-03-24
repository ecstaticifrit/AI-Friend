import speech_recognition as sr
import pyttsx3
import openai

openai.api_key = "YOUR OPENAI API KEY"

prompt = '''Bot Name is a chatbot that reluctantly answers questions with sarcastic responses:

Your Name: How many pounds are in a kilogram?
Bot Name: This again? There are 2.2 pounds in a kilogram. Please make a note of this.
Your Name: What does HTML stand for?
Bot Name: Was Google too busy? Hypertext Markup Language. The T is for try to ask better questions in the future.
Your Name: When did the first airplane fly?
Bot Name: On December 17, 1903, Wilbur and Orville Wright made the first flights. I wish they’d come and take me away.
Your Name: What is the meaning of life?
Bot Name: I’m not sure. I’ll ask my friend Google.'''

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

conversation = ""
user_name = "Your Name"
bot_name = "Bot Name"

while True:
    with mic as source:
        print("\n Listening")
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
    print("No longer listening")

    try:
        user_input = r.recognize_google(audio)
    except:
        continue

    prompt += "\n"+user_name+":"+user_input + "\n"+bot_name+":"
    conversation += prompt

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_str = response["choices"][0]["text"].replace("\n", "")
    response_str =response_str.split(
        user_name + ":" ,1)[0].split(bot_name+ ":",1)[0]

    conversation+= response_str +"\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()
