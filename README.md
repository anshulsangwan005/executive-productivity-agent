# Executive Productivity Agent

An AI-powered executive productivity assistant built for Arjun Malhotra, VP Sales.

## Overview

The Executive Productivity Agent helps an executive understand important commitments, deadlines, meetings, pending tasks, and follow-ups from multiple information sources.

The prototype uses assignment-provided data from:

- Emails
- Calendar
- Voice notes
- Commitment records

## Key Features

- Executive productivity dashboard
- Open commitment tracking
- Critical item identification
- Calendar overview
- Natural-language question answering
- Deadline and status tracking
- Cross-source productivity insights
- Source-based information retrieval

## Example Questions

The agent can answer questions such as:

- What are my current priorities?
- What are my open commitments?
- What should I worry about before Friday?
- What is the status of the Mumbai lease?
- When is the Meridian Logistics call?
- What happened with the expense variance report?
- When is the Q3 Campaign Deck review?
- What meetings do I have this week?

## Architecture

```text
Executive / User
       |
       v
Next.js Frontend
       |
       v
FastAPI Backend
       |
       v
Agent Controller
       |
       +------------------+
       |                  |
       v                  v
Commitments          Information Sources
                     |               |       
                     v               v
                   Emails         Calendar
       |
       v
Reasoning & Response
       |
       v
Executive Answer