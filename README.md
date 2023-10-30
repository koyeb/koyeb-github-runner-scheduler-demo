## Koyeb GitHub Actions scheduler demo

This repository houses a simple application used to demonstrate how to deploy the [Koyeb GitHub Actions runner scheduler](https://github.com/koyeb/koyeb-github-runner-scheduler) on Koyeb.

You can read the [associated tutorial](https://www.koyeb.com/tutorials/) for more information about how to use this application.

## Using this repository

To use this repository, clone it into your own account.  [Generate a GitHub personal access token](https://github.com/settings/personal-access-tokens/new) with access to your cloned repository and "Administration" permissions set to "Read and write".

In the [Koyeb control panel](https://app.koyeb.com/), create a new [Koyeb personal access token](https://app.koyeb.com/user/settings/api) for the integration.

Next, click the "Deploy to Koyeb" button to configure the Scheduler deployment:

[![Deploy to Koyeb](https://www.koyeb.com/static/images/deploy/button.svg)](https://app.koyeb.com/deploy?name=github-runner-scheduler&type=docker&image=docker.io/koyeb/github-runner-scheduler&env[GITHUB_TOKEN]=CHANGE_ME&env[KOYEB_TOKEN]=CHANGE_ME&env[API_SECRET]=CHANGE_ME&env[MODE]=repository&env[DISABLE_DOCKER_DAEMON]=true&ports=8000;http;/)

Set the values for the following environment variables:

* `GITHUB_TOKEN`: The personal access token you generated on GitHub.
* `KOYEB_TOKEN`: The personal access token you generated on Koyeb.
* `API_SECRET`: A random secret used to authenticate requests with GitHub webhooks.  You can generate a good secret with `openssl rand -base64 30`.  You'll need this same value later to configure the webhook on GitHub.

Click "Deploy" when you are finished.  Copy the "Public URL" for the scheduler when it starts to deploy.

In your clone of this repository, click the repository settings and select "Webhooks".  Click "Add webhook" and set the following values:

* Payload URL: The public URL you copied from the Koyeb scheduler deployment.
* Content type: `application/json`.
* Secret: The same value you set for `API_SECRET` in the Koyeb scheduler deployment.
* Which events would you like to trigger this webhook? **Let me select individual events.**
    * **De-select** the **Pushes** item.
    * **Select** the **Workflow jobs** item.

Click "Add webhook".

Now, when a new change is detected in the repository, GitHub will dispatch the job to your Koyeb Scheduler vis webhooks.  The scheduler will provision Koyeb GitHub runners as required by the Actions labels.  The job will be processed and the results will be reported back to GitHub.

After two hours of inactivity, the GitHub runners will be deleted automatically.
