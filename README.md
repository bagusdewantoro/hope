Online shop using Django.

Will be deployed on pythonanywhere.com.
Virtual environment will be located on pythonanywhere : /home/haumea/.virtualenvs


**NOTES:**

**A. Additional Installation:**
1. pip install django-icons
2. pip install pillow
3. pip install django-ckeditor

**B. Git Notes:**
1. Clone to other device: **git clone https://github.com/bagusdewantoro/hope**
2. Always push after modify data in a device: **git push origin master**
3. After modify data in some device and push, to sync in other device: **git pull origin master**
4. If we had modified something in other device and need to sync more updated data from remote : **git fetch origin master**
5. Then **git checkout master** to move master branch (local), then **git merge master origin/master** to merge branch.

**C. Model Mmodification - Local:**
1. python manage.py makemigrations
2. python manage.py sqlmigrate blog

**D. Model Modification - pythonanywhere.com:**
1. cd haumea.pythonanyhwere.com
2. rm db.sqlite3
3. git pull
4. cd ..
5. pa_autoconfigure_django.py https://github.com/bagusdewantoro/mysite.git --python=3.8 --nuke
    (--nuke options to replace the files)
6. python manage.py createsuperuser
7. If we have database backup on our local, through \__FILE__ tab, we can upload to haumea.pythonanyhwere.com directory

**E. Insert Slug on existing models and database:**
https://www.codepolitan.com/cara-membuat-data-migration-dengan-django-5a749614988e4
