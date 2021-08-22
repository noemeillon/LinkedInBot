## LinkedIn Bot

### Objective

This bot scraps LinkedIn and report all the interesting jobs on a worksheet. The bot looks for the job ads that match the different parameters passed to the bot instance. This parameters are: job_type for the job title (e.g. Software Engineer), job_location is where the job is based (e.g. London) and number_of_jobs is total number number of jobs to be reported (e.g. 25).

### How to run the program

Make sure you have Python 3 installed.

To run the program:
- Download the project
- Replace the parameters in the runnable part of the project in linkedinBot > linkedinBot.py with the desired parameters. ![Screenshot from 2021-08-22 22-21-49](https://user-images.githubusercontent.com/39555683/130370414-ad5b9ec6-ccf6-48cb-873e-e0b50e8a7da6.png) <br />In this case, the bot looks for 26 Software Engineer opportunities based in London.

- Open a terminal within LinkedInBot > linkedinBot
- Run the command ![Screenshot from 2021-08-22 22-20-05](https://user-images.githubusercontent.com/39555683/130370450-2089ff0d-8444-4fa6-befe-29d4cf650b5d.png) or ![Screenshot from 2021-08-22 22-20-32](https://user-images.githubusercontent.com/39555683/130370457-60106a08-8800-4303-802e-5aede700db65.png) (depending on your default system python version).

### Disclaimer

I built this project in December 2020. Therefore, you might face some issues with dependencies or, if the website has been under some refurbishment, Selenium might struggle to identify the different web elements using their old hardcoded xpath or class name.
