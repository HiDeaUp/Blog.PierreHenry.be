+++
title = "Set a Default Application on Linux with xdg-mime"
slug = "set-a-default-application-on-linux-with-xdg-mime"
date = "2012-01-21T16:17:13+01:00"
lastmod = "2026-09-05T00:00:00+00:00"
draft = false
description = "How to inspect and change the default Linux application for a file type with xdg-mime, without editing system files as root."
summary = "Linux desktop applications are associated with MIME types. xdg-mime lets me identify the type, set its handler, and verify the result at user level."
tags = ["Linux", "Ubuntu", "xdg-mime", "MIME types", "desktop applications", "command line"]
priority = true
priority_topics = ["tech"]
original_title = "Comment définir un programme par défaut sous Ubuntu"
source_01script = "https://01script.com/comment-changer-un-programme-par-defaut-ubuntu/"
+++

My original article changed `/etc/gnome/defaults.list` with an editor running as root. That advice was tied to an old Ubuntu configuration and could be overwritten by an update.

I now change the association at user level with `xdg-mime`. This follows the desktop MIME association system instead of modifying a distribution file.

## Identify the MIME Type

Linux desktop environments choose an application from the file's MIME type, not only from its extension.

I start with a real file:

```bash
xdg-mime query filetype ./notes.txt
```

For a text file, the result will often be:

```text
text/plain
```

I do not assume that every Markdown, image, or archive file has the same type on every system. I query one of the files I actually need to open.

## Check the Current Handler

I can then ask which desktop entry handles that MIME type:

```bash
xdg-mime query default text/plain
```

The command returns a desktop file ID such as `org.gnome.TextEditor.desktop` or `geany.desktop`. A desktop file describes how an installed graphical application is launched and which file types it supports.

## Find the Application's Desktop File

If I do not know the desktop file ID, I search the standard application directories. For Geany, for example:

```bash
find /usr/share/applications ~/.local/share/applications \
  -iname '*geany*.desktop' 2>/dev/null
```

For an entry directly inside an `applications` directory, the ID is the filename. Nested entries use their relative path with `/` replaced by `-`, as defined by the [desktop entry specification](https://specifications.freedesktop.org/desktop-entry/latest/file-naming.html). Custom XDG directories and applications installed through Flatpak or Snap can store entries elsewhere; the search above covers the common native-package locations.

## Set and Verify the Default

To use Geany for plain-text files:

```bash
xdg-mime default geany.desktop text/plain
xdg-mime query default text/plain
```

I run these commands inside my desktop session and without `sudo`. The `xdg-mime` manual specifically treats the default-handler operation as a desktop-user action. A desktop environment can also apply its own policy, which is why I always run the query again.

I finish with an end-to-end check:

```bash
xdg-open ./notes.txt
```

If the wrong application still opens, I check that the desktop file exists and declares support for the MIME type. I also check the desktop's graphical association settings: the [Ubuntu manual](https://manpages.ubuntu.com/manpages/stonking/man1/xdg-mime.1.html) explains that the query can differ from what `xdg-open` launches because it delegates to desktop-specific tools. The underlying associations are stored in `mimeapps.list` files with a defined order of precedence.

The [freedesktop.org MIME applications specification](https://specifications.freedesktop.org/mime-apps/latest-single/) explains how defaults are selected. The [`xdg-mime` manual](https://portland.freedesktop.org/doc/xdg-mime.html) documents the commands used here.

The durable lesson from my original Ubuntu note is still useful: when a desktop setting is missing from the graphical interface, inspect the MIME association before editing a system configuration file.
