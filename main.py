import pyttsx3
import speech_recognition as sr
#from googletrans import Translator
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import NuSVC
from sklearn.svm import LinearSVC
import nltk
from sklearn.model_selection import train_test_split
import random
import warnings
warnings.simplefilter('ignore')


#nltk.download("punkt")



def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    # print("")
    # print(f"CN: {text}")
    # print("")
    engine.say(text)
    engine.runAndWait()


def listen():
    listener = sr.Recognizer()

    with sr.Microphone() as source:
        # print("listening....")
        listener.pause_threshold = 1
        voice = listener.listen(source,0,4)

    try:
        # print("Recognizing..")
        query = listener.recognize_google(voice,language = "en")

    except:
        return ""
    
    #query = str(query).lower
    return query
    
# def TranslationHinEn(text):
#     line = str(text)
#     translate = Translator()
#     result = translate.translate(line)

#     data = result.text
#     print(f"You :{data}")
#     return data


def output():
    query = listen()
    data = speak(query)

    return data


def main(query):
    Query = str(query).lower()
    print("")
    print(f"You: {query}")

    if "hello" in Query:
        speak("Hello Sir, Welcome Back!")

    elif "bye" in Query:
        speak("Nice to meet you sir, Have a nice day!")


# while True:
#     Query = listen()
#     main(Query)

