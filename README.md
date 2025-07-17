# automate-commit
Generates any number of commit upto 100 to your github account, using an automated shell script combined with python dev tools. 

#### How to run this project

##### 1. Pre-Requisite
Please ensure you have the following:
```yaml
- pipenv
- python3.13
- the-repo ( Where you want your automated commits to go to )
- git
```
Pre-Req:
``` shell 
git clone https://github.com/rahulgauli/automate-commit
```


##### Step I: 
Create a GitHub Fine Grained API Token with all permissions to the "the-repo". Make sure it has sudo to that repo. "Try to keep your token restricted to the repo you want to communicate with".

##### Step II: 
Create a .env file using the sample.env file in the / directory.

##### Step III:
Add the following:

``` shell
github_api_token=dummy_token
github_repo_name=the_repo
```

##### Step IV: 
If you have a windows and want to use powershell, please run the following:

``` shell
.\win_run_me.ps1
```

##### Step V: 
If you have a mac or a linux, please run the following:

``` shell
chmod +x run_me.sh
./run_me.sh
```

# Thank you for doing this :D  Please Add a Star :D 