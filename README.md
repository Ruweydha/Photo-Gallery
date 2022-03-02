# Photo-Gallery
#### By Ruweydha Abdinoor.
## Description
A website where a user can be able to view pitches images on the homepage. They can also search images based on their category and view them based on the location. They can also shar the links of the photos they like with friends.
## Setup and Installation
***
## Installation

* Open Terminal `ctrl+Alt+T`

* Git clone https://github.com/Ruweydha/Photo-Gallery

or

* Git fork - Enter into your own repository and search-https://github.com/Ruweydha/Photo-Gallery then click on fork to add
it on your own repository.

 Navigate into the cloned project. 
`cd albumarena`


* Create and activate the vitual Environment and install the from requirements.txt
`$ python3.6 -m virtualenv virtual`
`$ source virtual/bin/activate`
`$ pip install -r requirements.txt`

* Setting up environment variables

Create an `.env` and add the following.
```
SECRET_KEY='<Secret_key>'
DBNAME='tribune'
USER='<Username>'
PASSWORD='<password>'
DEBUG=True

EMAIL_USE_TLS=True
EMAIL_HOST='smtp.gmail.com'
EMAIL_PORT=587
EMAIL_HOST_USER='<your-email>'
EMAIL_HOST_PASSWORD='<your-password>'

```

requirements from 
---
`requirements.txt`


* Start the Server to run the app
* `$ python3 manage.py runserver`

* Open [localhost:8000](#)
***


## Requirements
* Either a computer,phone,tablet or an Ipad
* An access to the Internet

## Known Bugs
None at the moment.
## Technologies Used
* Django
* HTML
* Bootstrap

    
## Support and contact details
LinkedIn - [Ruweydha Abdinoor](https://www.linkedin.com/in/ruweydha-abdinoor-859921224/) 
### License
MIT License
​
Copyright (c) [2022] [Ruweydha Abdinoor]
​
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
​
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
​
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.