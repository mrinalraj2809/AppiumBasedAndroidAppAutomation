# Automated Playback of Amazon MiniTV Series
### Objective:
The objective of this assignment is to assess the candidate's skills in automating the playback of
a series on Amazon MiniTV using Python, Appium, and pytest. The candidate will be required to
open any series with multiple seasons on Amazon MiniTV and play the first episode of each
season in the series on the Amazon app on mobile.
### Instructions:
1. Set up the environment:
- Installed Python, Appium, and pytest.
- Configured the WebDriver for Appium as part of the setup.
2. Create a new Python file named "amazon_minitv_test.py" and implement the following tasks
using Selenium and pytest:
#### Task 1: Opening Amazon MiniTV
- Able to open Amazon App.
- Navigates to the Amazon MiniTV.
#### Task 2: Finding and Selecting a Series
- On the Amazon MiniTV homepage, locates a series of your choice (e.g., "The Office").
- Clicks on the series to open its details page.
#### Task 3: Playing the First Episode of Each Season
- On the series details page, finds the list of seasons.
- For each season, clicks on the first episode to start playing it.
- Waits for the video to start playing (you can add a delay of a few seconds to ensure the video
starts playing).
- Verifies that the video is playing (e.g., by checking the playback status).
#### Task 4: Assertion and Reporting
- Added assertions to validate that the first episode of each season is playing successfully.
- Generated and attached a report(basic pytest report) indicating the status of each episode's playback (e.g.,
passed or failed).
3. Write test cases using pytest:
- Added test cases for each task mentioned above.
- Ensured that the test cases are independent, isolated, and self-contained.
4. Execute the test cases:
- Run the test cases using pytest.
- Review the test execution results and ensure that all test cases pass.

### Submission Guidelines:
I have attached the Python code file (amazon_minitv_test.py).
If there are any specific instructions or notes for running the code, I’ve included them as well.
Additionally, I’ve provided a brief explanation of my approach along with the challenges I encountered during the assignment.
Note:

The assignment assumes a basic knowledge of Python, Selenium, Appium, and pytest.
I have ensured the code is well-structured, readable, and adheres to best practices.
The code is designed to handle potential exceptions and errors gracefully.
Care was taken to ensure that the automation does not violate any terms or cause harm while interacting with the Amazon MiniTV platform.
