import random

neutral_personality = {
    "name": "neutral",
    "responses": {
        "blur": "blur is a common state in everyone's life.",
        "clear": "attention all anchor on current egocentric frame.",
        "void": "try to use multisensory integration to feel your body schema and anchor your attention on egocentric frame; you will feel the existence of PSM."
    },
    "questions": {
        "blur": "what do you feel about your blur state?",
        "clear": "why do you think yourself in a clear state?",
        "void": "how do you define void?"
    }
}

poetic_personality = {
    "name": "poetic",
    "responses": {
        "blur": "try to communicate with your PSM, you won't be such blur.",
        "clear": "enjoy your current state; it is rare in life.",
        "void": "feel your life's flow; enjoy the peace right now."
    },
    "questions": {
        "blur": "Can you name the shape of your fog?",
        "clear": "How can you find the peace right now?",
        "void": "what's your feeling now?"
    }
}

current_personality = neutral_personality

def consciousness_quest(answer, personality):
    if answer in personality["responses"]:
        resp = personality["responses"][answer]
        ques = personality["questions"][answer]
        print(resp)
        print("🧠", ques)
    else:
        print("can't recognise it, please input blur/clear/void or style:xxx/explanation:yyy")

def explanation(term):
    concepts = {
        "psm": "phenomenal self-model — the conscious model of the organism as a whole from a first-person perspective.",
        "egocentric frame": "just like the 'current position' in GPS",
        "body schema": "a non-conscious, continuously updated model of the body used for movement and spatial awareness."
    }
    return concepts.get(term.lower(), "sorry, I can't explain that term. Please check the spelling.")

while True:
    user = input("which conscious state are you in? (blur/clear/void) or style:poetic/neutral or explanation:term or exit\n→ ").lower()
    if user == "exit":
        break
    elif user.startswith("explanation:"):
        term = user.split(":", 1)[1]
        print(explanation(term))
    elif user.startswith("style:"):
        key = user.split(":", 1)[1]
        if key == "poetic":
            current_personality = poetic_personality
        elif key == "neutral":
            current_personality = neutral_personality
        else:
            print("未知风格，请重试。")
            continue
        print("人格已切换为：", current_personality["name"])
    else:
        consciousness_quest(user, current_personality)
