# MySandbox Playlist Backend

## Setup

### Env
1. pip install pipenv
2. pipenv --python python3.6
3. pipenv instlall [--dev]
4. pipenv shell

### Project
5. make dirs - creates project's dirs
6. pipenv run python manage.py migrate (after activating pipenv simply: ./manage.py [command]
7. ./manage.py runserver
8. loading fixtures: pipenv run python manage.py loaddata

### additional static files
9. install bower, e.g. (global installation through nmp): npm install -g bower
10. make fetch_bower_components
11. django-grappelli styles may not show correctly - in such case: ./manage collectstatic

## Project's roadmap
1. Videos
    - [DONE] List, View, Create, Delete
    - [DONE] Search
    - Viewer Permissions:
        - membership, owner, anyone
        
2. Courses / Series
    - owned courses -- one click buy

3. Categories / Tags
    - List, View, Create, Delete
    - Add videos
    - Featured

4. Search -- site wide search

5. Analytics
    - Recommendations based on habits