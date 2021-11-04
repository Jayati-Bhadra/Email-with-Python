# Email-with-Python
Before you can start using the Nylas Python SDK, make sure you have done the following:

Sign up for your developer account.
Get your developer keys. You need to have your:
CLIENT_ID - The CLIENT ID found on the dashboard page for your Nylas App.
CLIENT_SECRET - The CLIENT SECRET found on the dashboard page for your Nylas App.
ACCESS_TOKEN - The access token provided when you authenticate an account to your Nylas App.
Ensure you have pip installed on your development environment.
Create a virtual environment to install Nylas.
At its core, the Nylas Communication Platform is an API client that interfaces with all of the major email providers. First, import the APIClient class from the nylas package, and create a new instance of this class, passing the variables you gathered when you got your developer API keys. In the following example, replaceCLIENT_ID, CLIENT_SECRET, and ACCESS_TOKEN with your values.