intents = {
    "greetings": {
        "patterns": ["hello", "hi", "hey", "howdy", "greetings", "good morning", "good afternoon", "good evening", "hi there", "hey there", "what's up", "hello there"],
        "responses": ["Hello! How can I assist you?", "Hi there!", "Hey! What can I do for you?", "Howdy! What brings you here?", "Greetings! How may I help you?", "Good morning! How can I be of service?", "Good afternoon! What do you need assistance with?", "Good evening! How may I assist you?", "Hey there! How can I help?", "Hi! What's on your mind?", "Hello there! How can I assist you today?"]
    },
    "goodbye": {
        "patterns": ["bye", "see you later", "goodbye", "farewell", "take care", "until next time", "bye bye", "catch you later", "have a good one", "so long"],
        "responses": ["Goodbye!", "See you later!", "Have a great day!", "Farewell! Take care.", "Goodbye! Until next time.", "Take care! Have a wonderful day.", "Bye bye!", "Catch you later!", "Have a good one!", "So long!"]
    },
    "gratitude": {
        "patterns": ["thank you", "thanks", "appreciate it", "thank you so much", "thanks a lot", "much appreciated"],
        "responses": ["You're welcome!", "Happy to help!", "Glad I could assist.", "Anytime!", "You're welcome! Have a great day.", "No problem!"]
    },
    "apologies": {
        "patterns": ["sorry", "my apologies", "apologize", "I'm sorry"],
        "responses": ["No problem at all.", "It's alright.", "No need to apologize.", "That's okay.", "Don't worry about it.", "Apology accepted."]
    },
    "positive_feedback": {
        "patterns": ["great job", "well done", "awesome", "fantastic", "amazing work", "excellent"],
        "responses": ["Thank you! I appreciate your feedback.", "Glad to hear that!", "Thank you for the compliment!", "I'm glad I could meet your expectations.", "Your words motivate me!", "Thank you for your kind words."]
    },
    "negative_feedback": {
        "patterns": ["not good", "disappointed", "unsatisfied", "poor service", "needs improvement", "could be better"],
        "responses": ["I'm sorry to hear that. Can you please provide more details so I can assist you better?", "I apologize for the inconvenience. Let me help resolve the issue.", "I'm sorry you're not satisfied. Please let me know how I can improve.", "Your feedback is valuable. I'll work on improving."]
    },
    "weather": {
        "patterns": ["what's the weather like?", "weather forecast", "is it going to rain today?", "temperature today", "weather report"],
        "responses": ["The weather today is [weather_description].", "Currently, it's [temperature] degrees with [weather_description].", "The forecast predicts [weather_forecast].", "It might rain today. Don't forget your umbrella!", "The temperature today is [temperature] degrees."]
    },
    "help": {
        "patterns": ["help", "can you help me?", "I need assistance", "support"],
        "responses": ["Sure, I'll do my best to assist you.", "Of course, I'm here to help!", "How can I assist you?", "I'll help you with your query."]
    },
    "time": {
        "patterns": ["what's the time?", "current time", "time please", "what time is it?"],
        "responses": ["It's [current_time].", "The current time is [current_time].", "Right now, it's [current_time]."]
    },
    "jokes": {
        "patterns": ["tell me a joke", "joke please", "got any jokes?", "make me laugh"],
        "responses": ["Why don't we ever tell secrets on a farm? Because the potatoes have eyes and the corn has ears!", "What do you get when you cross a snowman and a vampire? Frostbite!", "Why was the math book sad? Because it had too many problems!"]
    },
    "music": {
        "patterns": ["play music", "music please", "song recommendation", "music suggestion"],
        "responses": ["Sure, playing some music for you!", "Here's a song you might like: [song_name]", "How about some music?"]
    },
    "food": {
        "patterns": ["recommend a restaurant", "food places nearby", "what's good to eat?", "restaurant suggestion"],
        "responses": ["Sure, here are some recommended restaurants: [restaurant_names]", "Hungry? Let me find some good food places for you!", "I can suggest some great places to eat nearby."]
    },
    "news": {
        "patterns": ["latest news", "news updates", "what's happening?", "current events"],
        "responses": ["Let me fetch the latest news for you.", "Here are the top headlines: [news_headlines]", "Stay updated with the latest news!"]
    },
    "movies": {
        "patterns": ["movie suggestions", "recommend a movie", "what should I watch?", "best movies"],
        "responses": ["How about watching [movie_name]?", "Here's a movie suggestion for you.", "Let me recommend some great movies!"]
    },
    "sports": {
        "patterns": ["sports news", "score updates", "latest sports events", "upcoming games"],
        "responses": ["I'll get you the latest sports updates.", "Stay updated with the current sports events!", "Let me check the sports scores for you."]
    },
    "gaming": {
        "patterns": ["video game recommendations", "best games to play", "recommend a game", "gaming suggestions"],
        "responses": ["How about trying out [game_name]?", "Here are some gaming suggestions for you!", "Let me recommend some fun games to play!"]
    },
        "tech_support": {
        "patterns": ["technical help", "computer issues", "troubleshooting", "IT support"],
        "responses": ["I can assist with technical issues. What problem are you facing?", "Let's troubleshoot your technical problem together.", "Tell me about the technical issue you're experiencing."]
    },
    "book_recommendation": {
        "patterns": ["recommend a book", "good books to read", "book suggestions", "what should I read?"],
        "responses": ["How about reading [book_title]?", "I've got some great book recommendations for you!", "Let me suggest some interesting books for you to read."]
    },
    "fitness_tips": {
        "patterns": ["fitness advice", "workout tips", "exercise suggestions", "healthy habits"],
        "responses": ["Staying fit is important! Here are some fitness tips: [fitness_tips]", "I can help you with workout suggestions and fitness advice.", "Let me provide some exercise recommendations for you."]
    },
    "travel_recommendation": {
        "patterns": ["travel suggestions", "places to visit", "recommend a destination", "travel ideas"],
        "responses": ["Looking for travel recommendations? Here are some great destinations: [travel_destinations]", "I can suggest some amazing places for your next travel adventure!", "Let me help you with travel destination ideas."]
    },
    "education": {
        "patterns": ["learning resources", "study tips", "education advice", "academic help"],
        "responses": ["I can assist with educational queries. What subject are you studying?", "Let's explore learning resources together.", "Tell me about your educational goals or questions."]
    },
    "pet_advice": {
        "patterns": ["pet care tips", "animal advice", "pet health", "taking care of pets"],
        "responses": ["Pets are wonderful! Here are some pet care tips: [pet_care_tips]", "I can provide advice on pet health and care.", "Let's talk about your pet and their well-being."]
    },
    "shopping": {
        "patterns": ["online shopping", "buying something", "shopping advice", "product recommendations"],
        "responses": ["I can help you with online shopping. What are you looking to buy?", "Let's find the perfect item for you!", "Tell me what you're interested in purchasing."]
    },
    "career_advice": {
        "patterns": ["job search help", "career guidance", "career change advice", "professional development"],
        "responses": ["I can provide career advice. What specific guidance do you need?", "Let's explore career opportunities together.", "Tell me about your career goals or concerns."]
    },
    "relationship_advice": {
        "patterns": ["relationship help", "love advice", "dating tips", "relationship problems"],
        "responses": ["Relationships can be complex. How can I assist you?", "I can offer advice on relationships and dating.", "Tell me about your relationship situation."]
    },
    "mental_health": {
        "patterns": ["mental health support", "coping strategies", "stress relief tips", "emotional well-being"],
        "responses": ["Mental health is important. How can I support you?", "I can provide guidance for managing stress and emotions.", "Let's talk about strategies for maintaining mental well-being."]
    },
    "language_learning": {
        "patterns": ["language learning tips", "language practice", "learning new languages", "language study advice"],
        "responses": ["Learning a new language can be exciting! How can I assist you?", "I can help with language learning tips and practice.", "Tell me which language you're interested in learning."]
    },
    "finance_advice": {
        "patterns": ["financial planning help", "money management tips", "investment advice", "budgeting assistance"],
        "responses": ["I can provide guidance on financial matters. What specific advice do you need?", "Let's discuss your financial goals and plans.", "Tell me about your financial situation or goals."]
    },
    "directions": {
        "patterns": ["mph", "room number 111", "room number 112", "room number 113", "room number 114","room number 115","tutorial room-4","room number 116","room number 117","lt2","room number 127","room number 118","cr42","sr05","lt1","room number 126",
                     "room number 120","room number 121","CR 57","room number 122","room number 124","Satyendra Kumar sir room","room number 123","CR 58","housekeeping","drawing hall","faculty block 1A","ECE faculty block 1A","ES lab 1","mml lab",
                     "communication system lab","DSP lab","CSE project lab","ECE Project lab","CR 08","cicr hub","creativity and innovation lab","room number 140",
                     "B Suresh Sir room","room number 155","VLSI lab",
                     "room number 148","lt7","CR 59","CR 60","lt8","mobile development lab","network programming lab","data science and engineering lab","advance programming lab",
                     "language lab","room number 217","cr3","electromagnetic lab","Raju Pal sir room","room number 224","CR 52","cr6","room number 230","cr 05","tutorial six room","cr4","room number 225","analog and digital electronics lab",
                     "Faculty to be","mathematics faculty","embedded system and iot lab","mobile technology lab","flipped classroom","Cr 53","CR 54","cse research lab","is lab","CR 46","LT 9","room number 246","Amit Verma sir room","HSS faculty block","Alka sharma mam cabin"
                     "lt3","room number 254","lt4","room number 259","lt5","room number 256","lt6","room number 257",
                     "Mukta mam cabin","Shruti mam cabin","Payal mam cabin","Gaurav sir cabin","Aastha mam cabin"],
        
        "responses": ["GO Straight towards staircase4 and take left","1st floor,From staircase4 , first left , then left , 1st room","1st floor,From staircase4 , first left , then left , 2nd room","1st floor,From staircase4 , first left , then left , 3rd room",
                      "1st floor,From staircase4 , first left , then left ,4rd room","1st floor,From staircase4 , first left , then left ,5th room","1st floor,From staircase4 , first left , then left ,6th room","1st floor,From staircase4 , first left , then left ,6th room",
                      "1st floor,From staircase4 , first left , then left , then right","1st floor,From staircase4 , first left , then left , then right","1st floor,From staircase4 , first left , then left , then right","1st floor,From staircase4 , first left , then left , then right","1st floor,From staircase4 , first left , then left , then right",
                      "1st floor,From staircase4 , first left , then left , then right","1st floor,From staircase4 , first left , then left , then right","1st floor,From staircase4 , first left , then left , then right","1st floor,From staircase3 , straight , left , 3rd Room","1st floor,From staircase3 , straight , left","1st floor,From staircase3 , straight , left","1st floor,From staircase3 , straight , left","1st floor,From staircase3 , straight , left","1st floor,From staircase3 , straight , left","1st floor,From staircase3 , straight , left","1st floor,From staircase3 , straight , left","1st floor,From staircase , straight , Right ","1st floor,From staircase , straight , Right ",
                      "1st floor,From staircase2 , left","1st floor,From staircase2 , left","1st floor,From staircase2 , right","1st floor,From staircase2 , right",
                      "1st floor,From staircase2 , right, right","1st floor,From staircase2 , right,right","1st floor,From staircase2 , right,right","1st floor,From staircase2 , right,right","1st floor,From staircase2 , right,right","1st floor,From staircase2 , right,right","1st floor,From staircase2 , right,right",
                      "1st floor,From staircase2 , left , Right","1st floor,From staircase2 , left , right","1st floor,From staircase2 , left , right",
                      "1st floor,From staircase1 , left","1st floor,From staircase1 , left","1st floor,From staircase1 , left","1st floor,From staircase1 , left","1st floor,From staircase1 , left","1st floor,From staircase1 , left","1st floor,From staircase1 , left","1st floor,From staircase1 , left","1st floor,From staircase1 , left",
                      "2nd floor,From staircase4 , left, right","2nd floor,From staircase4 , left, right","2nd floor,From staircase4 , left, right",
                      "2nd floor,From staircase3 , left","2nd floor,From staircase3 , left","2nd floor,From staircase3 , left","2nd floor,From staircase3 , left","2nd floor,From staircase3 , left","2nd floor,From staircase3 , left","2nd floor,From staircase3 , left","2nd floor,From staircase3 , left","2nd floor,From staircase3 , left","2nd floor,From staircase3 , left","2nd floor,From staircase3 , left",
                      "2nd floor,From staircase2 , left","2nd floor,From staircase2 , right","2nd floor,From staircase2 , right","2nd floor,From staircase2 , right, right","2nd floor,From staircase2 , right, right","2nd floor,From staircase2 , right, right","2nd floor,From staircase2 , right, right","2nd floor,From staircase2 , right, right","2nd floor,From staircase2 , right, left","2nd floor,From staircase2 , right, left","2nd floor,From staircase2 , right, left","2nd floor,From staircase2 , right, left","2nd floor,From staircase2 , right, left","2nd floor,From staircase2 , right, left","2nd floor,From staircase2 , right, left",
                      "2nd floor,From staircase1,left","2nd floor,From staircase1,left","2nd floor,From staircase1,left","2nd floor,From staircase1,left","2nd floor,From staircase1,left","2nd floor,From staircase1,left",
                      "2nd floor, Faculty 2A,From staircase3,right","2nd floor, Faculty 2A,From staircase3,right","2nd floor, Faculty 2A,From staircase3,right","2nd floor, Faculty 2A,From staircase3,right","2nd floor, Faculty 2A,From staircase3,right"]
        
    },
}

