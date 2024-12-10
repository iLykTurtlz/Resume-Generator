from .data_generator import DataGenerator
import random
import json
import datetime

class ExperienceDataGenerator(DataGenerator):
    def __init__(self):
        super().__init__()
        
        with open("data/final_jobs_info.json", "r") as f:
            self.jobs_info = json.load(f)
            
        with open("data/cs_companies_with_counts.json") as f:
            counts_dict = json.load(f)
            
        # remove companies that have no postings from our count
        filtered_counts_dict = {name: count for name, count in counts_dict.items() if any(
            job["company_name"] == name for job in self.jobs_info.values()
        )}
            
        total_count = sum(filtered_counts_dict.values())
        self.company_proportions = {name: count / total_count for name, count in filtered_counts_dict.items()}
        self.jobs_by_company = {}
        for job_id, job in self.jobs_info.items():
            company_name = job["company_name"]
            if company_name not in self.jobs_by_company:
                self.jobs_by_company[company_name] = []
            self.jobs_by_company[company_name].append(job_id)
            
    def _generate_date_ranges(self, num_experiences, start_year=2020, end_year=2024):
        while True:
            try:
                ranges = []
                current_year = random.randint(start_year, end_year - 1)  # Random start year
                current_month = random.randint(1, 12)  # Random start month

                for i in range(num_experiences):
                    # Ensure the start date is within bounds
                    if current_year > end_year or (current_year == end_year and current_month > 1):
                        raise ValueError("Exceeded the last valid date in 2024.")
                    
                    # Calculate maximum months until 2024
                    max_duration_months = ((end_year - current_year) * 12) - (current_month - 1)
                    if max_duration_months < 3:
                        raise ValueError("Not enough time left for minimum job duration.")

                    # Randomize duration (minimum 3 months, maximum 24 months or remaining time)
                    duration_months = random.randint(3, min(24, max_duration_months))
                    start_date = datetime.date(current_year, current_month, 1)
                    end_date = start_date + datetime.timedelta(days=(duration_months * 30)) - datetime.timedelta(days=1)
                    

                    # Add the range and prepare for the next start date
                    ranges.append((start_date, end_date))
                    next_start_month = end_date.month + 1
                    next_start_year = end_date.year
                    if next_start_month > 12:
                        next_start_month -= 12
                        next_start_year += 1
                        
                    if i == num_experiences - 1 and random.random() < 0.8:
                        end_date = None # set it to present with an 80% chance if it's the last experience

                    current_year, current_month = next_start_year, next_start_month

                return ranges  # If all ranges are valid, return them
            except ValueError:
                continue  # Retry generation if the sequence is invalid
    
    def generate(self, context):
        date_ranges = self._generate_date_ranges(len(context))
        self.all_achievements = [] # list of all achievements
        for experience, (start_date, end_date) in zip(context, list(reversed(date_ranges))):
            company = random.choices(list(self.company_proportions.keys()), list(self.company_proportions.values()))[0]
            job_id = random.choice(self.jobs_by_company[company])
            job = self.jobs_info[job_id]
            value = r'''%s [\href{%s}{\faIcon{globe}}]''' % (company, job['site'])
            experience["CompanyName"].value = value
            experience["JobTitle"].value = job["job_title"]
            
            if end_date is None:  # End date is "Present"
                experience["DateRange"].value = f"{start_date.strftime('%B %Y')} - Present"
            else:
                experience["DateRange"].value = f"{start_date.strftime('%B %Y')} - {end_date.strftime('%B %Y')}"
            
            experience["GeographicalInfo"].value = job["location"]
            
            # list of strings
            job_achievements = random.sample(
                job["achievements"], 
                len(experience["ExperienceTasks"])
            )
            
            self.all_achievements += [achievement for achievement in job_achievements]
            
            for task, achievement in zip(experience["ExperienceTasks"], job_achievements):
                task.value = achievement.replace("%", "\%").replace("#", "\#")
