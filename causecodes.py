#!/usr/bin/python
#cisco CDR cause codes

disconnect_cause_codes = {0 :"No error",
1 :"Unallocated (unassigned) number",
2 :"No route to specified transit network (national use)",
3 :"No route to destination",
4 :"Send special information tone",
5 :"Misdialed trunk prefix (national use)",
6 :"Channel unacceptable",
7 :"Call awarded and being delivered in an established channel",
8 :"Preemption",
9 :"Preemption-circuit reserved for reuse",
16 :"Normal call clearing",
17 :"User busy",
18 :"No user responding",
19 :"No answer from user (user alerted)",
20 :"Subscriber absent",
21 :"Call rejected",
22 :"Number changed",
26 :"Non-selected user clearing",
27 :"Destination out of order",
28 :"Invalid number format (address incomplete)",
29 :"Facility rejected",
30 :"Response to STATUS ENQUIRY",
31 :"Normal, unspecified",
34 :"No circuit/channel available",
38 :"Network out of order",
39 :"Permanent frame mode connection out of service",
40 :"Permanent frame mode connection operational",
41 :"Temporary failure",
42 :"Switching equipment congestion",
43 :"Access information discarded",
44 :"Requested circuit/channel not available",
46 :"Precedence call blocked",
47 :"Resource unavailable, unspecified",
49 :"Quality of Service not available",
50 :"Requested facility not subscribed",
53 :"Service operation violated",
54 :"Incoming calls barred",
55 :"Incoming calls barred within Closed User Group (CUG)",
57 :"Bearer capability not authorized",
58 :"Meet-Me secure conference minimum security level not met",
62 :"Inconsistency in designated outgoing access information and subscriber class",
63 :"Service or option not available, unspecified",
65 :"Bearer capability not implemented",
66 :"Channel type not implemented",
69 :"Requested facility not implemented",
70 :"Only restricted digital information bearer capability is available (national use).",
79 :"Service or option not implemented, unspecified",
81 :"Invalid call reference value",
82 :"Identified channel does not exist.",
83 :"A suspended call exists, but this call identity does not.",
84 :"Call identity in use",
85 :"No call suspended",
86 :"Call having the requested call identity has been cleared.",
87 :"User not member of CUG (Closed User Group)",
88 :"Incompatible destination",
90 :"Destination number missing and DC not subscribed",
91 :"Invalid transit network selection (national use)",
95 :"Invalid message, unspecified",
96 :"Mandatory information element is missing.",
97 :"Message type nonexistent or not implemented",
98 :"Message not compatible with the call state, or the message type nonexistent or not implemented",
99 :"An information element or parameter non-existent or not implemented",
100 :"Invalid information element contents",
101 :"Message not compatible with the call state",
102 :"Call terminated when timer expired; a recovery routine executed to recover from the error.",
103 :"Parameter nonexistent or not implemented - passed on (national use)",
110 :"Message with unrecognized parameter discarded",
111 :"Protocol error, unspecified",
122 :"Precedence Level Exceeded",
123 :"Device not Preemptable",
125 :"Out of bandwidth (Cisco specific)",
126 :"Call split (Cisco specific)",
127 :"Interworking, unspecified",
129 :"Precedence out of bandwidth",
262144 :"Conference Full (was 124)",
393216 :"Call split (was 126)",
458752 :"Drop any party/drop last party (was 128)",
16777257 :"CCM_SIP_400_BAD_REQUEST",
33554453 :"CCM_SIP_401_UNAUTHORIZED",
50331669 :"CCM_SIP_402_PAYMENT_REQUIRED",
67108885 :"CCM_SIP_403_FORBIDDEN",
83886081 :"CCM_SIP_404_NOT_FOUND",
100663359 :"CCM_SIP_405_METHOD_NOT_ALLOWED",
117440591 :"CCM_SIP_406_NOT_ACCEPTABLE",
134217749 :"CCM_SIP_407_PROXY_AUTHENTICATION_REQUIRED",
150995046 :"CCM_SIP_408_REQUEST_TIMEOUT",
184549398 :"CCM_SIP__410_GONE",
201326719 :"CCM_SIP_411_LENGTH_REQUIRED",
234881151 :"CCM_SIP_413_REQUEST_ENTITY_TOO_LONG",
251658367 :"CCM_SIP_414_REQUEST_URI_TOO_LONG",
268435535 :"CCM_SIP_415_UNSUPPORTED_MEDIA_TYPE",
285212799 :"CCM_SIP_416_UNSUPPORTED_URI_SCHEME",
83886207 :"CCM_SIP_420_BAD_EXTENSION",
369098879 :"CCM_SIP_421_EXTENSION_REQUIRED",
402653311 :"CCM_SIP_423_INTERVAL_TOO_BRIEF",
1073741842 :"CCM_SIP_480_TEMPORARILY_UNAVAILABLE",
}

