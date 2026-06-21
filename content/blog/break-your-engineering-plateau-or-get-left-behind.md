+++
title = "Break Your Engineering Plateau or Get Left Behind"
slug = "break-your-engineering-plateau-or-get-left-behind"
date = "2025-12-12T11:40:07.328616"
draft = false
description = "Every engineer hits a plateau. Here’s how to break through it, every single day."
summary = "Every engineer hits a plateau. Here’s how to break through it, every single day."
tags = ["career development", "continuous learning", "professional growth", "skill improvement", "software engineering", "tasks", "tech"]
priority = true
priority_topics = ["tech", "tasks"]
original_title = "How Top Software Engineers Keep Getting Better Every Single Day"
source_medium = "https://medium.com/@phenrysay/285cd1cf2940"
+++

{{< figure src="https://images.unsplash.com/photo-1573166364524-d9dbfd8bbf83?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwxfHxzb2Z0d2FyZSUyMGVuZ2luZWVyaW5nJTIwcHJvZmVzc2lvbmFsJTIwZ3Jvd3RoJTIwY29udGludW91cyUyMGxlYXJuaW5nfGVufDB8MHx8fDE3NjU1MDAwMDV8MA&ixlib=rb-4.1.0&q=80&w=1080" alt="Man in black dress shirt writing on dry erase board 4T" title="Break Your Engineering Plateau or Get Left Behind" caption="Break Your Engineering Plateau or Get Left Behind - Photo by [Christina @ wocintechchat.com](https://unsplash.com/@wocintechchat) on [Unsplash](https://unsplash.com/photos/man-in-black-dress-shirt-writing-on-dry-erase-board-4T-02pK0jUg)" >}}

_Every engineer hits a plateau. Here’s how to break through it, every single day._

# How Top Software Engineers Keep Getting Better Every Single Day

## Staying Relevant, Avoiding Stagnation, and Embracing Change in Software Engineering

Let’s get straight to it. As a software engineer, especially if you’ve been around for a while—let’s say five, ten, or even twenty years—it’s dangerously easy to fall into a rut. You know there’s a better way to do things, but you keep repeating the same mistakes. Maybe you’re still using a language that’s lost its relevance, or you’re stuck on old patterns like server-side rendering when client-side rendering and APIs are the new standard. Sure, server rendering has its place, but it comes with its own set of disadvantages.

## The Trap of Comfort and Repetition

Here’s the thing: just because something worked before doesn’t mean it’s the best choice now. I see engineers still using outdated tools—like sticking with PL or only server-side rendering—when the ecosystem has clearly moved on. Or maybe you’re using a design pattern that’s basically an anti-pattern now, or your codebase is just a mess because you’re not paying attention to organization and cleanup.

This is a real danger. If you’re not careful, you end up with an inelegant codebase, and your skills actually decline over time. That’s the opposite of what should happen. With more years of experience, you should be getting better, not worse. But it’s easy to slip into bad habits and avoid learning new ways to do things.

## Outdated Technologies: Why Clinging to the Past Hurts

Let’s talk specifics. Remember when Ajax was the hot thing? It was great for its time, but it’s limited. With Ajax, you can only send data to the server; the server can’t push data back to the client. That’s why WebSockets became so popular—they allow for two-way communication. The server can send information back to the client in real time.

{{< figure src="https://images.unsplash.com/photo-1558301204-e3226482a77b?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwyfHxzb2Z0d2FyZSUyMGVuZ2luZWVyaW5nJTIwcHJvZmVzc2lvbmFsJTIwZ3Jvd3RoJTIwY29udGludW91cyUyMGxlYXJuaW5nfGVufDB8MHx8fDE3NjU1MDAwMDV8MA&ixlib=rb-4.1.0&q=80&w=1080" alt="Woman wearing grey hijab using laptop" title="Break Your Engineering Plateau or Get Left Behind" caption="Break Your Engineering Plateau or Get Left Behind - Photo by [FLASHCOM INDONESIA](https://unsplash.com/@flashcomindonesia) on [Unsplash](https://unsplash.com/photos/woman-wearing-grey-hijab-using-laptop-compiter-wr6eqJyxWy8)" >}}

But even WebSockets aren’t the end of the story. There’s always something new coming up. For example, there’s a new protocol that’s been gaining traction over the last couple of years (look it up—things move fast). Each new technology isn’t just about being new for the sake of it; it’s about solving real problems that older tech couldn’t handle.

Here’s a quick comparison:

```javascript
// Ajax Example
fetch('/api/data', {
  method: 'POST',
  body: JSON.stringify({ key: 'value' }),
  headers: { 'Content-Type': 'application/json' }
})
.then(response => response.json())
.then(data => console.log(data));

// WebSocket Example
const socket = new WebSocket('ws://yourserver.com/socket');
socket.onopen = () => socket.send('Hello Server!');
socket.onmessage = (event) => console.log('Message from server ', event.data);
```

With Ajax, you’re stuck with one-way communication. With WebSockets, you get real-time, two-way data flow.

## Letting Go of Old Habits

Sometimes, it’s not just about the technology, but the tools and frameworks you use. Maybe you’re still using a template engine like Smarty in PHP. That was fine back in 2008, but now? Not so much. The ecosystem has moved on, and so should you.

It’s time to wake up and realize that what was best practice a decade ago might be holding you back today. Don’t let nostalgia or comfort keep you from adopting better solutions.

{{< figure src="https://images.unsplash.com/photo-1621036579842-9080c7119f67?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=M3w2NjcyMjF8MHwxfHNlYXJjaHwzfHxzb2Z0d2FyZSUyMGVuZ2luZWVyaW5nJTIwcHJvZmVzc2lvbmFsJTIwZ3Jvd3RoJTIwY29udGludW91cyUyMGxlYXJuaW5nfGVufDB8MHx8fDE3NjU1MDAwMDV8MA&ixlib=rb-4.1.0&q=80&w=1080" alt="Boy in blue t shirt sitting on black office rolling chair in front of F" title="Break Your Engineering Plateau or Get Left Behind" caption="Break Your Engineering Plateau or Get Left Behind - Photo by [Nguyen Dang Hoang Nhu](https://unsplash.com/@nguyendhn) on [Unsplash](https://unsplash.com/photos/boy-in-blue-t-shirt-sitting-on-black-office-rolling-chair-in-front-of-computer-F-5UxARmads)" >}}

## The Habit of Continuous Learning

Here’s what it comes down to: make it a habit to always learn something new. Stay aware that there’s always room for improvement. You can always do better, and your code can always be cleaner, more efficient, and more maintainable.

The best engineers aren’t the ones who know the most—they’re the ones who never stop learning.

> “The best way to predict the future is to invent it.” — Alan Kay

## Key Takeaways

- **Avoid stagnation:** Don’t get stuck using outdated languages, frameworks, or patterns just because they’re familiar.
- **Embrace new technologies:** Each new tool or protocol solves problems that older ones couldn’t. Stay curious and experiment.
- **Refactor and organize:** Clean, well-organized codebases are a sign of a growing engineer. Don’t let your code become a mess.
- **Continuous learning:** Make it a habit to learn something new regularly. The field moves fast—keep up.
- **Challenge your habits:** What worked in 2008 might not work today. Be willing to let go and adopt better practices.

> “As a software engineer, your growth is directly tied to your willingness to evolve with the technology.”
