from roman import toRoman, fromRoman
from abc import ABC 

class Terminal(Symbol):
    pass




class Job:
    count = 0
    def __init__(self):
        Job.count += 1
        self.id = Job.count
        # self.company = company
        # self.city = city
        # self.country = country
        # self.job_title = job_title
        # self.start_date = start_date
        # self.end_date = end_date
        # self.achievements = achievements
        #'company', 'city', 'country', 'job_title, start_date, end_date, achievements
