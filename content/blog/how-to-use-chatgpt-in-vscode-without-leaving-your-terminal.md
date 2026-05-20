+++
title = "How to Use ChatGPT in VSCode Without Leaving Your Terminal"
slug = "how-to-use-chatgpt-in-vscode-without-leaving-your-terminal"
date = "2025-12-30T08:52:10.309990"
draft = false
description = "Alright, let’s get straight into something I’m genuinely excited about. I’ve been working on my MCP project, and I wanted to take my MCP server up a notch. You know how it goes: you build something..."
summary = "Alright, let’s get straight into something I’m genuinely excited about. I’ve been working on my MCP project, and I wanted to take my MCP server up a notch. You know how it goes: you build something..."
tags = ["ai integration", "chatgpt", "developer tools", "tasks", "tech", "terminal", "vscode"]
priority = true
priority_topics = ["tech", "tasks"]
original_title = "Connect ChatGPT to Your Terminal & VSCode in 5 Minutes!"
source_medium = "https://medium.com/@phenrysay/9263e841174c"
+++

![C plus plus code in an coloured editor square strongly foreshortened](https://images.unsplash.com/photo-1568716353609-12ddc5c67f04?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxDaGF0R1BUJTIwVlNDb2RlJTIwVGVybWluYWx8ZW58MHwwfHx8MTc2NzA0NTEyOXww&ixlib=rb-4.1.0&q=80&w=1080 "How to Use ChatGPT in VSCode Without Leaving Your Terminal")
*How to Use ChatGPT in VSCode Without Leaving Your Terminal - Photo by [Patrick Martin](https://unsplash.com/@patrickmmartin) on [Unsplash](https://unsplash.com/photos/a-close-up-of-a-computer-screen-with-code-on-it-UMlT0bviaek)*

Alright, let’s get straight into something I’m genuinely excited about. I’ve been working on my MCP project, and I wanted to take my MCP server up a notch. You know how it goes: you build something, it works, but then you get that itch—what if I could make it even better?

So, I started playing around with prompts for my MCP server, and then it hit me: “Pierre, you should just install the ChatGPT desktop app.” That’s exactly what I did. The cool thing? You can connect your terminal directly inside the app. Just a click, and boom—your terminal is right there, and you can interact with it or even hook up other applications like Visual Studio Code or whatever else you’ve got open.

## Setting Up: ChatGPT Meets Terminal

Let me walk you through what I did. I fired up my MCP server (after a bit of a wild goose chase finding the right window—classic), and I wasn’t totally happy with it yet. So I asked ChatGPT to help me improve it.

For context, I’m using Fastify for this server. I’ve been a Fastify fan for years—super reliable. I’m also using the usual suspects: `dotenv` for environment variables, `fastify-static` for serving static files (mostly schema files in this case), and `number` to cast the port from the environment variable into a digit, just in case it’s undefined. Then I start the server and set up the root endpoint. Nothing fancy, just the essentials for the MCP server.

Endpoints are standard—again, just what’s needed. For example, I split a string into an array using commas as delimiters. If you’re curious, that’s how I handle tags: each tag is separated by a comma, so `split` does the trick. It’s the classic way to turn a string into an array with a delimiter.

## The Real Magic: ChatGPT + VSCode

Here’s where things get really interesting. Inside the ChatGPT app, I decided to install the Visual Studio Code extension called “ChatGPT: Work with Code.” Now, everyone knows about the regular Copilot extension, but not many folks realize you can get ChatGPT working directly with your code on macOS. That’s the exciting bit.

So, I installed the extension. Now, I can add Visual Studio Code to the ChatGPT app. I had a bunch of unnecessary files open—like `hc.ts` (a health endpoint from another backend API), some scripts, my food tracking app, a Medium post script, and even a data science project. I closed everything except the MCP server to keep things clean.

Now, with just the MCP server open, I told ChatGPT: “Bring the improvements into the MCP server codebase. Test them. Only add relevant changes—no irrelevant stuff. Only the important, accurate improvements.” Sent it off.

![Photo by Growtika](https://images.unsplash.com/photo-1669023414180-4dcf35d943e1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwyfHxDaGF0R1BUJTIwVlNDb2RlJTIwVGVybWluYWx8ZW58MHwwfHx8MTc2NzA0NTEyOXww&ixlib=rb-4.1.0&q=80&w=1080 "How to Use ChatGPT in VSCode Without Leaving Your Terminal")
*How to Use ChatGPT in VSCode Without Leaving Your Terminal - Photo by [Growtika](https://unsplash.com/@growtika) on [Unsplash](https://unsplash.com/photos/a-computer-on-a-desk-FQ3lFA4Zi58)*

Honestly, this was my first time integrating ChatGPT with my codebase like this, and I wanted to do it live. It’s just more fun to discover things together, right?

## Health Endpoints and Real-Time Improvements

ChatGPT started suggesting improvements. For example, it added a health endpoint. If you’ve seen my earlier stuff, you know I had an `hc` endpoint before. These days, a health endpoint is more than just a ping—it gives you real details about your server’s status. Ping is just “hey, the server’s alive,” but health endpoints go deeper.

ChatGPT also generated new files like `types/mcp.ts` and `env.ts` with new variables. It actually read my VSCode project and understood what I had in there. That’s a good sign.

Now, here’s the catch: at first, it couldn’t write changes directly to VSCode. It could read everything, but writing was a no-go. It offered to bundle the changes into a zip file, but the zip came out empty. Classic “zip is invalid” error. I doubted myself for a second, but it was just an empty zip.

So, I asked ChatGPT if it could update the files directly in the VSCode project. And guess what? It can! There’s an “auto update code” feature. I tried it, and it worked. You can review the changes, see the diff, and save them. It’s even better than I expected.

## Everyday Learning: AI as a Coding Partner

Every day, I’m learning new possibilities with this setup. I didn’t know ChatGPT could write code directly into my project like that. If you want, you can just tell it to apply the changes, and it’ll update your codebase right away. It’s honestly amazing—imagination is the only limit here.

I’m a creative person, and today felt like one of those days where everything just clicks. Life is beautiful when your tools work with you, not against you.

Here’s a quick look at what the workflow looks like:

```js
// Example: Adding a health endpoint with Fastify
fastify.get('/health', async (request, reply) => {
  return {
    status: 'ok',
    uptime: process.uptime(),
    timestamp: Date.now()
  };
});
```

![Photo by Chris Stein](https://images.unsplash.com/photo-1701099153587-6f28b448ff0e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwzfHxDaGF0R1BUJTIwVlNDb2RlJTIwVGVybWluYWx8ZW58MHwwfHx8MTc2NzA0NTEyOXww&ixlib=rb-4.1.0&q=80&w=1080 "How to Use ChatGPT in VSCode Without Leaving Your Terminal")
*How to Use ChatGPT in VSCode Without Leaving Your Terminal - Photo by [Chris Stein](https://unsplash.com/@chris_s3tudios) on [Unsplash](https://unsplash.com/photos/a-close-up-of-a-sign-with-numbers-on-it-RntP-d2cxys)*

And for splitting tags:

```js
const tagsString = "ai,fastify,chatgpt";
const tagsArray = tagsString.split(','); // ['ai', 'fastify', 'chatgpt']
```

## Key Takeaways

- **You can connect ChatGPT directly to your terminal and VSCode, making real-time code improvements a breeze.**
- The “ChatGPT: Work with Code” extension for VSCode is a game changer—way more powerful than most people realize.
- Health endpoints are more than just a ping; they give you real insight into your server’s status.
- AI can read and write code in your project, review diffs, and apply changes—all from inside your editor.
- Every day brings new possibilities. Don’t be afraid to experiment and push your workflow further.

> “Imagination is the only limit here.”

> “Life is beautiful when your tools work with you, not against you.”

---
🤔 [Learn more about me on Dev.to](https://dev.to/pierre)  
🤖 Get inspired by [open-source projects I've built](https://github.com/pH-7) over the years  
🔥 Follow my [AI & tech journey on Substack](https://substack.com/@pierrehenry)

---

### Kicker:  
**AI isn’t just for chat—let it write, review, and improve your codebase right inside your favorite tools.**
