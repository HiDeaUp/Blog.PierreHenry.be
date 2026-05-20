+++
title = "How to Handle Markdown Images Without Tedious Formatting"
slug = "how-to-handle-markdown-images-without-tedious-formatting"
date = "2025-12-31T00:17:27.759472"
draft = false
description = "Alright, so today I want to show you a tiny but super handy trick with AI—specifically, how I use Copilot to make my life easier when working with Markdown files. This isn’t some grand, worldchangi..."
summary = "Alright, so today I want to show you a tiny but super handy trick with AI—specifically, how I use Copilot to make my life easier when working with Markdown files. This isn’t some grand, worldchangi..."
tags = ["ai productivity", "copilot tips", "image handling", "markdown automation", "productivity", "tasks", "tech", "wealth", "workflow optimization"]
priority = true
priority_topics = ["tech", "wealth", "tasks", "productivity"]
original_title = "The Smart Way to Use Copilot to Your Advantage"
source_medium = "https://medium.com/@phenrysay/d1ae4a5c3cb3"
+++

![Photo by Jonas Schöne](https://images.unsplash.com/photo-1668204865291-9e01578bfcd0?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxBSSUyMHByb2R1Y3Rpdml0eSUyMENvcGlsb3QlMjB0aXBzJTIwTWFya2Rvd24lMjBhdXRvbWF0aW9ufGVufDB8MHx8fDE3NjcxMDA2NDZ8MA&ixlib=rb-4.1.0&q=80&w=1080 "How to Handle Markdown Images Without Tedious Formatting")
*How to Handle Markdown Images Without Tedious Formatting - Photo by [Jonas Schöne](https://unsplash.com/@schoene) on [Unsplash](https://unsplash.com/photos/a-clock-hangs-from-the-ceiling-dC_VulRVRPM)*

Alright, so today I want to show you a tiny but super handy trick with AI—specifically, how I use Copilot to make my life easier when working with Markdown files. This isn’t some grand, world-changing feature, but it’s one of those little things that saves you time and just makes you feel a bit lazier (in a good way).

Let’s say you’re putting together a README or some documentation. You already know the Markdown syntax, right? But you want to spice things up a bit—maybe make your intro more engaging, maybe even a little clickbaity. And of course, you want a nice image or screenshot to go along with it.

Here’s what I do.

## The Screenshot Workflow

First, I take a screenshot of my application. In this case, it’s my video editing app with auto video effects. I drop that screenshot into my `assets/media` folder. Simple enough.

Now, in my Markdown file, I want to reference that image. So I add something like:

```markdown
![demo video editing app](assets/media/demo-video-editing-app.png)
```

But here’s the thing: sometimes the file name isn’t ideal. Maybe it’s just a jumble of letters or whatever the default screenshot name is. This is where AI comes in.

## Letting Copilot Do the Boring Stuff

![Photo by Enis Yavuz](https://images.unsplash.com/photo-1599474151975-1f978922fa02?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwyfHxBSSUyMHByb2R1Y3Rpdml0eSUyMENvcGlsb3QlMjB0aXBzJTIwTWFya2Rvd24lMjBhdXRvbWF0aW9ufGVufDB8MHx8fDE3NjcxMDA2NDZ8MA&ixlib=rb-4.1.0&q=80&w=1080 "How to Handle Markdown Images Without Tedious Formatting")
*How to Handle Markdown Images Without Tedious Formatting - Photo by [Enis Yavuz](https://unsplash.com/@enisyavuz) on [Unsplash](https://unsplash.com/photos/man-in-gray-shirt-sitting-on-red-plastic-chair-tZtgozUpZZc)*

Instead of sitting there thinking up the perfect file name, I just ask Copilot (or whatever AI you’re using) to suggest a better one. Something descriptive, something that actually makes sense. You can literally prompt it: “Rename this file to something more meaningful.”

Same goes for the alt text and the title attribute for the image. I just tell Copilot, “Give me a good alt text for this image,” or “What should the title attribute be?” And it spits out something like:

```markdown
![Demo video editing app](assets/media/demo-video-editing-app.png "Video editing application interface auto effect tools")
```

That’s it. I don’t have to overthink it. The AI does the heavy lifting, and I just review the suggestions.

## Centering Images in Markdown (Or Not)

Now, if you want to center the image, you might think, “Can I just ask Copilot to do that?” Well, in Markdown, you can’t really center images with pure syntax—there’s no style attribute. If you need it centered, you’ll have to use HTML inside your Markdown:

```html
<p align="center">
  <img src="assets/media/demo-video-editing-app.png" alt="Demo video editing app" title="Video editing application interface auto effect tools">
</p>
```

But honestly, I’m fine with the default. If you want it centered, just ask Copilot to give you the HTML version. Easy.

## Commit and Done

Once I’m happy with how everything looks, I check the README preview to make sure the image path works. If it does, I just commit the change. In Visual Studio Code, I stage the README, generate a commit message (again, Copilot can help here), and commit. That’s it.

![Photo by Arnaud Padallé](https://images.unsplash.com/photo-1708344377729-d3d638081685?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwzfHxBSSUyMHByb2R1Y3Rpdml0eSUyMENvcGlsb3QlMjB0aXBzJTIwTWFya2Rvd24lMjBhdXRvbWF0aW9ufGVufDB8MHx8fDE3NjcxMDA2NDZ8MA&ixlib=rb-4.1.0&q=80&w=1080 "How to Handle Markdown Images Without Tedious Formatting")
*How to Handle Markdown Images Without Tedious Formatting - Photo by [Arnaud Padallé](https://unsplash.com/@arnotho) on [Unsplash](https://unsplash.com/photos/a-black-and-white-photo-of-cars-in-a-parking-lot-PO1Z_h-rWBY)*

## Why Bother?

You might be thinking, “Isn’t this just basic stuff?” Sure, but the point is to let AI handle the repetitive, boring parts so you can focus on the interesting stuff. It’s about being efficient, not lazy. Or maybe a little bit of both.

> “The best programmers aren’t the ones who know the most, but the ones who know how to automate the boring stuff.”  
> — Me, probably

## Key Takeaways

- Use AI like Copilot to automate file naming, alt text, and title attributes for images in Markdown.
- Don’t waste time on repetitive tasks—let the AI handle it and just review the output.
- Markdown can’t center images natively, but you can use HTML if you need to.
- Commit your changes once you’re happy, and move on to more interesting problems.
