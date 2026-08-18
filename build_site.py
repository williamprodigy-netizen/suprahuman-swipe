#!/usr/bin/env python3
"""Build the Suprahuman swipe site.

Registered through the funnel and captured end to end. The mechanic worth having
is on the post-booking page, not in the pitch.

Run: python3 build_site.py
"""
import sys, os, glob, subprocess
sys.path.insert(0, os.path.expanduser("~/scripts/_swipe_builder"))
from swipebuild import build

REPO = os.path.dirname(os.path.abspath(__file__))
PKG = os.path.expanduser("~/Downloads/Swipes/SUPRAHUMAN_Swipe")


def _probe(p):
    try:
        return int(float(subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration",
             "-of", "csv=p=0", p], capture_output=True, text=True, timeout=60).stdout.strip()))
    except Exception:
        return 0


def video_library():
    rows = []
    for p in sorted(glob.glob(os.path.join(PKG, "Recording/*.mp4"))):
        mb = os.path.getsize(p) / 1e6
        rows.append((os.path.basename(p), _probe(p),
                     f"{mb/1000:.1f} GB" if mb >= 1000 else f"{mb:.0f} MB",
                     "The SH Method pitch video from the landing page."))
    return rows


CONFIG = {
    "SITE": "Suprahuman — the SH Method",
    "CREATOR": "John Madsen",
    "ADS_KEY": "suprahuman",
    "FUNNEL_IDS": [],
    "CAPTURED": "2 August 2026",
    "REPO": REPO,
    "PACKAGE": "~/Downloads/Swipes/SUPRAHUMAN_Swipe",
    "BLURB": "Online fitness coaching aimed at former athletes. The pitch is ordinary; "
             "the <b>post-booking page</b> does something almost nobody does &mdash; it "
             "warns the lead that an unknown number is about to text them.",

    "PAGES": [
        ("index.html", "Overview"),
        ("analysis.html", "Analysis"),
        ("transcripts.html", "Transcript"),
        ("videos.html", "Video library"),
    ],

    "STATS": [
        ("Presenter", "John Madsen"),
        ("Claim", "#1 in the US"),
        ("Clients claimed", "6,000+"),
        ("ICP", "Former athletes"),
        ("Pitch length", "~5 min"),
        ("Words", "2,351"),
        ("Income gate", "$150k/yr, stated in the VSL"),
        ("Registered", "yes"),
    ],

    "OFFER": [
        ("Product", "Suprahuman / SH Method &mdash; online fitness coaching"),
        ("Positioning", "&ldquo;the number one online fitness coaching program in the "
                        "United States&rdquo;"),
        ("ICP", "&ldquo;soft and out of shape former athletes&rdquo; &mdash; a specific "
                "identity, not a demographic"),
        ("Scale claimed", "6,000+ people helped"),
        ("Pitch length", "Opens by promising the whole thing in <b>five minutes</b>"),
        ("Path", "Long-form page &rarr; booked consultation &rarr; pre-call video + SMS confirm"),
        ("Price", "<b>Not observed.</b> No figure anywhere in the captured funnel"),
    ],

    "FINDINGS": [
        ("They warn you about the unknown number &mdash; steal this",
         "The post-booking page says plainly: <i>if a text arrives from an unknown number in "
         "the next hour, that is us, please reply.</i> It converts a message that would "
         "normally be ignored into an expected one, and the reply itself is a "
         "micro-commitment that confirms the lead is reachable. <b>We text booked leads from "
         "numbers they do not recognise and say nothing in advance.</b> This is a one-line "
         "change to our confirmation page."),
        ("The ICP is an identity, not a demographic",
         "&ldquo;Soft and out of shape <i>former athletes</i>&rdquo; describes who someone "
         "<i>used to be</i>. It selects on self-image rather than age or gender, and it "
         "carries the promise inside it &mdash; you were this once, you can be again. Sharper "
         "than anything demographic."),
        ("Five minutes, stated up front",
         "The video opens by committing to a five-minute runtime. Naming the cost of "
         "attention before asking for it is the opposite of the forced-consumption players "
         "elsewhere in this file, and it is a bet that respect converts better than capture."),
        ("Confirmation is a sequence, not a page",
         "Booking is followed by a pre-call video, a checklist and an SMS confirmation. The "
         "same pattern as Her Closing Academy and Warrior Babe: <b>three unrelated "
         "competitors all put work between booking and attending.</b>"),
    ],

    "FUNNEL": [
        ("Landing / pitch", "suprahumanceo.com/sh-method61258820",
         "Long-form page with the SH Method video. Registered here."),
        ("Booked", "suprahumanceo.com/appointment-booked",
         '<span class="tag good">the mechanic</span> Pre-call video, checklist, and the '
         '&ldquo;an unknown number will text you&rdquo; warning.'),
    ],

    "TRANSCRIPT_GROUPS": [
        ("The SH Method pitch", [os.path.join(PKG, "Transcript/transcript.md")]),
    ],

    "SLIDE_PAGES": [],
    "VIDEOS": video_library(),

    "ANALYSIS": """
<div class="note"><b>One idea here is worth more than the rest of the funnel.</b> Telling a
booked lead that an unknown number is about to text them, and asking for a reply, costs a
sentence and fixes a problem we actually have.</div>

<h2 class="sec">Why the SMS warning matters to us</h2>
<p>Our booked leads get texts from numbers they have never seen. Most people ignore an unknown
number, or treat it as spam &mdash; so our confirmation and reminder texts are fighting a
default. Suprahuman removes the default by naming it in advance, on the page, while the lead
is still paying attention.</p>
<p>The ask for a reply does double duty: it confirms the number is real and reachable
<i>before</i> the call, and a lead who has already replied once is materially more likely to
reply to a reminder. We could add this to our confirmation page today.</p>

<h2 class="sec">He disqualifies on money in the first 49 seconds</h2>
<p>Most funnels hide the money question until the application, or until the call. Madsen puts
it in the opening minute of the VSL and frames the exclusion as respect &mdash; <i>&ldquo;there
are millions of other fitness programs out there for cheap and for free. We are not one of
them.&rdquo;</i> The lead who cannot pay leaves before consuming the pitch, and the lead who
can has just been told they are in the room the others were kept out of.</p>
<p>He pairs it immediately with a full money-back guarantee: <i>&ldquo;if we don't deliver on
our promise to get you back to your physical prime&hellip; we will give you all your money
back.&rdquo;</i> Price gate and risk reversal in the same breath &mdash; the gate justifies the
price, the guarantee removes the reason to refuse it. <span class="tag good">worth
stealing</span></p>
<p>Read against our own funnel: <b>our income question sits in the application, after the
class.</b> His sits before the pitch even starts. That is the difference between filtering
leads and filtering attention.</p>

<h2 class="sec">The pattern across three competitors</h2>
<div class="tablewrap"><table>
<tr><th>Who</th><th>What sits between booking and attending</th></tr>
<tr><td>Her Closing Academy</td><td>&ldquo;Booked but not confirmed&rdquo; + cancellation threat + 2:00 lock</td></tr>
<tr><td>WarriorBabe</td><td>&ldquo;Final step to complete your application&rdquo; + pre-call checklist</td></tr>
<tr><td><b>Suprahuman</b></td><td>Pre-call video + checklist + <b>SMS expectation set in advance</b></td></tr>
</table></div>
<p style="margin-top:12px">Different markets, different products, same conclusion: <b>a booking
is not a commitment until the lead does something else.</b> Ours ends at the booking.</p>

<h2 class="sec">Read carefully</h2>
<p><b>Attribution resolved &mdash; VERIFIED.</b> The presenter is <b>John Madsen</b>. The name
appears three times in the raw HTML of both captured pages and once in the extracted visible
text. The &ldquo;Rich Soltis&rdquo; name came from the intake doc line &ldquo;John / Rich Soltis&rdquo; and has
<i>no</i> supporting evidence anywhere in the capture. Dropped 18 Aug 2026. (The transcript renders it as
&ldquo;Mattson&rdquo; &mdash; that is whisper mis-hearing the surname, not a second name.)</p>
<p><b>No price appears anywhere in the captured funnel</b> &mdash; but the $150,000 figure is
<i>not</i> an illustration, as an earlier pass of this page claimed. It is a hard qualifier,
spoken at <b>00:00:49</b>: <i>&ldquo;You must earn, at the very least, $150,000 annually. I'm
not here to take people's money who can barely afford food for their families.&rdquo;</i> He
disqualifies on income inside the first minute of the VSL, before any pitch.</p>
<p>&ldquo;#1 online fitness coaching program in the United States&rdquo; and the 6,000-client
figure are <i>their</i> claims, stated in their own video, and are recorded here as claims
rather than verified facts.</p>
""",
}

if __name__ == "__main__":
    build(CONFIG)