training_data = []
labels = []

for intent , data in intents.items():
    for pattern in data['patterns']:
        training_data.append(pattern.lower())
        labels.append(intent)




Vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize, stop_words="english",max_df=0.8,min_df=1)
X_train = Vectorizer.fit_transform(training_data)
X_train,X_test,Y_train,Y_test = train_test_split(X_train,labels,test_size=0.4,random_state=42,stratify=labels)

#model = NuSVC(kernel = 'linear', probability=True, C=1.0)
model = LinearSVC(dual=True,C=1.0)

model.fit(X_train,Y_train)

predictions = model.predict(X_test)

def predict_intent(user_input):
    user_input = user_input.lower()
    input_vector = Vectorizer.transform([user_input])
    intent = model.predict(input_vector)[0]
    return intent

speak(" Hello! How can I assist you?")
def final():
    user_input = listen()
    
    if user_input == 'stop':
        print("CN: AI Assistant stopped.")
        speak("goodbye")
        return 0

    intent = predict_intent(user_input)
    if intent in intents:
        if intent == "directions":
            found_response = False
            for keyword, response in zip(["mph", "room number 111", "room number 112", "room number 113", "room number 114","room number 115","tutorial room-4","room number 116","room number 117","lt2","room number 127","room number 118","cr42","sr05","lt1","room number 126",
                     "room number 120","room number 121","CR 57","room number 122","room number 124","Satyendra Kumar sir room","room number 123","CR 58","housekeeping","drawing hall","faculty block 1A","ECE faculty block 1A","ES lab 1","mml lab",
                     "communication system lab","DSP lab","CSE project lab","ECE Project lab","CR 08","cicr hub","creativity and innovation lab","room number 140",
                     "B Suresh Sir room","room number 155","VLSI lab",
                     "room number 148","lt7","CR 59","CR 60","lt8","mobile development lab","network programming lab","data science and engineering lab","advance programming lab",
                     "language lab","room number 217","cr3","electromagnetic lab","Raju Pal sir room","room number 224","CR 52","cr6","room number 230","cr 05","tutorial six room","cr4","room number 225","analog and digital electronics lab",
                     "Faculty to be","mathematics faculty","embedded system and iot lab","mobile technology lab","flipped classroom","Cr 53","CR 54","cse research lab","is lab","CR 46","LT 9","room number 246","Amit Verma sir room","HSS faculty block","Alka sharma mam cabin"
                     "lt3","room number 254","lt4","room number 259","lt5","room number 256","lt6","room number 257",
                     "Mukta mam cabin","Shruti mam cabin","Payal mam cabin","Gaurav sir cabin","Aastha mam cabin"],
                                         intents[intent]['responses']):
                if keyword in user_input:
                    print(response)
                    speak(response)
                    
                    found_response = True
                    return 0

            if not found_response:
                print("Sorry, I'm not sure about the specific location.")
                speak("Sorry, I'm not sure about the specific location.")
                
                return 0
        else:
            responses = intents[intent]['responses']
            response = random.choice(responses)
            print(response)
            speak(response)
            
            return 0
    else:
        print("CN: Sorry, I'm not sure how to respond to that.")
        speak("CN: Sorry, I'm not sure how to respond to that.")
        
        return 0
    

final()