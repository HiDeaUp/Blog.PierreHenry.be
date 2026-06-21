+++
title = "How to Automate Pull Requests and Save Hours Every Week"
slug = "how-to-automate-pull-requests-and-save-hours-every-week"
date = "2025-12-30T12:16:41.202726"
draft = false
description = "Let’s talk about something that’s saved me a ridiculous amount of time: automating pull requests with tools like Clo Code Actions. If you’re still manually writing out every detail in your PR descr..."
summary = "Let’s talk about something that’s saved me a ridiculous amount of time: automating pull requests with tools like Clo Code Actions. If you’re still manually writing out every detail in your PR descr..."
tags = ["ai tools", "automation", "code review", "developer productivity", "nomad", "productivity", "pull requests", "tech"]
priority = true
priority_topics = ["tech", "nomad", "productivity"]
original_title = "Automate Your PRs, Save Hours #substack #shorts"
source_medium = "https://medium.com/@phenrysay/0bd6b7eba891"
+++

{{< figure src="https://images.unsplash.com/photo-1695426585371-2052b20d260d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxwdWxsJTIwcmVxdWVzdHMlMjBhdXRvbWF0aW9uJTIwQUklMjB0b29sc3xlbnwwfDB8fHwxNzY3MDU3Mzk5fDA&ixlib=rb-4.1.0&q=80&w=1080" alt="waiting to go to work" title="How to Automate Pull Requests and Save Hours Every Week" caption="How to Automate Pull Requests and Save Hours Every Week - Photo by [Townsend Walton](https://unsplash.com/@twalton) on [Unsplash](https://unsplash.com/photos/a-black-and-white-photo-of-a-cordless-drill-b5ThA54YsC8)" >}}

Let’s talk about something that’s saved me a ridiculous amount of time: automating pull requests with tools like Clo Code Actions. If you’re still manually writing out every detail in your PR descriptions, you’re living in the past, my friend. I used to spend hours—literally hours—writing out what changed, why it changed, and all the requirements. I’d even throw in screenshots, especially when working with remote teams. Back then, there was no AI to help, so you had to be super specific, or your teammates would ping you non-stop for context.

Now, with tools like Clo Code Actions, you can generate a pull request straight from your terminal. It’s not just Clo, either. Codeex and a bunch of other tools do the same thing. The point is, you want to automate as much as possible. Not only does it save you time, but these tools often generate better descriptions than if you wrote them yourself. Seriously, the AI is pretty good at summarizing what’s changed and why.

Here’s why this matters: when you’re working remotely or with a distributed team, your PR description is the main way people understand what you’ve done. It’s not just about reviewing your code. Reviewers need to know if your solution actually solves the problem. If your PR is missing context, people have to chase you down for answers, and everything slows to a crawl.

Let me show you how I do it:

{{< figure src="https://images.unsplash.com/photo-1694903110330-cc64b7e1d21d?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwyfHxwdWxsJTIwcmVxdWVzdHMlMjBhdXRvbWF0aW9uJTIwQUklMjB0b29sc3xlbnwwfDB8fHwxNzY3MDU3Mzk5fDA&ixlib=rb-4.1.0&q=80&w=1080" alt="Two hands each other in front of a pink" title="How to Automate Pull Requests and Save Hours Every Week" caption="How to Automate Pull Requests and Save Hours Every Week - Photo by [Igor Omilaev](https://unsplash.com/@omilaev) on [Unsplash](https://unsplash.com/photos/two-hands-touching-each-other-in-front-of-a-pink-background-gVQLAbGVB6Q)" >}}

```bash
# Example: Creating a PR with Clo Code Actions
clo pr create --auto-describe --attach-screenshots
```

That’s it. The tool grabs the relevant changes, generates a solid description, and even attaches screenshots if you want. No more endless typing or copy-pasting Jira tickets.

If you’re not using something like this, you’re wasting time and probably annoying your teammates. Automate your PRs, and you’ll free up hours every week. Plus, your team will thank you for making their lives easier.

> “It’s not just about reviewing the code. No, no, no. It’s about: is your solution the appropriate one?”

## Key Takeaways

- Automate your pull request creation with tools like Clo Code Actions or Codeex.
- AI-generated PR descriptions are often clearer and more complete than manual ones.
- Good PR descriptions help remote teams understand context and reduce back-and-forth.
- Save hours every week and make your workflow smoother by letting automation handle the boring stuff.

{{< figure src="https://images.unsplash.com/photo-1708621810057-b24eed577bfd?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwzfHxwdWxsJTIwcmVxdWVzdHMlMjBhdXRvbWF0aW9uJTIwQUklMjB0b29sc3xlbnwwfDB8fHwxNzY3MDU3NDAwfDA&ixlib=rb-4.1.0&q=80&w=1080" alt="A black and white photo of an engine" title="How to Automate Pull Requests and Save Hours Every Week" caption="How to Automate Pull Requests and Save Hours Every Week - Photo by [Dan Crile](https://unsplash.com/@dancrile) on [Unsplash](https://unsplash.com/photos/a-black-and-white-photo-of-an-engine-MjVwL1aMpEE)" >}}