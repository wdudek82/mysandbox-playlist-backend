# MySandbox Playlist Backend

## Setup

### Env
1. pip install pipenv
2. pipenv --python python3.6
3. pipenv instlall [--dev]
4. pipenv shell

### Project
5. make dirs - creates project's dirs
6. ./manage.py migrate
7. ./manage.py runserver


## Project's roadmap
1. Videos -> Albums
    - [DONE] List, View, Create, Delete
    - [DONE] Search
    - Viewer Permissions:
        - membership, owner, anyone
        
2. Songs

3. Categories / Tags
    - List, View, Create, Delete
    - Add videos
    - Featured

4. Search -- site wide search

5. Analytics
    - Recommendations based on habits