# rtx3080_scraper

Using web scraping in order to check RTX 3080 stock in NVIDIA webpage among others.

  <img src="https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/ampere/rtx-3080/geforce-rtx-3080-shop-600-p@2x.png" alt="drawing" width="750"/>

## How to use

* Download the required files for your desired OS. 
* Check whether you have already installed the browser used in each option: 
  * **GNU/Linux -> Chromium or Google Chrome**
  * **Windows -> Google Chrome**
  * Alternatively you can use other browsers such as **Firefox**, but check Selenium page for documentation and instructions
    on how to install webdrivers: https://selenium-python.readthedocs.io/
* Download webdriver for selected browser:
  * **chromedriver** compatible with **Google Chrome** 87 is provided in this GitHub project.
* Install **Selenium** package on latest version of **Python** using `pip3 install selenium` (check whether `pip` or `pip3` is used on you environment).
* Enjoy!!!

## Recommended setup

Although you can run the scraper on its own, it is highly recommended that you run it using any kind of task scheduler such as `crontab` in **GNU/Linux**. Please note that if you are using an arm device such as a **Raspberry Pi**, the driver binaries must be compiled for the arm arquitecture. Furthermore, as the goal of this program is to be executed 24/7 it is advised that the program is run on services such as **AWS EC2** or low power devices such as the mentioned **Raspberry Pi**.

## How to set up task scheduler in GNU/Linux

* Use the command `crontab -e` in order to add a new rule to the scheduler.
* Add a new rule such as: 

```
SHELL=/bin/bash

* 8-23,0-3 * * * DISPLAY=:0 /usr/bin/python3 /home/alvar/Documentos/Scraper/linux_scraper_se.py >> /home/alvar/Documentos/Scraper/log.out
```

* `* 8-23,0-3 * * *` represents: “At every minute past every hour from 8 through 23 and every hour from 0 through 3”.
* It is very important that you use absolute paths and avoid using environment variables. If that is not the case the script won´t be executed properly.
* `SHELL=/bin/bash` makes sure that the terminal used is bash.
* `DISPLAY=:0` may be needed in order to initialise the display from crontab and avoid errors when using webdriver,
* For more information on how to set time intervals check this page: https://crontab.guru/

## Redistribution
Feel free to take this code and modify it as you want ;)
