class student:
    def __init__(self):
        print("student called")
        roll = 1
        standard = '9th'
        marks = 80

    def presentation(self, topic):
        print("presentation on topic", topic)

rohan = student()
rohan.presentation('sst')