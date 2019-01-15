import datetime

now = datetime.datetime.now()

obj = {
    "first": "colin",
    "last": "daniel",
    "age": 20,
    "birth_year": 1998,
    "birth_month": "12",
    "birth_day": "27"
}

class Person:
    def __init__(self, firstName, lastName , age, month, day, job="unemployed"):
        self.firstName = firstName
        self.lastName = lastName
        self.job = job
        self.age = age
        self.month = month
        self.day = day

    def hello(self):
        if(self.job != "unemployed"):
            print("Hi my name is " + self.firstName + " " + self.lastName + ", and i am a " + self.job)
        else:
            print("Hi my name is " + self.firstName + " " + self.lastName + ", and i am currently looking for a job as a software dev intern")

    def level_up(self):
        if(now.strftime("%m") == self.month):
            if(now.strftime("%d") == self.day):
                self.age += 1
                print("happy birthday " + self.firstName + "!")
        else:
            print("it's not your birthday today")


Me = Person(obj["first"], obj["last"], obj["age"], obj["birth_month"], obj["birth_day"])

if(now.strftime("%H") == "00"):
    Me.level_up()