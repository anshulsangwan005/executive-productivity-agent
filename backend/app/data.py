people = {
    "Arjun Malhotra": {
        "role": "VP Sales",
        "email": "arjun.malhotra@veridian-corp.example"
    },
    "Neha Kapoor": {
        "role": "Marketing Lead",
        "email": "neha.kapoor@veridian-corp.example"
    },
    "Raghav Sethi": {
        "role": "Ops Manager",
        "email": "raghav.sethi@veridian-corp.example"
    },
    "Divya Rao": {
        "role": "Finance",
        "email": "divya.rao@veridian-corp.example"
    },
    "Priya Nair": {
        "role": "Meridian Logistics",
        "email": "priya.nair@meridianlogistics.example"
    }
}


commitments = [
    {
        "id": 1,
        "title": "Send updated vendor list to Raghav",
        "owner": "Arjun Malhotra",
        "deadline": "Wednesday morning",
        "status": "Pending",
        "priority": "High",
        "source": "Vendor List email thread",
        "details": "Arjun committed to sending the updated vendor list to Raghav."
    },
    {
        "id": 2,
        "title": "Q3 Campaign Deck review",
        "owner": "Arjun Malhotra",
        "deadline": "Thursday, 24 September at 9:30 AM",
        "status": "Scheduled",
        "priority": "High",
        "source": "Q3 Campaign Deck email thread",
        "details": "The review moved from Wednesday to Thursday morning and was confirmed for 9:30 AM."
    },
    {
        "id": 3,
        "title": "Review July expense variance report",
        "owner": "Arjun Malhotra",
        "deadline": "Wednesday evening",
        "status": "Completed",
        "priority": "Medium",
        "source": "Expense Variance Report email thread",
        "details": "Divya sent the report Wednesday evening and Arjun confirmed receipt."
    },
    {
        "id": 4,
        "title": "Meridian Logistics call",
        "owner": "Arjun Malhotra",
        "deadline": "Wednesday, 23 September at 3:00 PM",
        "status": "Confirmed",
        "priority": "High",
        "source": "Call Reschedule email thread",
        "details": "Priya confirmed that Wednesday at 3 PM works."
    },
    {
        "id": 5,
        "title": "Mumbai office lease renewal",
        "owner": "Unconfirmed",
        "deadline": "Friday, 25 September EOD",
        "status": "Unowned",
        "priority": "Critical",
        "source": "Mumbai Office Lease Renewal email thread",
        "details": "The renewal requires an authorized signature, but ownership is still unconfirmed."
    }
]


calendar = [
    {
        "date": "Monday, 21 September",
        "time": "9:00 AM - 9:35 AM",
        "event": "Leadership Sync"
    },
    {
        "date": "Monday, 21 September",
        "time": "2:00 PM - 2:30 PM",
        "event": "1:1 with Neha"
    },
    {
        "date": "Tuesday, 22 September",
        "time": "11:00 AM - 12:00 PM",
        "event": "Internal Budget Review"
    },
    {
        "date": "Wednesday, 23 September",
        "time": "3:00 PM - 3:30 PM",
        "event": "Call — Meridian Logistics"
    },
    {
        "date": "Thursday, 24 September",
        "time": "9:00 AM - 10:00 AM",
        "event": "Board Prep Session"
    },
    {
        "date": "Thursday, 24 September",
        "time": "4:00 PM - 5:00 PM",
        "event": "Hiring Panel — Sales Associate"
    },
    {
        "date": "Friday, 25 September",
        "time": "10:00 AM - 10:30 AM",
        "event": "Facilities Check-in"
    }
]


emails = [
    {
        "thread": "Vendor List",
        "messages": [
            "Raghav asked Arjun to send the updated vendor list.",
            "Arjun said he would send it first thing Tuesday morning.",
            "Raghav said Tuesday works.",
            "Arjun then committed to Wednesday morning.",
            "Raghav checked Wednesday morning asking if it was still on."
        ]
    },
    {
        "thread": "Q3 Campaign Deck",
        "messages": [
            "Neha initially targeted Wednesday for review.",
            "Neha moved the review to Thursday morning.",
            "Arjun agreed to Thursday.",
            "Neha confirmed 9:30 AM Thursday.",
            "Neha said the deck was ready before the review."
        ]
    },
    {
        "thread": "Call Reschedule",
        "messages": [
            "Priya requested a new time for the Meridian Logistics call.",
            "Arjun proposed Wednesday at 3 PM.",
            "Priya confirmed Wednesday at 3 PM.",
            "Priya checked again before the call.",
            "Arjun confirmed the call."
        ]
    },
    {
        "thread": "Expense Variance Report",
        "messages": [
            "Divya started the July variance report.",
            "Arjun requested it by Wednesday evening.",
            "Divya agreed.",
            "Divya sent the report Wednesday evening.",
            "Arjun confirmed receipt."
        ]
    },
    {
        "thread": "Mumbai Office Lease Renewal",
        "messages": [
            "Facilities announced an authorized signature was required by Friday.",
            "Raghav asked who was responsible.",
            "Divya said she believed Facilities handled it.",
            "Facilities sent a second reminder Thursday.",
            "Raghav said the item was still unowned."
        ]
    }
]


voice_notes = [
    {
        "date": "Monday, 21 September",
        "text": "Arjun reminded himself about the vendor list and said the Mumbai lease still needed an owner."
    },
    {
        "date": "Wednesday, 23 September",
        "text": "Arjun reminded himself that the expense variance report should be in his hands Wednesday evening and that he needed to lock the Meridian call time."
    }
]