LinkedIn Job Search and Apply Bot


This project is a LinkedIn Job Search and Apply Bot that automates the process of searching for jobs on LinkedIn and applying to them. The bot utilizes AI to evaluate whether you have a high chance of securing the job before applying. Additionally, if any job application asks questions, the bot will use your YAML-formatted resume to provide relevant answers.

Features
    - Automated Job Search: The bot automatically searches for jobs based on your preferred keywords, location, and other filters.
    - AI-Powered Job Evaluation: The bot uses an AI algorithm to analyze the job description and compare it to your skills and experience, ensuring a higher likelihood of success before applying.
    - Automated Job Application: Once a suitable job is found, the bot automatically fills in application forms with your details (e.g., resume, cover letter).
    - YAML Resume Integration: The bot extracts details from your resume stored in a YAML format and uses this information to respond to job-specific questions during the application process.

How It Works
    - Login: The bot logs into your LinkedIn account using your credentials.
    - Search for Jobs: The bot searches for jobs using specified keywords and location filters.
    - AI Evaluation: The bot assesses each job listing to determine if you have a high probability of securing the position based on the job description and your resume.
    - Application: If the AI evaluates that you are a strong match, the bot automatically applies to the job by filling in the application form.
    - Answering Questions: If the job application asks any specific questions, the bot will refer to your YAML resume to provide appropriate responses.

Getting Started
Prerequisites
Python 3.x
    - Selenium: For automating web interactions with LinkedIn.
    - WebDriver Manager: For automatically managing the appropriate WebDriver version for your browser.
    - AI Model: A simple AI evaluation model (could be a custom machine learning model or an API like OpenAI).
    - YAML Resume: Your resume should be formatted in YAML for the bot to extract information.
    LinkedIn Account: Your LinkedIn credentials (email and password) for login.



    # LinkedIn Job Search Bot

This is a beta version of the LinkedIn Job Search Bot, developed to automate the job search process on LinkedIn. Currently, the bot can log in to LinkedIn and perform job searches for specific job titles.

## Beta Testing
This bot is under beta testing. The functionality is still being refined, and some features (such as error handling and advanced search filters) will be improved in future updates.

## Upcoming Features
- **Graphical User Interface (GUI):** A GUI will be added in future updates to allow for easy interaction and configuration.
- **Job Application Automation:** The bot will be updated to automate job applications directly from the search results.

## How to Use
1. Clone the repository.
2. Install the necessary dependencies.
3. Replace the LinkedIn login credentials with your own.
4. Run the `main.py` script.

## Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome, especially for adding features or improving the bot’s performance!

## License
MIT License
