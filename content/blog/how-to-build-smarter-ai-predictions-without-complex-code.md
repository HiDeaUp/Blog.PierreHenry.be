+++
title = "How to Build Smarter AI Predictions Without Complex Code"
slug = "how-to-build-smarter-ai-predictions-without-complex-code"
date = "2025-12-30T11:16:43.815342"
draft = false
description = "Alright, let’s get right into it. Today, I’m going to walk you through a project I’ve been working on that uses generalized linear models—specifically, logistic regression. Most of my experiments h..."
summary = "Alright, let’s get right into it. Today, I’m going to walk you through a project I’ve been working on that uses generalized linear models—specifically, logistic regression. Most of my experiments h..."
tags = ["fastapi", "glm", "logistic regression", "machine learning", "openai", "tech"]
priority = true
priority_topics = ["tech"]
original_title = "This GLM Learning Project Will Change How You Code AI"
source_medium = "https://medium.com/@phenrysay/777e7f1361dc"
+++

{{< figure src="https://images.unsplash.com/photo-1692598578454-570cb62ecf2f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxHTE0lMjBtYWNoaW5lJTIwbGVhcm5pbmclMjBsb2dpc3RpYyUyMHJlZ3Jlc3Npb258ZW58MHwwfHx8MTc2NzA1MzgwMXww&ixlib=rb-4.1.0&q=80&w=1080" alt="A white board with writing written on it" title="How to Build Smarter AI Predictions Without Complex Code" caption="How to Build Smarter AI Predictions Without Complex Code - Photo by [Bernd 📷 Dittrich](https://unsplash.com/@hdbernd) on [Unsplash](https://unsplash.com/photos/a-white-board-with-writing-written-on-it-1xE5QnNXJH0)" >}}

Alright, let’s get right into it. Today, I’m going to walk you through a project I’ve been working on that uses generalized linear models—specifically, logistic regression. Most of my experiments here are in Python, because, let’s be honest, Python just makes this stuff way easier.

The main goal with these projects is to train a model that can estimate outcomes based on the data we have. Basically, we want to make predictions. That’s the heart of it. If you’re building anything with AI, you know that prediction is the name of the game.

### The Project: Logistic Regression with FastAPI

This is a small project, but it packs a punch. What it does is run a logistic regression, and then exposes the prediction functionality through a FastAPI endpoint. Why FastAPI? Because it’s fast (duh), and it lets you call your model in real time. You just hit the API with your data, and boom—you get a prediction back instantly.

Here’s a quick look at how I set it up:

```python
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load("logistic_regression_model.pkl")

class InputData(BaseModel):
    feature1: float
    feature2: float
    # add more features as needed

@app.post("/predict")
def predict(data: InputData):
    features = [[data.feature1, data.feature2]]
    prediction = model.predict(features)
    return {"prediction": int(prediction[0])}
```

With this setup, you can call the `/predict` endpoint with your data, and it’ll return the model’s prediction. Super handy for integrating into any pipeline.

### Real-Time Updates and Integration

One of the best things about this approach is that any new changes in your data can be immediately reflected. You just update your model, and your API is ready to serve the latest predictions. This is crucial if you’re working in environments where things change fast and you need your AI to keep up.

### Adding Summarization with OpenAI

Now, here’s where it gets even more interesting. I’m also using OpenAI for summarization. Why? Because sometimes you don’t just want a raw prediction—you want a summary of what’s going on. Summarization can be super useful for giving quick overviews of your logistic regression results, especially if you’re sharing them with people who aren’t deep into the technical details.

Here’s a quick example of how you might hook that up:

```python
import openai

def summarize_results(results):
    prompt = f"Summarize these logistic regression results: {results}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text.strip()
```

So, after you get your prediction, you can pass the results to OpenAI and get a nice, readable summary. It’s a small touch, but it makes your project way more user-friendly.

### Why This Matters

At the end of the day, what we want is to make our AI projects more accessible and more useful. By combining logistic regression, FastAPI, and OpenAI, you can build something that not only predicts but also explains. That’s a big deal.

As I always say: *“A model that can’t communicate its results is only half as useful.”*

---

## Key Takeaways

- **Logistic regression is a powerful tool for making predictions on your data.**
- **FastAPI makes it easy to serve your model in real time, so you can integrate predictions anywhere.**
- **OpenAI’s summarization helps make your results understandable, even for non-technical folks.**
- *“Prediction is the name of the game in AI. But making those predictions accessible? That’s next level.”*

---
🤔 [Learn more about me on Dev.to](https://dev.to/pierre)
