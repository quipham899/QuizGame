import random

class TarotCards(object):
    def predictions(self):
        scenarios = ["How you feel about yourself","What you want most right now", "Your fears", "What is going on for you","What is going against you", "The likely outcome",""]
        cards = ["Hermit","The World","Death","Hanged Man", "The magician","Emperor","Hierophant","Empress","Strength", "Wheel of Fortune", "Justice", "Judgement", "High-Priestess", "Lover"]
        question = "What is your questions?"
        print(f"Here are the results for your questions")
        for i in range(6):
            print(scenarios[i])
            print(f"{i}.{cards[random.randrange(13)]}")


class Oracle(object):
    def predictions(self):
        responses = ["Yes", "No", "Potentially", "Could be","Don't doubt it.","Doubt it", "Definitely doubt it", "Absolutely not, what are you even thinking?", "I'd believe more in the U.S currency, than I would that. "]
        print("What is your name?")
        name = input("Enter your name: ")
        question = input("What is your questions?")
        print(f"Well {name}, in respond to your {question} the answer is {responses[random.randrange(8)]}")


class FortuneTelling(object) :
    list = {
    'TarotCards' : TarotCards(),
    'Oracle' : Oracle(),
    }
    def telling():
        fortuneTelling = ["TarotCards", "Oracle", 'IChing',"Astrology"]
        for i in range(3):
            print(f"{i}.{fortuneTelling[i]}")
        choice = int(input("Which method of fortune telling do you want to use?"))
        FortuneTelling.list.get(fortuneTelling[choice]).predictions()



FortuneTelling.telling()
