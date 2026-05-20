+++
title = "How to Use GitHub Copilot Without Breaking Your Codebase"
slug = "how-to-use-github-copilot-without-breaking-your-codebase"
date = "2026-01-01T18:08:40.644132"
draft = false
description = "Alright, let’s get straight into it. Today, I’m diving into how I use GitHub Copilot to build a food tracker app, and more importantly, how I avoid the classic pitfalls that come with relying on AI..."
summary = "Alright, let’s get straight into it. Today, I’m diving into how I use GitHub Copilot to build a food tracker app, and more importantly, how I avoid the classic pitfalls that come with relying on AI..."
tags = ["best practices", "code quality", "github copilot", "productivity", "software engineering", "tech"]
priority = true
priority_topics = ["tech", "productivity"]
original_title = "From Zero to Hero: Successfully Master GitHub Copilot in Your Organization As A Software Engineer"
source_medium = "https://medium.com/@phenrysay/401d418182e3"
+++

![Photo by Nejc Soklič](https://images.unsplash.com/photo-1694716711674-beadd3b2a8af?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxHaXRIdWIlMjBDb3BpbG90JTIwc29mdHdhcmUlMjBlbmdpbmVlcmluZyUyMHByb2R1Y3Rpdml0eXxlbnwwfDB8fHwxNzY3MjUxMzE5fDA&ixlib=rb-4.1.0&q=80&w=1080 "How to Use GitHub Copilot Without Breaking Your Codebase")
*How to Use GitHub Copilot Without Breaking Your Codebase - Photo by [Nejc Soklič](https://unsplash.com/@nejc_soklic) on [Unsplash](https://unsplash.com/photos/a-close-up-of-the-controls-of-a-plane-t0NoPas_2ds)*

Alright, let’s get straight into it. Today, I’m diving into how I use GitHub Copilot to build a food tracker app, and more importantly, how I avoid the classic pitfalls that come with relying on AI for coding. I’ve been a software engineer for over 12 years now—10 of those professionally—and I can honestly say, it’s never been as exciting as it is right now. The tools we have at our disposal are just wild. But with great power comes great responsibility, right? So let’s talk about how to actually use Copilot in a way that helps you, not hurts you.

### Setting Up Copilot: Instructions and Tooling

First off, Copilot has gotten way better. I used to think Cursor and Windsurf were ahead, but now Copilot is right up there. The new versions are solid. One thing I love is the ability to give Copilot instructions. You can load up an `instructions.md` file (it’s just Markdown) and tell Copilot exactly how you want it to behave. Cursor had something similar with its rules file, but Copilot’s approach is a bit more flexible now.

Here’s how it works: Copilot will generate an `instructions.md` file inside your `.github` folder. If you’re used to GitHub, you know this folder is where all your workflows, CI/CD pipelines, and other config files live. Now, Copilot drops its own instructions file in there, so it’s all in one place. Super handy.

### Committing with Copilot

Another neat trick: Copilot can generate commit messages for you. This used to be part of GitHub Labs, but now it’s built right into the Copilot extension. You just click the little star icon, and boom, it spits out a commit message with the right prefix—like `docs:`, `feat:`, `fix:`, or `refactor:`. For documentation updates, it’ll use `docs:`. It’s a small thing, but it keeps your commit history clean and consistent.

### The Real Danger: AI-Generated Bloat

Now, here’s where you need to be careful. Copilot (and honestly, most AI coding tools) has a bad habit of adding extra code you don’t need. I’ve seen it make my app slower and heavier for no good reason. For example, I asked it to reuse a function for formatting meal times in my food label component. Instead of just reusing the function, it tried to import a function that didn’t even exist anymore—`formatMealTimeShort`—and the app crashed. The import was messy, and it was pulling from an outdated cache.

Even worse, Copilot loves to add redundant styles. You’ll see stuff like:

![Photo by Liv Bruce](https://images.unsplash.com/photo-1504233138167-a91c038f5e64?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwyfHxHaXRIdWIlMjBDb3BpbG90JTIwc29mdHdhcmUlMjBlbmdpbmVlcmluZyUyMHByb2R1Y3Rpdml0eXxlbnwwfDB8fHwxNzY3MjUxMzE5fDA&ixlib=rb-4.1.0&q=80&w=1080 "How to Use GitHub Copilot Without Breaking Your Codebase")
*How to Use GitHub Copilot Without Breaking Your Codebase - Photo by [Liv Bruce](https://unsplash.com/@livvie_bruce) on [Unsplash](https://unsplash.com/photos/aerial-photography-of-ocean-tKTxGPswME8)*

```js
const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    width: '100%',
    maxWidth: '100%',
    // ...more unnecessary stuff
  },
  indicatorRow: {
    alignItems: 'flex-start',
    alignItems: 'flex-end', // Redundant!
  },
});
```

Sometimes it’ll tell you to remove a style, and if you do, something breaks. Other times, it’ll insist you need something that’s totally unnecessary. So you really have to stay vigilant.

### How I Audit Copilot’s Suggestions

Here’s my process: I always question Copilot’s output. If I see multiple `alignItems` or `flexEnd` properties, I’ll ask Copilot directly, “Are there any redundant `flexEnd` styles in this component?” You can even use voice input with the right extension, which is pretty cool.

But here’s a pro tip: If Copilot is working off an old version of your component, just copy-paste the latest code into the prompt. That way, it’s working with the freshest version and won’t hallucinate outdated stuff.

I treat Copilot like a junior engineer. I’m the product owner—I know what needs to be built. I communicate super clearly, with all the details, so there’s no misunderstanding. That’s how you get the most out of AI coding tools.

### Staying Lean: Cleaning Up Your App

If you’re building a React Native app (like my food tracker), always keep an eye on your app size. Users will delete your app if it’s too big—trust me, I do it myself. On my phone, I check which apps are taking up the most space and delete the biggest ones first. I don’t want my app to be the first to go.

So, regularly clean up unused images, binaries, and especially unused npm packages. Check your dependencies and devDependencies. If something isn’t used in production, get rid of it. For example, I double-checked that `react-native-safe-area-context` was actually used before keeping it.

You can even prompt Copilot: “Please remove any unused files or imports after refactoring my code.” Make this a habit, and your app will stay lean.

### The Mindset: Never Stop Improving

![Photo by Lukas Souza](https://images.unsplash.com/photo-1575931277869-447d2ea11db1?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwzfHxHaXRIdWIlMjBDb3BpbG90JTIwc29mdHdhcmUlMjBlbmdpbmVlcmluZyUyMHByb2R1Y3Rpdml0eXxlbnwwfDB8fHwxNzY3MjUxMzE5fDA&ixlib=rb-4.1.0&q=80&w=1080 "How to Use GitHub Copilot Without Breaking Your Codebase")
*How to Use GitHub Copilot Without Breaking Your Codebase - Photo by [Lukas Souza](https://unsplash.com/@lukassouza) on [Unsplash](https://unsplash.com/photos/grayscale-photo-of-aircraft-controller-ZMt67IB8nHc)*

AI models are getting better every month, but you have to keep improving too. Learn how to prompt better, give more context, and always look for ways to optimize your workflow. Treat every day as a chance to get a little bit better—not just at coding, but at using your time wisely and staying healthy. Burnout is real, especially with the pace of competition right now. So take breaks, stay balanced, and don’t let the rat race get to you.

---

## Key Takeaways

- **Always review Copilot’s suggestions.** Don’t trust AI-generated code blindly—double-check for redundant or outdated code.
- **Use instruction files to guide Copilot.** Be explicit about your coding standards and requirements.
- **Keep your app size small.** Regularly clean up unused files and dependencies to avoid being the first app users delete.
- **Treat Copilot like a junior engineer.** Communicate clearly, provide context, and question its output.
- **Continuously improve your prompting skills.** The better your prompts, the better Copilot’s output.
- **Balance productivity with self-care.** Don’t let the drive to do more lead to burnout.

> “You have to question your AI model with this kind of prompt—always asking it to re-evaluate itself and see yourself as a product owner.”  
> “Every day is a new opportunity to improve. Every day you have the chance to be better, to be more proactive.”

---
🤔 [Learn more about me on Dev.to](https://dev.to/pierre)

---

**Kicker:**  
Mastering Copilot is about staying sharp, questioning everything, and never letting AI make you lazy.
