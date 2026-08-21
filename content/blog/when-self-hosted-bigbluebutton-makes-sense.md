+++
title = "When Self-Hosted BigBlueButton Makes Sense"
slug = "when-self-hosted-bigbluebutton-makes-sense"
date = "2026-08-22T03:20:00+10:00"
draft = false
description = "How I evaluate self-hosted BigBlueButton for virtual classrooms, including server capacity, WebRTC networking, recordings, integration, and operations."
summary = "BigBlueButton is designed for virtual classrooms, but running it in production requires more than installing an open-source video application."
tags = ["BigBlueButton", "WebRTC", "self-hosting", "open source", "infrastructure", "video conferencing"]
priority = true
priority_topics = ["tech"]
original_title = "Outil de Vidéo Conférence Web open source - BigBlueButton"
source_01script = "https://01script.com/outil-video-conference-web-bigbluebutton/"
+++

I discovered BigBlueButton in 2012 as an open-source video-conferencing tool. My original article focused on voice, video, slides, screen sharing, and chat.

Many services now provide those features. BigBlueButton has a more specific purpose: it is designed for virtual classrooms, with presentations, whiteboards, polls, breakout rooms, and structured recordings.

Self-hosting gives an organisation more control. It also creates an operational responsibility that needs to be measured before installation.

## Start With the Teaching Requirement

I would not use BigBlueButton as an automatic replacement for every video meeting.

I would consider it when the service needs several of these capabilities:

- distinct teacher, moderator, and participant roles;
- slides that can be annotated during a session;
- polls and a shared whiteboard;
- separate breakout rooms;
- integration with a learning platform;
- recordings organised around the lesson.

If the requirement is a few internal calls, a managed service will often require less work. Real-time video operations are not a minor hosting task.

## Read the Requirements Before Choosing a Server

The current [BigBlueButton 3.0 installation guide](https://docs.bigbluebutton.org/administration/install/) recommends a dedicated Ubuntu 22.04 server with 8 CPU cores, 16 GB of memory, 250 Mbit/s symmetric bandwidth, and substantial storage when recording is enabled.

Those figures are a starting point, not a capacity promise. Webcam count, video quality, screen sharing, recordings, and participant locations all affect the load.

I run a test that represents the real session. Ten people listening to a presentation do not create the same workload as several groups using cameras, microphones, and whiteboards at the same time.

## The Network Matters as Much as the CPU

A virtual classroom depends on the path between every browser and the server. Spare CPU does not correct packet loss or a firewall that blocks WebRTC traffic.

I verify at least:

- a domain name with a valid TLS certificate;
- the TCP and UDP ports required by the documentation;
- a TURN server for restrictive networks;
- inbound and outbound bandwidth;
- latency from the regions where participants live;
- behaviour on mobile and shared networks.

The test needs to include the browsers and devices participants actually use. A clean result from an office connection is not enough.

## Recordings Change the Operating Model

A recording is not simply one video file. BigBlueButton captures session events and media, then processes them for playback. Its [recording documentation](https://docs.bigbluebutton.org/development/recording/) explains that pipeline.

Before enabling it, I decide:

- which sessions may be recorded;
- who can start recording;
- how long the source data and result are retained;
- who can view, export, or delete them;
- which files need backups;
- how participants are informed.

Storage, processing time, and retention rules need to be planned before the first recorded lesson.

## Integrate Without Exposing Secrets

BigBlueButton provides an API for creating meetings, generating join links, and checking their state. A learning platform or application can manage accounts while BigBlueButton handles the live session.

I keep the API secret on the server. The browser should not be able to create a moderator link or alter sensitive meeting settings by itself.

I also test failures: an unavailable server, an ended meeting, a recording still being processed, and a user without permission. The integration is complete when these states are understandable, not when the first API call succeeds.

## Plan for Long-Term Operations

A production installation needs monitoring, logs, backups, updates, and capacity planning. I check the server before an important session and keep a fallback procedure if the platform is unavailable.

I also test upgrades on a separate machine. Video dependencies, client browsers, and the operating system change over time. Updating the production server immediately before a lesson adds avoidable risk.

Capacity needs to be reviewed as usage changes. The first successful class does not prove that five simultaneous classes will work.

## Self-Hosted or Managed

I would self-host BigBlueButton when data control, integration, customisation, or usage volume justifies dedicated operational knowledge.

I would choose managed hosting when the team wants to focus on teaching and does not have the time to operate real-time infrastructure.

The software is open source. The service still has a cost: compute, storage, bandwidth, updates, and human time. The right decision compares that cost with the control the organisation genuinely needs.
