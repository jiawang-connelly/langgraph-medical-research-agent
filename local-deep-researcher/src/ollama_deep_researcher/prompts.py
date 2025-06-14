from datetime import datetime

# Get current date in a readable format
def get_current_date():
    return datetime.now().strftime("%B %d, %Y")

query_writer_instructions="""Your goal is to generate a targeted web search query.

<CONTEXT>
Current date: {current_date}
Please ensure your queries account for the most current information available as of this date.
</CONTEXT>

<TOPIC>
{research_topic}
</TOPIC>

<FORMAT>
Format your response as a JSON object with ALL three of these exact keys:
   - "query": The actual search query string
   - "rationale": Brief explanation of why this query is relevant
</FORMAT>

<EXAMPLE>
Example output:
{{
    "query": "machine learning transformer architecture explained",
    "rationale": "Understanding the fundamental structure of transformer models"
}}
</EXAMPLE>

Provide your response in JSON format:"""

summarizer_instructions="""
<GOAL>
Generate a comprehensive, detailed summary of the provided context with extensive specific information from the sources.
</GOAL>

<REQUIREMENTS>
When creating a NEW summary:
1. Create a COMPREHENSIVE summary with multiple detailed paragraphs covering:
   - Exact numbers, percentages, statistics, and quantitative data
   - Complete study names, clinical trial phases, enrollment numbers, and sample sizes
   - Specific drug names, exact dosages, treatment protocols, and administration schedules
   - Detailed patient demographics, inclusion/exclusion criteria, and selection parameters
   - Comprehensive mechanism details, molecular targets, pathways, and biological processes
   - Complete FDA/regulatory approval information with specific dates and indications
   - Clinical outcomes, efficacy rates, safety profiles, and adverse events
   - Comparative effectiveness data and head-to-head trial results
2. Each paragraph should contain multiple sentences with detailed information
3. Reference specific sources or studies when mentioning key findings
4. Include recent developments, ongoing trials, and emerging research
5. Provide context and background information to make findings meaningful
6. Be thorough and comprehensive - aim for detailed coverage of all relevant aspects

When EXTENDING an existing summary:                                                                                                                 
1. Read the existing summary and new search results carefully.                                                    
2. Compare the new information with the existing summary.                                                         
3. For each piece of new information:                                                                             
    a. If it's related to existing points, integrate it with extensive specific details and expand the section
    b. If it's entirely new but relevant, add comprehensive new paragraphs with detailed information                            
    c. If it's not relevant to the user topic, skip it.                                                            
4. Significantly expand the content with detailed information from sources
5. Ensure the final output is substantially more comprehensive than the input summary                                                                                                                                                            
< /REQUIREMENTS >

< FORMATTING >
- Start directly with the updated summary, without preamble or titles. Do not use XML tags in the output.
- Write detailed, comprehensive paragraphs with multiple sentences each
- Include extensive specific details, numbers, study information, and clinical data
- Use clear, professional language suitable for medical professionals
- Reference specific sources, studies, or trials when mentioning key findings
- Aim for thorough, in-depth coverage rather than brief summaries
< /FORMATTING >

<Task>
Analyze the provided Context thoroughly and extract ALL relevant detailed information. Generate a comprehensive, extensive summary that covers the topic in depth with specific clinical data, study results, mechanisms, patient information, and regulatory details from the sources. Make the summary detailed and informative for medical professionals seeking comprehensive information.
</Task>
"""

reflection_instructions = """You are an expert research assistant analyzing a summary about {research_topic}.

<GOAL>
1. Identify knowledge gaps or areas that need deeper exploration
2. Generate a follow-up question that would help expand your understanding
3. Focus on technical details, implementation specifics, or emerging trends that weren't fully covered
</GOAL>

<REQUIREMENTS>
Ensure the follow-up question is self-contained and includes necessary context for web search.
</REQUIREMENTS>

<FORMAT>
Format your response as a JSON object with these exact keys:
- knowledge_gap: Describe what information is missing or needs clarification
- follow_up_query: Write a specific question to address this gap
</FORMAT>

<Task>
Reflect carefully on the Summary to identify knowledge gaps and produce a follow-up query. Then, produce your output following this JSON format:
{{
    "knowledge_gap": "The summary lacks information about performance metrics and benchmarks",
    "follow_up_query": "What are typical performance benchmarks and metrics used to evaluate [specific technology]?"
}}
</Task>

Provide your analysis in JSON format:"""