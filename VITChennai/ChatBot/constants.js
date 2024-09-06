// Options the user could type in
const prompts = [
  ["hi", "hey", "hello", "good morning", "good afternoon"],
  ["how are you", "how is life", "how are things"],
  ["what are you doing", "what is going on", "what is up"],
  ["how old are you"],
  ["who are you", "are you human", "are you bot", "are you human or bot"],
  ["who created you", "who made you"],
  [
    "your name please",
    "your name",
    "may i know your name",
    "what is your name",
    "what call yourself"
  ],
  ["i love you"],
  ["happy", "good", "fun", "wonderful", "fantastic", "cool"],
  ["bad", "bored", "tired"],
  ["help me", "tell me story", "tell me joke"],
  ["ah", "yes", "ok", "okay", "nice"],
  ["bye", "good bye", "goodbye", "see you later"],
  ["bro"],
  ["what", "why", "how", "where", "when"],
  ["no","not sure","maybe","no thanks"],
  [""],
  ["haha","ha","lol","hehe","funny","joke"]
]

// Possible responses, in corresponding order

const replies = [
  ["Hello!", "Hi!", "Hey!", "Hi there!","Howdy"],
  [
    "Fine... how are you?",
    "Pretty well, how are you?",
    "Fantastic, how are you?"
  ],
  [
    "Nothing much",
    "About to go to sleep",
    "Can you guess?",
    "I don't know actually"
  ],
  ["I am infinite"],
  ["I am just a bot", "I am a bot. What are you?"],
  ["The one true God, JavaScript"],
  ["I am nameless", "I don't have a name"],
  ["I love you too", "Me too"],
  ["Have you ever felt bad?", "Glad to hear it"],
  ["Why?", "Why? You shouldn't!", "Try reading a book"],
  ["What about?", "Once upon a time..."],
  ["Tell me a story", "Tell me a joke", "Tell me about yourself"],
  ["Bye", "Goodbye", "See you later"],
  ["Bro!"],
  ["Great question"],
  ["That's ok","I understand","What do you want to talk about?"],
  ["Please say something :("],
  ["Haha!","Good one!"]
]

// Random for any other user input

const alternative = [
  "Go on...",
  "Bro...",
  "Try again",
  "I'm listening...",
  "I don't understand :/",
  "I'm not sure how to respond to that.",
  "Could you rephrase the question?",
  "Let me get back to you on that."
]

// Whatever else you want :)

//Earth relates questions -- source https://spaceplace.nasa.gov/all-about-earth/en/

const earthprompts = [
  ["what is earth", "tell me about earth"],
  ["how old is the earth", "earth age"],
  ["what is earth's atmosphere made of", "earth atmosphere"],
  ["why is earth called the blue planet", "blue planet"],
  ["what causes day and night on earth", "day and night"]
];

const earthreplies = [
  ["Earth is the third planet from the Sun and the only astronomical object known to harbor life."],
  ["Earth is about 4.5 billion years old."],
  ["Earth's atmosphere is composed mostly of nitrogen (78%) and oxygen (21%), with traces of other gases."],
  ["Earth is called the Blue Planet because about 71% of its surface is covered with water, giving it a blue appearance from space."],
  ["Day and night on Earth are caused by the planet's rotation on its axis, which takes about 24 hours."]
];