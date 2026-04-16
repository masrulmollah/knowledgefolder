import streamlit as st

# ── NO st.set_page_config() here — already called in Homepage ──────────────

st.markdown("""
<style>
.hero-banner { background: linear-gradient(135deg, #0b132b 0%, #1c2951 50%, #2d4a8a 100%); padding: 2.5rem 2rem; border-radius: 16px; margin-bottom: 1.5rem; border-left: 6px solid #4fc3f7; }
.hero-title { font-size: 2rem; font-weight: 800; color: #ffffff; margin: 0 0 0.4rem 0; }
.hero-subtitle { font-size: 1.05rem; color: #a8b2d8; margin: 0; }
.hero-badge { display: inline-block; background: #4fc3f7; color: #0b132b; font-size: 0.75rem; font-weight: 700; padding: 0.2rem 0.7rem; border-radius: 20px; margin-bottom: 0.8rem; text-transform: uppercase; }
.progress-container { background: #e9ecef; border-radius: 20px; height: 10px; margin: 0.3rem 0 0.5rem 0; }
.progress-bar { background: linear-gradient(90deg, #4fc3f7, #2d4a8a); height: 10px; border-radius: 20px; width: 37.5%; }
.progress-label { font-size: 0.78rem; color: #6c757d; margin-bottom: 0.2rem; }
.stat-card { background: white; border: 1px solid #dee2e6; border-radius: 12px; padding: 1.2rem; text-align: center; box-shadow: 0 2px 6px rgba(0,0,0,0.06); }
.stat-number { font-size: 1.8rem; font-weight: 800; color: #2d4a8a; }
.stat-label { font-size: 0.78rem; color: #6c757d; margin-top: 0.2rem; }
.finance-lens { background: linear-gradient(135deg, #fff3cd, #fff8e1); border: 1px solid #ffc107; border-left: 5px solid #f5a623; border-radius: 10px; padding: 1rem 1.2rem; margin: 0.5rem 0; }
.finance-lens-title { font-size: 0.85rem; font-weight: 700; color: #856404; text-transform: uppercase; letter-spacing: 0.05em; margin-bottom: 0.4rem; }
.finance-lens-body { font-size: 0.88rem; color: #5a4200; line-height: 1.6; }
.section-heading { font-size: 1.15rem; font-weight: 700; color: #1a1a2e; border-bottom: 2px solid #4fc3f7; padding-bottom: 0.3rem; margin: 1.5rem 0 1rem 0; }
.layer-box { background: #e8f4f8; border: 1px solid #4fc3f7; border-radius: 8px; padding: 0.7rem 1rem; margin: 0.3rem 0; text-align: center; font-weight: 600; font-size: 0.9rem; }
.quiz-box { background: #f0f4ff; border: 1px solid #c5d0f5; border-radius: 12px; padding: 1.2rem 1.4rem; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-banner">
  <div class="hero-badge">📘 Module 3 of 8 &nbsp;|&nbsp; AI Series</div>
  <div class="hero-title">Deep Learning & Neural Networks</div>
  <div class="hero-subtitle">Demystify the "black box" — understand how neural networks learn,
  what transformers are, and how these power the document AI and LLM tools reshaping finance.</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="progress-label">Series progress — Module 3 of 8</div>', unsafe_allow_html=True)
st.markdown('<div class="progress-container"><div class="progress-bar"></div></div>', unsafe_allow_html=True)

c1,c2,c3,c4 = st.columns(4)
with c1: st.markdown('<div class="stat-card"><div class="stat-number">6</div><div class="stat-label">Network Types</div></div>', unsafe_allow_html=True)
with c2: st.markdown('<div class="stat-card"><div class="stat-number">~35</div><div class="stat-label">Min Read Time</div></div>', unsafe_allow_html=True)
with c3: st.markdown('<div class="stat-card"><div class="stat-number">1950s</div><div class="stat-label">Neural Net Origin</div></div>', unsafe_allow_html=True)
with c4: st.markdown('<div class="stat-card"><div class="stat-number">5</div><div class="stat-label">Quiz Questions</div></div>', unsafe_allow_html=True)
st.markdown("")

with st.sidebar:
    st.markdown("### 🤖 AI Series — Modules")
    modules = [("1","Foundations of AI",False),("2","Machine Learning Essentials",False),("3","Deep Learning & Neural Networks",True),("4","Generative AI & LLMs",False),("5","AI in Finance & Accounting",False),("6","Building AI Models",False),("7","AI Ethics, Risk & Governance",False),("8","Future of AI & Career Readiness",False)]
    for num, name, active in modules:
        st.markdown(f"**▶ M{num} — {name}** ✅" if active else f"M{num} — {name}")
    st.markdown("---")
    st.info("💡 M2 (Machine Learning) is a helpful prerequisite.")

st.markdown('<div class="section-heading">🧠 What is a Neural Network?</div>', unsafe_allow_html=True)
with st.expander("📖 The Brain Metaphor — And Where It Breaks Down", expanded=True):
    st.markdown("""
    A **neural network** is a computational model loosely inspired by how biological neurons in the
    brain connect and signal each other. It consists of layers of interconnected **nodes (neurons)**
    that transform input data into an output prediction.

    **The three layer types:**
    """)
    st.markdown('<div class="layer-box">🟢 Input Layer — receives raw data (e.g. invoice amount, customer age, transaction type)</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-size:1.5rem">↓</div>', unsafe_allow_html=True)
    st.markdown('<div class="layer-box" style="background:#d4edff">🔵 Hidden Layers — learn increasingly abstract representations of the data</div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center;font-size:1.5rem">↓</div>', unsafe_allow_html=True)
    st.markdown('<div class="layer-box" style="background:#d4f0d4">🟩 Output Layer — produces the final prediction (e.g. fraud probability, document category)</div>', unsafe_allow_html=True)
    st.markdown("""

    **How a neuron works:**
    1. Receives inputs from the previous layer
    2. Multiplies each input by a **weight** (how important is this input?)
    3. Sums the weighted inputs and adds a **bias**
    4. Applies an **activation function** to introduce non-linearity
    5. Passes the result to the next layer

    **Deep Learning** = neural networks with *many* hidden layers (typically 3+).
    The "deep" refers to depth of layers, not profundity!
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens</div>
      <div class="finance-lens-body">
        A fraud detection neural network might have: Input layer (30 transaction features) →
        Hidden layer 1 (learns basic patterns: large amounts, unusual merchants) →
        Hidden layer 2 (learns combinations: large amount + overseas + new device) →
        Output layer (fraud probability: 0.94 — flag this transaction).
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-heading">⚡ How Neural Networks Learn — Backpropagation</div>', unsafe_allow_html=True)
with st.expander("🔄 Training: Forward Pass → Loss → Backward Pass → Update"):
    st.markdown("""
    Neural networks learn by repeatedly adjusting their **weights** to reduce prediction errors:

    **Step 1 — Forward Pass:**
    Data flows through the network layer by layer. The network makes a prediction.

    **Step 2 — Loss Calculation:**
    The prediction is compared to the actual answer. The difference is the **loss** (error).
    *Example: Predicted default probability = 0.2, but the loan actually defaulted (label = 1). Loss is high.*

    **Step 3 — Backpropagation:**
    The error signal travels backwards through the network. Using calculus (chain rule),
    each weight's contribution to the error is calculated — this is the **gradient**.

    **Step 4 — Weight Update (Gradient Descent):**
    Each weight is adjusted slightly in the direction that reduces the loss.
    The size of the step is controlled by the **learning rate**.

    **Step 5 — Repeat:**
    This cycle repeats thousands of times across the full training dataset until the loss
    is minimised — the network has "learned."
    """)
    st.info("💡 **Analogy:** Imagine adjusting the dials on a complex mixing desk — backpropagation tells you which dial to turn and by how much, to get the output sound you want.")
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — Why Learning Rate Matters</div>
      <div class="finance-lens-body">
        Too high a learning rate → model overshoots, never converges (like overcorrecting a financial
        forecast every time it misses by a tiny amount). Too low → training takes forever.
        This hyperparameter tuning is why data scientists iterate extensively before deploying
        a financial model.
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-heading">🔧 Activation Functions</div>', unsafe_allow_html=True)
with st.expander("⚙️ Why Non-Linearity Matters"):
    st.markdown("""
    Activation functions introduce **non-linearity** into the network. Without them, stacking
    many layers would be mathematically equivalent to a single linear transformation — no
    matter how deep, the network couldn't learn complex patterns.

    | Activation | Formula (simplified) | Output Range | Best Used For |
    |-----------|---------------------|--------------|---------------|
    | **ReLU** | max(0, x) | 0 to ∞ | Hidden layers — most common, fast |
    | **Sigmoid** | 1/(1+e⁻ˣ) | 0 to 1 | Output layer — binary classification (fraud yes/no) |
    | **Softmax** | eˣⁱ / Σeˣ | 0 to 1, sums to 1 | Output — multi-class (document type A/B/C) |
    | **Tanh** | (eˣ−e⁻ˣ)/(eˣ+e⁻ˣ) | -1 to 1 | Hidden layers in RNNs |
    | **GELU** | smooth ReLU variant | -∞ to ∞ | Transformer models (BERT, GPT) |
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens</div>
      <div class="finance-lens-body">
        The <b>Sigmoid</b> activation function is why a fraud model outputs a probability between
        0 and 1 rather than raw numbers. A score of 0.93 means "93% likely to be fraud" —
        directly usable as a risk threshold for your operations team.
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-heading">🏗️ Types of Neural Networks</div>', unsafe_allow_html=True)
with st.expander("🌐 CNN, RNN, LSTM, Transformer — Which Does What?"):
    tab1, tab2, tab3, tab4 = st.tabs(["🖼️ CNN", "🔄 RNN / LSTM", "⚡ Transformer", "🔢 Autoencoder"])
    with tab1:
        st.markdown("""
        ### Convolutional Neural Network (CNN)
        Originally designed for image recognition. Learns **spatial patterns** by sliding filters
        across the input — detecting edges, shapes, and textures in images; characters and layouts in documents.

        **Architecture:** Input → Convolutional Layers (feature detection) → Pooling Layers (dimensionality reduction) → Fully Connected Layers → Output

        **Finance applications:**
        - 📄 **Document classification** — scanning invoices, receipts, financial statements
        - 🔍 **OCR and data extraction** — reading amounts, dates, account numbers from scanned documents
        - 📊 **Chart pattern recognition** — detecting chart patterns in technical analysis
        - 🪪 **KYC document verification** — validating identity documents
        """)
        st.markdown("""
        <div class="finance-lens">
          <div class="finance-lens-title">💼 Finance Lens</div>
          <div class="finance-lens-body">
            When your AP automation software "reads" a scanned invoice and extracts the vendor name,
            invoice number, and amount — a CNN is doing the heavy lifting. Tools like ABBYY, Rossum,
            and AWS Textract use CNN-based architectures.
          </div>
        </div>
        """, unsafe_allow_html=True)
    with tab2:
        st.markdown("""
        ### Recurrent Neural Network (RNN) & LSTM
        Designed for **sequential data** — where order matters. Unlike CNNs, RNNs have a
        "memory" of previous inputs via hidden state.

        **RNN limitation:** Struggles with long sequences — forgets distant context (vanishing gradient problem).

        **LSTM (Long Short-Term Memory):** Solves this with **gates** that control what to remember
        and forget over long sequences.

        **Finance applications:**
        - 📈 **Time series forecasting** — revenue, cash flow, stock prices
        - 💰 **Transaction sequence modelling** — understanding spending patterns over time
        - 📝 **Sentiment analysis** — reading earnings call transcripts sequentially
        - ⚠️ **Fraud sequence detection** — catching multi-step fraud across transactions
        """)
        st.markdown("""
        <div class="finance-lens">
          <div class="finance-lens-title">💼 Finance Lens</div>
          <div class="finance-lens-body">
            An LSTM trained on monthly revenue, expense, and macroeconomic data can forecast
            next quarter's cash flow — capturing seasonality, trends, and multi-period dependencies
            that simple regression misses. Many FP&A platforms use LSTM-based forecasting engines.
          </div>
        </div>
        """, unsafe_allow_html=True)
    with tab3:
        st.markdown("""
        ### Transformer — The Architecture Behind Modern AI
        Introduced in the landmark 2017 paper *"Attention Is All You Need"*, the Transformer
        architecture revolutionised AI. It processes entire sequences in **parallel** (not step-by-step
        like RNNs) using a mechanism called **Self-Attention**.

        **Self-Attention:** For each word/token, the model learns how much attention to pay to every
        other word in the sequence — capturing long-range dependencies efficiently.

        **Key components:**
        - **Encoder** — reads and understands input (used in BERT)
        - **Decoder** — generates output token by token (used in GPT)
        - **Encoder-Decoder** — translation and summarisation (T5, BART)

        **Why it matters:** GPT-4, Claude, Gemini, BERT — all are transformer-based.
        The transformer IS the foundation of the generative AI revolution.

        **Finance applications:**
        - 📋 **Contract and document understanding** — reading complex legal/financial text
        - 📊 **Earnings call analysis** — extracting sentiment, guidance, risk factors
        - 🔍 **Financial report question answering** — "What was the EBITDA growth rate?"
        - 📝 **Regulatory filing analysis** — parsing XBRL, 10-K, annual reports
        """)
        st.markdown("""
        <div class="finance-lens">
          <div class="finance-lens-title">💼 Finance Lens</div>
          <div class="finance-lens-body">
            When you ask Microsoft Copilot to "summarise the key risks in this 80-page annual report"
            and it gives you a coherent 5-bullet summary in 10 seconds — that is a transformer model
            processing the entire document using self-attention to identify the most relevant passages.
          </div>
        </div>
        """, unsafe_allow_html=True)
    with tab4:
        st.markdown("""
        ### Autoencoder
        A network trained to **compress** input data into a compact representation (encoding),
        then **reconstruct** it back to the original. The bottleneck layer captures the most
        essential features.

        **Architecture:** Input → Encoder (compresses) → Bottleneck (latent space) → Decoder (reconstructs) → Output

        **Key property:** Trained only on normal data. When anomalous data is fed in, reconstruction
        error is high — revealing the anomaly.

        **Finance applications:**
        - 🔍 **Unsupervised fraud detection** — anomalous transactions have high reconstruction error
        - 📊 **Journal entry anomaly detection** in audit (no fraud labels needed)
        - 🗜️ **Dimensionality reduction** — compressing financial features for downstream models
        """)

st.markdown('<div class="section-heading">🔤 Key Deep Learning Concepts</div>', unsafe_allow_html=True)
with st.expander("📚 Embeddings, Tokenisation, Attention — Explained"):
    st.markdown("""
    **Tokenisation**
    Before text enters a language model, it must be converted to numbers. Tokenisation splits
    text into **tokens** (roughly sub-words) and maps each to an integer ID.
    *"Balance sheet" → [token 8234, token 3917]*

    ---
    **Embeddings**
    Tokens are mapped to dense numerical vectors (embeddings) in a high-dimensional space.
    Words with similar meanings land near each other in this space.
    *"Revenue" and "Sales" will have similar embedding vectors. "Invoice" and "Receipt" likewise.*

    ---
    **Attention Mechanism**
    For each token, attention computes a weighted sum of all other tokens' representations,
    where weights reflect relevance. This allows the model to consider full context.
    *When processing "the profit margin improved this quarter", attention links "margin" to "profit"
    and "quarter" to "this" — capturing the relationship across the sentence.*

    ---
    **Pre-training and Fine-tuning**
    - **Pre-training:** Train on massive text corpora (the entire internet) to learn language patterns
    - **Fine-tuning:** Further train on domain-specific data (financial documents, earnings calls)
      to improve performance on finance tasks
    """)
    st.markdown("""
    <div class="finance-lens">
      <div class="finance-lens-title">💼 Finance Lens — Why Embeddings Matter</div>
      <div class="finance-lens-body">
        Financial document search and retrieval uses embeddings. When you ask an AI "find all
        contracts with change of control clauses", it converts your query to an embedding vector
        and finds document chunks with similar vectors — even if the exact words differ.
        This is called Retrieval-Augmented Generation (RAG), covered in Module 4.
      </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-heading">⚠️ Deep Learning Challenges</div>', unsafe_allow_html=True)
with st.expander("🚧 Limitations Finance Professionals Must Know"):
    challenges = [
        ("🔲 Black Box Problem", "Deep neural networks are difficult to interpret. You cannot easily explain why a model made a specific prediction — a major challenge for regulated financial applications.", "Explainability requirements under GDPR, SR 11-7, and fair lending laws mean pure deep learning models may require post-hoc explanation tools (SHAP, LIME) or simpler surrogate models for credit decisions."),
        ("📦 Data Hunger", "Deep learning requires large amounts of high-quality training data. Performance degrades significantly with limited data.", "Many finance teams don't have millions of labelled examples of fraud or default. Gradient Boosting often outperforms deep learning on small–medium tabular financial datasets."),
        ("💻 Computational Cost", "Training large neural networks requires expensive GPU hardware and significant energy consumption.", "Training GPT-4 cost an estimated $100M+. Fine-tuning smaller models for specific financial tasks is far more cost-effective."),
        ("🎲 Hallucination", "Generative models can produce confident, fluent, but factually incorrect outputs.", "A critical risk in financial applications. Never use LLM output for financial figures without verification against authoritative source data."),
        ("📉 Distribution Shift", "A model trained on pre-2020 data may perform poorly during a financial crisis or regime change.", "Models must be continuously monitored and retrained as economic conditions evolve — a key model risk management requirement."),
    ]
    for icon_title, desc, finance in challenges:
        st.markdown(f"**{icon_title}**")
        st.markdown(desc)
        st.markdown(f"""<div class="finance-lens"><div class="finance-lens-title">💼 Finance Lens</div><div class="finance-lens-body">{finance}</div></div>""", unsafe_allow_html=True)
        st.divider()

# Quiz
st.markdown('<div class="section-heading">🧩 Knowledge Check</div>', unsafe_allow_html=True)
st.markdown('<div class="quiz-box">', unsafe_allow_html=True)

questions = [
    {"q": "Which component of a neural network introduces non-linearity, allowing it to learn complex patterns?", "options": ["Weight matrix", "Activation function", "Loss function", "Learning rate"], "answer": "Activation function", "explanation": "Activation functions like ReLU and Sigmoid introduce non-linearity. Without them, stacking layers would still produce only linear transformations."},
    {"q": "Which neural network architecture is best suited for understanding sequential financial data, such as monthly cash flow over 3 years?", "options": ["CNN", "Autoencoder", "LSTM", "Simple perceptron"], "answer": "LSTM", "explanation": "LSTM (Long Short-Term Memory) is designed for sequential data where order and long-range dependencies matter — ideal for time series like cash flows."},
    {"q": "The Transformer architecture's key innovation was:", "options": ["Using more hidden layers than previous networks", "Processing sequences using the self-attention mechanism", "Removing the need for training data", "Using convolutional filters on text"], "answer": "Processing sequences using the self-attention mechanism", "explanation": "Self-attention allows transformers to capture relationships between all tokens simultaneously, enabling parallel processing and long-range dependency modelling."},
    {"q": "A deep learning model for credit decisions is challenged by regulators who ask 'why was this application rejected?' This relates to which limitation?", "options": ["Data hunger", "Distribution shift", "The black box problem", "Computational cost"], "answer": "The black box problem", "explanation": "Deep neural networks are difficult to interpret. Regulators and fair lending laws require explainable decisions — deep learning models need post-hoc explainability tools or simpler alternatives for credit decisions."},
    {"q": "An autoencoder trained on normal journal entries is given an unusual journal entry. The reconstruction error is very high. This suggests:", "options": ["The model needs retraining", "The journal entry is likely anomalous — a potential audit flag", "The model has underfitted the data", "The learning rate was too high"], "answer": "The journal entry is likely anomalous — a potential audit flag", "explanation": "Autoencoders learn to reconstruct normal patterns well. High reconstruction error on new data indicates it doesn't match the learned normal pattern — a useful unsupervised anomaly detection signal for audit."},
]

for key in ["m3_q_index","m3_score","m3_answered","m3_selected","m3_quiz_done"]:
    if key not in st.session_state: st.session_state[key] = 0 if "index" in key or "score" in key else False

if not st.session_state.m3_quiz_done:
    q_data = questions[st.session_state.m3_q_index]
    st.markdown(f"**Question {st.session_state.m3_q_index + 1} of {len(questions)}**")
    st.markdown(f"##### {q_data['q']}")
    choice = st.radio("Select your answer:", q_data["options"], key=f"m3_q_{st.session_state.m3_q_index}")
    col_s, col_n = st.columns(2)
    with col_s:
        if st.button("✅ Submit", key=f"m3_sub_{st.session_state.m3_q_index}"):
            st.session_state.m3_answered = True; st.session_state.m3_selected = choice
            if choice == q_data["answer"]: st.session_state.m3_score += 1
    if st.session_state.m3_answered:
        if st.session_state.m3_selected == q_data["answer"]: st.success(f"✅ Correct! {q_data['explanation']}")
        else: st.error(f"❌ Answer: **{q_data['answer']}** — {q_data['explanation']}")
        with col_n:
            if st.session_state.m3_q_index < len(questions)-1:
                if st.button("Next ➡️", key=f"m3_next_{st.session_state.m3_q_index}"):
                    st.session_state.m3_q_index += 1; st.session_state.m3_answered = False; st.rerun()
            else:
                if st.button("🏁 Results"):
                    st.session_state.m3_quiz_done = True; st.rerun()
else:
    s,t = st.session_state.m3_score, len(questions); pct = int((s/t)*100)
    st.markdown(f"### {'🏆' if pct>=80 else '👍' if pct>=60 else '📚'} Score: {s}/{t} ({pct}%)")
    st.progress(pct/100)
    st.info("Excellent!" if pct>=80 else "Good — review transformer and LSTM sections." if pct>=60 else "Revisit the network types and re-attempt.")
    if st.button("🔄 Retry"):
        for k,v in [("m3_q_index",0),("m3_score",0),("m3_answered",False),("m3_selected",None),("m3_quiz_done",False)]: st.session_state[k]=v
        st.rerun()
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-heading">💡 Key Takeaways</div>', unsafe_allow_html=True)
for i,t in enumerate(["Neural networks learn by adjusting **weights** through backpropagation — minimising prediction error iteratively.","**CNNs** excel at document and image processing; **LSTMs** at time series; **Transformers** at language understanding — all relevant in finance.","The **Transformer and self-attention mechanism** is the architecture underpinning ChatGPT, Claude, Copilot, and all modern LLMs.","**Deep learning requires large data**, significant compute, and careful validation — not always the best choice for small financial datasets.","The **black box problem** is a real governance constraint — explainability tools (SHAP, LIME) are often required for regulated financial model deployments.","**Hallucination** in language models is a critical risk — never use AI-generated financial figures without verification."],1):
    st.markdown(f"**{i}.** {t}")

st.markdown("---")
col1,col2,col3 = st.columns(3)
with col1:
    if st.button("⬅️ M2: Machine Learning", use_container_width=True): st.info("Navigate to Module 2 from the sidebar.")
with col2: st.markdown("<div style='text-align:center;padding-top:0.4rem'>📘 Module 3 of 8</div>", unsafe_allow_html=True)
with col3:
    if st.button("M4: Generative AI ➡️", use_container_width=True): st.info("Navigate to Module 4 from the sidebar.")
st.caption("Knowledge Folder · AI Series · Module 3 — Deep Learning & Neural Networks · © 2025")