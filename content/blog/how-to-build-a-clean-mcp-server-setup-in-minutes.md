+++
title = "How to Build a Clean MCP Server Setup in Minutes"
slug = "how-to-build-a-clean-mcp-server-setup-in-minutes"
date = "2025-12-31T00:02:31.776631"
draft = false
description = "Alright, let’s get straight into it. I want to show you how my MCP server works. This is going to be a quick one, just a couple of minutes, because I’m a bit short on time, but I really wanted to s..."
summary = "Alright, let’s get straight into it. I want to show you how my MCP server works. This is going to be a quick one, just a couple of minutes, because I’m a bit short on time, but I really wanted to s..."
tags = ["behind the scenes", "entrepreneurship", "mcp servers", "server architecture", "server setup", "tech", "technology"]
priority = true
priority_topics = ["tech", "entrepreneurship"]
original_title = "Behind the Scenes of My MCP Servers. This is everything you have wanted to know"
source_medium = "https://medium.com/@phenrysay/dfe9332cca6c"
+++

{{< figure src="https://images.unsplash.com/photo-1628698959977-625e4efabac9?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxNQ1AlMjBzZXJ2ZXJzJTIwc2VydmVyJTIwYXJjaGl0ZWN0dXJlJTIwc2VydmVyJTIwc2V0dXB8ZW58MHwwfHx8MTc2NzA5OTc1MHww&ixlib=rb-4.1.0&q=80&w=1080" alt="White and black" title="How to Build a Clean MCP Server Setup in Minutes" caption="How to Build a Clean MCP Server Setup in Minutes - Photo by [Dylann Hendricks | 딜란](https://unsplash.com/@dylanhendricks) on [Unsplash](https://unsplash.com/photos/white-and-black-concrete-building-WIpORbReaTA)" >}}

Alright, let’s get straight into it. I want to show you how my MCP server works. This is going to be a quick one, just a couple of minutes, because I’m a bit short on time, but I really wanted to share this with you before I head out.

### The Architecture: Keeping It Clean and Simple

So, here’s how I’ve set things up. At the root of my project, I’ve got a `routes` folder. Inside, there’s a single file: `context.route.ts`. I decided to keep all my routes in this one file instead of dumping them into `index.ts` or `server.ts`. It just feels cleaner that way. Trust me, having a dedicated routes file makes things easier to manage, especially as your project grows.

#### What’s Inside the Context Route?

In this context route, I basically display my services. For my MCP server, the sample endpoint just lists out what I do, who I am, and my details. There’s also a new endpoint I added recently. The idea is simple:  
- **Title**: What I do (so if someone wants a specific service, they know where to look)
- **Description**: A quick blurb about me and what I offer
- **Keywords**: Just some tags to help categorize things

Here’s a rough example of what the route might look like:

```typescript
// context.route.ts
import { FastifyInstance } from 'fastify';

export default async function (fastify: FastifyInstance) {
  fastify.get('/context', async (request, reply) => {
    return {
      title: 'MCP Server Services',
      description: 'All the services I offer, who I am, and my details.',
      keywords: ['MCP', 'API', 'services', 'TypeScript']
    };
  });
}
```

{{< figure src="https://images.unsplash.com/photo-1548544027-1a96c4c24c7a?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwyfHxNQ1AlMjBzZXJ2ZXJzJTIwc2VydmVyJTIwYXJjaGl0ZWN0dXJlJTIwc2VydmVyJTIwc2V0dXB8ZW58MHwwfHx8MTc2NzA5OTc1MHww&ixlib=rb-4.1.0&q=80&w=1080" alt="Black steel device" title="How to Build a Clean MCP Server Setup in Minutes" caption="How to Build a Clean MCP Server Setup in Minutes - Photo by [Denny Bú](https://unsplash.com/@dennyisrael) on [Unsplash](https://unsplash.com/photos/black-steel-electronic-device-Jth4utoCVNo)" >}}

### The Server: Fastify, but You’ve Got Options

The main server file, `server.ts`, is super straightforward. I’m using Fastify here, but honestly, you can use Express (which is probably the most popular TypeScript/JavaScript framework out there), or even NestJS. I’ve used Nest before, and it’s great. They all get the job done.

Here’s the basic setup:

```typescript
// server.ts
import Fastify from 'fastify';
import contextRoutes from './routes/context.route';
import dotenv from 'dotenv';

dotenv.config();

const server = Fastify();
const PORT = process.env.PORT || 3000;

server.register(contextRoutes);

server.listen({ port: Number(PORT) }, (err, address) => {
  if (err) {
    console.error(err);
    process.exit(1);
  }
  console.log(`Server running at ${address}`);
});
```

A quick note: I used to hardcode the port number, but that’s not great practice. So now, I’m pulling it from an `.env` file using the `dotenv` package. Make sure your `PORT` variable is in uppercase in your `.env` file, or you’ll run into issues. (Yeah, I made that typo myself. Lesson learned.)

{{< figure src="https://images.unsplash.com/photo-1667264501379-c1537934c7ab?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwzfHxNQ1AlMjBzZXJ2ZXJzJTIwc2VydmVyJTIwYXJjaGl0ZWN0dXJlJTIwc2VydmVyJTIwc2V0dXB8ZW58MHwwfHx8MTc2NzA5OTc1MHww&ixlib=rb-4.1.0&q=80&w=1080" alt="Cables and wires" title="How to Build a Clean MCP Server Setup in Minutes" caption="How to Build a Clean MCP Server Setup in Minutes - Photo by [Kier in Sight Archives](https://unsplash.com/@kierinsightarchives) on [Unsplash](https://unsplash.com/photos/a-close-up-of-a-server-room-3Nwt6w-KU3E)" >}}

### The Rest: Package Scripts and TypeScript Config

The rest of the setup is pretty standard:
- `package.json` to start the app
- A build script to run `tsc` and compile TypeScript to JavaScript
- A start command
- A simple `README`
- `tsconfig.json` because, well, this is a TypeScript app

That’s it. It’s a really simple API, but it’s built specifically for my MCP server. The structure, especially the endpoints and output, is a bit different from a typical RESTful API, but otherwise, it’s pretty close.

## Key Takeaways

- Keep your routes organized in a dedicated file for clarity and scalability.
- Use environment variables for config like port numbers—don’t hardcode them.
- Fastify, Express, NestJS: pick the framework that fits your style. They all work.
- Simplicity wins. Don’t overcomplicate your server setup if you don’t need to.
- “All code is guilty until proven innocent.” (Robert C. Martin)

---
#
