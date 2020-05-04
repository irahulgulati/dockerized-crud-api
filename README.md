## Production ready Restful API written in Python with help of Flask, SQLALchemy and postgres.
### Built by irahulgulati

# Techologies used
 1. Language   - Python 3.7
 2. Framework  - Flask Framework
 3. ORM	       - SQLAlchemy
 4. Database   - sqlite/postgres
 5. Web Server - Nginx

# Setup
 1. Docker should be installed. (check docker --version)
 2. docker-compose should be installed. (check docker-compose --version)
 3. clone this repository into a folder using git clone.
 4. go inside the folder with docker-compose.yml file.
 5. Run "docker-compose up"
 6. Services should be up on port 80 (localhost or public IP, if installing on server)
 - Note: docker might sometime gives issue with database volume getting persistent, so i suggest to first install and run this application on a fresh system with no  similar docker images running.Otherwise, if you have other docker services running with same name, please change the  services name in docker-compose.yml file accordingly.


# API Endpoints
 1. GET    /api/patients: Gives you all the details of the patients stored in database. Return an empty array if there are no records.
 2. POST   /api/patients: Allows you to post patient details in form of HTTP POST request. Header should contain "content-type:application/json" and it accepts                              (name,location,streetname,status) parameters.
 3. DELETE /api/patients/id: Allows you to delete patient record that matches the id.
 4. PUT    /api/patients/id: Allows you to update patient record that matched the id.
 5. GET    /api/patients/id: Allows you to query single patient record from the database.