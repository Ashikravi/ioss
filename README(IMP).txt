
Quick Start Options
Choose either Docker (recommended/incase any errors occurs in docker image use ==> )  manual setup below.

Option 1: Docker Setup (Recommended)
Prerequisites
* Docker Desktop installed and running
Building and Running Your Application
When you're ready, start your application by running:
docker compose up --build
The development server will start at http://0.0.0.0:8000/ inside the container.
Your application will be available at http://localhost: #important
Docker Commands
* Start the application: docker compose up --build
* Stop the application: docker compose down
* View logs: docker compose logs



###########################################################

Option 2: Without Docker (If Docker Doesn't Work). 
Prerequisites
* Python 3.8+
* pip
Setup Instructions
1. Clone the repositorygit clone <your-repo-url>
2. cd <project-name>
3. 
4. Create a virtual environmentpython -m venv myenv
5. 
6. Activate the virtual environment# On macOS/Linux:
7. source myenv/bin/activate

8. # On Windows:
9. myenv\Scripts\activate
10. 
11. Install requirementspip install -r requirements.txt
12. 
13. Run database migrationspython manage.py migrate
14. 
15. Start the development serverpython manage.py runserver
16. 
17. Open your browserNavigate to http://127.0.0.1:8000
Deactivating Virtual Environment
When you're done, deactivate the virtual environment:
deactivate