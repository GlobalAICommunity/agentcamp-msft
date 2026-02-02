# Get started

> [!TIP]
> What is the **AI Toolkit(AITK)**? [The AI Toolkit (AITK)](https://code.visualstudio.com/docs/intelligentapps/overview) is an extension for Visual Studio Code that provides a unified interface to access and interact with various AI models and services. It allows users to easily explore, compare, and utilize different AI models from multiple providers, both proprietary and open source, hosted on several platforms, such as Github, Microsoft Foundry or even locally. With AITK, developers can streamline their Generative AI development workflow by integrating model selection, prompt engineering, and agent prototyping and testing directly within their code editor.

## Open workshop in a GitHub Codespace

In this workshop, we will be using **GitHub Codespaces** to launch a cloud-hosted development environment with all the necessary tools and dependencies pre-installed. This will allow you to focus on learning and prototyping without worrying about local setup.

1. Navigate to the [GitHub repo](https://github.com/GlobalAICommunity/agentcamp-msft) hosting the lab code and resources.

    > [!TIP]
    > Click the Star button in the top right corner, this will help you easily find it later.

2. To launch a codespace, you need a **GitHub account**.

    > [!NOTE]
    > If you already have a GitHub account, you can move to step 3 directly.

    To create one, click on the **Sign up** button and follow the instructions below:
    - In the new window, enter a personal email address, create a password, and choose a username.
    - Select your Country/Region and agree to the terms of service.
    - Click on the **Create account** button and wait for the verification email to arrive in your inbox.

    ![GitHub Account Sign Up](../../img/github_signup.png)

    - Copy the verification code from the email and paste it into the verification field on the GitHub website. Then click on **Continue**.
    - Once the account is created, you'll be redirected back to the GitHub repo page and you'll see a green banner at the top, like the one in the screenshot below.

    ![GitHub Repo Banner](../../img/github_repo_banner.png)

> [!WARNING]
> If your personal GitHub account is a free-tier one, you will have some limitations in the range of GitHub-hosted models you can access in the AI Toolkit Model Catalog.

3. Click on **Sign in** and enter your GitHub credentials to log in. If you just created your account, use the username and password you set during the sign-up process.

3. Once you are signed in, you'll be redirected to the [GitHub repo](https://github.com/skillable-events/ignite25-LAB512-prototyping-multimodal-agents-with-azure-ai-foundry-and-the-ai-toolkit) hosting the lab code and resources.

4. Next, click on the green **Code** button and select **Create codespace on main** from the **Codespaces** tab.

    ![Create Codespace](../../img/create_codespace.png)

> [!WARNING]
> The codespace creation process might take a few minutes, as all the necessary dependencies and tools are being set up in the cloud environment.

5. Once the codespace is created, you'll see a Visual Studio Code environment loaded in your browser.
![Codespace layout](../../img/codespace_layout.png)

6. You might choose to continue working in the browser or click on the **Open in VS Code** button to open it in the desktop application (recommended option).

![Open in VS Code](../../img/open_in_vscode.png)

7. If you choose to open it in the desktop application, you'll be prompted to confirm opening the VS Code Desktop app. Click **Open** to proceed.

> [!NOTE]
> You'll also get a popup *"All done. You can close this tab now."* in the browser, that you can just ignore.

![Confirm opening VS Code App](../../img/confirm_opening_vscode.png)

8. Once VS Code Desktop is opened, you'll be asked to allow access to the codespace. Click **Open** to proceed.

![Open Codespaces in VS Code Desktop](../../img/open_codespaces_vscode.png)

9. Next, you'll be asked to sign in to GitHub from VS Code. By clicking **Allow**, a browser window will open to complete the sign-in process. Click **Continue** to proceed with the GitHub account you used to create the Codespace. And then click on **Authorize Visual Studio Code** to complete the sign-in process.

10. Once the sign-in process is completed, the site will try to redirect you back to VS Code. Click on the **Open** button to proceed.
![Redirect back to VS Code](../../img/redirect_back_to_vscode.png)

11. Back in VS Code, you are now set to start working in the codespace environment. You should see a layout pretty similar to what you had in the browser.

## Login to Azure

In the GitHub Codespace, you should be able to see two Visual Studio Code extensions already installed:

- The **AI Toolkit**: this is the extension we will be using to interact with various AI models and services in this lab.
- The **Microsoft Foundry** extension: it's installed as a bundle of the AI Toolkit and provides access to Microsoft Foundry hosted models.
If they are correctly installed, you should see their icons in the left sidebar of VS Code, as per screenshot below.

![Installed extensions](../../img/installed_extensions.png)

> [!TIP]
> If you don't see the icons, click on the ellipsis (...) at the bottom of the sidebar to see the full list of installed extensions. If you still don't see them, and you are still in the browser-based experience, try refreshing the page or re-opening the codespace in VS Code Desktop app.

Now click on the Microsoft Foundry extension icon, and then click on **Set Default Project** -> **Sign in to Azure**.

![Set Default Project](../../img/set_default_project.png)

You'll be prompted with a popup to confirm with the Azure login. Click **Allow**.

![Azure Login Popup](../../img/azure_login_popup.png)

Next, you'll be redirected to a browser window to complete the login process. Enter the credentials of your Azure subscription, where you provisioned the Microsoft Foundry project for this workshop. 

Back in your codespace or your VS Code instance, you'll be asked to select the Foundry project to use. Select the project you created for this workshop from the dropdown menu.

![Select Project](../../img/select_project.png)