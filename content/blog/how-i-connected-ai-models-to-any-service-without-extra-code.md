+++
title = "How I Connected AI Models to Any Service Without Extra Code"
slug = "how-i-connected-ai-models-to-any-service-without-extra-code"
date = "2025-12-30T17:58:09.663855"
draft = false
description = "Alright, let’s get straight to it. I ended up building an MCP server almost by accident, and honestly, it’s way more useful than I expected. If you’re wondering what an MCP server is, let me break..."
summary = "Alright, let’s get straight to it. I ended up building an MCP server almost by accident, and honestly, it’s way more useful than I expected. If you’re wondering what an MCP server is, let me break..."
tags = ["accidental project", "ai integration", "mcp server", "model context protocol", "nomad", "tasks", "tech", "third-party services"]
priority = true
priority_topics = ["tech", "nomad", "tasks"]
original_title = "I ACCIDENTALLY BUILT AN MCP SERVER!"
source_medium = "https://medium.com/@phenrysay/ff5e69473c10"
+++

{{< figure src="https://images.unsplash.com/photo-1692598578454-570cb62ecf2f?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxNQ1AlMjBzZXJ2ZXIlMjBBSSUyMGludGVncmF0aW9uJTIwTW9kZWwlMjBDb250ZXh0JTIwUHJvdG9jb2x8ZW58MHwwfHx8MTc2NzA3Nzg4OHww&ixlib=rb-4.1.0&q=80&w=1080" alt="A white board with writing written on it" title="How I Connected AI Models to Any Service Without Extra Code" caption="How I Connected AI Models to Any Service Without Extra Code - Photo by [Bernd 📷 Dittrich](https://unsplash.com/@hdbernd) on [Unsplash](https://unsplash.com/photos/a-white-board-with-writing-written-on-it-1xE5QnNXJH0)" >}}

Alright, let’s get straight to it. I ended up building an MCP server almost by accident, and honestly, it’s way more useful than I expected. If you’re wondering what an MCP server is, let me break it down in my own words: it’s basically a bridge between an AI model and another service. That could be a local database, a remote API, or something like Google Analytics. The whole idea is to let your AI model talk to other services, fetch data, push results, or just generally be more useful.

Historically, this was called “function calling.” OpenAI used that term for a while. Now, the mainstream name is Model Context Protocol (MCP), and that comes from Anthropic—the folks behind Claude. They coined MCP, and it’s catching on. If you haven’t checked out the Model Context Protocol yet, I really recommend it. It’s a protocol, but more importantly, it’s a practical way to connect the dots between your AI model and whatever other service you want to hook up.

#### Why MCP Servers Matter

Recently, I saw that Google released a Python MCP server for Google Analytics. Brilliant move. Imagine having a dashboard where you can literally *talk* to your Google Analytics data using an AI model—OpenAI, Claude, Mistral, whatever. You can ask questions, get insights, and automate stuff that used to be a pain.

That got me thinking, so I built my own little MCP server. Here’s what I learned and how I set it up.

#### Anatomy of My MCP Server

With MCP, you need specific endpoints. The protocol is pretty clear about this. It’s kind of like OAuth for authentication, but for connecting models and services. There’s this “well-known” endpoint, which is new-ish. It’s not strictly mandatory, but it’s recommended now. Then you’ve got your model context endpoint, usually something like `/model-context/v1`. That’s where your data schema lives.

In my setup, I’ve got a local data schema. Here’s a quick look at the structure:

```typescript
// server.ts (using Fastify)
import Fastify from 'fastify';
import dotenv from 'dotenv';

dotenv.config();

const fastify = Fastify();
const PORT = process.env.APP_PORT || 3000;

fastify.get('/.well-known/model-context', async (request, reply) => {
  return {
    "@context": "https://schema.org",
    "schemaVersion": "v1",
    // ...your schema here
  };
});

![Photo by GuerrillaBuzz](https://images.unsplash.com/photo-1664526937033-fe2c11f1be25?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwyfHxNQ1AlMjBzZXJ2ZXIlMjBBSSUyMGludGVncmF0aW9uJTIwTW9kZWwlMjBDb250ZXh0JTIwUHJvdG9jb2x8ZW58MHwwfHx8MTc2NzA3Nzg4OHww&ixlib=rb-4.1.0&q=80&w=1080 "How I Connected AI Models to Any Service Without Extra Code")
*How I Connected AI Models to Any Service Without Extra Code - Photo by [GuerrillaBuzz](https://unsplash.com/@guerrillabuzz) on [Unsplash](https://unsplash.com/photos/diagram-7hA2wqBcSF8)*

fastify.get('/model-context/v1/content', async (request, reply) => {
  // Return some data
});

fastify.get('/model-context/v1/model', async (request, reply) => {
  // Prediction, regression, whatever you need
});

fastify.get('/model-context/v1/extra', async (request, reply) => {
  // Third-party service integration
});

fastify.listen({ port: PORT }, (err, address) => {
  if (err) throw err;
  console.log(`Server running at ${address}`);
});
```

