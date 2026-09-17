from .data import commitments, calendar, emails, voice_notes


def get_open_items():
    return [
        item for item in commitments
        if item["status"] in ["Pending", "Unowned"]
    ]


def get_critical_items():
    return [
        item for item in commitments
        if item["priority"] == "Critical"
    ]


def get_completed_items():
    return [
        item for item in commitments
        if item["status"] == "Completed"
    ]


def get_scheduled_items():
    return [
        item for item in commitments
        if item["status"] in ["Scheduled", "Confirmed"]
    ]


def get_dashboard():
    return {
        "open_items": get_open_items(),
        "critical_items": get_critical_items(),
        "completed_items": get_completed_items(),
        "scheduled_items": get_scheduled_items()
    }


def search_sources(question):
    question = question.lower()

    results = []

    for item in commitments:
        text = (
            item["title"]
            + " "
            + item["details"]
            + " "
            + item["source"]
        ).lower()

        words = question.split()

        if any(word in text for word in words if len(word) > 3):
            results.append(item)

    return results


def answer_question(question):

    q = question.lower()

    if "priority" in q or "priorities" in q:

        items = get_open_items()

        answer = "Your current priorities are:\n\n"

        for item in items:
            answer += (
                f"• {item['title']}\n"
                f"  Deadline: {item['deadline']}\n"
                f"  Priority: {item['priority']}\n"
                f"  Status: {item['status']}\n\n"
            )

        return answer

    if "open" in q or "task" in q or "commitment" in q:

        items = get_open_items()

        answer = "Your open commitments are:\n\n"

        for item in items:
            answer += (
                f"• {item['title']}\n"
                f"  Deadline: {item['deadline']}\n"
                f"  Status: {item['status']}\n\n"
            )

        return answer

    if "overdue" in q:

        return (
            "The vendor list is still pending. "
            "Arjun had committed to sending the updated vendor list "
            "to Raghav by Wednesday morning. "
            "Raghav followed up Wednesday morning asking for an update."
        )

    if "friday" in q or "before friday" in q:

        return (
            "The main unresolved item before Friday is the Mumbai office "
            "lease renewal. It requires an authorized signature by Friday, "
            "25 September, end of day. The responsible owner is still unconfirmed."
        )

    if "lease" in q or "mumbai" in q:

        return (
            "The Mumbai office lease renewal requires an authorized signature "
            "by Friday, 25 September, end of day. The item is currently unowned."
        )

    if "campaign" in q or "deck" in q:

        return (
            "The Q3 Campaign Deck review was moved from Wednesday to Thursday "
            "morning. The final time was confirmed as Thursday at 9:30 AM."
        )

    if "expense" in q or "variance" in q:

        return (
            "The July expense variance report was requested for Wednesday evening. "
            "Divya sent it Wednesday evening and Arjun confirmed receiving it, "
            "so this item is completed."
        )

    if "meridian" in q or "client" in q:

        return (
            "The Meridian Logistics call was confirmed for Wednesday, "
            "23 September at 3:00 PM."
        )

    if "meeting" in q or "calendar" in q:

        answer = "Your scheduled calendar events are:\n\n"

        for event in calendar:
            answer += (
                f"• {event['date']} — {event['time']}\n"
                f"  {event['event']}\n\n"
            )

        return answer

    if "voice" in q or "reminder" in q:

        answer = "Your personal reminders include:\n\n"

        for note in voice_notes:
            answer += f"• {note['date']}: {note['text']}\n\n"

        return answer

    results = search_sources(question)

    if results:

        answer = "I found the following relevant information:\n\n"

        for item in results[:3]:
            answer += (
                f"• {item['title']}\n"
                f"  {item['details']}\n"
                f"  Source: {item['source']}\n\n"
            )

        return answer

    return (
        "I can help you with priorities, commitments, deadlines, "
        "calendar events, the campaign deck, vendor list, Mumbai lease, "
        "expense report, and Meridian Logistics."
    )