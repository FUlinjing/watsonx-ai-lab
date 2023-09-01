# Prompt engineering

Complete the following exercises using Prompt Lab from watsonx.ai.

**Ćwiczenia**
<table>
<tr>
<td><a href="#1-classify">1. Classification</a></td>
<td>Classify the intentions of chatbot users</td>
</tr>
<tr>
<td><a href="#2-rewrite">2. Rewrite</a></td>
<td>Convert Markdown to HTML</td>
</tr>
<tr>
<td><a href="#3-study-questions">3. Anticipating questions</a></td>
<td>Anticipate potential customer questions</td>
</tr>
<tr>
<td><a href="#4-text-extraction">4. Entity extraction</a></td>
<td>Extract the names from the sentence</td>
</tr>
<tr>
<td><a href="#5-summarization">5. Summarization</a></td>
<td>Summarize the given text</td>
</tr>
</table>

<p>&nbsp;</p>


## 1. Classification
**Goal** 
<table>
<tr>
<td>
Classify the intentions of chatbot users
</td>
</tr>
</table>
  
**Class examples**<br/>
[Example dataset](https://github.com/spackows/CASCON-2017_Analyzing_chat/blob/master/sample-data/sample-NLC-training-data.csv)

Class: "hi"
```
Hello
Hi there
Good evening
Hi
Hi good morning
```
Class: "question"
```
Hi I wanted to know how to export data from python notebooks?
Hi there can i recover a deleted notebook?
Hi how do you add a folder of files to a project?
Hi team How can you change the name of a Notebook?
How to upload a dataset from local to RStudio
Good morning can you help me upload a shapefile?
How to start creating R notebook?
```
Class: "problem"
```
Hi cant login today with this err The owners accout is not active. This might be caused by expired membership.
I am not able to register my account need your help
Hi I got the message failed to prepare Object-Storage. Would you please give me a suggestion. Thank you.
Hi I am trying to request a new API access key but I dont know what the ID should be for me
When I try to add a model to any project I get an Unauthorized error.
```
**Test input**
```
Hi  Anyone there?
```
```
Having issues setup WML service
```
```
Hi team how can i import data into a project?
```

Check: [Example answer](prompt-engineering-exercise-answers.md#1-classify)

<p>&nbsp;</p>


## 2. Rewrite
**Goal** 
<table>
<tr>
<td>
Convert Markdown to HTML
</td>
</tr>
</table>

**Markdown**
```
## Background
The [IBM Watson Natural Language Processing library](https://dataplatform.cloud.ibm.com/docs/
content/wsj/analyze-data/watson-nlp.html) is a Python library that provides basic natural 
language processing (NLP) such as syntax analysis and keyword extraction with out-of-the-box, 
pre-trained models. The Watson NLP library also makes it simple to customize the language 
models with dictionaries of your domain-specific terms.
```
```
[MURAL](https://mural.co) is an online tool that is like a virtual whiteboard: you can draw 
shapes, stick notes, and move things around. It’s a fabulous tool for visually organizing ideas, 
designing solutions, and collaborating with teammates — in real time or asynchronously.
```
```
## Function
Using LLMs is pretty easy: prompt the model with text (eg. "I took my dog") and the model 
generates text as output (eg. "for a walk").
```
```
## Hall of shame: when LLMs go wrong
Even the creators of LLMs cannot always fully anticipate or explain these models' output: 
[ChatGPT's creators can’t figure out why it won’t talk about Trump](https://www.semafor.com/
article/02/03/2023/how-chatgpt-inadvertently-learned-to-avoid-talking-about-trump)
```

Check: [Example answer](prompt-engineering-exercise-answers.md#2-rewrite)

<p>&nbsp;</p>

## 3. Anticipating questions
**Goal** 
<table>
<tr>
<td>
Anticipate potential customer questions
</td>
</tr>
</table>

**Opisy posczególnych narzędzi**

[Creating notebooks](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/creating-notebooks.html)
```
You can add a notebook to your project by using one of these methods: creating a notebook file, 
copying a sample notebook from the Gallery, or adding a notebook from a catalog. You must have 
the Admin or Editor role in the project to create a notebook.
```
[Using Spark in RStudio](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/rstudio-spark.html)
```
Although the RStudio IDE cannot be started in a Spark with R environment runtime, you can use 
Spark in your R scripts and Shiny apps by accessing Spark kernels programmatically. RStudio uses
the sparklyr package to connect to Spark from R. The sparklyr package includes a dplyr interface
to Spark data frames as well as an R interface to Spark’s distributed machine learning pipelines.
```
[AutoAI overview](https://dataplatform.cloud.ibm.com/docs/content/wsj/analyze-data/autoai-overview.html)
```
The AutoAI graphical tool in Watson Studio analyzes your data and discovers data transformations, 
algorithms, and parameter settings that work best for your predictive modeling problem. AutoAI 
displays the results as model candidate pipelines ranked on a leaderboard for you to choose from.
```

Check: [Example answer](prompt-engineering-exercise-answers.md#3-study-questions)

<p>&nbsp;</p>


## 4. Entity extraction
**Goal** 
<table>
<tr>
<td>
Extract the names from the sentence
</td>
</tr>
</table>

**Examples**
```
As soon as Karolina and Ania met in the park, they rushed
in their arms and started reminiscing about their old school years.
```
```
Marcin and Michał, while working on a joint project, quickly discovered
that they have a lot in common, they share love for animals and fascination with climbing.
```
```
When I looked out the window, I saw that my old friend
Diana returned to her homeland after many years of absence.
```
```
Every time I go to pick up a package in my pajamas,
I hope I won't meet anyone. Unfortunately, this time
Marek, my greatest enemy, stood in my way.
```

Check: [Example answer](prompt-engineering-exercise-answers.md#4-text-extraction)

<p>&nbsp;</p>

## 5. Summarization
**Goal** 
<table>
<tr>
<td>
Summarize the given text
</td>
</tr>
</table>

**Examples**
```
The little bird chirped as she gathered twigs and bits of moss in her beak, flew away and
further between the trees. With each journey, her nest took shape, becoming more cozy and inviting.
She soon created a cozy home where she raised her flock of chirping chicks.
```
```
As soon as the package was opened, the little cat's eyes lit up with excitement. She threw herself
on a new toy, happily tossing it around the room. With a pleased purr, she
she cuddled up to her toy, feeling grateful for the love and attention of the caring owner.
```
```
The ship rolled and rolled in the rough seas as the storm raged. Waves as high as mountains
hit the hull, threatening to capsize the ship. But the captain and crew held out
steady, navigating the treacherous waters with skill and determination, until finally
the storm subsided and the ship emerged triumphant, battered but intact.
```
```
As soon as the two dogs met in the park, their tails began to wag and jump
yourself with joy. Their owners struck up a conversation and it soon turned out that they did
they have a lot in common, uniting their shared love of dogs and the outdoors. To end
On that day, new friendships were formed and both dogs and their owners left the park
happy hearts and wagging tails.
```

Check: [Example answer](prompt-engineering-exercise-answers.md#5-summarization)