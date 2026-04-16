import streamlit as st

# ── NO st.set_page_config() here — already called in Homepage ──────────────

st.markdown("""
<style>
.hero-banner { background: linear-gradient(135deg, #1a0533 0%, #3d1268 50%, #6a1f9e 100%); padding: 2.5rem 2rem; border-radius: 16px; margin-bottom: 1.5rem; border-left: 6px solid #c084fc; }
.hero-title { font-size: 2rem; font-weight: 800; color: #ffffff; margin: 0 0 0.4rem 0; }
.hero-subtitle { font-size: 1.05rem; color: #ddd6fe; margin: 0; }
.hero-badge { display: inline-block; background: #c084fc; color: #1a0533; font-size: 0.75rem; font-weight: 700; padding: 0.2rem 0.7rem; border-radius: 20px; margin-bottom: 0.8rem; text-transform: uppercase; }
.progress-container { background: #e9ecef; border-radius: 20px; height: 10px; margin: 0.3rem 0 0.5rem 0; }
.progress-bar { background: linear-gradient(90deg, #c084fc, #6a1f9e); height: 10px; border-radius: 20px; width: 50%; }
.progress-label { font-size: 0.78rem; color: #6c757d; margin-bottom: 0.2rem; }
.stat-card { background: white; border: 1px solid #dee2e6; border-radius: 12px; padding: 1.2rem; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
.stat-number { font-size: 1.8rem; font-weight: 800; color: #6a1f9e; }
.stat-label { font-size: 0.78rem; color: #6c757d; margin-top: 0.2rem; }
.finance-lens { background: linear-gradient(135deg, #fff3cd, #fff8e1); border: 1px solid #ffc107; border-left: 5px solid #f5a623; border-radius: 10px; padding: 1rem 1.2rem; margin: 0.5rem 0; }
.finance-lens-title { font-size: 0.85rem; font-weight: 700; color: #856404; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.4rem; }
.finance-lens-body { font-size: 0.88rem; color: #5a4200; line-height: 1.6; }
.section-heading { font-size: 1.15rem; font-weight: 700; color: #1a1a2e; border-bottom: 2px solid #c084fc; padding-bottom: 0.3rem; margin: 1.5rem 0 1rem 0; }
.prompt-box { background: #f9f0ff; border: 1px solid #d8b4fe; border-radius: 10px; padding: 1rem 1.2rem; font-family: monospace; font-size: 0.88rem; margin: 0.5rem 0; }
.quiz-box { background: #f5f0ff; border: 1px solid #d8b4fe; border-radius: 12px; padding: 1.2rem 1.4rem; }
.llm-card { background: white; border: 1px solid #e9ecef; border-radius: 12px; padding: 1rem 1.2rem; margin-bottom: 0.6rem; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-banner">
  <div class="hero-badge">💜 Module 4 of 8 &nbsp;|&nbsp; AI Series</div>
  <div class="hero-title">Generative AI & Large Language Models</div>
  <div class="hero-subtitle">Master the tools reshaping finance — understand how ChatGPT, Claude,
  and Copilot work, how to prompt them effectively, and how to use RAG for financial documents.</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="progress-label">Series progress — Module 4 of 8</div>', unsafe_allow_html=True)
st.markdown('<div class="progress-container"><div class="progress-bar"></div></div>', unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown('<div class="stat-card"><div class="stat-number">5</div><div class="stat-label">Gen AI Techniques</div></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="stat-card"><div class="stat-number">10+</div><div class="stat-label">Prompt Examples</div></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="stat-card"><div class="stat-number">~35</div><div class="stat-label">Min Read Time</div></div>', unsafe_allow_html=True)
with c4: st.markdown('<div class="stat-card"><div class="stat-number">5</div><div class="stat-label">Quiz Questions</div></div>', unsafe_allow_html=True)
st.markdown("")

with st.sidebar:
    st.markdown("### 🤖 AI Series — Modules")
    modules = [("1","Foundations of AI",False),("2","Machine Learning Essentials",False),("3","Deep Learning & Neural Networks",False),("4","Generative AI & LLMs",True),("5","AI in Finance & Accounting",False),("6","Building AI Models",False),("7","AI Ethics, Risk & Governance",False),("8","Future of AI & Career Readiness",False)]
    for num, name, active in modules:
        st.markdown(f"**▶ M{num} — {name}** ✅" if active else f"M{num} — {name}")
    st.markdown("---")
    st.info("💡 M3 (Deep Learning) provides useful context for this module.")

st.markdown('<div class="section-heading">🤖 What is Generative AI?</div>', unsafe_allow_html=True)
with st.expander("📖 Definition & How It Differs from Predictive AI", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        #### 📊 Predictive AI (Traditional ML)
        - Analyses existing data
        - Outputs a **prediction** or **classification**
        - *"Is this transaction fraud? Probability: 0.94"*
        - *"What will revenue be next quarter? $12.4M"*
        - Discriminative models
        """)
    with col2:
        st.markdown("""
        #### ✨ Generative AI
        - Creates **new content** from learned patterns
        - Outputs text, images, code, audio, video
        - *"Write a board paper on our Q3 results"*
        - *"Generate Python code to analyse this data"*
        - Generative models
        """)
    st.markdown("""
    **Generative AI** refers to AI systems that can produce new content — text, images, code, audio —
    that resembles the data they were trained on. The key models are:
    - **Large Language Models (LLMs)** → generate text and code (ChatGPT, Claude, Gemini)
    - **Diffusion Models** → generate images (DALL-E, Stable Diffusion, Midjourney)
    - **Multimodal Models** → handle text + images + audio together (GPT-4V, Gemini Ultra)
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens</div>
      <div class="finance-lens-body">
        In finance, Generative AI is most transformative for <b>text-heavy workflows</b>:
        drafting variance commentary, summarising board papers, analysing contracts,
        answering tax queries, writing audit findings, and generating financial model code in Python/VBA.
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-heading">🏗️ How Large Language Models Work</div>', unsafe_allow_html=True)
with st.expander("⚙️ From Training to Token Generation"):
    st.markdown("""
    **What is an LLM?**
    A Large Language Model is a transformer-based neural network trained on massive amounts of text
    (hundreds of billions to trillions of tokens from the internet, books, code, and documents).

    **Training phases:**

    **Phase 1 — Pre-training (Self-supervised)**
    The model learns to predict the next token in a sequence from billions of text examples.
    No human labels needed — the text itself provides the training signal.
    *Scale: GPT-4 trained on ~1 trillion tokens. Cost: ~$100M+.*

    **Phase 2 — Instruction Fine-tuning (SFT)**
    The pre-trained model is further trained on high-quality question-answer pairs to follow
    instructions helpfully and accurately.

    **Phase 3 — RLHF (Reinforcement Learning from Human Feedback)**
    Human raters compare model outputs and rank them. A reward model learns human preferences.
    The LLM is then fine-tuned to maximise the reward model's score — making it more helpful,
    harmless, and honest.

    **Generation (Inference)**
    At inference time, the model predicts the next token given all previous tokens — one token
    at a time — using probability distributions over its vocabulary. Temperature controls
    randomness: low temperature = more deterministic; high = more creative.
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — What "Context Window" Means</div>
      <div class="finance-lens-body">
        The <b>context window</b> is how much text the LLM can "see" at once. GPT-4 Turbo: 128K tokens
        (~96,000 words). Claude 3: 200K tokens (~150,000 words). This determines whether a model can
        read an entire annual report in one go. For very long financial documents, you may need
        chunking strategies or RAG (covered below).
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-heading">🌐 Major LLMs — A Finance Professional\'s Guide</div>', unsafe_allow_html=True)
with st.expander("📋 ChatGPT vs Claude vs Gemini vs Copilot"):
    llms = [
        ("ChatGPT (GPT-4o)", "OpenAI", "General purpose, strong coding, web search with plugins.", "Finance report analysis, Python model building, tax research."),
        ("Claude (Anthropic)", "Anthropic", "Very long context (200K tokens), careful reasoning, strong at document analysis.", "Reading full annual reports, contract review, nuanced financial writing."),
        ("Gemini Ultra", "Google", "Multimodal (text+image+audio), strong factual grounding, Google Workspace integration.", "Analysing charts in reports, Google Sheets AI, integrated research."),
        ("Microsoft Copilot", "Microsoft / OpenAI", "Deeply integrated into Microsoft 365 — Word, Excel, Teams, Outlook.", "Excel formula generation, PowerPoint slide drafting, email summarisation."),
        ("Llama 3 / Mistral", "Meta / Mistral AI", "Open-source models — can be run privately on your own infrastructure.", "Sensitive financial data scenarios where data cannot leave the organisation."),
    ]
    for name, provider, strength, finance in llms:
        st.markdown(f"""
        <div class="llm-card">
        <b>{name}</b> &nbsp;<span style="color:#6c757d;font-size:0.8rem">by {provider}</span><br>
        <span style="font-size:0.87rem">{strength}</span><br>
        <span style="font-size:0.82rem;color:#5a4200">💼 Finance: {finance}</span>
        </div>
        """, unsafe_allow_html=True)
    st.warning("⚠️ **Data Privacy Alert:** Do NOT enter confidential client data, MNPI (material non-public information), or sensitive personal data into public LLM interfaces. Use enterprise versions (Microsoft 365 Copilot, Azure OpenAI) which provide data privacy guarantees.")

st.markdown('<div class="section-heading">✍️ Prompt Engineering for Finance</div>', unsafe_allow_html=True)
with st.expander("🎯 How to Get Better Outputs from AI Tools"):
    st.markdown("""
    **Prompt engineering** is the practice of crafting effective instructions to get the best
    output from an LLM. It is arguably the most immediately valuable AI skill for finance professionals.
    """)

    tab1, tab2, tab3 = st.tabs(["📋 Core Techniques", "💼 Finance Prompt Examples", "🧪 Try It Yourself"])

    with tab1:
        techniques = [
            ("1. Be Specific & Detailed", "Vague prompts → vague outputs. Specify format, length, audience, and constraints.", '❌ "Summarise this report" → ✅ "Summarise this annual report in 5 bullet points for a non-finance executive audience, focusing on revenue, profitability, and key risks."'),
            ("2. Assign a Role (System Prompt)", "Tell the model what role to play — this frames its expertise and tone.", '✅ "You are a senior chartered accountant reviewing a client\'s draft financial statements for IFRS compliance. Identify any issues with the revenue recognition policy."'),
            ("3. Provide Context", "Include relevant background that the model needs to answer well.", '✅ "The company uses percentage-of-completion for long-term contracts. Review the following revenue recognition note and flag any IFRS 15 compliance issues..."'),
            ("4. Chain-of-Thought", "Ask the model to reason step-by-step for complex problems.", '✅ "Think step by step: What are the tax implications of this corporate restructuring? First identify the relevant provisions, then analyse each entity, then summarise the overall impact."'),
            ("5. Output Format Instructions", "Specify exactly how you want the answer structured.", '✅ "Return your response as a table with columns: Issue | IFRS Reference | Risk Level (High/Medium/Low) | Recommendation."'),
            ("6. Few-Shot Examples", "Show the model 1–2 examples of the output format you want.", '✅ "Here is an example variance commentary: [example]. Now write a similar commentary for the following data: [data]."'),
        ]
        for title, desc, example in techniques:
            st.markdown(f"**{title}**")
            st.markdown(desc)
            st.markdown(f'<div class="prompt-box">{example}</div>', unsafe_allow_html=True)
            st.markdown("")

    with tab2:
        finance_prompts = {
            "📊 Variance Commentary": 'You are a finance analyst. Write a concise management commentary (max 150 words) explaining the following revenue variances versus budget. Use professional tone suitable for a CFO. Format as short paragraphs.\n\nActual Revenue: $45.2M | Budget: $48.0M | Prior Year: $41.5M\nKey drivers provided: new market launch delayed by 6 weeks, FX headwind of $0.8M, volume growth in core segment +12%.',
            "📋 Contract Risk Summary": 'You are a legal and financial risk analyst. Review the following contract clause and identify: (1) Financial exposure, (2) Key risk, (3) Recommended action. Be concise.\n\n[Paste contract clause here]',
            "🔍 Audit Finding": 'You are a senior auditor. Write a formal audit finding based on the following observation. Include: Criteria, Condition, Cause, Effect (using dollar estimate if possible), and Recommendation.\n\nObservation: [describe finding here]',
            "📈 Excel Formula Help": 'I am building a financial model in Excel. Write a formula to calculate rolling 12-month revenue, where revenue data is in column B (rows 2 to 200) and dates are in column A. The formula should work in cell C13 and be draggable downward.',
            "📝 Tax Research": 'You are a tax adviser specialising in Singapore corporate tax. Explain in plain language whether a Singapore company can deduct the following expense under the Income Tax Act. Cite the relevant section.\n\nExpense: [describe expense]',
        }
        selected_prompt = st.selectbox("Select a finance prompt template:", list(finance_prompts.keys()))
        st.markdown("**Prompt template:**")
        st.code(finance_prompts[selected_prompt], language="text")
        st.info("💡 Copy this template, fill in the bracketed sections with your actual data, and paste into your LLM of choice.")

    with tab3:
        st.markdown("**Build your own finance prompt using best practices:**")
        role = st.selectbox("1. Assign a role:", ["Senior finance analyst", "Chartered accountant", "Tax adviser", "Internal auditor", "FP&A manager", "CFO"])
        task = st.text_input("2. What task do you need done?", placeholder="e.g. Review this P&L for unusual items")
        context = st.text_area("3. Add context:", placeholder="e.g. This is a manufacturing company. The period is Q3 2024. Currency is USD.", height=80)
        output_format = st.selectbox("4. Desired output format:", ["Bullet points", "Table", "Short paragraphs", "Step-by-step", "Executive summary"])
        if st.button("🔧 Generate Prompt"):
            if task:
                prompt = f"""You are a {role}.\n\nTask: {task}\n\nContext: {context if context else 'No additional context provided.'}\n\nProvide your response as {output_format.lower()}. Be concise and professional."""
                st.markdown("**Your generated prompt:**")
                st.code(prompt, language="text")
                st.success("✅ Copy this prompt and use it in ChatGPT, Claude, or Copilot.")
            else: st.warning("Please enter a task description.")

st.markdown('<div class="section-heading">🔍 Retrieval-Augmented Generation (RAG)</div>', unsafe_allow_html=True)
with st.expander("📚 Connecting LLMs to Your Financial Documents"):
    st.markdown("""
    **The Problem:** LLMs have a training cutoff date and don't know your company's specific
    documents, policies, contracts, or financial data.

    **The Solution: RAG (Retrieval-Augmented Generation)**

    RAG combines an LLM with a document retrieval system:

    **How RAG works (step by step):**
    1. **Ingest documents** → Split financial documents into chunks (paragraphs/pages)
    2. **Embed chunks** → Convert each chunk into a numerical embedding vector
    3. **Store in vector database** → ChromaDB, Pinecone, Azure AI Search
    4. **User asks a question** → Query is also embedded
    5. **Retrieve relevant chunks** → Find document chunks with similar embeddings to the query
    6. **Augment the prompt** → Inject retrieved chunks into the LLM context
    7. **LLM generates answer** → Based on the actual document content, not just training memory
    """)
    st.markdown("""
    ```
    User Question
         ↓
    [Embedding Model] → Query Vector
         ↓
    [Vector Database] → Retrieve Top-K Relevant Chunks
         ↓
    [LLM Prompt] = "Answer this question: [question]
                    Using only this context: [retrieved chunks]"
         ↓
    Grounded, Accurate Answer with Source Citations
    ```
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — RAG in Practice</div>
      <div class="finance-lens-body">
        <b>Annual report Q&A:</b> "What was the effective tax rate in 2023 and what drove the change?" →
        RAG retrieves the relevant tax note → LLM answers from the actual document.<br><br>
        <b>Contract search:</b> "Find all contracts with payment terms exceeding 90 days" →
        RAG retrieves matching clauses across 500 contracts.<br><br>
        <b>Policy compliance:</b> "Does this expense claim comply with our T&E policy?" →
        RAG retrieves relevant policy sections → LLM provides a compliant/non-compliant assessment.
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-heading">⚙️ Fine-tuning vs Prompting vs RAG</div>', unsafe_allow_html=True)
with st.expander("🔀 Which Approach Should You Use?"):
    import pandas as pd
    df = pd.DataFrame({
        "Approach": ["Prompting only", "RAG", "Fine-tuning", "Pre-training from scratch"],
        "When to use": ["General tasks, ad-hoc analysis", "Document-specific Q&A, proprietary data", "Consistent style/format, domain terminology", "Very specialised domain with no existing model"],
        "Cost": ["Free/minimal", "Low-Medium", "Medium-High", "Very High ($M+)"],
        "Data needed": ["None", "Your documents", "100–10,000 examples", "Billions of tokens"],
        "Finance example": ["Variance commentary drafting", "Annual report Q&A system", "Custom audit report style", "Bloomberg proprietary model"],
    })
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.info("💡 **For most finance teams:** Start with prompting. Move to RAG when you need to query your own documents. Consider fine-tuning only for consistent, high-volume output generation tasks.")

st.markdown('<div class="section-heading">⚠️ Hallucination — The #1 Risk in Finance AI</div>', unsafe_allow_html=True)
with st.expander("🚨 Understanding and Managing AI Hallucinations"):
    st.markdown("""
    **What is hallucination?**
    LLMs sometimes generate plausible-sounding but **factually incorrect** information — confidently
    presenting invented facts, wrong figures, non-existent regulations, or fabricated citations.

    **Why it happens:**
    LLMs don't "know" facts — they predict statistically likely token sequences. When uncertain,
    they generate text that *sounds* correct rather than admitting ignorance.

    **Hallucination risk by finance task type:**
    """)
    risks = [("🔴 High Risk — Always Verify", ["Specific financial figures", "Tax rates and thresholds", "Regulatory citations and section numbers", "Case law references", "Accounting standard specifics (IFRS/GAAP paragraph numbers)"]),
             ("🟡 Medium Risk — Spot Check", ["Process descriptions", "General regulatory frameworks", "Industry benchmarks", "Historical context"]),
             ("🟢 Lower Risk", ["Drafting and formatting tasks", "Summarising text you provided", "Explaining concepts", "Restructuring information you gave it"]),]
    for category, items in risks:
        st.markdown(f"**{category}**")
        for item in items: st.markdown(f"  - {item}")
    st.error("⛔ **Critical Rule:** Never use an LLM as the source of truth for financial figures, tax rates, or regulatory citations. Always verify against primary sources — legislation, IFRS standards, official publications.")

# Quiz
st.markdown('<div class="section-heading">🧩 Knowledge Check</div>', unsafe_allow_html=True)
st.markdown('<div class="quiz-box">', unsafe_allow_html=True)

questions = [
    {"q": "What is the key difference between Generative AI and traditional Predictive AI?", "options": ["Generative AI is faster", "Generative AI creates new content; Predictive AI classifies or forecasts from existing data", "Predictive AI uses more data", "Generative AI cannot make mistakes"], "answer": "Generative AI creates new content; Predictive AI classifies or forecasts from existing data", "explanation": "Generative AI produces new content (text, images, code). Predictive AI outputs predictions, classifications, or forecasts based on patterns in existing data."},
    {"q": "What does RLHF (Reinforcement Learning from Human Feedback) achieve in LLM training?", "options": ["It makes the model faster", "It teaches the model to follow human preferences for helpful, harmless, honest responses", "It reduces the model's size", "It pre-trains the model on internet data"], "answer": "It teaches the model to follow human preferences for helpful, harmless, honest responses", "explanation": "RLHF uses human rankings of model outputs to train a reward model, which then guides the LLM to produce responses aligned with human preferences — making it more useful and safer."},
    {"q": "A finance team wants to build an AI system that answers questions about their own internal contracts and policies. The MOST appropriate approach is:", "options": ["Pre-train a new LLM from scratch", "Use prompting alone with no documents", "Implement RAG (Retrieval-Augmented Generation)", "Use image generation AI"], "answer": "Implement RAG (Retrieval-Augmented Generation)", "explanation": "RAG connects an LLM to your document database — the model retrieves relevant chunks and answers based on actual document content rather than training memory. Ideal for proprietary internal documents."},
    {"q": "Which prompt engineering technique involves showing the model 1-2 examples of the output format you want before asking it to complete the task?", "options": ["Chain-of-thought prompting", "Zero-shot prompting", "Role assignment", "Few-shot prompting"], "answer": "Few-shot prompting", "explanation": "Few-shot prompting provides examples (shots) of the desired input-output format before the actual task. It's particularly effective for generating consistently formatted outputs like audit findings or variance commentaries."},
    {"q": "A finance manager asks an LLM: 'What is the withholding tax rate on dividends paid to a Singapore resident company?' The LLM gives a confident answer. What should the manager do?", "options": ["Trust the answer — LLMs are always accurate on tax", "Use the answer directly in the tax return", "Verify the answer against IRAS official guidance before using it", "Ask the same question three times and average the answers"], "answer": "Verify the answer against IRAS official guidance before using it", "explanation": "LLMs can hallucinate specific tax rates, thresholds, and regulatory details confidently. Tax-specific figures must always be verified against primary sources — IRAS publications, legislation, or professional advice."},
]

for key in ["m4_q_index","m4_score","m4_answered","m4_selected","m4_quiz_done"]:
    if key not in st.session_state: st.session_state[key] = 0 if "index" in key or "score" in key else False

if not st.session_state.m4_quiz_done:
    q_data = questions[st.session_state.m4_q_index]
    st.markdown(f"**Question {st.session_state.m4_q_index + 1} of {len(questions)}**")
    st.markdown(f"##### {q_data['q']}")
    choice = st.radio("Select your answer:", q_data["options"], key=f"m4_q_{st.session_state.m4_q_index}")
    col_s, col_n = st.columns(2)
    with col_s:
        if st.button("✅ Submit", key=f"m4_sub_{st.session_state.m4_q_index}"):
            st.session_state.m4_answered = True; st.session_state.m4_selected = choice
            if choice == q_data["answer"]: st.session_state.m4_score += 1
    if st.session_state.m4_answered:
        if st.session_state.m4_selected == q_data["answer"]: st.success(f"✅ Correct! {q_data['explanation']}")
        else: st.error(f"❌ Answer: **{q_data['answer']}** — {q_data['explanation']}")
        with col_n:
            if st.session_state.m4_q_index < len(questions)-1:
                if st.button("Next ➡️", key=f"m4_next_{st.session_state.m4_q_index}"):
                    st.session_state.m4_q_index += 1; st.session_state.m4_answered = False; st.rerun()
            else:
                if st.button("🏁 Results"): st.session_state.m4_quiz_done = True; st.rerun()
else:
    s,t = st.session_state.m4_score, len(questions); pct = int((s/t)*100)
    st.markdown(f"### {'🏆' if pct>=80 else '👍' if pct>=60 else '📚'} Score: {s}/{t} ({pct}%)")
    st.progress(pct/100)
    st.info("Excellent Gen AI knowledge!" if pct>=80 else "Good — review RAG and hallucination sections." if pct>=60 else "Revisit the LLM and prompt engineering sections.")
    if st.button("🔄 Retry"):
        for k,v in [("m4_q_index",0),("m4_score",0),("m4_answered",False),("m4_selected",None),("m4_quiz_done",False)]: st.session_state[k]=v
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-heading">💡 Key Takeaways</div>', unsafe_allow_html=True)
for i,t in enumerate(["**Generative AI** creates new content; all current tools (ChatGPT, Claude, Copilot) are transformer-based LLMs trained via pre-training + RLHF.","**Prompt engineering** is the most immediately valuable AI skill — specificity, role assignment, chain-of-thought, and output format instructions dramatically improve results.","**RAG** connects LLMs to your own documents — essential for building AI tools on internal financial data.","**Hallucination** is the #1 finance risk — always verify specific figures, tax rates, and regulatory citations against primary sources.","Choose **prompting** for general tasks, **RAG** for document Q&A, **fine-tuning** for consistent style — pre-training is rarely needed.","**Data privacy** is critical — use enterprise versions (Microsoft 365 Copilot, Azure OpenAI) for sensitive financial data."],1):
    st.markdown(f"**{i}.** {t}")

st.markdown("---")
col1,col2,col3 = st.columns(3)
with col1:
    if st.button("⬅️ M3: Deep Learning", use_container_width=True): st.info("Navigate to Module 3 from the sidebar.")
with col2: st.markdown("<div style='text-align:center;padding-top:0.4rem'>💜 Module 4 of 8</div>", unsafe_allow_html=True)
with col3:
    if st.button("M5: AI in Finance ➡️", use_container_width=True): st.info("Navigate to Module 5 from the sidebar.")
st.caption("Knowledge Folder · AI Series · Module 4 — Generative AI & LLMs · © 2025")