You can add more endpoints for specific tasks. For example, if you want to do logistic regression or anything data science-y, just add another route. If you want to keep it simple, that’s fine too.

I split my routes into different files, but you could totally keep everything in one file if you want. My main server file is `server.ts`. I use Fastify, but you could use Express.js or NestJS. I also use an `.env` file to store generic data for the API.

#### Project Structure and Build

Here’s how I set up the build process:

- **TypeScript**: I use `tsc` to compile to JavaScript. My `tsconfig.json` outputs to a `dist` folder.
- **Scripts**: In `package.json`, I’ve got scripts for building, cleaning up (`rimraf`), and running the server in dev mode with `ts-node-dev`. It’s like nodemon but better for TypeScript. Use it in development, not production.
- **Dependencies**: Fastify for the server, dotenv for environment variables, and a few dev dependencies for building and cleaning.

Here’s a snippet from my `package.json`:

```json
{
  "scripts": {
    "build": "tsc",
    "clean": "rimraf dist",
    "dev": "ts-node-dev server.ts",
    "start": "node dist/server.js"
  },
  "dependencies": {
    "fastify": "^4.0.0",
    "dotenv": "^16.0.0"
  },
  "devDependencies": {
    "ts-node-dev": "^2.0.0",
    "typescript": "^5.0.0",
    "rimraf": "^5.0.0"
  }
}
```

#### Publishing and Documentation

I’m putting the whole thing on GitHub, so you’ll have everything you need. The repo will be at [open-data-for-science/mcp-server-api](https://github.com/open-data-for-science/mcp-server-api). The README explains the structure, why I use the “well-known” endpoint, and how to define your public semantic schema with JSON-LD and context. That’s important for interoperability.

I also use a utility file to keep the code clean, and I fixed a little typo in my `.env` (should be `APP_PORT`, not `REAME_TO_PORT`—oops). I use Copilot to generate commit messages, which is a nice little hack.

{{< figure src="https://images.unsplash.com/photo-1762939079730-23708c0dd337?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwzfHxNQ1AlMjBzZXJ2ZXIlMjBBSSUyMGludGVncmF0aW9uJTIwTW9kZWwlMjBDb250ZXh0JTIwUHJvdG9jb2x8ZW58MHwwfHx8MTc2NzA3Nzg4OHww&ixlib=rb-4.1.0&q=80&w=1080" alt="Qc med logo with graphic" title="How I Connected AI Models to Any Service Without Extra Code" caption="How I Connected AI Models to Any Service Without Extra Code - Photo by [marko marko](https://unsplash.com/@marko07) on [Unsplash](https://unsplash.com/photos/qc-med-logo-with-heartbeat-graphic-H_jcoR5kWLA)" >}}

#### Wrapping Up

So yeah, that’s my accidental MCP server. It’s actually pretty simple. At the end of the day, an MCP server is just a protocol—a way to let your AI model and another service talk to each other. If you want to dig deeper, check out the Model Context Protocol docs. There’s a lot to learn, and honestly, it’s a game changer for making AI models more useful in real-world applications.

If you want to look up more, just search for “function calling” or “MCP.” They’re basically the same thing.

> “An MCP server is just a protocol—a way to let your AI model and another service talk to each other.”

Happy AI learning!

---

## Key Takeaways

- **MCP (Model Context Protocol) servers bridge AI models and third-party services**—local or remote, databases or APIs.
- **Endpoints matter:** Follow the protocol for `/well-known` and `/model-context/v1` endpoints.
- **You can use Fastify, Express.js, or NestJS**—whatever you’re comfortable with.
- **Keep your build process clean:** Use TypeScript, `ts-node-dev` for development, and proper environment variables.
- **Check out the Model Context Protocol docs** for more details and best practices.
- **Don’t overthink it:** An MCP server is just a way to connect your model to the outside world.

> “If you want to make your AI model actually useful, let it talk to your data.”

---

🤔 [Learn more about me on Dev.to](https://dev.to/pierre)

---

#### Sometimes, the best tools are the ones you build by accident.
