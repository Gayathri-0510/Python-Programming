def tech(d1,d2,d3):
    d1=set(email.lower() for email in d1)
    d2=set(email.lower() for email in d2)
    d3=set(email.lower() for email in d3)
    all_attendees=d1|d2|d3
    print("People attended ",all_attendees)
    three_days_attendees= d1&d2&d3
    print("People attended all three days ",three_days_attendees)
    one_day_attendees=(d1-(d2|d3))|(d2-(d1|d3))|(d3-(d1|d2))
    print("People attended only one day ",one_day_attendees)
    overlap1=(d1&d2)
    overlap2=d2&d3
    overlap3=d3&d1
    print("People attended day 1 and 2 :",overlap1)
    print("People attended day 2 and 3 :",overlap2)
    print("People attended day 3 and 1 :",overlap3)
d1=["adi@gmail.com","shiv@gmail.com","Maya@gmail.com"]
d2=["shiv@gmail.com","adi@gmail.com","ayu@gmail.com"]
d3=["anshu@gmail.com","shiv@gmail.com","ayu@gmail.com"]
tech(d1,d2,d3)
