# Pixiv GitHub Action
Crawls Pixiv daily rank list pictures and pushes to a GitHub repository every day

Usage:  
1. Create a new branch place the crawled pictures
2. Specify your GitHub username, your GitHub email address, and the branch to place the crawled pictures in ```.github/workflows/pixiv_crawler.yml```.
```yaml
name: "Pixiv Crawler"

on:
  schedule:
    - cron: '0 6 * * *'  
  push:
  
env:
  ACTIONS_ALLOW_UNSECURE_COMMANDS: true

jobs:
  job_1:
    name: Python Crawler
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
      with:
        ref: runner # Change to your branch to place crawled pictures
    - name: Clear Previous
      run: |
        rm -f -- *.jpg
        rm -f -- *.png
    - name: Setup Python environment
      uses: actions/setup-python@v1.1.1 
    - name: Install Dependence
      run: pip install requests
    - name: Run pa.py
      run: python pa.py
    - name: list
      run: ls
    - name: Upload to this repo
      run: |
        git config --global user.name "No5972" # Change to your GitHub user name
        git config --global user.email "wujiuqier@foxmail.com" # Change to your GitHub email address
        git add "*.jpg" "*.png" && echo "Git Added" # Guess if there are any other types of pictures - Ref: https://stackoverflow.com/questions/25083290/git-add-error-unknown-switch
        git commit -m 'upload pa result' && echo "Git Committed"
        git push -u origin runner && echo "Git Pushed Origin" # Change to your branch to place crawled pictures
    - name: Failure test
      if: failure()
      run: | 
        ls
        echo "Error on running!"
```
