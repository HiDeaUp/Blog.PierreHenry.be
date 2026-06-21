+++
title = "How I Build Apps Faster With Cursor AI Instead of VS Code"
slug = "how-i-build-apps-faster-with-cursor-ai-instead-of-vs-code"
date = "2025-12-31T00:32:33.309326"
draft = false
description = "Let me walk you through something I genuinely enjoy about working with Cursor: it just gets out of my way and does things for me. For example, when I’m building an app, Cursor will automatically tr..."
summary = "Let me walk you through something I genuinely enjoy about working with Cursor: it just gets out of my way and does things for me. For example, when I’m building an app, Cursor will automatically tr..."
tags = ["ai tools", "app development", "cursor ai", "developer workflow", "entrepreneurship", "productivity", "tasks", "tech", "vs code alternative"]
priority = true
priority_topics = ["tech", "tasks", "productivity", "entrepreneurship"]
original_title = "Building an app with Cursor: Reasons I use Cursor AI over VS Code"
source_medium = "https://medium.com/@phenrysay/03292da11e25"
+++

{{< figure src="https://images.unsplash.com/photo-1642132652935-d750e2014719?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxDdXJzb3IlMjBBSSUyMGFwcCUyMGRldmVsb3BtZW50JTIwVlMlMjBDb2RlJTIwYWx0ZXJuYXRpdmV8ZW58MHwwfHx8MTc2NzEwMTU1MXww&ixlib=rb-4.1.0&q=80&w=1080" alt="A screen with a web page on it LWFdfx 5oEE" title="How I Build Apps Faster With Cursor AI Instead of VS Code" caption="How I Build Apps Faster With Cursor AI Instead of VS Code - Photo by [Team Nocoloco](https://unsplash.com/@teamnocoloco) on [Unsplash](https://unsplash.com/photos/a-computer-screen-with-a-web-page-on-it-LWFdfx-5oEE)" >}}

Let me walk you through something I genuinely enjoy about working with Cursor: it just gets out of my way and does things for me. For example, when I’m building an app, Cursor will automatically try to execute the right program. So, if I’m working on an iOS app, it’ll run `npm run ios` and fire up the emulator without me having to fiddle around. Same deal for Android. That’s a feature I really appreciate, because honestly, I don’t want to spend time on boilerplate stuff like launching emulators.

I’ve used Copilot and other AI assistants in JetBrains IDEs, and they just don’t offer this kind of automation. Cursor goes way beyond what you get from the usual AI copilot plugins or IDE tools. It’s not just about code suggestions—it’s about actually running your project and managing the workflow.

### Debugging and Project Structure Fixes

Now, not everything is always smooth. Sometimes you’ll open your app and the screen is just blank. That happened to me—the simulator was running, but nothing was showing up. Turns out, my `src` folder was empty. So, I switched to edit mode, moved the `src` folder to the right place, and that sorted it out. Cursor made it easy to spot and fix the issue.

Here’s a quick example of what I did:
```bash
# Move the src folder to the correct location
mv src/ correct/path/
```
After that, I just ran everything again:
```bash
npm expo start
```
and waited for the iOS emulator to spin up. This time, the app loaded as expected. There was a little hiccup with duplicate `App.tsx` files, but once I cleaned that up, everything worked.

### Building Features and UI

I wanted the app to show sleep statistics—like, if I slept from 6 to 9, it should tell me how much sleep I got, and display stats for today as well as the whole week (Monday to Sunday). Turns out, Cursor’s AI was smart enough to already have some of that logic in place. Sometimes I doubt it, but then I check and, yeah, it’s already there. That’s pretty cool.

{{< figure src="https://images.unsplash.com/photo-1554306274-f23873d9a26c?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwyfHxDdXJzb3IlMjBBSSUyMGFwcCUyMGRldmVsb3BtZW50JTIwVlMlMjBDb2RlJTIwYWx0ZXJuYXRpdmV8ZW58MHwwfHx8MTc2NzEwMTU1MXww&ixlib=rb-4.1.0&q=80&w=1080" alt="Turned on macbook pro" title="How I Build Apps Faster With Cursor AI Instead of VS Code" caption="How I Build Apps Faster With Cursor AI Instead of VS Code - Photo by [Safar Safarov](https://unsplash.com/@safarslife) on [Unsplash](https://unsplash.com/photos/turned-on-macbook-pro-LKsHwgzyk7c)" >}}

I also started thinking about adding a widget to display today’s stats on the home screen. I’m not sure if that’s possible on Android, but it’s something I want to explore further.

### Publishing to the App Store

When it came time to publish, Cursor really shined. I had a bunch of tabs open, juggling different tasks, but Cursor helped me keep track. For example, it automatically generated scripts to build and deploy the app to the App Store, using my team ID. It even created a `build-deployer` script for me.

Here’s what that looked like:
```bash
# Script to build and deploy
npm install
npm run build-deployer
```
If something didn’t work—like a missing package version—I could just copy the error into Cursor’s chat and ask for help. That’s super handy. If you hit a wall, you can always run `expo build` manually, but having the AI there to troubleshoot is a big time-saver.

### Git Integration and Commit Messages

Another thing I love: Cursor can generate commit messages based on what’s staged. If I’m not sure what to write, I just let it suggest something. Here’s my usual flow:
```bash
git add .
# Let Cursor suggest a commit message
git commit -m "AI-generated commit message"
```
Then I push to a new private repo on GitHub. Cursor even finds errors by itself and suggests fixes. It’s one of the best features, honestly. It does make a lot of requests to the AI model, but it’s so efficient that I don’t mind.

### Handling Permissions and Final Steps

Sometimes you’ll hit permission issues when deploying. If that happens, just type your password when prompted, and you’re good. Cursor will walk you through the rest—submitting to the App Store, testing, and even updating your README with deployment instructions.

**It’s really exciting to see how much Cursor automates. It’s not just an AI code assistant—it’s like having a junior developer who handles the boring stuff and lets you focus on building.**

---

{{< figure src="https://images.unsplash.com/photo-1604536264507-020ce894daf1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwzfHxDdXJzb3IlMjBBSSUyMGFwcCUyMGRldmVsb3BtZW50JTIwVlMlMjBDb2RlJTIwYWx0ZXJuYXRpdmV8ZW58MHwwfHx8MTc2NzEwMTU1MXww&ixlib=rb-4.1.0&q=80&w=1080" alt="monitor showing mobile layout in android studio" title="How I Build Apps Faster With Cursor AI Instead of VS Code" caption="How I Build Apps Faster With Cursor AI Instead of VS Code - Photo by [Muhammad Rosyid Izzulkhaq](https://unsplash.com/@rsdiz) on [Unsplash](https://unsplash.com/photos/black-flat-screen-computer-monitor-pBTggy2z2do)" >}}

## Key Takeaways

- Cursor automates project setup, emulator launching, and even deployment scripts, saving tons of time.
- The AI assistant is more proactive than Copilot or JetBrains plugins, handling workflow tasks, not just code suggestions.
- Debugging is easier—just ask Cursor about errors, and it’ll help you fix them or generate scripts.
- Git integration is smooth, with AI-generated commit messages and error detection.
- Cursor’s automation lets you focus on building features, not fighting with your tools.

> “Cursor is like having a junior developer who handles the boring stuff and lets you focus on building.”

> “Sometimes I doubt the AI, but then I check and, yeah, it’s already there. That’s pretty cool.”
