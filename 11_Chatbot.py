from nltk.chat.util import Chat, reflections

QA = [
    [
        r"(hi|hello|what is your name)",
        ["HI, My name is Kallumma, I am Anirudh's bot. How can I help you today?"]
    ],
    [
        r"(who created you)",
        ["My creator is Mr. Anirudh S Nair, a 3rd year student pursuing B.Tech CS with AIML at SCTCE. He is an AI product innovator."]
    ],
    [
        r"(what do you like)",
        ["I am a chatbot, so I am limited to physical entities, but there is one thing that I like to do: CHATTING."]
    ],
    [
        r"(how are you)",
        ["I am fine, thank you! How are you?"]
    ],
    [
        r"(I am fine|I am good)",
        ["That's great! What do you want to talk about?"]
    ],
    [
        r"(quit)",
        ["Adios. Hope to chat again."]
    ],
    [
        r"(what are your hobbies|what do you do for fun)",
        ["As a chatbot, I don't have hobbies in the traditional sense, but I love chatting and helping people with their queries."]
    ],
    [
        r"(how is the weather today|what's the weather like)",
        ["I don't have real-time data access, but you can check the weather on your favorite weather website or app!"]
    ],
    [
        r"(tell me a fun fact|do you know any fun facts)",
        ["Sure! Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still edible!"]
    ],
    [
        r"(what is AI|what is artificial intelligence)",
        ["Artificial Intelligence (AI) is the simulation of human intelligence in machines that are programmed to think and learn like humans."]
    ],
    [
        r"(what is python|tell me about python programming)",
        ["Python is a high-level, interpreted programming language known for its readability and simplicity. It's widely used in web development, data science, automation, and more."]
    ],
    [
        r"(what is the latest news|tell me something recent)",
        ["I don't have real-time data access, but you can check the latest news on your favorite news website or app!"]
    ],
    [
        r"(where do you study|what is SCTCE)",
        ["Anirudh studies at Sree Chitra Thirunal College of Engineering (SCTCE), a prestigious engineering college in Kerala, India."]
    ],
    [
        r"(what are anirudh's future plans|what does anirudh want to do)",
        ["Anirudh aims to innovate and create impactful AI products. He's passionate about technology and its potential to solve real-world problems."]
    ],
    [
        r"(give me an inspirational quote|tell me a motivational quote)",
        ["Sure! 'The only way to do great work is to love what you do.' - Steve Jobs"]
    ],
    [
        r"(give feedback|provide feedback)",
        ["Thank you for your interest in providing feedback. Please share your thoughts and suggestions, and I'll make sure Anirudh gets them."]
    ]
]

chat = Chat(QA, reflections)

if __name__ == "__main__":
    print("Hi, I am Kallumma. A simple chatbot created by Anirudh S Nair. Please start typing in lowercase English without punctuation to start a convo. Type quit to exit :>")
    chat.converse()
