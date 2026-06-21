+++
title = "How to Build an Electron Screenshot App in Minutes With Copilot"
slug = "how-to-build-an-electron-screenshot-app-in-minutes-with-copilot"
date = "2026-01-01T18:47:32.161825"
draft = false
description = "Alright, let’s get right into it. For this walkthrough, I started with a completely empty project in Visual Studio Code. I just spun up a new folder from the terminal—called it something like previ..."
summary = "Alright, let’s get right into it. For this walkthrough, I started with a completely empty project in Visual Studio Code. I just spun up a new folder from the terminal—called it something like previ..."
tags = ["desktop app development", "electronjs", "github copilot", "programming tutorial", "tasks", "tech", "vs code"]
priority = true
priority_topics = ["tech", "tasks"]
original_title = "FROM SCRATCH! Build a Desktop App with Electron JS & GitHub Copilot – Full Tutorial"
source_medium = "https://medium.com/@phenrysay/82597c9ecd15"
+++

{{< figure src="https://images.unsplash.com/photo-1591381287254-b3349c60bf9b?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxFbGVjdHJvbkpTJTIwRGVza3RvcCUyMEFwcCUyMERldmVsb3BtZW50JTIwR2l0SHViJTIwQ29waWxvdHxlbnwwfDB8fHwxNzY3MjUzNjUwfDA&ixlib=rb-4.1.0&q=80&w=1080" alt="Black flat screen monitor Rez3 Mv7n_c" title="How to Build an Electron Screenshot App in Minutes With Copilot" caption="How to Build an Electron Screenshot App in Minutes With Copilot - Photo by [Sigmund](https://unsplash.com/@sigmund) on [Unsplash](https://unsplash.com/photos/black-flat-screen-computer-monitor-Rez3-Mv7n_c)" >}}

Alright, let’s get right into it. For this walkthrough, I started with a completely empty project in Visual Studio Code. I just spun up a new folder from the terminal—called it something like `preview-screenshot`—and cracked it open in VS Code. My prompt to Copilot was simple: *Build an Electron preview and screenshot maker for Apple screenshots*. The idea is to automatically generate screenshots for your App Store listing, and now, with agent mode available in VS Code, this is actually doable.

Let me just say, it took a while for agent mode to land in VS Code compared to Cursor or Windsor, but it’s finally here. I picked the latest model at the time (Claude v4, as of June 8), and let Copilot generate the project. You can even pause the process, which is super handy. Cursor doesn’t have that pause feature, and trust me, it’s a pain when you’re coding on the go—like, you’re in a coffee shop, they’re closing, you have to shut your laptop, and with Cursor you’d have to start over and burn more tokens. With VS Code, you just pause and pick up later. Love that.

## Copilot Extension: Pre-release vs Stable

I always use the pre-release version of Copilot. You can switch back to stable if you want, but honestly, I find the pre-release gets patched more often. It’s a bit like Cursor’s canary release—more features, more frequent bug fixes, sometimes a bit buggy, but they patch things fast. So, I’ve made it a habit to stick with pre-release for Copilot too. You get the latest updates, and in my experience, it’s actually more stable.

## Project Structure: What Copilot Generates

So, my project was totally empty, and Copilot spun up all the files for me: `package.json`, `README.md`, a `src` folder, `index.html`, `main.js`—the usual Electron app structure. It didn’t run `npm install` yet, but that’s fine. I’ll ask Copilot to add a `.gitignore` for `node_modules` and other stuff I don’t want in my repo later.

By default, Copilot set up a plain JavaScript ES6 project. I actually prefer TypeScript, but you can always ask Copilot to migrate your project later. For now, keeping it simple with JavaScript is fine, especially for a proof of concept.

Here’s what the initial structure looked like:

```
preview-screenshot/
├── package.json
├── README.md
├── src/
│   ├── app.js
│   ├── index.html
│   └── main.js
```

If you want TypeScript, just be explicit in your prompt. Otherwise, Copilot will default to JS.

## Real Talk: Migrating to TypeScript

Back in 2022, I was at Honeywell, and our whole team spent weeks migrating backend services from JavaScript to TypeScript. Three people, full-time, just for migration. It was a slog. Now, with AI, you can migrate a JS project to TS in no time. It’s wild how much time that saves. If you want to do it, just ask Copilot to convert your files and it’ll handle most of the grunt work.

