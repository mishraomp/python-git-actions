The source code is available here -> https://github.com/mishraomp/python-git-actions
Please follow the below steps to set up your environment. This repository has 3 environments: `dev`, `test` and `prod`. but you can add more environments.

1. Create a repository in GitHub.
2. Clone the repository, create the branches as per your requirements, (`deploy/dev`, `deploy/test`, `deploy/prod`) in this case.
   1. you can create the branches directly in git or in your IDE.
   2. Development is not done on these branches , these branches are updated through pull requests only.
   3. Since the script is executed on a schedule, this approach of creating branches is necessary to avoid execution of code which is not ready for that environment.
3. Create a directory where your python code resides. This repository uses `app` but you can name the folder based on your needs.
4. if your script depends on 3rd party libraries, then you can use Pipfile approach as used in this repository, otherwise you can use requirements.txt.
5. Setup environments in GitHub.
   1. Go to the settings of the repository(the settings tab is only visible if you have admin permission on the repository), find the environment section, for this repository, it is here https://github.com/mishraomp/python-git-actions/settings/environments
   2. This repository has 3 environments: dev, test and prod. but you can add more environments.
   3. dev environment uses dev branch code, test uses test and prod uses prod.
   4. if there is a need for staging environment, then you can create a new branch and environment in your repo.
   5. Create branch protection rules for these branches so that they are not deleted.
      1. Click on Branches under Code and automation
      2. Enter the branch name pattern, this repository uses `deploy/*` but you can use your own pattern, based on naming of the branches you have made.
      3. Check all the checkboxes mentioned below.
         1. Require a pull request before merging
         2. Require approvals
         3. Include administrators
   6. Create 3 new environment in GitHub (dev,test and prod). you can create more based on your needs
      1. Go to the settings of the repository(the settings tab is only visible if you have admin permission on the repository), find the environment section, and click on `New Environment`, this will create a new environment, and you need to repeat this for the number of environments you need.
      2. Name your environment (`dev` or `test` or `prod`) Set which code branch to use for this environment. for example:- this repository uses `deploy/dev` for `dev` environment, `deploy/test` for `test` environment and `deploy/prod` for prod environment.
      3. Click and select `Selected branches` dropdown under `Deployment branches` and then click on `Add deployment branch rule` , this opens a modal window where you can type the branch name for this environment. This protects different branch from being deployed to the environment, and you will get error similar to this `Branch "main" is not allowed to deploy to dev due to environment protection rules.`
      4. due to limitations on scheduled jobs, minimum threshold is 15 minutes and runs on base/default branch, which is `main` in this repository. From GitHub `You can schedule a workflow to run at specific UTC times using POSIX cron syntax. Scheduled workflows run on the latest commit on the default or base branch. The shortest interval you can run scheduled workflows is once every 15 minutes.`
      5. if your script requires API_KEYS or other secrets, then you can create a secret in GitHub and add it to the environment. Click on `Add secret` under `Environment secrets` that opens up a modal, and then it is a key value pair. GitHub encrypts the secret and stores it in the environment.
6. Create a folder in your repository called `.github/workflows`, this contains all the deployment `.yaml` files which will have execution steps. This repo has 3 different `.yaml`, one for each environment`${env}-schedule.yaml`.
7. The yaml file contains instruction set which will be executed by GitHub during workflow execution. Few key aspects are mentioned below.
      1. The scripts are run on a schedule basis, detailed information available in the link, navigate to the `schedule` section, https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows 
      2. It uses cron to define the schedule and is on _**UTC timezone**_.
         1. This repository also has `workflow_dispatch` which is to manually trigger the workflow for debugging purposes.
      3. The jobs sections has steps to create the environment and execute the script.
         1. runs-on: this defines which Operating System to use.
         2. environment: which pre-configured environment to use (`dev` or `test` or `prod`).
         3. The series of steps are pretty much same for all the environments,except if you need different environment variables. For Example: This repository has different log levels as environment variables.
         4. The way to pass secrets as environment variables is  like `API_KEY: ${{ secrets.API_KEY }}` within the `env:` section. More details can be found here https://docs.github.com/en/actions/security-guides/encrypted-secrets
