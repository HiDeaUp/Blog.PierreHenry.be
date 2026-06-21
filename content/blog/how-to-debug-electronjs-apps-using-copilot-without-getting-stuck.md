+++
title = "How to Debug ElectronJS Apps Using Copilot Without Getting Stuck"
slug = "how-to-debug-electronjs-apps-using-copilot-without-getting-stuck"
date = "2025-12-30T23:47:35.275337"
draft = false
description = "Alright, let’s get into it. I want to walk you through a project I’ve been building—a desktop app using ElectronJS. Not the latest Electron, by the way. I’m on version 25, and I think Electron is u..."
summary = "Alright, let’s get into it. I want to walk you through a project I’ve been building—a desktop app using ElectronJS. Not the latest Electron, by the way. I’m on version 25, and I think Electron is u..."
tags = ["ai tools", "debugging", "electronjs", "github copilot", "money", "productivity", "software engineering", "tech"]
priority = true
priority_topics = ["tech", "money", "productivity"]
original_title = "How to Master GitHub Copilot AI and Become a Better Curious Engineer,Debugging an ElectronJS Desktop"
source_medium = "https://medium.com/@phenrysay/5e307d5d286a"
+++

{{< figure src="https://images.unsplash.com/photo-1711322161199-9258364e0be8?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxHaXRIdWIlMjBDb3BpbG90JTIwRWxlY3Ryb25KUyUyMGRlYnVnZ2luZ3xlbnwwfDB8fHwxNzY3MDk4ODU0fDA&ixlib=rb-4.1.0&q=80&w=1080" alt="A hot air balloon with a piece of luggage inside of it" title="How to Debug ElectronJS Apps Using Copilot Without Getting Stuck" caption="How to Debug ElectronJS Apps Using Copilot Without Getting Stuck - Photo by [Thomas Fore](https://unsplash.com/@tomfromnm) on [Unsplash](https://unsplash.com/photos/a-hot-air-balloon-with-a-piece-of-luggage-inside-of-it-D9OKItZ0BZ8)" >}}

Alright, let’s get into it. I want to walk you through a project I’ve been building—a desktop app using ElectronJS. Not the latest Electron, by the way. I’m on version 25, and I think Electron is up to 31 now, but honestly, that’s not the point. This isn’t about Electron versions. This is about how I use AI, specifically GitHub Copilot and GPT-4.1, to debug and improve my workflow as a software engineer.

So, here’s the deal: I’ve got this open-source YouTube Thumbnail Maker Studio. The idea is to make it super easy to generate thumbnails. But after some recent changes, I hit a snag. The app wouldn’t let me click on anything. Classic. I took a screenshot and started a conversation with Copilot, asking it to dig into the issues. Copilot offered to generate a full HTML patch to restore the controls, and I said, “Sure, go for it.” But then, image selection broke too. So, I asked Copilot to check that out as well.

I’m running Copilot in agent mode because I need more complex help than just code completion. And, by the way, if you’re curious, the project’s on my GitHub. You can poke around if you want.

### Debugging ElectronJS with Copilot and GPT-4.1

Let’s talk about the debugging process. Electron apps are basically browser windows, so you can use the dev tools just like in Chrome. But here’s where things get interesting: Copilot isn’t always the best at debugging, especially compared to GPT-4.1. I’ve found GPT-4.1 (or even Claude, when I have premium requests left) is way better at finding and fixing issues.

But there’s a catch. With my Copilot premium open-source license, I hit request limits. Once you run out, you get bumped back to GPT-4.1, and if you want more, you have to pay for extra requests. So, sometimes you just have to wait for your quota to reset. Annoying, but that’s life.

#### Example: Rolling Back and Isolating Issues

Here’s a practical bit. When Copilot suggests a bunch of changes and things get messy, I just roll back with `git checkout` to erase uncommitted changes. Then I isolate the problem—like the image selection bug—and restart the app to see if it’s fixed.

```bash
git checkout -- .
npm start
```

If the UI looks wrong (like toggles turning into checkboxes), I check the diff. If Copilot removed a ton of code, that’s a red flag. I’ll just revert and try a more focused prompt.

