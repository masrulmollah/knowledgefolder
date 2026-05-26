import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

def show():
    st.title("📊 Statistics for Finance Professionals — Complete Course Overview")
    st.markdown("*Your comprehensive guide to all 12 modules — summaries, formulas, and interactive review tools*")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "🗺️ Course Map", "📖 Module Summaries", "🧮 Formula Bank",
        "📊 Visual Dashboard", "✅ Master Quiz", "🎓 Study Planner"
    ])

    # ══════════════════════════════════════════════════════════════════
    with tab1:
        st.header("🗺️ Course Map — 12 Modules at a Glance")

        st.markdown("""
        ### Welcome to Statistics for Finance Professionals
        This course transforms you from a beginner to an **expert** in statistical analysis for finance.
        Below is your complete learning roadmap across **12 comprehensive modules**.
        """)

        # Module cards
        modules_info = [
            {"num": 1, "title": "Foundations of Statistics",
             "icon": "📊", "color": "#2E86C1",
             "topics": ["Data Types", "Descriptive Statistics", "Mean/Median/Mode", "Variance & Std Dev", "Skewness & Kurtosis"],
             "key_skill": "Summarize and describe any dataset", "difficulty": "Beginner"},

            {"num": 2, "title": "Probability Theory",
             "icon": "🎲", "color": "#27AE60",
             "topics": ["Probability Rules", "Bayes' Theorem", "Distributions", "Normal Distribution", "Binomial & Poisson"],
             "key_skill": "Calculate probabilities and use distributions", "difficulty": "Beginner"},

            {"num": 3, "title": "Statistical Inference",
             "icon": "🔍", "color": "#8E44AD",
             "topics": ["Sampling Methods", "Confidence Intervals", "Hypothesis Testing", "t-tests", "Type I & II Errors"],
             "key_skill": "Test hypotheses and build confidence intervals", "difficulty": "Intermediate"},

            {"num": 4, "title": "Regression Analysis",
             "icon": "📈", "color": "#E67E22",
             "topics": ["Simple Linear Regression", "Multiple Regression", "OLS Method", "R-squared", "Model Diagnostics"],
             "key_skill": "Build and interpret regression models", "difficulty": "Intermediate"},

            {"num": 5, "title": "Time Series Analysis",
             "icon": "⏱️", "color": "#E74C3C",
             "topics": ["Stationarity", "ACF/PACF", "ARIMA Models", "GARCH Volatility", "Forecasting"],
             "key_skill": "Forecast financial time series", "difficulty": "Intermediate"},

            {"num": 6, "title": "Portfolio Statistics",
             "icon": "💼", "color": "#1ABC9C",
             "topics": ["Portfolio Return/Risk", "Correlation", "Efficient Frontier", "Sharpe Ratio", "Diversification"],
             "key_skill": "Optimize portfolios using statistics", "difficulty": "Intermediate"},

            {"num": 7, "title": "Risk Analytics",
             "icon": "⚠️", "color": "#C0392B",
             "topics": ["Value at Risk (VaR)", "CVaR/Expected Shortfall", "Stress Testing", "Risk Decomposition", "Max Drawdown"],
             "key_skill": "Measure and manage financial risk", "difficulty": "Advanced"},

            {"num": 8, "title": "Advanced Statistical Methods",
             "icon": "🔬", "color": "#7D3C98",
             "topics": ["PCA", "Non-Parametric Tests", "Bayesian Statistics", "Bootstrap Methods", "Spearman Correlation"],
             "key_skill": "Apply advanced techniques beyond basics", "difficulty": "Advanced"},

            {"num": 9, "title": "Machine Learning for Finance",
             "icon": "🤖", "color": "#117A65",
             "topics": ["Supervised Learning", "Classification & Regression", "Random Forest", "Model Evaluation", "Overfitting"],
             "key_skill": "Build predictive ML models", "difficulty": "Advanced"},

            {"num": 10, "title": "Business Analytics Applications",
             "icon": "💡", "color": "#D68910",
             "topics": ["Customer Segmentation", "CLV", "Churn Prediction", "A/B Testing", "Sales Forecasting"],
             "key_skill": "Solve real business problems with analytics", "difficulty": "Advanced"},

            {"num": 11, "title": "Tools and Software",
             "icon": "🛠️", "color": "#2874A6",
             "topics": ["Excel for Analytics", "Python & R", "SQL for Data", "Tableau & Power BI", "Cloud Platforms"],
             "key_skill": "Master essential analytics tools", "difficulty": "Intermediate"},

            {"num": 12, "title": "Case Studies and Projects",
             "icon": "🎯", "color": "#229954",
             "topics": ["Real-World Applications", "Portfolio Projects", "Credit Risk Modeling", "End-to-End Analysis", "Communication"],
             "key_skill": "Execute complete analytics projects", "difficulty": "Expert"},
        ]

        # Display in rows of 3
        difficulty_colors = {"Beginner": "🟢", "Intermediate": "🟡", "Advanced": "🟠", "Expert": "🔴"}

        for row_start in range(0, len(modules_info), 3):
            cols = st.columns(3)
            for col_idx, mod in enumerate(modules_info[row_start:row_start+3]):
                with cols[col_idx]:
                    difficulty_icon = difficulty_colors.get(mod["difficulty"], "⚪")
                    st.markdown(f"""
                    <div style="background-color:{mod['color']}22; border-left:5px solid {mod['color']};
                    padding:12px; border-radius:8px; margin-bottom:8px; min-height:200px;">
                    <h4 style="color:{mod['color']}; margin:0;">{mod['icon']} Module {mod['num']}</h4>
                    <strong>{mod['title']}</strong><br>
                    <small>{difficulty_icon} {mod['difficulty']}</small><br><br>
                    <small>🔑 <em>{mod['key_skill']}</em></small>
                    </div>
                    """, unsafe_allow_html=True)

        st.markdown("---")
        st.subheader("📈 Learning Progression")

        learning_path = pd.DataFrame({
            "Phase": ["Phase 1: Foundations", "Phase 2: Core Methods", "Phase 3: Advanced Analytics", "Phase 4: Applied Finance"],
            "Modules": ["1 – 3", "4 – 7", "8 – 10", "11 – 12"],
            "Focus": ["Statistics basics, Probability, Inference", "Regression, Time Series, Portfolio, Risk", "PCA, ML, Business Analytics", "Tools, Projects, Real-world"],
            "Duration": ["~2 weeks", "~4 weeks", "~4 weeks", "~4 weeks"]
        })
        st.dataframe(learning_path, use_container_width=True, hide_index=True)

        st.subheader("🎓 Professional Certifications & Applications")
        cert_df = pd.DataFrame({
            "Role/Certification": ["CFA (Chartered Financial Analyst)", "FRM (Financial Risk Manager)", "Data Analyst", "Quantitative Analyst"],
            "Modules Most Relevant": [
                "Modules 1-7, 11 — Quantitative Methods and Portfolio Management",
                "Modules 1-3, 6-7 — Risk Analytics and Statistical Methods",
                "All modules — comprehensive statistical and analytics training",
                "Modules 4-9, 11 — Advanced statistics, ML, and programming"
            ],
            "Coverage": ["~60% of Quant section", "~75% of statistical methods", "~100% comprehensive", "~85% of core skills"]
        })
        st.dataframe(cert_df, use_container_width=True, hide_index=True)

    # ══════════════════════════════════════════════════════════════════
    with tab2:
        st.header("📖 Module Summaries — Quick Reference Guide")

        module_summaries = {
            1: {
                "title": "Foundations of Statistics",
                "summary": "Master the fundamentals of descriptive statistics. Learn to classify data types, calculate measures of central tendency and dispersion, and understand distribution shapes.",
                "key_concepts": ["Data types (nominal, ordinal, interval, ratio)", "Mean, median, mode", "Variance and standard deviation", "Skewness and kurtosis", "Box plots and histograms"],
                "formulas": ["σ² = Σ(x - μ)² / N", "Skewness = E[(X-μ)³] / σ³"],
                "applications": ["Portfolio return analysis", "Risk measurement", "Data quality assessment"]
            },
            2: {
                "title": "Probability Theory",
                "summary": "Build foundation in probability theory. Master probability rules, conditional probability, Bayes' theorem, and key probability distributions used in finance.",
                "key_concepts": ["Addition and multiplication rules", "Conditional probability", "Bayes' theorem", "Binomial, Poisson, Normal distributions", "Expected value and variance"],
                "formulas": ["P(A|B) = P(A∩B) / P(B)", "P(A|B) = P(B|A)×P(A) / P(B)", "E[X] = Σ x·P(x)"],
                "applications": ["Credit default probability", "Options pricing foundations", "Risk modeling"]
            },
            3: {
                "title": "Statistical Inference",
                "summary": "Learn to make inferences from samples to populations. Master confidence intervals, hypothesis testing, and understand Type I and Type II errors.",
                "key_concepts": ["Sampling distributions", "Central Limit Theorem", "Confidence intervals (z and t)", "Hypothesis testing (one-sample, two-sample)", "p-values and significance"],
                "formulas": ["CI = x̄ ± z(σ/√n)", "t = (x̄ - μ) / (s/√n)"],
                "applications": ["Testing trading strategies", "Comparing fund performance", "Quality control"]
            },
            4: {
                "title": "Regression Analysis",
                "summary": "Build predictive models using regression. Understand OLS estimation, interpret coefficients, assess model fit, and diagnose problems.",
                "key_concepts": ["Simple linear regression", "Multiple regression", "OLS estimation", "R-squared and adjusted R-squared", "Residual analysis"],
                "formulas": ["Y = β₀ + β₁X + ε", "β₁ = Cov(X,Y) / Var(X)", "R² = 1 - (SSR/SST)"],
                "applications": ["CAPM beta estimation", "Factor models", "Return prediction"]
            },
            5: {
                "title": "Time Series Analysis",
                "summary": "Analyze and forecast time-dependent data. Master stationarity, ARIMA models, volatility modeling with GARCH, and forecast evaluation.",
                "key_concepts": ["Stationarity (ADF test)", "ACF and PACF", "ARIMA(p,d,q) models", "GARCH volatility models", "Forecast accuracy"],
                "formulas": ["AR(1): Y_t = φ₁Y_{t-1} + ε_t", "GARCH(1,1): σ²_t = ω + αε²_{t-1} + βσ²_{t-1}"],
                "applications": ["Stock price forecasting", "Volatility prediction", "Economic indicators"]
            },
            6: {
                "title": "Portfolio Statistics",
                "summary": "Apply statistics to portfolio management. Calculate portfolio risk/return, construct efficient frontiers, and understand diversification benefits.",
                "key_concepts": ["Portfolio return/risk formulas", "Correlation and covariance", "Efficient frontier", "Sharpe ratio", "Diversification benefits"],
                "formulas": ["σₚ² = Σᵢ Σⱼ wᵢwⱼσᵢσⱼρᵢⱼ", "Sharpe = (Rₚ - Rf) / σₚ"],
                "applications": ["Portfolio optimization", "Asset allocation", "Risk budgeting"]
            },
            7: {
                "title": "Risk Analytics",
                "summary": "Measure and manage financial risk. Calculate VaR using multiple methods, understand CVaR, stress testing, and risk decomposition.",
                "key_concepts": ["Value at Risk (VaR)", "Conditional VaR (CVaR)", "Parametric vs Historical vs Monte Carlo", "Stress testing", "Maximum drawdown"],
                "formulas": ["VaR = -(μ - z_α × σ) × V", "CVaR = E[Loss | Loss > VaR]"],
                "applications": ["Risk limits", "Regulatory capital", "Risk reporting"]
            },
            8: {
                "title": "Advanced Statistical Methods",
                "summary": "Master advanced techniques. Apply PCA for dimensionality reduction, use non-parametric methods, understand Bayesian statistics and bootstrap.",
                "key_concepts": ["Principal Component Analysis", "Mann-Whitney U test", "Spearman correlation", "Bayesian updating", "Bootstrap confidence intervals"],
                "formulas": ["X = TP^T + E (PCA)", "ρ_s = 1 - 6Σd²/n(n²-1) (Spearman)"],
                "applications": ["Factor extraction", "Robust hypothesis testing", "Uncertainty quantification"]
            },
            9: {
                "title": "Machine Learning for Finance",
                "summary": "Build predictive models using ML. Master classification and regression, understand model evaluation, prevent overfitting, and apply to finance.",
                "key_concepts": ["Supervised learning", "Logistic regression", "Decision trees and Random Forest", "Precision, Recall, F1, ROC-AUC", "Cross-validation"],
                "formulas": ["P(Y=1) = 1/(1+e^{-z})", "Accuracy = (TP+TN)/(TP+TN+FP+FN)"],
                "applications": ["Credit scoring", "Fraud detection", "Stock movement prediction"]
            },
            10: {
                "title": "Business Analytics Applications",
                "summary": "Solve business problems with analytics. Master customer segmentation, CLV calculation, churn prediction, A/B testing, and forecasting.",
                "key_concepts": ["K-means clustering", "Customer Lifetime Value", "Churn prediction", "A/B testing", "Price elasticity"],
                "formulas": ["CLV = Avg Profit / Churn Rate", "Elasticity = %ΔQ / %ΔP"],
                "applications": ["Customer analytics", "Marketing optimization", "Pricing decisions"]
            },
            11: {
                "title": "Tools and Software",
                "summary": "Master essential analytics tools. Learn Excel, Python, SQL, and BI tools like Tableau and Power BI for professional analytics work.",
                "key_concepts": ["Excel formulas and PivotTables", "Python (pandas, numpy, sklearn)", "SQL queries and joins", "Tableau/Power BI dashboards", "Cloud platforms"],
                "formulas": ["N/A - Focus on tool proficiency"],
                "applications": ["Financial modeling", "Data analysis", "Reporting and dashboards"]
            },
            12: {
                "title": "Case Studies and Projects",
                "summary": "Apply everything in real-world projects. Work through case studies, build portfolio projects, and learn to communicate results effectively.",
                "key_concepts": ["End-to-end analytics workflow", "Credit risk modeling", "Portfolio optimization projects", "Effective communication", "Ethics and best practices"],
                "formulas": ["Applied use of all previous formulas"],
                "applications": ["Complete analytics projects", "Portfolio building", "Professional presentations"]
            }
        }

        selected_module = st.selectbox("Select Module for Details:", 
                                      [f"Module {k}: {v['title']}" for k, v in module_summaries.items()])
        
        mod_num = int(selected_module.split(":")[0].split()[1])
        mod_data = module_summaries[mod_num]

        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown(f"### {modules_info[mod_num-1]['icon']} {mod_data['title']}")
            st.markdown(f"**{mod_data['summary']}**")
            
            st.markdown("#### 🔑 Key Concepts:")
            for concept in mod_data['key_concepts']:
                st.markdown(f"- {concept}")
            
            st.markdown("#### 📐 Important Formulas:")
            for formula in mod_data['formulas']:
                st.code(formula)
        
        with col2:
            st.info(f"**Difficulty:** {modules_info[mod_num-1]['difficulty']}")
            
            st.markdown("#### 💼 Applications:")
            for app in mod_data['applications']:
                st.markdown(f"• {app}")

    # ══════════════════════════════════════════════════════════════════
    with tab3:
        st.header("🧮 Complete Formula Bank — All Key Formulas")

        st.markdown("### Quick Formula Reference by Category")

        formula_categories = {
            "Descriptive Statistics": [
                ("Mean", "μ = Σx / n", "Average value", "M1"),
                ("Variance", "σ² = Σ(x - μ)² / N", "Measure of dispersion", "M1"),
                ("Standard Deviation", "σ = √(σ²)", "Square root of variance", "M1"),
                ("Coefficient of Variation", "CV = σ / μ", "Relative variability", "M1"),
                ("Skewness", "Skew = E[(X-μ)³] / σ³", "Asymmetry measure", "M1"),
                ("Kurtosis", "Kurt = E[(X-μ)⁴] / σ⁴", "Tail heaviness", "M1"),
            ],
            "Probability": [
                ("Bayes' Theorem", "P(A|B) = P(B|A)×P(A) / P(B)", "Update probabilities", "M2"),
                ("Expected Value", "E[X] = Σ x·P(x)", "Mean of distribution", "M2"),
                ("Variance of RV", "Var(X) = E[X²] - (E[X])²", "Dispersion of RV", "M2"),
                ("Binomial Probability", "P(X=k) = C(n,k)×p^k×(1-p)^(n-k)", "Discrete events", "M2"),
                ("Normal Distribution", "f(x) = (1/σ√(2π))×e^(-(x-μ)²/2σ²)", "Continuous bell curve", "M2"),
            ],
            "Statistical Inference": [
                ("Confidence Interval (z)", "CI = x̄ ± z(σ/√n)", "Population mean CI", "M3"),
                ("Confidence Interval (t)", "CI = x̄ ± t(s/√n)", "Sample mean CI", "M3"),
                ("t-statistic", "t = (x̄ - μ) / (s/√n)", "Hypothesis test statistic", "M3"),
                ("Standard Error", "SE = σ / √n", "Sampling variability", "M3"),
                ("Sample Size", "n = (z×σ / E)²", "Required sample size", "M3"),
            ],
            "Regression": [
                ("Simple Regression", "Y = β₀ + β₁X + ε", "Linear relationship", "M4"),
                ("Beta Coefficient", "β₁ = Cov(X,Y) / Var(X)", "Slope estimate", "M4"),
                ("R-squared", "R² = 1 - (SSR/SST)", "Variance explained", "M4"),
                ("Adjusted R²", "Adj R² = 1 - [(1-R²)(n-1)/(n-k-1)]", "Penalized R²", "M4"),
                ("Multiple Regression", "Y = β₀ + β₁X₁ + β₂X₂ + ... + ε", "Multiple predictors", "M4"),
            ],
            "Portfolio & Risk": [
                ("Portfolio Return", "Rₚ = Σ wᵢRᵢ", "Weighted average return", "M6"),
                ("Portfolio Variance", "σₚ² = ΣΣ wᵢwⱼσᵢσⱼρᵢⱼ", "Portfolio risk", "M6"),
                ("Sharpe Ratio", "SR = (Rₚ - Rf) / σₚ", "Risk-adjusted return", "M6"),
                ("Correlation", "ρ = Cov(X,Y) / (σₓσᵧ)", "Linear relationship", "M6"),
                ("Beta", "β = Cov(Rᵢ,Rₘ) / Var(Rₘ)", "Systematic risk", "M4,M6"),
                ("Parametric VaR", "VaR = -(μ - z_α × σ) × V", "Maximum expected loss", "M7"),
                ("CVaR", "CVaR = E[Loss | Loss > VaR]", "Expected tail loss", "M7"),
            ],
            "Time Series": [
                ("AR(1)", "Y_t = φ₁Y_{t-1} + ε_t", "Autoregressive model", "M5"),
                ("MA(1)", "Y_t = ε_t + θ₁ε_{t-1}", "Moving average model", "M5"),
                ("ARIMA(p,d,q)", "Combines AR, I, MA components", "General TS model", "M5"),
                ("GARCH(1,1)", "σ²_t = ω + αε²_{t-1} + βσ²_{t-1}", "Volatility model", "M5"),
            ],
            "Machine Learning": [
                ("Logistic Function", "P(Y=1) = 1/(1+e^{-z})", "Probability output", "M9"),
                ("Accuracy", "Acc = (TP+TN)/(TP+TN+FP+FN)", "Overall correctness", "M9"),
                ("Precision", "Prec = TP/(TP+FP)", "Positive predictive value", "M9"),
                ("Recall", "Rec = TP/(TP+FN)", "Sensitivity", "M9"),
                ("F1 Score", "F1 = 2×(Prec×Rec)/(Prec+Rec)", "Harmonic mean", "M9"),
            ],
            "Business Analytics": [
                ("CLV", "CLV = Annual Profit / Churn Rate", "Customer lifetime value", "M10"),
                ("Price Elasticity", "E = %ΔQ / %ΔP", "Demand sensitivity", "M10"),
                ("LTV/CAC Ratio", "Ratio = CLV / CAC", "Customer value ratio", "M10"),
                ("EOQ", "EOQ = √(2DS/H)", "Economic order quantity", "M10"),
            ]
        }

        for category, formulas in formula_categories.items():
            with st.expander(f"📐 {category} ({len(formulas)} formulas)", expanded=False):
                formula_df = pd.DataFrame(formulas, columns=["Formula Name", "Formula", "Description", "Module"])
                st.dataframe(formula_df, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("🔍 Formula Search")
        search_term = st.text_input("Search for a formula:", "")
        
        if search_term:
            results = []
            for category, formulas in formula_categories.items():
                for fname, formula, desc, module in formulas:
                    if search_term.lower() in fname.lower() or search_term.lower() in desc.lower():
                        results.append({
                            "Category": category,
                            "Name": fname,
                            "Formula": formula,
                            "Description": desc,
                            "Module": module
                        })
            
            if results:
                st.success(f"Found {len(results)} matching formula(s):")
                st.dataframe(pd.DataFrame(results), use_container_width=True, hide_index=True)
            else:
                st.warning("No formulas found matching your search.")

    # ══════════════════════════════════════════════════════════════════
    with tab4:
        st.header("📊 Visual Learning Dashboard")

        st.subheader("📈 Course Complexity Progression")

        # Complexity chart
        complexity_data = pd.DataFrame({
            "Module": [f"M{i}" for i in range(1, 13)],
            "Module_Full": [m['title'] for m in modules_info],
            "Complexity": [3, 4, 6, 7, 8, 7, 9, 9, 9, 8, 5, 10],
            "Phase": ["Foundation"]*3 + ["Core Methods"]*4 + ["Advanced"]*3 + ["Applied"]*2
        })

        fig1 = px.line(complexity_data, x="Module", y="Complexity", 
                      title="Course Complexity Curve",
                      markers=True, color="Phase",
                      hover_data=["Module_Full"])
        fig1.update_layout(yaxis_title="Complexity (1-10 scale)", template="plotly_dark")
        st.plotly_chart(fig1, use_container_width=True)

        st.markdown("---")
        st.subheader("🎯 Skills Coverage Map")

        # Skills heatmap
        skills = ["Descriptive Stats", "Probability", "Inference", "Modeling", "Risk Analysis", 
                 "Programming", "ML/AI", "Communication"]
        modules_coverage = [
            [10, 5, 2, 1, 2, 1, 0, 2],  # M1
            [3, 10, 3, 2, 5, 1, 0, 2],  # M2
            [2, 5, 10, 3, 3, 2, 0, 3],  # M3
            [2, 2, 5, 10, 3, 5, 2, 4],  # M4
            [3, 3, 4, 10, 5, 7, 3, 3],  # M5
            [5, 5, 4, 8, 10, 5, 2, 4],  # M6
            [3, 4, 4, 6, 10, 5, 3, 5],  # M7
            [4, 6, 8, 7, 6, 7, 4, 4],  # M8
            [3, 3, 5, 9, 5, 8, 10, 5],  # M9
            [5, 4, 6, 8, 5, 7, 9, 7],  # M10
            [3, 2, 3, 5, 4, 10, 5, 6],  # M11
            [7, 5, 7, 9, 8, 8, 7, 10],  # M12
        ]

        heatmap_df = pd.DataFrame(modules_coverage, 
                                  columns=skills,
                                  index=[f"M{i}" for i in range(1, 13)])

        fig2 = px.imshow(heatmap_df, 
                        labels=dict(x="Skill Area", y="Module", color="Coverage"),
                        title="Skill Coverage by Module (0=None, 10=Heavy)",
                        color_continuous_scale="Viridis")
        fig2.update_layout(template="plotly_dark")
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("---")
        st.subheader("💼 Career Path Alignment")

        career_paths = {
            "Financial Analyst": [8, 7, 8, 9, 7, 9, 8, 5, 4, 6, 9, 7],
            "Data Analyst": [9, 6, 8, 9, 7, 6, 7, 8, 9, 9, 10, 8],
            "Quantitative Analyst": [7, 9, 9, 10, 10, 10, 10, 10, 9, 7, 9, 8],
            "Risk Manager": [7, 8, 8, 8, 9, 10, 10, 8, 7, 6, 8, 8],
            "Portfolio Manager": [6, 7, 7, 8, 8, 10, 9, 7, 6, 5, 7, 7],
        }

        career_df = pd.DataFrame(career_paths, index=[f"M{i}" for i in range(1, 13)])
        
        fig3 = go.Figure()
        for career in career_paths.keys():
            fig3.add_trace(go.Scatter(x=career_df.index, y=career_df[career],
                                     mode='lines+markers', name=career))
        
        fig3.update_layout(title="Module Relevance by Career Path (1-10 scale)",
                          xaxis_title="Module", yaxis_title="Relevance",
                          template="plotly_dark", hovermode='x unified')
        st.plotly_chart(fig3, use_container_width=True)

        st.info("""
        **How to use this chart:**
        - Pick your target career path
        - Focus extra attention on modules rated 8-10 for your path
        - Modules rated 5-7 are still important but less critical
        - All modules build foundational knowledge useful across careers
        """)

    # ══════════════════════════════════════════════════════════════════
    with tab5:
        st.header("✅ Master Quiz — Test Your Knowledge Across All Modules")

        st.markdown("""
        This comprehensive quiz covers all 12 modules. Test yourself to identify areas for review.
        Each question is tagged with its module for targeted study.
        """)

        if 'quiz_submitted' not in st.session_state:
            st.session_state.quiz_submitted = {}

        quiz_questions = [
            {"q": "The standard deviation is the square root of:", 
             "opts": ["Mean", "Variance", "Range", "Median"], 
             "ans": "Variance", "mod": "M1",
             "exp": "Standard deviation = √Variance. It measures dispersion in the same units as the data."},
            
            {"q": "Bayes' theorem is used to:", 
             "opts": ["Calculate variance", "Update probabilities given new evidence", "Find correlation", "Test hypotheses"], 
             "ans": "Update probabilities given new evidence", "mod": "M2",
             "exp": "Bayes' theorem: P(A|B) = P(B|A)×P(A)/P(B) - updates prior probabilities with new information."},
            
            {"q": "A Type I error occurs when you:", 
             "opts": ["Reject a true null hypothesis", "Fail to reject a false null", "Calculate wrong variance", "Use wrong sample size"], 
             "ans": "Reject a true null hypothesis", "mod": "M3",
             "exp": "Type I error (α) = false positive, rejecting H₀ when it's actually true."},
            
            {"q": "R-squared measures:", 
             "opts": ["Correlation coefficient", "Proportion of variance explained", "Regression slope", "Standard error"], 
             "ans": "Proportion of variance explained", "mod": "M4",
             "exp": "R² = 1 - (SSR/SST), showing how much variance in Y is explained by X. Range: 0 to 1."},
            
            {"q": "ARIMA models are primarily used for:", 
             "opts": ["Cross-sectional data", "Time series forecasting", "Classification", "Clustering"], 
             "ans": "Time series forecasting", "mod": "M5",
             "exp": "ARIMA (AutoRegressive Integrated Moving Average) models time-dependent data for forecasting."},
            
            {"q": "Diversification in portfolios reduces:", 
             "opts": ["Systematic risk", "Unsystematic risk", "All risk", "Expected return"], 
             "ans": "Unsystematic risk", "mod": "M6",
             "exp": "Diversification eliminates unsystematic (specific) risk but cannot remove systematic (market) risk."},
            
            {"q": "A 1-day 95% VaR of $100,000 means:", 
             "opts": ["Average loss is $100k", "Maximum possible loss is $100k", "95% of days, loss < $100k", "Loss is always $100k"], 
             "ans": "95% of days, loss < $100k", "mod": "M7",
             "exp": "VaR is a threshold: 95% confidence means losses exceed VaR on only 5% of days."},
            
            {"q": "PCA (Principal Component Analysis) is used for:", 
             "opts": ["Hypothesis testing", "Dimensionality reduction", "Regression", "Clustering"], 
             "ans": "Dimensionality reduction", "mod": "M8",
             "exp": "PCA reduces many correlated variables to fewer uncorrelated principal components."},
            
            {"q": "Overfitting in ML occurs when:", 
             "opts": ["Model is too simple", "Training accuracy >> Test accuracy", "Both accuracies are high", "Sample size is large"], 
             "ans": "Training accuracy >> Test accuracy", "mod": "M9",
             "exp": "Overfitting: model memorizes training data but fails to generalize to new data."},
            
            {"q": "Customer Lifetime Value (CLV) represents:", 
             "opts": ["One-time purchase value", "Total customers", "Present value of future profits from customer", "Marketing cost"], 
             "ans": "Present value of future profits from customer", "mod": "M10",
             "exp": "CLV = total profit expected from a customer over their entire relationship with company."},
            
            {"q": "SQL is primarily used for:", 
             "opts": ["Creating visualizations", "Querying databases", "Machine learning", "Statistical testing"], 
             "ans": "Querying databases", "mod": "M11",
             "exp": "SQL (Structured Query Language) retrieves and manipulates data from relational databases."},
            
            {"q": "The most important aspect of an analytics project is:", 
             "opts": ["Using complex models", "Addressing a business question", "Having big data", "Perfect accuracy"], 
             "ans": "Addressing a business question", "mod": "M12",
             "exp": "Analytics projects must solve real business problems - models are tools, not the goal."},
            
            {"q": "The Central Limit Theorem states that sample means:", 
             "opts": ["Are always normal", "Approach normal distribution as n increases", "Equal population mean", "Have zero variance"], 
             "ans": "Approach normal distribution as n increases", "mod": "M3",
             "exp": "CLT: regardless of population distribution, sample means → normal as sample size increases."},
            
            {"q": "The Sharpe ratio measures:", 
             "opts": ["Total return", "Excess return per unit of risk", "Volatility only", "Correlation"], 
             "ans": "Excess return per unit of risk", "mod": "M6",
             "exp": "Sharpe = (Rₚ - Rf)/σₚ - shows risk-adjusted performance. Higher is better."},
            
            {"q": "In A/B testing, you should determine sample size:", 
             "opts": ["After running the test", "Before starting", "When you see results", "Never"], 
             "ans": "Before starting", "mod": "M10",
             "exp": "Sample size calculation (power analysis) must be done before testing to ensure valid results."},
        ]

        num_q = len(quiz_questions)
        st.info(f"**{num_q} questions** covering all modules. Select your answer and click 'Check' to see if you're correct.")

        for idx, q in enumerate(quiz_questions):
            st.markdown(f"**Q{idx+1}** ({q['mod']}): {q['q']}")
            
            col1, col2 = st.columns([3, 1])
            with col1:
                answer = st.radio("Select answer:", q["opts"], key=f"quiz_{idx}", label_visibility="collapsed")
            with col2:
                if st.button("Check ✓", key=f"check_{idx}"):
                    st.session_state.quiz_submitted[idx] = (answer == q["ans"])
            
            if idx in st.session_state.quiz_submitted:
                if answer == q["ans"]:
                    st.success(f"✅ Correct! {q['exp']}")
                else:
                    st.error(f"❌ Incorrect. The correct answer is: **{q['ans']}**")
                    st.info(f"💡 {q['exp']}")
            
            st.markdown("---")

        answered = len(st.session_state.quiz_submitted)
        correct = sum(1 for v in st.session_state.quiz_submitted.values() if v)
        
        if answered > 0:
            pct = correct / answered * 100
            col1, col2, col3 = st.columns(3)
            with col1: st.metric("Questions Answered", f"{answered}/{num_q}")
            with col2: st.metric("Correct Answers", f"{correct}")
            with col3: st.metric("Score", f"{pct:.0f}%")

            if pct >= 90:
                st.success("🏆 Outstanding! You have mastered the course material!")
            elif pct >= 75:
                st.info("✅ Excellent! Strong understanding across modules.")
            elif pct >= 60:
                st.warning("⚠️ Good progress! Review modules where you made mistakes.")
            else:
                st.error("❌ Keep studying! Focus on the fundamentals.")

        if st.button("🔄 Reset Quiz"):
            st.session_state.quiz_submitted = {}
            st.rerun()

    # ══════════════════════════════════════════════════════════════════
    with tab6:
        st.header("🎓 Study Planner & Progress Tracker")

        st.subheader("📅 Suggested Study Schedule")

        schedule_df = pd.DataFrame({
            "Week": ["Week 1", "Week 2", "Week 3", "Week 4", "Week 5-6", "Week 7-8", 
                    "Week 9-10", "Week 11-12", "Week 13", "Week 14"],
            "Modules": ["1", "2", "3", "4", "5", "6-7", "8-9", "10-11", "12", "All (Review)"],
            "Topics": [
                "Foundations: descriptive stats, distributions",
                "Probability theory, Bayes, distributions",
                "Statistical inference, hypothesis testing",
                "Regression analysis, CAPM, model diagnostics",
                "Time series: ARIMA, GARCH, forecasting",
                "Portfolio statistics, VaR and risk analytics",
                "PCA, non-parametric, ML for finance",
                "Business analytics, tools (Excel, Python, SQL)",
                "Case studies, projects, communication",
                "Final review, practice problems, capstone project"
            ],
            "Focus Activity": [
                "Calculate mean, std dev, create visualizations",
                "Probability problems, Bayes theorem exercises",
                "Confidence intervals, t-tests, hypothesis testing",
                "Build regression models, interpret R², residuals",
                "Forecast time series, model volatility",
                "Portfolio optimization, calculate VaR/CVaR",
                "PCA analysis, bootstrap CIs, build ML models",
                "Customer segmentation, A/B tests, SQL queries",
                "Complete end-to-end project, presentation",
                "Timed practice across all modules"
            ]
        })
        st.dataframe(schedule_df, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("✅ My Progress Tracker")
        st.markdown("Track your completion of each module:")

        progress_data = []
        total_completed = 0
        for mod in modules_info:
            col1, col2, col3, col4 = st.columns([2, 1, 1, 2])
            with col1:
                st.markdown(f"**{mod['icon']} Module {mod['num']}: {mod['title']}**")
            with col2:
                completed = st.checkbox("Completed ✅", key=f"prog_done_{mod['num']}")
            with col3:
                practiced = st.checkbox("Practiced 🧮", key=f"prog_prac_{mod['num']}")
            with col4:
                confidence = st.select_slider(
                    "Confidence", ["❓", "😰", "😐", "😊", "🌟"],
                    value="😐", key=f"prog_conf_{mod['num']}"
                )
            if completed:
                total_completed += 1

        overall_progress = total_completed / 12 * 100
        st.progress(overall_progress / 100)
        st.metric("Overall Progress", f"{total_completed}/12 modules ({overall_progress:.0f}%)")

        if total_completed == 12:
            st.success("🎉 🏆 Congratulations! You have completed all 12 modules of Statistics for Finance Professionals!")
            st.balloons()

        st.markdown("---")
        st.subheader("📌 Quick Reference — Top 10 Statistical Principles")

        principles = [
            ("1", "Correlation ≠ Causation", "Association doesn't prove cause-and-effect", "M1, M4"),
            ("2", "Always check assumptions", "Tests require assumptions (normality, independence)", "M3, M4, M5"),
            ("3", "Larger samples → Better estimates", "Law of Large Numbers and Central Limit Theorem", "M3"),
            ("4", "Diversification reduces unsystematic risk only", "Cannot eliminate systematic (market) risk", "M6"),
            ("5", "VaR doesn't tell you tail severity", "Use CVaR to understand worst-case losses", "M7"),
            ("6", "Simple models often outperform complex ones", "Occam's Razor applies to statistics", "M4, M9"),
            ("7", "Always validate on out-of-sample data", "In-sample fit can be misleading (overfitting)", "M9"),
            ("8", "P-value < 0.05 doesn't mean important", "Statistical significance ≠ practical significance", "M3"),
            ("9", "Outliers can drive results", "Always examine and understand extreme values", "M1, M8"),
            ("10", "Context matters more than technique", "Start with business question, not the method", "M12"),
        ]

        principles_df = pd.DataFrame(principles, columns=["#", "Principle", "Why It Matters", "Module(s)"])
        st.dataframe(principles_df, use_container_width=True, hide_index=True)

        st.markdown("---")
        st.subheader("🔗 Module Connections — How Everything Links Together")
        st.markdown("""
        Understanding how modules connect deepens your mastery:

        | Connection | Link |
        |-----------|------|
        | **M1 → M2** | Descriptive statistics → Probability distributions (understanding data shapes) |
        | **M2 → M3** | Probability theory → Inference (sampling distributions, CLT) |
        | **M3 → M4** | Hypothesis testing → Regression significance testing |
        | **M4 → M5** | Regression → Time series regression (ARIMA has AR component) |
        | **M4 → M6** | Regression (CAPM) → Portfolio beta and systematic risk |
        | **M6 → M7** | Portfolio variance → VaR calculation methods |
        | **M3 → M8** | Parametric tests → Non-parametric alternatives |
        | **M8 → M9** | Statistical methods → Machine learning foundations |
        | **M9 → M10** | ML techniques → Business analytics applications |
        | **M1-M10 → M11** | All statistical methods → Implemented in software tools |
        | **M1-M11 → M12** | All techniques → Applied in real-world projects |
        """)

        st.success("🎓 Use this overview page as your companion throughout the course. Return to it for quick reference, formula lookup, progress tracking, and exam preparation!")

if __name__ == "__main__":
    show()