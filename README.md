# cloud-actions/python-actions-github

## test locally
```bash
/opt/python/3.8/bin/python -m venv env
source env/bin/activate
pip install fire
pip freeze > requirements.txt
cd 5-github-actions/

python main.py

python main.py hello -h

python main.py hello --message="there!"

python main.py goodbye "now!"

# test with local docker
#docker build -t fire .
#docker run --rm -it fire
```

## create a repo with action
```
git init .
git add .
git commit -m "initial commit"
git remote add origin https://github.com/cloud-actions/python-actions-github
git push -u origin master
```

## use image
1. Open <https://github.com/settings/tokens>
1. Create token with `repo` and `read.packages` scopes:
    ```
    USERNAME='asw101'
    TOKEN='...'
    docker login docker.pkg.github.com -u $USERNAME -p $TOKEN
    ```
1. Run `docker pull` command from: <https://github.com/cloud-actions/python-actions-github/packages>

## Resources
- https://github.com/google/python-fire/blob/master/docs/guide.md
- https://github.com/google/python-fire
- https://help.github.com/en/github/managing-packages-with-github-packages/configuring-docker-for-use-with-github-packages
