usage:
	@echo "   .: Options :."
	@echo "   dirs - create project's directories"

dirs:
	@mkdir assets
	@mkdir -p assets/static
	@mkdir backups
	@mkdir local

fixtures:
	@echo " .: Creating fixtures :."
	@echo "videos_video"
	@pipenv run python manage.py dumpdata videos -o apps/videos/fixtures/video.fixtures.json
	@echo ""
	@echo "courses_course" 
	@pipenv run python manage.py dumpdata courses -o apps/courses/fixtures/courses.fixtures.json
	@echo ""
	@echo "Fixtures created!"    
