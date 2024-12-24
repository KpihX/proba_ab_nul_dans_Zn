# Probability of having $ab = 0$ in $\mathbb{Z}/n\mathbb{Z}$

## 🧮 Mathematical Exploration 🔢

### 📝 Project Description

---

This project investigates the probability of having $ab = 0$ for pairs $(a, b) \in (\mathbb{Z}/n\mathbb{Z})^2$, exploring different computational methods and mathematical formulas.

### 🔬 Methodology

---

The project implements three distinct approaches to calculate the probability:

1. **Direct Evaluation** 🎯

   - Directly counts the number of pairs $(a, b)$ where $ab = 0$ in $\mathbb{Z}/n\mathbb{Z}$
   - Computational method with direct counting
2. **Sum Formula** 📊

   - Uses the mathematical formula: $\frac{1}{n}\sum_{d|n} \frac{\phi(d)}{d}$
   - Leverages number theory and divisor properties
3. **Product Formula** 🧮

   - Applies the formula: $\prod_{k=1}^{m} \frac{p_k \cdot (\alpha_k + 1) - \alpha_k}{p_k^{\alpha_k + 1}}$
   - Where $n = \prod_{k=1}^{m} p_k^{\alpha_k}$

### 📈 Results

---

Results are computed for values of $n$ from 2 to 99, providing a comprehensive analysis of the probability distribution.

### 🚧 Generalization Status

---

**Generalization is currently on STANDBY! 🛑**

We are seeking contributions to extend the project. Specifically, we need help with:

- Theoretical extensions of the probability calculation
- More efficient computational methods
- Visualization and statistical analysis of the results

#### Desired Generalization Contributions:

1. 📊 Statistical analysis of probability trends
2. 🧮 Theoretical proofs for the observed patterns
3. 💻 Optimization of computational methods
4. 📈 Advanced visualization techniques

### 📂 Results Storage

---

Computational results are stored in the `results/` directory for further analysis and reference.

### 🛠️ Dependencies

---

- NumPy

- Matplotlib
- Pandas

### 📜 License

---

MIT

### 👨‍💻 Author

---

K𝛑X

### 🤝 Contributions Welcome!

---

Feel free to open issues, submit pull requests, or reach out with ideas for generalization.
