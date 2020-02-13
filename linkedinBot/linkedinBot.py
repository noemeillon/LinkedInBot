import time
from selenium import webdriver
import worksheetHandler
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import ElementClickInterceptedException

""" Create a LinkedIn Bot that scrapes the site with in info entered in parameters of the constructor"""

# Salary: .find_element_by_xpath(".//*[contains text(), 'salary']")


class LinkedInBot:

    """Constructor of the class, job_type is the type of job, job_location is where the job is located
     and number_of_jobs is the number of jobs the number that are going to be scraped"""
    def __init__(self, job_type, job_location, number_of_jobs):

        # Create the webdriver that scrapes the website with particular parameters (headless)
        self.__options = webdriver.ChromeOptions()
        # self.options.add_argument("headless")
        self.__driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=self.__options)

        # Handling the parameters to form a correct LinkedIn url (the one of the page that is going to be scrapped)
        job_type.replace(" ", "%20")
        self.__url = "https://linkedin.com/jobs/search?keywords=" + job_type + "&location=" + job_location + \
                     "&trk=guest_job_search_jobs-search-bar_search-submit&redirect=false&position=1&pageNum=0&f"

        # Handle to spreadsheet where we save the data scrapped. Not necessary when using DB
        self.__wb = worksheetHandler.Workbook()

        # Two dimensional array that stores the data scrapped for each job
        self.__jobs_scrapped = []

        # Call the methods that perform the scrapping
        self.__nav()
        self.__scrawl_jobs(number_of_jobs)
        self.__save_jobs(self.__jobs_scrapped)

    """Method that navigates to the LinkedIn url"""
    def __nav(self):
        self.__driver.get(self.__url)

    """Method that scrapes a certain number of jobs in the web page"""
    def __scrawl_jobs(self, number_of_jobs):

        # Display the list of jobs that are going to be scrapped
        self.__display_jobs_list(number_of_jobs)

        # Create a list of jobs of the size number_of_jobs from the LinkedIn page
        jobs = self.__driver.find_element_by_class_name("jobs-search__results-list").find_elements_by_xpath(".//li")
        del jobs[number_of_jobs:]

        # Gets the data from each list of jobs and stores it in the array __jobs_scrapped
        for job in jobs:
            try:
                link = job.find_element_by_xpath(".//a").get_attribute('href')
            except (NoSuchElementException, NoSuchAttributeException):
                link = "Link not found"
            try:
                title = job.find_element_by_xpath(".//span[@class = 'screen-reader-text']").get_attribute("innerHTML")
            except (NoSuchElementException, NoSuchAttributeException):
                title = "Title not found"
            try:
                company = job.find_element_by_xpath(".//h4//a").get_attribute("innerHTML")
            except (NoSuchElementException, NoSuchAttributeException):
                company = "Company not found"
            try:
                location = job.find_element_by_class_name("job-result-card__location").get_attribute("innerHTML")
            except (NoSuchElementException, NoSuchAttributeException):
                location = "Location not found"

            self.__jobs_scrapped.append([title, company, location, link])

        print(len(jobs), "jobs scrapped")

        print(self.__jobs_scrapped)

    """Method that displays the list of jobs necessary to scrap the required number of jobs (presses buttons)"""
    def __display_jobs_list(self, number_of_jobs):
        jobs = self.__driver.find_element_by_class_name("jobs-search__results-list").find_elements_by_xpath(".//li")

        # Click one time more than enough!!!
        while number_of_jobs > len(jobs):
            time.sleep(1)
            if len(jobs) >= number_of_jobs:
                break
            try:
                self.__driver.find_element_by_xpath("//button[contains(text(), 'See more jobs')]").click()
            except (NoSuchElementException, ElementNotInteractableException, ElementClickInterceptedException) as e:
                print("Something went wrong", e)
                continue

            jobs = self.__driver.find_element_by_class_name("jobs-search__results-list").find_elements_by_xpath(".//li")

        print(len(jobs), "jobs loaded")

    """Method that saves the data in the spreadsheet, not needed when using DB"""
    def __save_jobs(self, jobs_array):
        for job in jobs_array:
            self.__wb.write_row(job)
        self.__wb.save()


if __name__ == '__main__':

    bot = LinkedInBot("Software Engineer", "London", 26)
