# RPI Transfer Course Locator
This script will access Rensselaer Polytechnic Institute's SIS Transfer Course Guide and locate every school that offers a specific transferable course.

### Getting Started
The main.py script requires Python and Selenium. You can install Selenium by running, `pip install selenium`, in your prefered terminal. There is no need to download a driver. This repository comes with one.

Once you have fulfilled the installtion requirements simply change the course_code variable to the course you are looking for. The script can take anywhere from 2-10 mins to look through every school on SIS. All schools that RPI accepted the inputted transferable course from will be outputed.
