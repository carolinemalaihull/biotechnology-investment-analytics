*BioSafety Check*


**Scenario:**

You are a Venture Capital analyst evaluating early-stage biotech investments. Because your fund is risk-averse, you need to understand the clinical landscape surrounding different biologics, including any reported adverse reactions, before pitching opportunities to your team.

**Purpose:**

BioSafety Check retrieves real-world safety data from the FDA (Food and Drug Administration) Adverse Event Reporting System (FAERS) and summarises key information such as the most common reactions and any serious adverse events such as death. This allows you to make informed investment decisions quickly and efficiently.

**Workflow**
1. Ask the user for input (drug/biologic name)
2. Fetch data from the FDA API (get_fda_data)
3. Process the data: extract reactions, flag serious events, count occurrences
4. Save results to a readable file (results.txt)
5. Notify the user that the process is complete

**Key Features:**

Fetches up to 500 adverse event reports per drug from the FDA API.
Counts and ranks the most common reactions.
Flags serious reactions (e.g., death, hospitalization, life-threatening).
Saves a clear and readable safety summary to file (results.txt).
Designed to be reusable and extendable for any biologic or drug name.

**Why This Matters**

Real-world safety data is crucial when evaluating biotech investments. However, the landscape changes all the time making it time-consuming to monitor and stay up-to-date. This programme produces clear and concise summaries quickly and easily meaning decision making can be smoother.

**API Source** 

FAERS API:

https://api.fda.gov/drug/event.json 

**Dependencies**

requests (fetches data from the FDA API)
collections.Counter (counts reaction occurrences)

**Example Search Terms**

- Paracetamol

- Pembrolizumab

- CAR T cell

**Example Search Result**

CAR T Cell Safety Summary:
----------------------------------------
Total reports analyzed: 500

Top reported reactions: 
 - Fatigue (49)
 - White blood cell count increased (43)
 - White blood cell count decreased (43)
 - Anaemia (39)
 - Platelet count decreased (39)

Serious reactions found: 26
Details: Death
----------------------------------------