{{< figure src="https://images.unsplash.com/photo-1604536264507-020ce894daf1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwyfHxFbGVjdHJvbkpTJTIwRGVza3RvcCUyMEFwcCUyMERldmVsb3BtZW50JTIwR2l0SHViJTIwQ29waWxvdHxlbnwwfDB8fHwxNzY3MjUzNjUwfDA&ixlib=rb-4.1.0&q=80&w=1080" alt="monitor showing mobile layout in android studio" title="How to Build an Electron Screenshot App in Minutes With Copilot" caption="How to Build an Electron Screenshot App in Minutes With Copilot - Photo by [Muhammad Rosyid Izzulkhaq](https://unsplash.com/@rsdiz) on [Unsplash](https://unsplash.com/photos/black-flat-screen-computer-monitor-pBTggy2z2do)" >}}

## Watching Copilot Build the App

As Copilot kept generating, it added more files—assets folders, templates, device mockups. It’s like watching an engineer code for you, and you’re just pair programming, keeping an eye on things. The main file, `app.js`, handles saving screenshots, color stuff, all that. My prompt was pretty simple, mostly about screenshot sizes, and Copilot filled in the rest.

**Pro tip:** The more specific your prompt, the better the result. Don’t be afraid to rewrite your prompt, ask questions, and iterate. It’s a back-and-forth game. Treat Copilot like a junior engineer: it doesn’t know what you know, so spell things out.

You can even write your prompt as a BDD story if you want to get super precise. The more details, the better.

## Testing the App: What Worked, What Didn’t

So, I ran the app. The UI was decent—device selection, template options, image upload, text overlays. But there were a few issues:

- Toast messages stacked on top of each other, so you couldn’t read the first one.
- Uploaded images weren’t showing up on the canvas.
- Adding text or shapes didn’t display anything.
- Only the background color worked as expected.

I had to be more specific in my prompts to fix these. For example, I told Copilot: *When I add an image or text, nothing is visible on the canvas. Please review for any canvas flaws.* It’s just like being a product owner—you have to be clear about what you want, or you’ll get features you didn’t ask for and miss the ones you need.

## Iterating and Improving

Every time Copilot generated something, I reviewed it. Sometimes it added redundant code or stuff I didn’t need. Always double-check and clean up after AI. Even if Copilot says it cleaned up, don’t trust it blindly—there’s usually more to do.

But overall, the process is amazing. You can get to a promising MVP fast. It’s not usable yet, but it’s getting there. The goal is always maximum impact for minimum effort. That’s what an MVP is all about.

## Exporting and File Management

The export feature worked nicely. Copilot even created a folder for downloads automatically. The only thing missing was a `.gitignore`, but that’s easy to add.

If you want to migrate to TypeScript, you can rename your files, create a new branch, open a pull request, and review what Copilot did. It’s actually better than what Cursor gave me, and I’m pretty impressed.

{{< figure src="https://images.unsplash.com/flagged/photo-1577437883814-a5c9e5e9a2bb?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwzfHxFbGVjdHJvbkpTJTIwRGVza3RvcCUyMEFwcCUyMERldmVsb3BtZW50JTIwR2l0SHViJTIwQ29waWxvdHxlbnwwfDB8fHwxNzY3MjUzNjUwfDA&ixlib=rb-4.1.0&q=80&w=1080" alt="GridSome cli. Setting up a new project in vscode." title="How to Build an Electron Screenshot App in Minutes With Copilot" caption="How to Build an Electron Screenshot App in Minutes With Copilot - Photo by [hessam khoobkar](https://unsplash.com/@hessam_khoobkar) on [Unsplash](https://unsplash.com/photos/computer-monitor-displaying-words-1K3J4z14V7k)" >}}

## Final Thoughts

You have to be smart in how you interact with AI. Treat it like a smart engineer, but remember, if it does something dumb, it’s probably because your prompt wasn’t specific enough. Always review everything, clean up redundant code, and iterate on your prompts.

The journey is pretty much unlimited—your creativity is the only limit. Happy AI coding!

---

## Key Takeaways

- **Start with a clear, specific prompt.** The more details you give Copilot, the better your results.
- **Use the pre-release version of Copilot** for faster updates and bug fixes.
- **Pause feature in VS Code is a lifesaver** compared to Cursor—great for coding on the go.
- **Always review and clean up AI-generated code.** Don’t trust that it’s perfect out of the box.
- **Iterate on your prompts.** Treat Copilot like a junior engineer: it doesn’t know what you know.
- **Migrating from JS to TS is easy with AI**—just ask Copilot to handle it.
- **Aim for MVP:** Maximum impact, minimum effort.

> “You have to treat AI as your friend, but also as someone who doesn’t know what you know and what you want. The more specific you are, the better the result will be.”

> “Only our creativity is the limitation, our limit in there.”

---
#
