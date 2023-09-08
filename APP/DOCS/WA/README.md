## 1. Creating Watson Assistant instance

Perform this step if you do not already have a Watson Assisant resource available.

First, go to https://cloud.ibm.com/resources where you need to click the "Create resource" button

<p align="center">
  <img src="0.png" width="600"/>
</p>

Then search in the resource directory for Watson Assistant and then select it

<img src="./1.png" width="80%" alt="prompt" />

Select the instance location that suits you (Dallas by default) (1.). Then pricing the plan that matches your expectations - Lite will be sufficient for this demo. (2.) Accept the license terms. (3.) And finally, click the "Create" button. (4.)

<img src="./2.png" width="80%" alt="prompt" />

## 2. Accessing Watson Assistant instance

Once you have a Watson Assistant instance, it will be available at https://cloud.ibm.com/resources under the AI / Machine Learning category. Click on it to proceed further.

Once in the instance, click on the "Launch Watson Assistant" button to start working with it.

<img src="./3.png" width="80%" alt="prompt" />

## 3. Creating new assistant

Once in the Watson Assistant instance, you need to start by creating a new assistant. You can do this by clicking "Create New+" in the menu at the top, or if you are in a new instance, create your first assistant.

<img src="./4.png" width="80%" alt="prompt" />

Give your assistant a name (1.) and select the assistant's language (2.). In our case, we use Polish, so we chose "Another language".

<img src="./5.png" width="80%" alt="prompt" />

## 4. Working in new assistant

Now that you have created the assistant, go to it and select "Integrations" in the menu on the left

<img src="./6.png" width="80%" alt="prompt" />

Inside "Integrations" look for the Extensions option and select "Build custom extension"

<img src="./7.png" width="80%" alt="prompt" />

Now we need to go to our API that we created earlier and download the json file in which we have the API configuration.

<img src="./8.png" width="80%" alt="prompt" />

In the downloaded json file, change the "url" in the last 4 lines to the link to our API, from which you previously downloaded the json file with the same format as in the screen below

<img src="./9.png" width="80%" alt="prompt" />

<img src="./10.png" width="80%" alt="prompt" />

Now go back to the assistant page where we entered the "Build custom extension" option. We name our "Extension" (1.) and click "Next" (2.).

<img src="./12.png" width="80%" alt="prompt" />

Now in Import OpenAPI, select our json file that we downloaded earlier and load it into the assistant (1.), then click "Next". (2.)

<img src="./13.png" width="80%" alt="prompt" />

After clicking "Next" we are again in "Integrations" where our newly created integration appeared in the "Extensions" section. We select it by clicking "Add +".

<img src="./14.png" width="80%" alt="prompt" />

In the "Get started" section, click "Next".

We choose "Authentication type" as "API key auth" (1.). In the API key field, enter our API key (2.). Click "Next" (3.) and we reach the end. 

<img src="./15.png" width="80%" alt="prompt" />

Now that we have integrations with our API service that supports watsonx, we need to adjust "Actions" to be able to query it.

To do this, go to the "Actions" section (1.), click on "Set by assistant" (2.) and select "No action matches" (3.). We will configure the assistant in such a way that if the assistant does not find another action to match, it will use watsonx. In our case, this will be the only possibility, because we do not plan to add any more actions in this demo.

<img src="./16.png" width="80%" alt="prompt" />

While inside an action, you can delete all existing "Steps" by clicking the trash can icon in the lower right corner of each step.

We create 3 new steps. Let's take the first step (1.) and choose it to be taken without conditions (2.). We add a variable by clicking "New session variable". We call it "query_text" and assign it with "Expression" the value "input.text". (3.).

<img src="./17.png" width="80%" alt="prompt" />

Go to the second step (1.) and select "Use an extension" in "And then" (2.)

<img src="./18.png" width="80%" alt="prompt" />

Now we are in the Extension setup menu, we select our newly created integration in Extension (1.). We select Operation "Retrieval Augumented Generation..." (2.) and in Optional parameters we assign the "question" variable to the "query_text" variable (3.). Now integration to Extension is complete.

<img src="./19.png" width="80%" alt="prompt" />

We go to the last third step (1.) and to the text returned by the assistant "Assistant says" we add the variable (2.) from step 2 of the integration we created - "body.answer" (3.)

<img src="./20.png" width="80%" alt="prompt" />

Finally, inside the third step, select the "And then" option so that the action ends on this step "End the action"

<img src="./21.png" width="80%" alt="prompt" />

Now in the lower right corner we can see how our integration works by clicking "Preview" and writing some query to the assistant.

<img src="./22.png" width="80%" alt="prompt" />

Now if we want to embed the assistant on our website, we can go to the "Preview" section (1.) in the menu on the left and click "Customize web chat" (2.)

<img src="./23.png" width="80%" alt="prompt" />

To add the created assistant to our website, we only need to go to the "Embed" section (1.) and copy the code below (2.). In order for the assistant to appear on the website, we only need to copy the code and insert it at the end of the website's html code.

<img src="./24.png" width="80%" alt="prompt" />






















