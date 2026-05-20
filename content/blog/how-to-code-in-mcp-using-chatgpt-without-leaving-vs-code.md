+++
title = "How to Code in MCP Using ChatGPT Without Leaving VS Code"
slug = "how-to-code-in-mcp-using-chatgpt-without-leaving-vs-code"
date = "2025-12-30T18:18:05.814035"
draft = false
description = "Alright, I’ve got something extremely exciting for you today. I’m deep into my MCP project, and I decided to shake things up a bit. So, here’s what happened: I created a prompt for my MCP to improv..."
summary = "Alright, I’ve got something extremely exciting for you today. I’m deep into my MCP project, and I decided to shake things up a bit. So, here’s what happened: I created a prompt for my MCP to improv..."
tags = ["chatgpt", "codebase integration", "developer productivity", "entrepreneurship", "mcp", "productivity", "tech", "vs code"]
priority = true
priority_topics = ["tech", "productivity", "entrepreneurship"]
original_title = "Use ChatGPT Connectors with MCP to work on a codebase directly through your ChatGPT discussions"
source_medium = "https://medium.com/@phenrysay/a768416369fc"
+++

![Photo by Markus Winkler](https://images.unsplash.com/photo-1740393068163-b2be0c47b9f8?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxDaGF0R1BUJTIwTUNQJTIwY29kZWJhc2UlMjBpbnRlZ3JhdGlvbnxlbnwwfDB8fHwxNzY3MDc5MDg0fDA&ixlib=rb-4.1.0&q=80&w=1080 "How to Code in MCP Using ChatGPT Without Leaving VS Code")
*How to Code in MCP Using ChatGPT Without Leaving VS Code - Photo by [Markus Winkler](https://unsplash.com/@markuswinkler) on [Unsplash](https://unsplash.com/photos/a-wooden-block-spelling-the-word-chat-on-a-table-ktrS_unoFTI)*

Alright, I’ve got something extremely exciting for you today. I’m deep into my MCP project, and I decided to shake things up a bit. So, here’s what happened: I created a prompt for my MCP to improve my MCP server. My existing MCP server was fine, but I thought, “What about building a more exciting MCP server?” I started playing around with prompts, and then I had a lightbulb moment.

I thought, “Pierre, you should actually install the ChatGPT app.” So I did. That’s the desktop ChatGPT app, and here’s the cool part: you can connect your terminal directly inside it. Just click, and boom, your terminal is connected. What’s really cool is that it can interact with your terminal or with different applications—Visual Studio Code, your code editor, or any other app you’ve got open.

So, from my MCP server (which, by the way, wasn’t even open at first—classic), I said, “Okay, can you improve it? I’m not happy yet with that one. Please improve it.” If you’ve seen my other videos, you know I’m using Fastify for this. I’ve used Fastify for years and I really like it. I’m also using classic libraries like `dotenv` (for environment variables), `fastify-static` (for serving static files, like schema files), and `number` (to cast the port number from the environment variable, just in case it’s undefined).

Here’s a quick look at the basic server setup:

```js
import Fastify from 'fastify';
import dotenv from 'dotenv';
import fastifyStatic from 'fastify-static';

dotenv.config();

const fastify = Fastify();

fastify.register(fastifyStatic, {
  root: path.join(__dirname, 'public'),
});

const port = Number(process.env.PORT) || 3000;

![HTC icon in 3D. My 3D work may be seen in the section titled "3D Render."](https://images.unsplash.com/photo-1681928412599-8e7533ee5ef1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwyfHxDaGF0R1BUJTIwTUNQJTIwY29kZWJhc2UlMjBpbnRlZ3JhdGlvbnxlbnwwfDB8fHwxNzY3MDc5MDg0fDA&ixlib=rb-4.1.0&q=80&w=1080 "How to Code in MCP Using ChatGPT Without Leaving VS Code")
*How to Code in MCP Using ChatGPT Without Leaving VS Code - Photo by [Rubaitul Azad](https://unsplash.com/@rubaitulazad) on [Unsplash](https://unsplash.com/photos/a-computer-keyboard-with-the-word-htc-on-it-UQT2ZpYiOP8)*

fastify.listen(port, (err, address) => {
  if (err) throw err;
  console.log(`Server listening at ${address}`);
});
```

Nothing too fancy—just what’s needed for our MCP server. The endpoints are standard, and for tags, I split the string into an array based on commas. If you’re curious, here’s how that works:

```js
const tags = tagString.split(',');
```

That’s pretty much it for the basics. But here’s where things get really interesting.

### Connecting ChatGPT to Your Codebase

So, I’m looking at my terminal, thinking, “What should I do next?” I decided to install this Visual Studio Code extension called `chatgpt`. Now, everyone knows about the usual Copilot extension, but not many people know about ChatGPT’s “work with code” on macOS. That’s the exciting one.

I installed it—beautiful, now it’s installed. Now you can add Visual Studio Code as a connected app. I had some files I didn’t need, like `hc.ts` (a health endpoint from another backend API), so I cleaned those up. Closed a bunch of tabs—food tracking app, YouTube-to-Medium post script, backend API SaaS, linear model data science project—just to keep things tidy. Now, only the MCP server is open. Much easier.

So, I add VS Code. Beautiful. Now, I want to bring improvements into the MCP server codebase. I want to test them and only add changes that matter. No irrelevant changes—only important, accurate improvements. Perfect. I send the prompt.

This is actually the first time I’m integrating this way, and I wanted to do it live because it’s more fun when we discover things together. Otherwise, I’d already know the outcome, and that’s less fun for you.

### Real-Time Code Improvements with ChatGPT

So, ChatGPT starts reading my codebase. It suggests returning a status for the uptime health endpoint. Speaking of health endpoints, you know I had my `hc` endpoint earlier. Sometimes you’ll see a `/healthz` endpoint or even `/metrics`. Back in the day, it was just `/ping`, but now we want more details about the server’s health. That’s where a health endpoint comes in.

ChatGPT gives me a new `MCPTypes.ts` file. I didn’t have a types folder or file before, so that’s really exciting. It also suggests improvements for `env.ts`—new variables, better context for routes. It actually reads what I have in my VS Code, which is a good sign.

![Hello World!](https://images.unsplash.com/photo-1636586108931-a8b9b8796ba6?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwzfHxDaGF0R1BUJTIwTUNQJTIwY29kZWJhc2UlMjBpbnRlZ3JhdGlvbnxlbnwwfDB8fHwxNzY3MDc5MDg0fDA&ixlib=rb-4.1.0&q=80&w=1080 "How to Code in MCP Using ChatGPT Without Leaving VS Code")
*How to Code in MCP Using ChatGPT Without Leaving VS Code - Photo by [Taiki Ishikawa](https://unsplash.com/@fl__q) on [Unsplash](https://unsplash.com/photos/a-computer-screen-with-a-bunch-of-text-on-it-PUXFKuVf_84)*

Now, I’m not sure if it can write directly to VS Code. I see “inactive” in the status, which is a bit concerning. Let’s see if it does anything. Nope, still inactive. Then it asks if I want to bundle the changes into a zip file. Sure, why not? But when I unzip it, it’s empty. That’s why I got an error—zip is invalid. Normally, it would give an actual zip, but not here.

So, I ask if it can update the files from the VS Code project directly. It starts planning, and then—auto-update code. Yes! It can do this. I close the update, apply it, and… oh, amazing! It’s even better than I thought. You just need to ask for a review, and you get a diff right there. Save changes, and if you want, you can revert. It works for all files.

Every day, I’m learning something new. You can write code with the ChatGPT “work with code” extension. I didn’t know it would be possible, but here we are. If you want, you can directly update the codebase. Just pull, apply the changes, and you’re done.

Everything is possible. We’re updating a project live, and it’s just amazing. Imagination is the only limit here. I’m a creative person, and today feels like the best day of my life. I love it.

That’s it for now, but you can see it works. Those are the new files I have now, and after this, I’ll test everything. I’ll probably make another video about the results. Stay tuned!

---

## Key Takeaways

- You can connect your terminal and Visual Studio Code directly to the ChatGPT desktop app for real-time codebase interaction.
- ChatGPT can read your code, suggest improvements, and even apply changes directly in your project.
- Health endpoints are more than just “ping” now—they provide detailed server status.
- The “work with code” extension for ChatGPT unlocks a whole new workflow for developers.
- “Imagination is the only limit.”  
- “Every day, I’m learning new possibilities.”

---
🔥 Follow my [AI & tech journey on Substack](https://substack.com/@pierrehenry)
