usage:
	@echo "   .: Options :."
	@echo "   dirs - create project's directories"
	@echo "   fixtures - creates fixtures for all specified apps"
	@echo "   load_all_data - loads all fixtures to the database"
	@echo "   fetch_bower_components - download packages specified in assets/static/bower.json"

dirs:
	@mkdir assets
	@mkdir -p assets/static
	@mkdir backups
	@mkdir local

fixtures:
	@echo " .: Creating fixtures :."
	@echo "* courses_course" 
	@pipenv run python manage.py dumpdata courses -o apps/courses/fixtures/courses.fixture.json --indent 2
	@echo ""
	@echo "* videos_video"
	@pipenv run python manage.py dumpdata videos -o apps/videos/fixtures/videos.fixture.json --indent 2
	@echo ""
	@echo "Fixtures created!"

load_all_data:
	@echo " .: Loading all fixtures :."
	@echo ""
	@echo "* courses:"
	@pipenv run python manage.py loaddata --ignorenonexistent courses.fixture.json
	@echo ""
	@echo "* videos:" 
	@pipenv run python manage.py loaddata --ignorenonexistent videos.fixture.json 

fetch_bower_components:
	@cd assets/static && bower install