redirect_reason_codes = {\
0 : "Unknown",
1 : "Call Forward Busy",
2 : "Call Forward No Answer",
4 : "Call Transfer",
5 : "Call Pickup",
7 : "Call Park",
8 : "Call Park Pickup",
9 : "CPE Out of Order",
10 : "Call Forward",
11 : "Call Park Reversion",
15 : "Call Forward All",
18 : "Call Deflection",
34 : "Blind Transfer",
50 : "Call Immediate Divert",
66 : "Call Forward Alternate Party",
82 : "Call Forward On Failure",
98 : "Conference",
114 : "Barge",
129 : "Aar",
130 : "Refer",
146 : "Replaces",
162 : "Redirection (3xx)",
177 : "SIP-forward busy greeting",
207 : "Follow Me (SIP-forward all greeting)",
209 : "Out of Service (SIP-forward busy greeting)",
239 : "Time Of Day (SIP-forward all greeting)",
242 : "Do Not Disturb (SIP-forward no answer greeting)",
257 : "Unavailable (SIP-forward busy greeting)",
274 : "Away (SIP-forward no answer greeting)",
303 : "Mobility HandIn",
319 : "Mobility HandOut",
335 : "Mobility Cell Pickup",
354 : "Recording",
370 : "Monitoring",
399 : "Mobility IVR",
}

on_behalf_of_codes = {\
0 : "Unknown",
1 : "CctiLine",
2 : "Unicast Shared Resource Provider",
3 : "Call Park",
4 : "Conference",
5 : "Call Forward",
6 : "Meet-Me Conference",
7 : "Meet-Me Conference Intercepts",
8 : "Message Waiting",
9 : "Multicast Shared Resource Provider",
10 : "Transfer",
11 : "SSAPI Manager",
12 : "Device",
13 : "Call Control",
14 : "Immediate Divert",
15 : "Barge",
16 : "Pickup",
17 : "Refer",
18 : "Replaces",
19 : "Redirection",
20 : "Callback",
21 : "Path Replacement",
22 : "FacCmc Manager",
23 : "Malicious Call",
24 : "Mobility",
25 : "Aar",
26 : "Directed Call Park",
27 : "Recording",
28 : "Monitoring",
}

codec_types = {\
1 : "NonStandard",
2 : "G711Alaw 64k",
3 : "G711Alaw 56k",
4 : "G711mu-law 64k",
5 : "G711mu-law 56k",
6 : "G722 64k",
7 : "G722 56k",
8 : "G722 48k",
9 : "G7231",
10 : "G728",
11 : "G729",
12 : "G729AnnexA",
13 : "Is11172AudioCap",
14 : "Is13818AudioCap",
15 : "G.729AnnexB",
16 : "G.729 Annex AwAnnexB",
18 : "GSM Full Rate",
19 : "GSM Half Rate",
20 : "GSM Enhanced Full Rate",
25 : "Wideband 256K",
32 : "Data 64k",
33 : "Data 56k",
40 : "G7221 32K",
41 : "G7221 24K",
42 : "AAC",
80 : "GSM",
81 : "ActiveVoice",
82 : "G726_32K",
83 : "G726_24K",
84 : "G726_16K",
86 : "iLBC",
100 : "H261",
101 : "H263",
102 : "Vieo",
103 : "H264",
106 : "H224",
}

dtmf_method_codes = {\
0 : "No DTMF",
1 : "OOB",
2 : "RFC2833",
3 : "OOB and RFC2833",
4 : "Unknown",
}

call_security_codes = {\
0 : "Non-secured",
1 : "Authenticated (not encrypted)",
2 : "Secured (encrypted)",
}