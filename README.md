# Django Rest Framework Course

## Overview
This is a comprehensive Django Rest Framework course that takes you from a beginner to an advanced level. You can follow the commits in this repository sequentially to see all the changes made step by step to achieve the full functionality of the RestAPI.

## Project Details
**Project Hosting:** Vercel [here](https://django-rest-framework-gamma.vercel.app/)

**Database:** Initially uses sqlite3 (recommended for beginners), later integrated with MongoDB.

**Credits:** The project is based on the course provided by
 - [CodingEntrepreneurs](https://www.youtube.com/@CodingEntrepreneurs)
 - [BestTutorial07](https://www.youtube.com/@BestTutorial07)

## Django Apps and Features
 - [***restapi***](https://github.com/DataRohit/Django-Rest-Framework-Course/tree/main/backend/restapi)
   - Echo Request Data as JSON

 - [***products***](https://github.com/DataRohit/Django-Rest-Framework-Course/tree/main/backend/products)
   - Return Random Product
   - Product Detail using ID
   - Product Update using ID
   - Product Delete using ID
   - List All Products
   - Create New Product
   - Search Product in DB

 - [***tokenauth***](https://github.com/DataRohit/Django-Rest-Framework-Course/tree/main/backend/tokenauth)
   - Generate Django Auth Token

 - [***task_scheduler***](https://github.com/DataRohit/Django-Rest-Framework-Course/tree/main/backend/task_scheduler)
   - Clear Expired Django Auth Token

 - [***jwtauth***](https://github.com/DataRohit/Django-Rest-Framework-Course/tree/main/backend/jwtauth)
   - Generate Json Web Token
   - Refresh Json Web Token
   - Verify Json Web Token

# Requirements

 - django
 - django-cors-headers
 - djangorestframework
 - djangorestframework-simplejwt
 - djongo==1.3.6
 - pymongo==3.11.3
 - dnspython
 - apscheduler
 - pyyaml
 - requests
 - python-dotenv
 - markdown
 - whitenoise

All the above metioned packages are listed in [requirements.txt](https://github.com/DataRohit/Django-Rest-Framework-Course/blob/main/backend/requirements.txt) file.

# Concepts Covered
 - JSON Response
 - Decorators
 - Validators
 - Serializers
 - Models
 - Views
 - URLs
 - CRUD Operation
 - Generic API Views
 - Token Authentication
 - Custom Expiring Tokens
 - Model Permissions
 - Custom Permissions
 - Mixins
 - JSON Web Token
 - Django CORS
 - Throttling
 - Scheduler
 - MongoDB Integration
 - WhiteNoise Static Hosting
 - Vercel Setup