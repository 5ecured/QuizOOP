class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

quest = Question('aaa','bbb')
print(quest.text)
print(quest.answer)