{{< figure src="https://images.unsplash.com/photo-1663422468271-dc79caa4b02f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwyfHxHaXRIdWIlMjBDb3BpbG90JTIwRWxlY3Ryb25KUyUyMGRlYnVnZ2luZ3xlbnwwfDB8fHwxNzY3MDk4ODU0fDA&ixlib=rb-4.1.0&q=80&w=1080" alt="A person using a tool" title="How to Debug ElectronJS Apps Using Copilot Without Getting Stuck" caption="How to Debug ElectronJS Apps Using Copilot Without Getting Stuck - Photo by [Matias Luge](https://unsplash.com/@matiasluge) on [Unsplash](https://unsplash.com/photos/a-person-using-a-tool-vf6xZRgewTQ)" >}}

#### Chasing Down a JS Error

At one point, I hit a JavaScript error: “Cannot read property ‘value’ of undefined.” Classic. I prompt Copilot with the error and the relevant code. But if Copilot can’t help (or if I’m out of premium requests), I’ll just have to dig in manually.

Sometimes, you just have to copy-paste the latest file version into the prompt to make sure Copilot isn’t working off a cached, outdated version. VS Code makes it easy to see diffs and select files, which is super handy.

### The Modern Engineer: More Hats, More Responsibility

Here’s something I’ve noticed: being a software engineer today is a lot like being a pilot. You need to know how to prompt AI, analyze its output, and take responsibility for the final result. You’re not just coding—you’re QA, product owner, automation engineer, and sometimes even DevOps.

I see people at my company using Microsoft Copilot 365 to break down tasks and become better product owners. AI tools are everywhere, and they’re making us wear more hats than ever.

Most of my APIs run in Docker on AWS. Nothing fancy—just keep it simple. I’ve got a Go API on Railway, which is a great hosting platform. Most of my apps are React Native with TypeScript. I’ve used Flutter, but these days I stick with React Native. For data science, I use Python (matplotlib, numpy, pandas, PyTorch) and R (RStudio has a great Copilot integration). At the end of the day, it’s about using the tools you like best, because AI can handle most of the grunt work.

### Copilot Instructions and Custom Models

One feature I love: Copilot’s instructions file. You can generate a `copilot-instructions.md` in your `.github` folder, and Copilot will use it to give better answers tailored to your repo. Highly recommend setting that up.

There’s also the toolset for custom chat models. You can create files for specific debugging tasks or bug finding. And then there’s MCP server—a protocol for interacting with other apps and services. It’s a big step forward for AI integration.

### Debugging Mindset: Don’t Blame the AI

Here’s a mindset tip: if AI doesn’t give you the answer you want, don’t blame the AI. Ask yourself what you could have done differently. Maybe your prompt wasn’t clear enough. If you always blame the tool, you’ll never improve as an engineer. Take responsibility, refine your prompts, and keep iterating.

{{< figure src="https://images.unsplash.com/photo-1723345505144-7c34cb5c64b5?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwzfHxHaXRIdWIlMjBDb3BpbG90JTIwRWxlY3Ryb25KUyUyMGRlYnVnZ2luZ3xlbnwwfDB8fHwxNzY3MDk4ODU0fDA&ixlib=rb-4.1.0&q=80&w=1080" alt="Boeing 747 interior cockpit" title="How to Debug ElectronJS Apps Using Copilot Without Getting Stuck" caption="How to Debug ElectronJS Apps Using Copilot Without Getting Stuck - Photo by [Theo Wilden](https://unsplash.com/@twilden) on [Unsplash](https://unsplash.com/photos/a-close-up-of-a-control-panel-in-a-plane-izwGOc5v_0k)" >}}

### Wrapping Up: Iteration and Progress

Sometimes, after all the debugging and rolling back, you just have to find the last working version and start from there. I do a lot of trial and error—run the app, test image selection, try adding text, tweak the overlay settings. Some features work, some don’t. That’s normal. The important thing is to keep iterating and learning.

I love playing with effects like glow and background boxes. Even if something breaks, I know I’ll get it working eventually. That’s the fun of building with AI and modern tools.

---

## Key Takeaways

- **AI tools like Copilot and GPT-4.1 are powerful, but you need to learn how to prompt them and analyze their output.**
- Don’t be afraid to roll back changes and isolate issues. Use `git checkout` and focused prompts.
- Modern software engineers wear many hats: coder, QA, product owner, automation, and DevOps.
- Use the tools you like best—AI can handle most of the heavy lifting.
- Copilot’s instructions file and custom models can make your workflow smoother.
- *“If AI doesn’t give you the answer you want, don’t blame the AI. Refine your prompt and take responsibility.”*
- Iteration is key. Keep testing, rolling back, and improving your app.

---
#
