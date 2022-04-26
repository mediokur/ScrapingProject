# (In Process)

### Pre Market Approval Scraping 

This project has a simple start. I have built a web scraper that can take a PMA number and pump it through the FDA's
database and then pull out all of the necessary information for all of the supplements attached to the PMA. This
will then take that data and store it into both an excel and csv doc stored on a static directory. I am going to be
developing this into a web app with its entire goal being to take certain inputs for information from an FDA documents
and automate scraping tasks. I want it to be a simple process eventually such that anybody can quickly gather large
amounts of data. You can look through my code all you want, but keep in mind that I am literally not doing anything 
special. Anyone who spends just a small amount of time working with Selenium and has a basic understanding of conditionals
in Python will be able to accomplish this. I am just using this as a way of understanding how to build webapps using 
Python and Django, and all of the other libraries and modules and jazz I will need. That being said some basic setup
stuff if you want to give my code a try (there is no error management at all this is as bare bones as it gets for the
moment).

### Things You Will Need

Cash Monayyy. I'll take 70k for this open source work. Much grattitudes.
For serious though you will need the following things.
1. Visual Studio with Python or PyCharm (higly recommended but other IDE's will work as well)
2. Selenium
3. Webdriver for the browser you intend to use ( I use chrome because I can afford the ram )
4. Pandas
5. Time
6. Date
7. Openpyxl
8. Wheel (recommended but not always necessary for handling)

After you have an IDE with a python intreper(Conda, Virenv, etc., etc.) you will need to install all of the other items
in your terminal so that the imports work and get your webdriver in a directory that is easy to reach. My explanations are
going to be simple because they assume understanding of browser automation. I will provide links as I think are needed though.
The documentation on Selenium and Webdriver it uses can be found at the following link: <https://www.selenium.dev/documentation/>  

#### Chrome Webdriver
The webdriver is how selenium is actually interacting with your browser to either pull information or perform actions. In my code you will see
that I created a variable that reaches out to pull the executable chrome driver file from my physical drive. To get to that point I performed the following steps:  
1. Found out what chrome version I was currently using (google should be able to help there)
2. I then went to this site and downloaded the driver for the version of chrome I was using: <https://chromedriver.chromium.org/downloads>
3. I placed the .exe file into my program files(x86) directory so I can keep my code short and use an absolute path
4. I created a variable called "PATH" and set it to equal the location of that .exe file on my drive
5. I created another variable called "driver" so that anytime I want to use a webdriver function(which is 99% of this) I just had to call out driver.method() rather
than the entire "webdriver.Chrome("some drive location") everytime I used it. Have an example from my code:  
```
#-----locates the chrome driver executable location and calls it into the driver
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
```
#### Other Packages
Now that we have webdriver located and called into Python, we need to set ourselves up so we can actually use it. We will do that by installing the rest of the
packages mentioned in the list. Packages and libraries, etc. can be installed through tools in many IDE's where you can inspect your environment and then search and
add them as you desire. I used a pip install to bring my packages in. To see if pip is working go into your terminal and type: pip  
If you see an error, then google PIP python issues and start hunting my friend. Otherwise if a bunch of help text pops up in the terminal you're good to go.
Install the following items by typing these phrases as you read them into your terminal  
> Ensure you are in your terminal, command prompt, command line, etc. and not in a python shell. If you are unsure then type the following into the terminal:
> > exit()  

> You will either see an error saying thats not a real command(meaning you were already not in python) or it will seem like nothing happened. That means you exited 
> Python and are now in the regular terminal. Type in the following commands as you see them, and be aware that for each item it may take a minute or two to install 
> them so wait to see a message that starts with "Successfully Installed...etc...etc" before installing the next package:
> > pip install wheel <br>
> > pip install numpy <br>
> > pip install pandas <br>
> > pip install selenium <br>
> > pip install openpyxl <br>

Now that you have installed those, just import them at the top of your python file as shown in the block below and then, idk well continue lol. 
```
import pandas as pd
import numpy as np
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
```

  

