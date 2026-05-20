+++
title = "How to Build an MCP Server and Boost Data Without the Hassle"
slug = "how-to-build-an-mcp-server-and-boost-data-without-the-hassle"
date = "2026-01-01T17:18:36.781473"
draft = false
description = "Alright, today I want to walk you through the basics of setting up an MCP server architecture. This is something I’ve been tinkering with, and honestly, it’s way simpler than you might think. I’ll..."
summary = "Alright, today I want to walk you through the basics of setting up an MCP server architecture. This is something I’ve been tinkering with, and honestly, it’s way simpler than you might think. I’ll..."
tags = ["data processing", "fastify", "mcp server", "productivity", "server setup", "tech", "typescript"]
priority = true
priority_topics = ["tech", "productivity"]
original_title = "Online or Offline, this is how MCP Servers can BOOST any Data. And You Won't Believe How Easy It Is!"
source_medium = "https://medium.com/@phenrysay/dfc6edad8235"
+++

![HTC icon in 3D. My 3D work may be seen in the section titled "3D Render."](https://images.unsplash.com/photo-1681928412599-8e7533ee5ef1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxNQ1AlMjBzZXJ2ZXIlMjBGYXN0aWZ5JTIwVHlwZVNjcmlwdHxlbnwwfDB8fHwxNzY3MjQ4MzE1fDA&ixlib=rb-4.1.0&q=80&w=1080 "How to Build an MCP Server and Boost Data Without the Hassle")
*How to Build an MCP Server and Boost Data Without the Hassle - Photo by [Rubaitul Azad](https://unsplash.com/@rubaitulazad) on [Unsplash](https://unsplash.com/photos/a-computer-keyboard-with-the-word-htc-on-it-UQT2ZpYiOP8)*

Alright, today I want to walk you through the basics of setting up an MCP server architecture. This is something I’ve been tinkering with, and honestly, it’s way simpler than you might think. I’ll show you my setup, some practical code, and a few tips I picked up along the way. If you’re curious about how MCP servers work, or you want to build your own, you’re in the right place.

## What’s an MCP Server Anyway?

Let’s start with the basics. MCP stands for Model Context Protocol. Think of it as a RESTful API, but with a twist: it’s got a very specific set of endpoints and a unique way of returning data. The whole idea is to act as a bridge between an API model and an application—or even between two different applications. Recently, I saw Google Analytics release their own MCP server in Python (it’s open source on GitHub, by the way), which lets LLMs talk directly to Google Analytics. Super cool.

## My Minimal MCP Server Setup

I built a tiny MCP server to show you the essentials. Here’s how I structured it:

- **ENV file**: I use this for storing config info—nothing secret, just stuff like app version, MCP name, description, tags, contact email, website, base URL, and the port. Here’s a peek at what it looks like:

```env
    APP_VERSION=1.0.0
    MCP_NAME=MyMCPApp
    DESCRIPTION=Minimal MCP server example
    TAGS=ai,api,fastify
    CONTACT_EMAIL=me@example.com
    WEBSITE=https://example.com
    BASE_URL=http://localhost
    PORT=3000
    ```

- **Fastify**: I’m a big fan of Fastify for JavaScript or TypeScript apps. It’s fast, lightweight, and easy to use. Of course, you could use Express or Nest.js if you prefer, but Fastify just feels right for this kind of project.

- **Static Public Folder**: I register `fastify-static` to serve a public folder. This is where I keep the MCP server’s specification file—just a simple JSON that lays out the API’s structure.

- **Entry Point**: My entry point is `server.ts`, but you could call it `index.ts` if you want. The important thing is to set the right entry in your `package.json`:

```json
    "main": "dist/server.js",
    "scripts": {
      "build": "tsc",
      "start": "node dist/server.js",
      "dev": "ts-node-dev --respawn server.ts"
    }
    ```

- **TypeScript Compilation**: I use `tsc` to compile TypeScript to JavaScript. Nothing fancy here.

## Routing and Context

Here’s where things get interesting. The MCP server has a set of context routes. In Fastify, this is just like setting up any other route, but with a focus on returning specific metadata from the ENV file.

![Next.js server script](https://images.unsplash.com/photo-1643116774075-acc00caa9a7b?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwyfHxNQ1AlMjBzZXJ2ZXIlMjBGYXN0aWZ5JTIwVHlwZVNjcmlwdHxlbnwwfDB8fHwxNzY3MjQ4MzE1fDA&ixlib=rb-4.1.0&q=80&w=1080 "How to Build an MCP Server and Boost Data Without the Hassle")
*How to Build an MCP Server and Boost Data Without the Hassle - Photo by [James Wiseman](https://unsplash.com/@jameswiseman) on [Unsplash](https://unsplash.com/photos/a-computer-screen-with-a-program-running-on-it-imgCpfIMoRw)*

```typescript
fastify.get('/.well-known/model-context', async (request, reply) => {
  return {
    name: process.env.MCP_NAME,
    description: process.env.DESCRIPTION,
    tags: process.env.TAGS.split(','),
    contact_email: process.env.CONTACT_EMAIL,
    website: process.env.WEBSITE,
    version: process.env.APP_VERSION
  };
});
```

Notice how I split the `TAGS` string into an array using `.split(',')`. If you ever want to turn it back into a string, just use `.join(',')`. Simple and effective.

## Versioning and Breaking Changes

I like to version my API endpoints. So, for content, I use `/v1/content`. If I ever need to make breaking changes, I’ll bump it to `/v2/content`. This keeps things clean and avoids breaking clients unexpectedly.

## The Well-Known Model Context

This is a newer part of the spec, but it’s super useful. Instead of just `/context`, I use the well-known path: `/.well-known/model-context`. You can read more about this online, but the gist is that it standardizes where clients can find your API’s metadata.

## Serving the Specification

I serve the API spec as a static JSON file from the public folder. This makes it easy for others (or even yourself, six months from now) to see exactly how the API is structured.

## Handling Dependencies and Updates

I ran into a version mismatch with Fastify at one point. The fix? Just install the latest versions:

```bash
npm install fastify@latest
npm install
```

Always good to keep your dependencies up to date. I also commit my `package-lock.json` so everyone gets the exact same versions.

## Citations and Licensing

I generate a citation file for the GitHub repo using AI. It’s just a simple citation in CSL-JSON format, so people know how to cite your work. For the license, I use Markdown for clarity.

## Quick Note on MVP vs MCP

Just to clear up any confusion: MVP is Minimum Viable Product—build something with minimal effort for maximum impact. MCP, on the other hand, is Model Context Protocol (or, as I like to call it, Machine Consumable Protocol). Two very different things!

## Example: Splitting Tags

![A 3D render of the Mastodon logo](https://images.unsplash.com/photo-1698209652952-6ccdcf934f13?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwzfHxNQ1AlMjBzZXJ2ZXIlMjBGYXN0aWZ5JTIwVHlwZVNjcmlwdHxlbnwwfDB8fHwxNzY3MjQ4MzE1fDA&ixlib=rb-4.1.0&q=80&w=1080 "How to Build an MCP Server and Boost Data Without the Hassle")
*How to Build an MCP Server and Boost Data Without the Hassle - Photo by [Chethan](https://unsplash.com/@ch3thanhs) on [Unsplash](https://unsplash.com/photos/a-purple-and-white-letter-q-on-a-black-background-FntA-iLzGxU)*

Here’s a quick example of how I handle tags in the context route:

```typescript
const tags = process.env.TAGS ? process.env.TAGS.split(',') : [];
// To convert back to a string:
const tagsString = tags.join(',');
```

It’s all about keeping things simple and readable.

## Wrapping Up

That’s pretty much it for my minimal MCP server. The code is small, the architecture is straightforward, and you can easily adapt it to your own needs. If you want to check out the repo, it’s at [github.com/open-data-for-science/mcp-server-api](https://github.com/open-data-for-science/mcp-server-api). I’ve added some useful info there to help you build your own MCP server.

If you have questions or suggestions, let me know! I’m always happy to hear feedback and ideas.

---

## Key Takeaways

- **MCP servers are lightweight REST APIs with a specific structure for model-to-app communication.**
- Fastify is a great choice for building MCP servers in JavaScript or TypeScript, but Express or Nest.js work too.
- Use an ENV file for configuration—keep it simple, no secrets.
- Version your endpoints to avoid breaking changes for clients.
- The well-known model context path (`/.well-known/model-context`) is becoming a standard for API metadata.
- Keep dependencies updated and commit your lock files for consistency.
- Splitting and joining tags is as easy as `.split(',')` and `.join(',')`.

> “Minimum effort for maximum impact—that’s the goal of a good MVP. But with MCP, it’s all about making your API machine-consumable and easy to integrate.”

> “If you want to build something useful, start small, keep it clean, and iterate fast.”

---
🤖 Get inspired by [open-source projects I've built](https://github.com/pH-7) over the years

---

### Kicker:  
MCP servers are surprisingly easy to set up—give it a try and see how much data you can boost!
